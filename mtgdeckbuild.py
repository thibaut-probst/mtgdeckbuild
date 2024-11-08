from argparse import ArgumentParser, RawTextHelpFormatter
from rich.prompt import Prompt
from requests import get, post
from urllib.parse import quote
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from re import compile, match
from rapidfuzz import distance as lev

mtgtop8_base_url = 'https://mtgtop8.com'
user_agent = {'User-agent': 'Mozilla/5.0'}


def select_format():
    '''
    Parses the website data source website to identify the available Magic: The Gathering formats and prompts the user to select a format.

    Returns:
        The selected Magic: The Gathering format.
    '''

    # Format discovery
    format_choice_str = 'Select a format:\n'
    mtg_formats = {}
    response = get(f'{mtgtop8_base_url}', headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    n = 1
    for link in links:
        href = link.get('href')
        if href:
            if href.startswith('/format?f='):
                mtg_formats[n] = href.split('=')[1]
                if link.text.lower() == 'cedh':
                    format_choice_str += f'{n} - cEDH\n'
                else:
                    format_choice_str += f'{n} - {link.text.title()}\n'
                n += 1

    # Format choice
    format_choice = 0
    while format_choice == 0:
        format_choice = Prompt.ask(format_choice_str, choices=[f'{n}' for n in mtg_formats], show_choices=False)
        try:
            format_choice = int(format_choice)
            if format_choice == 0:
                print('Invalid choice.')
        except Exception:
            print('Invalid choice.')
    
    return mtg_formats[format_choice]


def select_archetypes(mtg_format, top):
    '''
    Parses the website data source to identify the available Magic: The Gathering archetypes of a given format and prompts the user to select an archetype.
    
    Args:
        mtg_format (str): The Magic: The Gathering format.
        top (int): The number of top archetypes to select.

    Returns:
        The selected Magic: The Gathering archetypes.
    '''

    # Archetypes discovery
    archetypes_list = []
    
    if mtg_format == 'EDH':
        response = get(f'{mtgtop8_base_url}/cEDH_decks?format?f={mtg_format}&meta=121', headers=user_agent)
    else:
        response = get(f'{mtgtop8_base_url}/format?f={mtg_format}', headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        txt = link.text
        if href and txt:
            href = href.lower()
            # Only keep deck archetypes
            if href.startswith('archetype?a='):
                archetypes_list.append((href.split('archetype?a=')[1].split('&')[0], txt))

    if top > 0:
        archetypes_list = sorted(archetypes_list[0:top], key=lambda x: x[1])
    else:
        archetypes_list = sorted(archetypes_list, key=lambda x: x[1])

    # Archetypes choice
    archetypes_dict = {}
    archetype_choice_str = 'Select an archetype:\n'
    archetype_choice_str += '0 - All archetypes\n'
    archetypes_dict[0] = 'All archetypes'

    n = 0

    for a in archetypes_list:
        archetypes_dict[n] = a[1]
        archetype_choice_str += f'{n+1} - {a[1]}\n'
        n += 1
    selected_archetypes = []
    while not selected_archetypes:
        archetype_choices = Prompt.ask(archetype_choice_str, show_choices=False)
        try:
            archetype_choices = archetype_choices.split(',')
            for choice in archetype_choices:
                choice = int(choice)
                if choice == 0:
                    selected_archetypes = [0]
                else:
                    if choice > 0:
                        choice = choice - 1
                        selected_archetypes.append(archetypes_list[choice][0])
                    elif choice < 0:
                        print('Invalid choice.')
            if not selected_archetypes:
                print('Invalid choice.')              
        except Exception:
            print('Invalid choice.')

    if 0 in selected_archetypes:
        return False

    return selected_archetypes


def find_archetype(mtg_format, archetype_name):
    '''
    Parses the website data source to find the Magic: The Gathering archetype identifier based on the provided name.
    
    Args:
        archetype_name (str): The Magic: The Gathering archetype name.

    Returns:
        The found Magic: The Gathering archetype identifier.
    '''

    archetype_id = False

    # Archetypes discovery
    archetypes = {}
    if mtg_format == 'EDH':
        response = get(f'{mtgtop8_base_url}/cEDH_decks?f=EDH&show=pop&cid=&meta=283&cEDH_cp=1', headers=user_agent)
    else:
        response = get(f'{mtgtop8_base_url}/format?f={mtg_format}', headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        txt = link.text
        if href and txt:
            href = href.lower()
            # Only keep deck archetypes
            if href.startswith('archetype?a='):
                archetypes[txt.lower()] = href.split('archetype?a=')[1].split('&')[0]

    archetype_name_lower = archetype_name.lower()
    # Try to find archetype with Leveinshtein distance or if provided archetype string is the start of a known one
    if archetype_name_lower not in archetypes:
        print(f'Archetype not found: {archetype_name}')
        for a in archetypes:
            a_lower = a.lower()
            dist = lev.Levenshtein.distance(archetype_name_lower, a)
            if (dist <= 3) or (a_lower.startswith(archetype_name_lower) and (len(archetype_name_lower) >= 5)):
                answer = Prompt.ask(f'Did you mean {a.title()}?', choices=['y', 'n'], default='y')
                if answer.lower() == 'y':
                    archetype_name_lower = a_lower
                    break

    if archetype_name_lower not in archetypes:
        exit()

    archetype_id = archetypes[archetype_name_lower]

    return archetype_id
    

def print_avg_deck(avg_deck, total_decks, print_with_details, maybeboard):
    '''
    Prints the average deck

    Args:
        avg_deck (dict): The average deck to print.
        total_decks (int): The total number of analyzed decks.
        print_with_details (bool): Whether to print the decklist with more details or not.
        maybeboard (bool): Whether to print the maybeboard or not.
    '''

    if print_with_details:
        # Main deck
        for section in avg_deck['main']:
            sorted_section = sorted(avg_deck['main'][section].items(), key=lambda x: x[1], reverse=True)
            nb_cards_section = 0
            for card in sorted_section:
                nb_cards_section += card[1][0]
            print('//----------------------------------------------------------------------')
            print(f'// {section.upper()} - {nb_cards_section} cards')
            print('//----------------------------------------------------------------------')
            for card in sorted_section:
                print(f'{card[1][0]} {card[0]} - Used by {card[1][1]}/{total_decks} decks ({int(round(card[1][1]/total_decks, 2)*100)}%)')
 
        # Sideboard
        sorted_side = sorted(avg_deck['side'].items(), key=lambda x: x[1], reverse=True)
        nb_cards_side = 0
        for card in sorted_side:
            nb_cards_side += card[1][0]
        print('//----------------------------------------------------------------------')
        print(f'// SIDEBOARD - {nb_cards_side} cards')
        print('//----------------------------------------------------------------------')
        for card in sorted_side:
            print(f'{card[1][0]} {card[0]} - Used by {card[1][1]}/{total_decks} decks ({int(round(card[1][1]/total_decks, 2)*100)}%)')
       
        if maybeboard:
            # Maybeboard
            if 'maybeboard' in avg_deck:
                sorted_maybe = sorted(avg_deck['maybeboard'].items(), key=lambda x: x[1], reverse=True)
                nb_cards_maybe = 0
                for card in sorted_maybe:
                    nb_cards_maybe += card[1][0]
                print('//----------------------------------------------------------------------')
                print(f'// MAYBEBOARD - {nb_cards_maybe} cards')
                print('//----------------------------------------------------------------------')
                for card in sorted_maybe:
                    print(f'{card[1][0]} {card[0]} - Used by {card[1][1]}/{total_decks} decks ({int(round(card[1][1]/total_decks, 2)*100)}%)')

    else:
        # Main deck
        main_cards = []
        for section in avg_deck['main']:
            for card in avg_deck['main'][section]:
                main_cards.append([card, avg_deck['main'][section][card][0]])
        print('// MAIN DECK')
        for main_card in main_cards:
            print(f'{main_card[1]} {main_card[0]}')

        # Sideboard
        side_cards = []
        for card in avg_deck['side']:
            side_cards.append([card, avg_deck['side'][card][0]])
        print('// SIDEBOARD')
        for side_card in side_cards:
            print(f'{side_card[1]} {side_card[0]}')
        
        if maybeboard:
            # Maybeboard
            if 'maybeboard' in avg_deck:
                print('// MAYBEBOARD')
                for card, info in avg_deck['maybeboard'].items():
                    print(f'{info[0]} {card}')



def build_avg_deck(sorted_main_card_counts, sorted_side_card_counts, main_target, side_target, section_avg, nb_analyzed_decks):
    '''
    Builds an average deck based on the provided average card counts.

    Args:
        sorted_main_card_counts (list): A sorted list of (average or top quantity) card counts for the main deck. Each item in the list is a tuple of (card, [count, decks, section]).
        sorted_side_card_counts (list): A sorted list of (average or top quantity) card counts for the sideboard. Each item in the list is a tuple of (card, [count, decks, section]).
        main_target (int): The target number of cards for the main deck.
        side_target (int): The target number of cards for the sideboard.
        section_avg (dict): The average number of cards per section for the main deck.
        nb_analyzed_decks (int): The total number of analyzed decks.
        
    Returns:
        A dictionary representing the average deck.
    '''

    avg_deck = {'main': {'lands': {}, 'creatures': {}, 'other spells': {}}, 'side': {}}

    # Main deck building
    main_cards = []
    delta_sections = {}

    if sorted_main_card_counts:
        main_deck_total = 0
        n = 0
        reset = False

        while not (main_deck_total == main_target): # Process available cards while we haven't reached the target
            
            # Retrieve card information
            card_count = sorted_main_card_counts[n]
            card = card_count[0]
            nb_decks = card_count[1][0]
            nb_cards = card_count[1][2]
            section = card_count[1][3]
            
            # Update remaining spots for main deck and each section
            delta_main = main_target - main_deck_total
            for s in section_avg:
                total_c = 0
                for c in avg_deck['main'][s]:
                    total_c += avg_deck['main'][s][c][0]
                delta_sections[s] = section_avg[s] - total_c

            # Add cards unless if we'll go over target number of cards, just reach the target otherwise. Take into account cards section balance.
            if nb_cards <= delta_main:
                if nb_cards <= delta_sections[section]: # Add cards to the section unless we're over target number of cards for this section
                    if card not in avg_deck['main'][section]:
                        avg_deck['main'][section][card] = [nb_cards, nb_decks]
                        main_deck_total += nb_cards
                        main_cards.append(card)
                elif all(value == 0 for value in delta_sections.values()): # Add cards to the section only if all sections are full and this is not the lands section
                    if not reset:
                        n = 0 # Reset card parser to 0 not to miss some cards not added previously due to section limit full
                        reset = True
                    elif section != 'lands':
                        if card not in avg_deck['main'][section]:
                            avg_deck['main'][section][card] = [nb_cards, nb_decks]
                            main_deck_total += nb_cards
                            main_cards.append(card)
                elif (nb_cards > delta_sections[section]) and (delta_sections[section] > 0): # Add cards to the section until the target for this section
                    if card not in avg_deck['main'][section]:
                        avg_deck['main'][section][card] = [nb_cards-delta_sections[section], nb_decks]
                        main_deck_total += nb_cards-delta_sections[section]
                        main_cards.append(card)
            else:
                if (delta_main <= delta_sections[section]): # Add cards to the section unless we're over target number of cards for this section
                    if card not in avg_deck['main'][section]:
                        avg_deck['main'][section][card] = [delta_main, nb_decks]
                        main_deck_total += delta_main
                        main_cards.append(card)
                elif all(value == 0 for value in delta_sections.values()): # Add cards to the section only if all sections are full and this is not the lands section
                    if not reset:
                        n = 0 # Reset card parser to 0 not to miss some cards not added previously due to section limit full
                        reset = True
                    elif section != 'lands':
                        if card not in avg_deck['main'][section]:
                            avg_deck['main'][section][card] = [delta_main, nb_decks]
                            main_deck_total += delta_main
                            main_cards.append(card)
                elif (delta_main > delta_sections[section]) and (delta_sections[section] > 0): # Add cards to the section until the target for this section
                    if card not in avg_deck['main'][section]:
                        avg_deck['main'][section][card] = [delta_main-delta_sections[section], nb_decks]
                        main_deck_total += delta_main-delta_sections[section]
                        main_cards.append(card)

            n += 1

        n = 0
        # Maybeboard
        if n < len(sorted_main_card_counts):
            nb_decks_min = nb_decks
            nb_decks_next = sorted_main_card_counts[n][1][0]
            while ( (nb_decks_next == nb_decks_min) or (nb_decks_next >= (nb_decks_min-round(nb_analyzed_decks/4))) ):
                card_count = sorted_main_card_counts[n]
                card = card_count[0]
                nb_decks = card_count[1][0]
                nb_cards = card_count[1][2]
                if 'maybeboard' not in avg_deck:
                    avg_deck['maybeboard'] = {}
                if card not in main_cards:
                    avg_deck['maybeboard'][card] = [nb_cards, nb_decks]
                n += 1
                if n < len(sorted_main_card_counts):
                    nb_decks_next = sorted_main_card_counts[n][1][0]
                else:
                    break

    # Sideboard building
    if sorted_side_card_counts:
        side_deck_total = 0
        n = 0
        while not (side_deck_total == side_target): # Process while we haven't reached the target
            card_count = sorted_side_card_counts[n]
            card = card_count[0]
            nb_decks = card_count[1][0]
            nb_cards = card_count[1][2]
            delta_side = side_target - side_deck_total
            # Add cards unless if we'll go over target number of cards, just reach the target so don't add the full cardset
            if card not in main_cards:
                if nb_cards <= delta_side:
                    avg_deck['side'][card] = [nb_cards, nb_decks]
                    side_deck_total += nb_cards
                else:
                    avg_deck['side'][card] = [delta_side, nb_decks]
                    side_deck_total += delta_side
            n += 1
    
    return avg_deck


if __name__ == '__main__':

    # Argument parsing from command-line
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '--top-archetypes', '-t',
        type = int,
        action = 'store',
        default = 0,
        help = 'The number of top archetypes to parse (default: all archetypes)'
    )

    parser.add_argument(
        '--format', '-f',
        type = str,
        action = 'store',
        default = '',
        help = 'The format to analyze (default: interactive mode)'
    )
    
    parser.add_argument(
        '--archetype', '-a',
        type = str,
        action = 'store',
        default = '',
        help = 'The archetype to analyze (default: interactive mode, must be used along with --format/-f)'
    )

    parser.add_argument(
        '--decks', '-d',
        type = int,
        action = 'store',
        default = 25,
        help = 'The maximum number of decks to analyze (default: 25)'
    )

    parser.add_argument(
        '--print-details', '-p',
        action = 'store_true',
        help = 'Print deck with details: sections and number of decks using each card'
    )

    parser.add_argument(
        '--competitive-only', '-c',
        action = 'store_true',
        default = False,
        help = 'Only consider competitive decks'
    )

    parser.add_argument(
        '--name', '-n',
        type = str,
        action='store',
        help = 'Only consider decks including given deck name'
    )

    parser.add_argument(
        '--include-cards', '-i',
        type = str,
        action='store',
        help = 'Only consider decks including given cards (use dash-separated card names if passing multiple cards, must be used with --main-deck/-m, --sideboard/-s arguments or both)'
    )

    parser.add_argument(
        '--main-include', '-m',
        action = 'store_true',
        default = False,
        help = 'Consider cards to include for the main deck (must be used with --include-cards/-i)'
    )

    parser.add_argument(
        '--side-include', '-s',
        action = 'store_true',
        default = False,
        help = 'Consider cards to include for the sideboard (must be used with --include-cards/-i)'
    )

    parser.add_argument(
        '--last-months', '-l',
        type = int,
        action='store',
        help = 'Only consider decks from the last given months'
    )

    parser.add_argument(
        '--since', '-S',
        type = str,
        action='store',
        help = 'Only consider decks since the given start date (DD-MM-YYYY)'
    )

    parser.add_argument(
        '--top-quantity', '-T',
        action = 'store_true',
        default = False,
        help = 'Build average deck based on the top used quantity for each most used card in analyzed decks (default: based on the average quantity)'
    )

    parser.add_argument(
        '--balance', '-b',
        action = 'store_true',
        default = False,
        help = 'Balance the number of cards for each section (lands, creatures, other spells) based on the average number of cards per section in the analyzed decks (default: do not balance and just retain the most used cards)'
    )

    parser.add_argument(
        '--balance-lands', '-B',
        action = 'store_true',
        default = False,
        help = 'Balance the number of cards for the lands section based on the average number of lands in the analyzed decks (default: do not balance and just retain the most used cards)'
    )

    parser.add_argument(
        '--maybeboard', '-M',
        action = 'store_true',
        default = False,
        help = 'Print Maybeboard (additional cards that are tied or minus a number (analyzed decks / 4) in terms of number of decks using them for main deck and sideboard)'
    )

    args = vars(parser.parse_args())
    top = args['top_archetypes']
    if top and (top < 1):
        print('argument --top-archetypes/-t: cannot be lower than 1')
        exit()
    
    input_format = args['format']
    mtg_format = input_format.upper()
    allowed_formats = ['ST', 'STD', 'STANDARD', 'PI', 'PIONEER', 'MO', 'MODERN', 'LE', 'LEGACY', 'VI', 'VINTAGE', \
                       'PAU', 'PAUPER', 'cEDH', 'COMMANDER', 'DC', 'EDH', 'DUELCOMMANDER', 'DUEL COMMANDER', 'PREM', 'PREMODERN']
    if mtg_format:
        if mtg_format not in allowed_formats:
            print(f'{input_format} is not in the list of supported formats.')
            exit()
        else:
            if (mtg_format == 'PAUPER'):
                mtg_format = 'PAU'
            elif (mtg_format == 'COMMANDER'):
                mtg_format = 'cEDH'
            elif (mtg_format == 'DC') or (mtg_format == 'EDH') or mtg_format.startswith('DUEL'):
                mtg_format = 'EDH'
            elif (mtg_format == 'PREMODERN'):
                mtg_format = 'PREM'
            else:
                mtg_format = mtg_format[0:2]
    archetype = args['archetype']
    if archetype and not format:
        print('argument --archetype/-a: must be used along with --format/-f')
        exit()

    max_number_decks = args['decks']
    if max_number_decks and (max_number_decks < 1):
        print('argument --decks/-d: cannot be lower than 1')
        exit()

    print_with_details = args['print_details']

    competitive = args['competitive_only']

    deck_name = args['name']

    included_cards = args['include_cards']
    if included_cards:
        if not match(r'^[\w\s\',]+(-[\w\s\', ]+)?$', included_cards):
            print('argument --include-cards/-i: must be a dash-separated list of strings')
            exit()
        else:
            included_cards = included_cards.replace(' - ', '\r\n')
            included_cards = included_cards.replace('-', '\r\n')
            included_cards = included_cards.replace('- ', '\r\n')
            included_cards = included_cards.replace(' -', '\r\n')
    main_include = args['main_include']
    side_include = args['side_include']
    if (included_cards and not (main_include or side_include)) or (not included_cards and (main_include or side_include)):
        print('argument --include-cards/-i: must be used along with --main-include/-m and/or --side-include/-s')
        exit()

    last_months = args['last_months']
    since_date = args['since']

    if (last_months and since_date):
        print('argument --last-months/-l: cannot be used along with --since/-S')
        exit()

    if last_months and (last_months < 1):
        print('argument --last-months/-l: must be a positive number')
        exit()
    elif last_months:
        max_number_decks = 10000000
  
    if since_date:
        try:
            since_date = since_date.replace('/', '-')
            start_date = datetime.strptime(since_date, '%d-%m-%Y')
        except Exception:
            print('argument --since/-S: date format must be DD-MM-YYYY')
            exit()
        if start_date > datetime.now():
            print('argument --since/-S: date must be in the past')
            exit()   
        start_date_enc = start_date.strftime('%d-%m-%Y').replace('-', '%2F')
        max_number_decks = 10000000
        
    top_method = args['top_quantity']
    balance = args['balance']
    balance_lands = args['balance_lands']
    if balance and balance_lands:
        print('argument --balance/-b: cannot be used along with --balance-lands/-B')
        exit() 
    maybeboard = args['maybeboard']

    if not mtg_format:
        mtg_format = select_format()

    if archetype:
        mtg_archetype = find_archetype(mtg_format, archetype)
        mtg_archetypes = [mtg_archetype]
    else:
        mtg_archetypes = select_archetypes(mtg_format, top)
        if not mtg_archetypes:
            mtg_archetypes = [0]

    # Deck search
    decks = {}

    # Max number of decks is split per archetypes
    max_number_decks_archetype = int((max_number_decks/len(mtg_archetypes)) // 1 + (1 if (max_number_decks/len(mtg_archetypes)) % 1 != 0 else 0))

    for mtg_archetype in mtg_archetypes:

        n_page = 1
        deck = {}

        while len(deck) < max_number_decks_archetype:
            if not mtg_archetypes:
                deck_search_str = f'current_page={n_page}&format={mtg_format}'
            else:
                deck_search_str = f'current_page={n_page}&format={mtg_format}&archetype_sel%5B{mtg_format}%5D={mtg_archetype}'
            if competitive:
                deck_search_str += '&compet_check%5BP%5D=1&compet_check%5BM%5D=1&compet_check%5BC%5D=1'
            if deck_name:
                deck_search_str += f'&deck_titre={deck_name}'
            if (main_include or side_include):
                if main_include:
                    deck_search_str += '&MD_check=1'
                if side_include:
                    deck_search_str += '&SB_check=1'
                deck_search_str += f'&cards={quote(included_cards)}'
            if last_months or since_date:
                if last_months:
                    date_str = (datetime.now()-timedelta(days=30*last_months)).strftime('%d/%m/%Y').replace('/', '%2F')
                    deck_search_str += f'&date_start={date_str}'
                elif since_date:
                    deck_search_str += f'&date_start={start_date_enc}'
            response = post(f'{mtgtop8_base_url}/search', data=deck_search_str, headers={'referer': f'{mtgtop8_base_url}/search', 'Content-Type': 'application/x-www-form-urlencoded'})
            compare_str = 'checkall=1'

            decks_matching_regex = compile('<div class=w_title align=center>([0-9]+) decks matching<div class=c_tl></div>')
            deck_count = int(decks_matching_regex.findall(response.text)[0])
            if deck_count == 0:
                print('No matching decks.')
                exit()
            elif deck_count < 25 and (deck_count < max_number_decks_archetype):
                max_number_decks_archetype = deck_count

            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('input')
            n = 1
            # Get deck references
            for link in links:
                try:
                    value = int(link.attrs['value'])
                    if value != 1:
                        value_str = link.attrs['value']
                        if (len(deck) + n) <= max_number_decks: # Stop before reaching the max number of decks to analyze      
                            compare_str += f'&deck_check%5B{n}%5D=1&deck_ref%5B{n}%5D={value_str}'
                            n += 1
                except Exception:
                    pass

            if compare_str == 'checkall=1': # No more decks available
                break

            # Deck comparison
            deck_section = ''
            card_count_regex = compile('<div class="c">([0-9]{0,2})</div>')
            
            # Deck comparison to get all the cards
            response = post(f'{mtgtop8_base_url}/compare', data = compare_str, headers={'referer': '{mtgtop8_base_url}/search', 'Content-Type': 'application/x-www-form-urlencoded'})   
            soup = BeautifulSoup(response.text, 'html.parser') # Parse the HTML content
            links = soup.find_all('a') # Find all the links on the page

            # Discover the decks
            current_decks = {}
            for link in links:
                href = link.get('href')
                if href:
                    href = href.lower()
                    if href.startswith('event?e='):
                        deck_id = href.split('&d=')[1]
                        # Create the deck
                        current_decks[deck_id] = {'main': {}, 'side': {}}

            # Parse the table of decks and cards
            table = soup.find_all('table')
            if table:
                table = table[-1]
                rows = table.find_all('tr')
                deck_part = 'main'
                deck_section = ''

                for row in rows:
                    cols = row.find_all('td')
                    card = ''
                    for col in cols:
                        if col:
                            # Detect sections
                            if col.text == 'LANDS':
                                deck_section = 'lands'
                                deck_part = 'main'
                            elif col.text == 'CREATURES':
                                deck_section = 'creatures'
                                deck_part = 'main'
                            elif col.text == 'OTHER SPELLS':
                                deck_section = 'other spells'
                                deck_part = 'main'
                            elif col.text == 'SIDEBOARDS':
                                deck_section = 'sideboard'
                                deck_part = 'side'
                            # Discover cards
                            card_name = col.find('div', {'class': 'c2'})
                            if card_name:
                                if card_name.text:
                                    card = card_name.text
                                    deck_iter = iter(current_decks)
                                    deck_cpt = 0
                            # Discover card counts
                            card_counts = card_count_regex.findall(str(col))
                            if card_counts and (deck_cpt < max_number_decks_archetype):
                                card_count = card_counts[0]
                                # Iterate over decks
                                current_deck = next(deck_iter)
                                # Add card to deck if counted in the deck
                                if card_count:
                                    quantity=int(card_count)
                                    current_decks[current_deck][deck_part][card] = [quantity, deck_section] # A card is added with a quantity and the righ section
                                deck_cpt += 1
                                
            deck = deck | current_decks
            n_page += 1

        decks = decks | deck
                 
    if not decks:
        print('No matching decks found')
        exit()

    # For EDH on mtgtop8.com, determine if different commanders to be able to filter on
    if 'EDH' in mtg_format:
        commanders = []
        # Find all used commanders
        for deck in decks:
            side_cards = decks[deck]['side']
            for card in side_cards:
                commanders.append(card)
        fixed_commander = ''
        commander_choice_str = '0 - Any\n'
        # Detect if a commander is always used anyway
        for commander in commanders:
            if commanders.count(commander) == len(decks):
                fixed_commander = commander
        commanders = set(commanders) # Turn it into a set to keep only unique values
        if fixed_commander:
            commanders.remove(fixed_commander)
        commanders_dict = {0: 'Any'}
        n = 1
        for commander in commanders:
            commander_choice_str += f'{n} - {commander}\n'
            commanders_dict[n] = commander
            n += 1
        if len(commanders) > 1:
            if fixed_commander:
                print(f'{fixed_commander} is used in all analyzed decks as Commander.')
            print('Different commanders are used in analyzed decks. Select those you want to keep. If you want to select multiple commanders, use comma-separated choices (e.g. "1, 2")')
            # Commander choice
            selected_commanders = []
            while not selected_commanders:
                commander_choices = Prompt.ask(commander_choice_str, show_choices=False)
                try:
                    commander_choices = commander_choices.split(',')
                    for choice in commander_choices:
                        selected_commanders.append(commanders_dict[int(choice)])
                    if not selected_commanders:
                        print('Invalid choice.')
                except Exception:
                    print('Invalid choice.')
            if {0: 'Any'} in selected_commanders:
                selected_commanders = [] 
            # Let's not forget to consider an always used commander if any
            if fixed_commander:
                selected_commanders.append(fixed_commander) 
            # Only keep decks using selected commanders
            filtered_decks = {}
            for deck in decks:
                commander_present_in_side = False
                side_cards = decks[deck]['side']
                for selected_commander in selected_commanders:
                    if selected_commander in side_cards:
                        commander_present_in_side = True
                if commander_present_in_side:
                    filtered_decks[deck] = decks[deck]
            decks = filtered_decks

    if not top_method:
        # Determine number of decks using each card and average number of cards in using decks
        main_avg_card_counts = {}
        side_avg_card_counts = {}
    else:
        # Determine number of decks using each card and top chosen number of cards in using decks
        main_top_card_counts = {}
        side_top_card_counts = {}

    # avg number of lands, creatures and other spells
    if balance:
        section_avg = {'lands':0, 'creatures':0, 'other spells': 0} # option chosen
    elif balance_lands:
        section_avg = {'lands':0, 'creatures':1000, 'other spells': 1000} # option chosen only for lands
    else:
        section_avg = {'lands':1000, 'creatures':1000, 'other spells': 1000} # option not chosen then set no limits

    for deck in decks:
        main_cards = decks[deck]['main']
        for card in main_cards:
            quantity = decks[deck]['main'][card][0]
            section = decks[deck]['main'][card][1]
            if not top_method:
                if card not in main_avg_card_counts:
                    main_avg_card_counts[card] = [1, quantity, quantity, section] # [number of using decks, total quantity, avg, section]
                else:
                    main_avg_card_counts[card][0] += 1
                    main_avg_card_counts[card][1] += quantity
                    main_avg_card_counts[card][2] = round(main_avg_card_counts[card][1] / main_avg_card_counts[card][0])
            else:
                if card not in main_top_card_counts:
                    main_top_card_counts[card] = [1, {quantity:1}, quantity, section] # [number of using decks, all quantities, top chosen quantity, section]
                else:
                    main_top_card_counts[card][0] += 1
                    if quantity not in main_top_card_counts[card][1]:
                        main_top_card_counts[card][1][quantity] = 1
                    else:
                        main_top_card_counts[card][1][quantity] += 1
                    main_top_card_counts[card][2] = max(main_top_card_counts[card][1], key=main_top_card_counts[card][1].get)
        
            # Compute average number of cards per section to have these as targets if option is chosen
            if balance:
                section_avg[section] += quantity
            elif balance_lands:
                if section == 'lands':
                    section_avg[section] += quantity

        side_cards = decks[deck]['side']
        for card in side_cards:
            quantity = decks[deck]['side'][card][0]
            section = decks[deck]['side'][card][1]
            if not top_method:
                if card not in side_avg_card_counts:
                    side_avg_card_counts[card] = [1, quantity, quantity, section] # [number of using decks, total quantity, avg, section]
                else:
                    side_avg_card_counts[card][0] += 1
                    side_avg_card_counts[card][1] += quantity
                    side_avg_card_counts[card][2] = round(side_avg_card_counts[card][1] / side_avg_card_counts[card][0])
            else:
                if card not in side_top_card_counts:
                    side_top_card_counts[card] = [1, {quantity:1}, quantity, section] # [number of using decks, all quantities, top chosen quantity, section]
                else:
                    side_top_card_counts[card][0] += 1
                    if quantity not in side_top_card_counts[card][1]:
                        side_top_card_counts[card][1][quantity] = 1
                    else:
                        side_top_card_counts[card][1][quantity] += 1
                    side_top_card_counts[card][2] = max(side_top_card_counts[card][1], key=side_top_card_counts[card][1].get)

    # Finish compute of average number of cards per section to have these as targets if option is chosen
    if balance:
        for section, avg in section_avg.items():
            section_avg[section] = round(avg / len(decks))
    elif balance_lands:
        section_avg['lands'] = round(section_avg['lands'] / len(decks))

    # For EDH and cEDH format, adapt target number of cards in deck
    if ('EDH' in mtg_format) or ('Commander' in mtg_format):
        main_target = 99
        side_target = 1
        # If the first parsed deck has 2 EDH commanders, let's adjust the targets
        if len(decks[list(decks)[0]]['side']) == 2:
            main_target = 98
            side_target = 2
    else:
        main_target = 60
        side_target = 15

    if top_method:
        # Sort by top used cards and build average deck
        sorted_main_top_card_counts = sorted(main_top_card_counts.items(), key=lambda x: x[1][0], reverse=True)
        sorted_side_top_card_counts = sorted(side_top_card_counts.items(), key=lambda x: x[1][0], reverse=True)
        avg_deck = build_avg_deck(sorted_main_top_card_counts, sorted_side_top_card_counts, main_target, side_target, section_avg, len(decks))
    else:
        # Sort by top used cards and build average deck
        sorted_main_avg_card_counts = sorted(main_avg_card_counts.items(), key=lambda x: x[1][0], reverse=True)
        sorted_side_avg_card_counts = sorted(side_avg_card_counts.items(), key=lambda x: x[1][0], reverse=True)
        avg_deck = build_avg_deck(sorted_main_avg_card_counts, sorted_side_avg_card_counts, main_target, side_target, section_avg, len(decks))

    print('\n')
    print_avg_deck(avg_deck, len(decks), print_with_details, maybeboard)
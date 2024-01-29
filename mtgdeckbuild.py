from argparse import ArgumentParser, RawTextHelpFormatter
from rich.prompt import Prompt
from requests import get, post
from urllib.parse import quote
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from re import compile, match


mtgtop8_base_url = 'https://mtgtop8.com'
mtgdecks_base_url = 'https://mtgdecks.net'
user_agent = {'User-agent': 'Mozilla/5.0'}


def select_format(mtg_source):
    '''
    Parses the website data source website to identify the available Magic: The Gathering formats and prompts the user to select a format.

    Args:
        mtg_source (str): The Magic: The Gathering website data source.

    Returns:
        The selected Magic: The Gathering format.
    '''

    # Format discovery
    format_choice_str = 'Select a format:\n'
    mtg_formats = {}
    if mtg_source == 'mtgtop8':
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
    elif mtg_source == 'mtgdecks':
        response = get(f'{mtgdecks_base_url}', headers=user_agent)
        soup = BeautifulSoup(response.text, 'html.parser')
        strongs = soup.find_all('strong')
        n = 1
        for strong in strongs:
            if strong.text.startswith('\xa0'):
                mtg_formats[n] = strong.text[2:]
                format_choice_str += f'{n} - {strong.text[2:].title()}\n'
                n += 1

    # Format choice
    format_choice = 0
    while format_choice == 0:
        format_choice = Prompt.ask(format_choice_str, choices=[f'{n}' for n in mtg_formats.keys()], show_choices=False)
        try:
            format_choice = int(format_choice)
            if format_choice == 0:
                print('Invalid choice.')
        except Exception:
            print('Invalid choice.')
    
    return mtg_formats[format_choice]


def select_archetype(mtg_source, mtg_format, top):
    '''
    Parses the website data source to identify the available Magic: The Gathering archetypes of a given format and prompts the user to select an archetype.
    
    Args:
        mtg_source (str): The Magic: The Gathering website data source.
        mtg_format (str): The Magic: The Gathering format.
        top (int): The number of top archetypes to select.

    Returns:
        The selected Magic: The Gathering archetype.
    '''

    # Archetypes discovery
    archetypes_list = []
    
    if mtg_source == 'mtgtop8':
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
    elif mtg_source == 'mtgdecks':
        response = get(f'{mtgdecks_base_url}/{mtg_format}', headers=user_agent)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            txt = link.text
            if href and txt:
                href = href.lower()
                # Only keep deck archetypes
                if ( href.startswith(f'{mtgdecks_base_url}/{mtg_format.lower()}/') or href.startswith(f'/{mtg_format.lower()}/') ) \
                    and ('/rotation-what-is-in-' not in href) \
                        and ('/staples' not in href) \
                            and ('/winrates' not in href) \
                                and ('/tournaments' not in href) \
                                    and ('/metagame' not in href):
                    if not href.startswith(f'{mtgdecks_base_url}/'):
                        href = f'{mtgdecks_base_url}{href}'
                    archetypes_list.append((href, txt))

    if top > 0:
        archetypes_list = sorted(archetypes_list[0:top], key=lambda x: x[1])
    else:
        archetypes_list = sorted(archetypes_list, key=lambda x: x[1])

    # Archetypes choice
    archetypes_dict = {}
    archetype_choice_str = 'Select an archetype:\n'
    n = 0
    for a in archetypes_list:
        archetypes_dict[n] = a[1]
        archetype_choice_str += f'{n+1} - {a[1]}\n'
        n += 1

    archetype_choice = 0
    while archetype_choice == 0:
        archetype_choice = Prompt.ask(archetype_choice_str, choices=[f'{n+1}' for n in archetypes_dict.keys()], show_choices=False)
        try:
            archetype_choice = int(archetype_choice) - 1
            if archetype_choice == 0:
                print('Invalid choice.')
        except Exception:
            print('Invalid choice.')

    return archetypes_list[archetype_choice][0]
    

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
        for section in avg_deck['main'].keys():
            sorted_section = sorted(avg_deck['main'][section].items(), key=lambda x: x[1], reverse=True)
            nb_cards_section = 0
            for card in sorted_section:
                nb_cards_section += card[1][0]
            print('//----------------------------------------------------------------------')
            print(f'// {section.upper()} - {nb_cards_section} cards')
            print('//----------------------------------------------------------------------')
            for card in sorted_section:
                print(f'{card[1][0]} {card[0]} - Used by {card[1][1]}/{total_decks} decks')
        
        # Sideboard
        sorted_side = sorted(avg_deck['side'].items(), key=lambda x: x[1], reverse=True)
        nb_cards_side = 0
        for card in sorted_side:
            nb_cards_side += card[1][0]
        print('//----------------------------------------------------------------------')
        print(f'// SIDEBOARD - {nb_cards_side} cards')
        print('//----------------------------------------------------------------------')
        for card in sorted_side:
            print(f'{card[1][0]} {card[0]} - Used by {card[1][1]}/{total_decks} decks')
       
        if maybeboard:
            # Maybeboard
            if 'maybeboard' in avg_deck.keys():
                print('//----------------------------------------------------------------------')
                print(f'// MAYBEBOARD - {len(avg_deck['maybeboard'].keys())} cards')
                print('//----------------------------------------------------------------------')
                for card in avg_deck['maybeboard'].keys():
                    print(f'{avg_deck['maybeboard'][card][0]} {card} - Used by {avg_deck['maybeboard'][card][1]}/{total_decks} decks')

    else:
        # Main deck
        main_cards = []
        for section in avg_deck['main'].keys():
            for card in avg_deck['main'][section].keys():
                main_cards.append([card, avg_deck['main'][section][card][0]])
        print('// MAIN DECK')
        for main_card in main_cards:
            print(f'{main_card[1]} {main_card[0]}')

        # Sideboard
        side_cards = []
        for card in avg_deck['side'].keys():
            side_cards.append([card, avg_deck['side'][card][0]])
        print('// SIDEBOARD')
        for side_card in side_cards:
            print(f'{side_card[1]} {side_card[0]}')
        
        if maybeboard:
            # Maybeboard
            if 'maybeboard' in avg_deck.keys():
                print('// MAYBEBOARD')
                for card in avg_deck['maybeboard'].keys():
                    print(f'{avg_deck['maybeboard'][card][0]} {card} - Used by {avg_deck['maybeboard'][card][1]}/{total_decks} decks')



def build_avg_deck(sorted_main_avg_card_counts, sorted_side_avg_card_counts, main_target, side_target):
    '''
    Builds an average deck based on the provided average card counts.

    Args:
        sorted_main_avg_card_counts (list): A sorted list of average card counts for the main deck. Each item in the list is a tuple of (card, [count, decks, section]).
        sorted_side_avg_card_counts (list): A sorted list of average card counts for the sideboard. Each item in the list is a tuple of (card, [count, decks, section]).
        main_target (int): The target number of cards for the main deck.
        side_target (int): The target number of cards for the sideboard.

    Returns:
        A dictionary representing the average deck.
    '''

    avg_deck = {'main': {'lands': {}, 'creatures': {}, 'other spells': {}}, 'side': {}}

    # Main deck building
    main_cards = []
    if sorted_main_avg_card_counts:
        main_deck_total = 0
        n = 0
        while not (main_deck_total == main_target): # Process while we haven't reached the target
            card_count = sorted_main_avg_card_counts[n]
            card = card_count[0]
            nb_decks = card_count[1][0]
            nb_cards = card_count[1][2]
            section = card_count[1][3]
            delta = main_target - main_deck_total
            # Add cards unless if we'll go over target number of cards, just reach the target so don't add the full cardset
            if nb_cards <= delta:
                avg_deck['main'][section][card] = [nb_cards, nb_decks]
                main_deck_total += nb_cards
            else:
                avg_deck['main'][section][card] = [delta, nb_decks]
                main_deck_total += delta
            main_cards.append(card)
            n += 1

        # Maybeboard
        if n < len(sorted_main_avg_card_counts):
            nb_decks_min = nb_decks
            nb_decks_next = sorted_main_avg_card_counts[n][1][0]
            while ( (nb_decks_next == nb_decks_min) or (nb_decks_next == (nb_decks_min-1)) ):
                card_count = sorted_main_avg_card_counts[n]
                card = card_count[0]
                nb_decks = card_count[1][0]
                nb_cards = card_count[1][2]
                if 'maybeboard' not in avg_deck.keys():
                    avg_deck['maybeboard'] = {}
                avg_deck['maybeboard'][card] = [nb_cards, nb_decks]
                n += 1
                if n < len(sorted_main_avg_card_counts):
                    nb_decks_next = sorted_main_avg_card_counts[n][1][0]
                else:
                    break

    # Sideboard building
    if sorted_side_avg_card_counts:
        side_deck_total = 0
        n = 0
        while not (side_deck_total == side_target): # Process while we haven't reached the target
            card_count = sorted_side_avg_card_counts[n]
            card = card_count[0]
            nb_decks = card_count[1][0]
            nb_cards = card_count[1][2]
            delta = side_target - side_deck_total
            # Add cards unless if we'll go over target number of cards, just reach the target so don't add the full cardset
            if card not in main_cards:
                if nb_cards <= delta:
                    avg_deck['side'][card] = [nb_cards, nb_decks]
                    side_deck_total += nb_cards
                else:
                    avg_deck['side'][card] = [delta, nb_decks]
                    side_deck_total += delta
            n += 1
        
        # Maybeboard
        if n < len(sorted_main_avg_card_counts):
            nb_decks_min = nb_decks
            nb_decks_next = sorted_main_avg_card_counts[n][1][0]
            while ( (nb_decks_next == nb_decks_min) or (nb_decks_next == (nb_decks_min-1)) ):
                card_count = sorted_main_avg_card_counts[n]
                card = card_count[0]
                nb_decks = card_count[1][0]
                nb_cards = card_count[1][2]
                if card not in main_cards:
                    if 'maybeboard' not in avg_deck.keys():
                        avg_deck['maybeboard'] = {}
                    avg_deck['maybeboard'][card] = [nb_cards, nb_decks]
                n += 1
                if n < len(sorted_main_avg_card_counts):
                    nb_decks_next = sorted_main_avg_card_counts[n][1][0]
                else:
                    break
    
    return avg_deck


if __name__ == '__main__':

    # Argument parsing from command-line
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '--website-source', '-w',
        type = str,
        action = 'store',
        default = 'mtgtop8',
        help = 'Website data source to use (mtgtop8 or mtgdecks ; default: mtgtop8)'
    )

    parser.add_argument(
        '--top-archetypes', '-t',
        type = int,
        action = 'store',
        default = 0,
        help = 'The number of top archetypes to parse (default: all archetypes)'
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
        help = 'Only consider competitive decks (only for MTGTOP8)'
    )

    parser.add_argument(
        '--name', '-n',
        type = str,
        action='store',
        help = 'Only consider decks including given deck name (only for MTGTOP8)'
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
        help = 'Consider cards to include for the main deck (must be used with --include-cards/-i, also include cards for the sideboard for MTGDECKS)'
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
        help = 'Only consider decks from the last given months (only for MTGTOP8)'
    )

    parser.add_argument(
        '--maybeboard',
        action = 'store_true',
        default = False,
        help = 'Print Maybeboard (additional cards that are tied or minus one in terms of number of decks using them)'
    )

    args = vars(parser.parse_args())

    mtg_source = args['website_source']
    allowed_sources = ['mtgtop8', 'mtgtop8.com', 'mtgdecks', 'mtgdecks.net']
    if mtg_source.lower() not in allowed_sources:
        print(f'{mtg_source} is not a supported source')
        exit()
    if mtg_source[-4] == '.':
        mtg_source = mtg_source[:-4]
    top = args['top_archetypes']
    if top and (top < 1):
        print('argument --top-archetypes/-t: cannot be lower than 1')
        exit()
    max_number_decks = args['decks']
    if max_number_decks and (max_number_decks < 1):
        print('argument --decks/-d: cannot be lower than 1')
        exit()
    print_with_details = args['print_details']
    competitive = args['competitive_only']
    if competitive and mtg_source == 'mtgdecks':
        print('argument --competitive-only/-c: cannot be used with website data source MTGDECKS')
        exit()
    deck_name = args['name']
    if deck_name and mtg_source == 'mtgdecks':
        print('argument --name/-n: cannot be used with website data source MTGDECKS')
        exit()
    included_cards = args['include_cards']
    if included_cards:
        if not match(r'^[\w\s\',]+(-[\w\s\', ]+)?$', included_cards):
            print('argument --include-cards/-i: must be a dash-separated list of strings')
            exit()
        else:
            if mtg_source == 'mtgtop8':
                included_cards = included_cards.replace(' - ', '\r\n')
                included_cards = included_cards.replace('-', '\r\n')
                included_cards = included_cards.replace('- ', '\r\n')
                included_cards = included_cards.replace(' -', '\r\n')
            elif mtg_source == 'mtgdecks':
                included_cards = included_cards.replace(' - ', ';')
                included_cards = included_cards.replace('-', ';')
                included_cards = included_cards.replace('- ', ';')
                included_cards = included_cards.replace(' -', ';')
    main_include = args['main_include']
    side_include = args['side_include']
    if (included_cards and not (main_include or side_include)) or (not included_cards and (main_include or side_include)):
        print('argument --include-cards/-i: must be used along with --main-include/-m and/or --side-include/-s')
        exit()
    last_months = args['last_months']
    if last_months and mtg_source == 'mtgdecks':
        print('argument --last-months/-l: cannot be used with website data source MTGDECKS')
        exit()
    if last_months and (last_months < 1):
        print('argument --last-months/-l: must be a positive number')
        exit()
    maybeboard = args['maybeboard']

    mtg_format = select_format(mtg_source)
    mtg_archetype = select_archetype(mtg_source, mtg_format, top)

    # Deck search
    decks = {}

    if mtg_source == 'mtgtop8':

        n_page = 1
        while len(decks.keys()) < max_number_decks:

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
            if last_months:
                date_str = (datetime.now()-timedelta(days=30*last_months)).strftime('%d/%m/%Y').replace('/', '%2F')
                deck_search_str += f'&date_start={date_str}'
            response = post(f'{mtgtop8_base_url}/search', data=deck_search_str, headers={'referer': f'{mtgtop8_base_url}/search', 'Content-Type': 'application/x-www-form-urlencoded'})
            compare_str = 'checkall=1'

            if 'O decks matching' in response.text:
                print('No matching decks.')
                exit()
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('input')
            n = 1
            # Get deck references
            for link in links:
                try:
                    value = int(link.attrs['value'])
                    if value != 1:
                        value_str = link.attrs['value']
                        if (len(decks.keys()) + n) <= max_number_decks: # Stop before reaching the max number of decks to analyze      
                            compare_str += f'&deck_check%5B{n}%5D=1&deck_ref%5B{n}%5D={value_str}'
                            n += 1
                except Exception:
                    pass

            if compare_str == 'checkall=1': # No more decks available
                break

            # Deck comparison
            deck_section = ''
            card_count_regex = compile('<div class="c">([1-9]{0,2})</div>')
            
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
                            # Discover card counts
                            card_counts = card_count_regex.findall(str(col))
                            for card_count in card_counts:
                                # Iterate over decks
                                current_deck = next(deck_iter)
                                # Add card to deck if counted in the deck     
                                if card_count:
                                    quantity=int(card_count)
                                    current_decks[current_deck][deck_part][card] = [quantity, deck_section] # A card is added with a quantity and the righ section
            
            decks = decks | current_decks
            n_page += 1

    elif mtg_source == 'mtgdecks':
        deck_links = []
        reached_target_nb_decks = False
        previous_first_link = ''
        n = 1
        while not reached_target_nb_decks:
            deck_search_str = ''
            if (main_include or side_include):
                deck_search_str += 'cards:'
                for card in included_cards.split(';'):
                    if side_include:
                        deck_search_str += f'SB:{quote(card)}{quote(';')}'
                    if main_include:
                        deck_search_str += f'{quote(card)}{quote(';')}'
                    deck_search_str = deck_search_str[0:-3]
            response = get(f'{mtg_archetype}/page:{n}/{deck_search_str}', headers=user_agent)
            if 'NO DECKS FOUND' in response.text:
                reached_target_nb_decks = True
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if ('-decklist-by-' in href):
                    first_link = link
                    break
            if first_link == previous_first_link:
                reached_target_nb_decks = True
                break
            for link in links:
                href = link.get('href')
                # Discover the decks
                if href:
                    if len(deck_links) < max_number_decks:
                        if ('-decklist-by-' in href):
                            if f'{mtgdecks_base_url}{href}' not in deck_links:
                                deck_links.append(f'{mtgdecks_base_url}{href}')
                    else:
                        reached_target_nb_decks = True
            previous_first_link = first_link
            n += 1
        for deck_link in deck_links:
            # Create the deck
            decks[deck_link[-7:]] = {'main': {}, 'side': {}}
            deck_part = ''
            deck_section = ''
            response = get(deck_link, headers=user_agent)
            soup = BeautifulSoup(response.text, 'html.parser')
            tables = soup.find_all('table')
            # Parse the tables of cards
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('th')
                    for col in cols:
                        # Detect sections
                        if col.has_attr('class'):
                            if col['class'][1] == 'Creature':
                                deck_section = 'creatures'
                                deck_part = 'main'
                            elif col['class'][1] == 'Land':
                                deck_section = 'lands'
                                deck_part = 'main'
                            elif col['class'][1] == 'Sideboard':
                                deck_section = 'sideboard'
                                deck_part = 'side'
                            else:
                                deck_section = 'other spells'
                                deck_part = 'main'
                    # Discover cards
                    if row.has_attr('data-required'):
                        quantity=int(row['data-required'])
                        decks[deck_link[-7:]][deck_part][row['data-card-id']] = [quantity, deck_section] # A card is added with a quantity and the righ section
                    
    if not decks:
        print('No matching decks found')
        exit()

    # For EDH on mtgtop8.com, determine if different commanders to be able to filter on
    if 'EDH' in mtg_format and mtg_source == 'mtgtop8':
        commanders = []
        # Find all used commanders
        for deck in decks.keys():
            side_cards = decks[deck]['side'].keys()
            for card in side_cards:
                commanders.append(card)
        fixed_commander = ''
        commander_choice_str = ''
        # Detect if a commander is always used anyway
        for commander in commanders:
            if commanders.count(commander) == len(decks.keys()):
                fixed_commander = commander
        commanders = set(commanders) # Turn it into a set to keep only unique values
        if fixed_commander:
            commanders.remove(fixed_commander)
        commanders_dict = {}
        n = 0
        for commander in commanders:
            commander_choice_str += f'{n+1} - {commander}\n'
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
                        selected_commanders.append(commanders_dict[int(choice)-1])
                    if not selected_commanders:
                        print('Invalid choice.')
                except Exception:
                    print('Invalid choice.')
            # Let's not forget to consider an always used commander if any
            if fixed_commander:
                selected_commanders.append(fixed_commander) 
            # Only keep decks using selected commanders
            filtered_decks = {}
            for deck in decks.keys():
                commander_present_in_side = False
                side_cards = decks[deck]['side'].keys()
                for selected_commander in selected_commanders:
                    if selected_commander in side_cards:
                        commander_present_in_side = True
                if commander_present_in_side:
                    filtered_decks[deck] = decks[deck]
            decks = filtered_decks

    # Determine number of decks using each card and average number of cards in using decks
    main_avg_card_counts = {}
    side_avg_card_counts = {}

    for deck in decks.keys():

        main_cards = decks[deck]['main'].keys()
        for card in main_cards:
            quantity = decks[deck]['main'][card][0]
            section = decks[deck]['main'][card][1]
            if card not in main_avg_card_counts.keys():
                main_avg_card_counts[card] = [1, quantity, quantity, section] # [number of using decks, total quantity, avg, section]
            else:
                main_avg_card_counts[card][0] += 1
                main_avg_card_counts[card][1] += quantity
                main_avg_card_counts[card][2] = round(main_avg_card_counts[card][1] / main_avg_card_counts[card][0])
            
        side_cards = decks[deck]['side'].keys()
        for card in side_cards:
            quantity = decks[deck]['side'][card][0]
            section = decks[deck]['side'][card][1]
            if card not in side_avg_card_counts.keys():
                side_avg_card_counts[card] = [1, quantity, quantity, section] # [number of using decks, total quantity, avg, section]
            else:
                side_avg_card_counts[card][0] += 1
                side_avg_card_counts[card][1] += quantity
                side_avg_card_counts[card][2] = round(side_avg_card_counts[card][1] / side_avg_card_counts[card][0])
        
    # Sort by top used cards
    sorted_main_avg_card_counts = sorted(main_avg_card_counts.items(), key=lambda x: x[1][0], reverse=True)
    sorted_side_avg_card_counts = sorted(side_avg_card_counts.items(), key=lambda x: x[1][0], reverse=True)

    # For EDH and cEDH format, adapt target number of cards in deck
    if ('EDH' in mtg_format) or ('Commander' in mtg_format):
        main_target = 99
        side_target = 1
        # If the first parsed deck has 2 EDH commanders, let's adjust the targets
        if len(decks[list(decks.keys())[0]]['side']) == 2:
            main_target = 98
            side_target = 2
    else:
        main_target = 60
        side_target = 15

    avg_deck = build_avg_deck(sorted_main_avg_card_counts, sorted_side_avg_card_counts, main_target, side_target)

    print('\n')
    print_avg_deck(avg_deck, len(decks.keys()), print_with_details, maybeboard)
from argparse import ArgumentParser, RawTextHelpFormatter
from rich.prompt import Prompt
from requests import get, post
from bs4 import BeautifulSoup
from re import compile


if __name__ == '__main__':

    # Argument parsing from command-line
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '--details', '-d',
        action = 'store_true',
        help = 'Print deck with details: sections and number of decks using each card'
    )

    parser.add_argument(
        '--minimum-number-of-decks', '-m',
        type = int,
        action = 'store',
        help = 'Minimum number of decks playing each card (default: automatically adjust the result to match the deck format\'s number of cards)'
    )

    parser.add_argument(
        '--competitive-only', '-c',
        action = 'store_true',
        default = False,
        help = 'Only consider competitive decks'
    )

    args = vars(parser.parse_args())
    print_with_details = args['details']
    min_decks = args['minimum_number_of_decks']
    if min_decks:
        if min_decks < 1:
            print('Minimum number of decks must be positive.')
            exit()
    competitive = args['competitive_only']

    mtgtop8_baseurl = 'https://mtgtop8.com'
    user_agent = {'User-agent': 'Mozilla/5.0'}

    # Format discovery
    format_choice_str = 'Select a format:\n'
    mtg_formats = {}
    response = get(f'{mtgtop8_baseurl}', headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    n = 1
    for link in links:
        href = link.get('href')
        if href:
            if href.startswith('/format?f='):
                mtg_formats[n] = href.split('=')[1]
                format_choice_str += f'{n} - {link.text.title()}\n'
                n += 1

    # Format choice
    format_choice = 0
    while format_choice == 0:
        format_choice = Prompt.ask(format_choice_str, choices=[f'{n}' for n in mtg_formats.keys()])
        try:
            format_choice = int(format_choice)
            if format_choice == 0:
                print('Invalid choice.')
        except:
            print('Invalid choice.')
    
    mtg_format = mtg_formats[format_choice]

    # Archetypes discovery
    archetypes_list = []
    response = get(f'{mtgtop8_baseurl}/format?f={mtg_format}', headers = user_agent)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Process the HTML content
    links = soup.find_all('a')
    for link in links:
        # Find all the links on the page
        href = link.get('href')
        txt = link.text
        if href and txt:
            href = href.lower()
            # Only keep deck archetypes
            if href.startswith('archetype?a='):
                archetypes_list.append((href.split('archetype?a=')[1].split('&')[0], txt))

    archetypes_list = sorted(archetypes_list, key=lambda x: x[1])

    # Archetypes choice
    archetypes_dict = {}
    archetype_choice_str = f'Select an archetype:\n'
    n = 0
    for a in archetypes_list:
        archetypes_dict[n] = a[1]
        archetype_choice_str += f'{n+1} - {a[1]}\n'
        n += 1

    archetype_choice = 0
    while archetype_choice == 0:
        archetype_choice = Prompt.ask(archetype_choice_str, choices=[f'{n+1}' for n in archetypes_dict.keys()])
        try:
            archetype_choice = int(archetype_choice) - 1
            if archetype_choice == 0:
                print('Invalid choice.')
        except:
            print('Invalid choice.')

    mtg_archetype = archetypes_list[archetype_choice][0]

    # Deck search
    deck_search_str = f'current_page=&format={mtg_format}&archetype_sel%5B{mtg_format}%5D={mtg_archetype}'
    if competitive:
        deck_search_str += f'&compet_check%5BP%5D=1&compet_check%5BM%5D=1&compet_check%5BC%5D=1'
    response = post(f'{mtgtop8_baseurl}/search', data=deck_search_str, headers={'referer': f'{mtgtop8_baseurl}/search', 'Content-Type': 'application/x-www-form-urlencoded'})
    compare_str = 'checkall=1'

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Process the HTML content
    links = soup.find_all('input')
    n = 1
    for link in links:
        try:
            value = int(link.attrs['value'])
            if value != 1:
                value_str = link.attrs['value']
                compare_str += f'&deck_check%5B{n}%5D=1&deck_ref%5B{n}%5D={value_str}'
                n += 1
        except:
            pass


    # Deck comparison
    response = post(f'{mtgtop8_baseurl}/compare', data = compare_str, headers={'referer': f'{mtgtop8_baseurl}/search', 'Content-Type': 'application/x-www-form-urlencoded'})

    soup = BeautifulSoup(response.text, 'html.parser')
    cards = {}
    table = soup.find_all('table')[-1]

    rows = table.find_all('tr')

    deck_section = ''

    for row in rows:
        cols = row.find_all('td')
        card = ''
        for col in cols:
            # Discover sections
            if col.text == 'LANDS':
                deck_section = 'LANDS'
                cards[deck_section] = {}
            elif col.text == 'CREATURES':
                deck_section = 'CREATURES'
                cards[deck_section] = {}
            elif col.text == 'OTHER SPELLS':
                deck_section = 'OTHER SPELLS'
                cards[deck_section] = {}
            elif col.text == 'SIDEBOARDS':
                deck_section = 'SIDEBOARDS'
                cards[deck_section] = {}
            card_name = col.find('div', {'class': 'c2'})
            # Discover cards
            if card_name:
                if card_name.text:
                    card = card_name.text
                    if not (card in cards[deck_section].keys()):
                        cards[deck_section][card] = [0, 0, 0]
            # Discover card counts
            if col:
                cards_counts = compile('<div class="c">([0-9]{1,2})<\/div>').findall(str(col))
                if cards_counts:
                    card_count = cards_counts[0]
                    cards[deck_section][card][0] = cards[deck_section][card][0] + int(card_count)
                    cards[deck_section][card][1] = cards[deck_section][card][1]+1
                    cards[deck_section][card][2] = round(cards[deck_section][card][0] / cards[deck_section][card][1], 1)

    sorted_cards = {}

    for deck_section in cards.keys():
        sorted_deck_section = sorted(cards[deck_section].items(), key=lambda x:x[1], reverse=True)
        sorted_cards[deck_section] = sorted_deck_section

    print(f'\n')
    main_total_cards = 0
    side_total_cards = 0
    main_target = 60
    side_target = 15
    if 'EDH' in mtg_format: # Adapt fromat's target number of cards for DC
        main_target = 99
        side_target = 2     
    # If the minimum number of decks using each card is provided, use it, else automatically adjust the result to match the format number of cards (except for DC)
    if min_decks:
        print(f'Minimum number of decks using each card: {min_decks}\n')
        # Print the cards
        for deck_section in sorted_cards.keys():
            nb_cards = 0
            if print_with_details:
                print('//--------------------------------------------------')
            if (not print_with_details) and (deck_section == 'SIDEBOARDS'):
                print(f'// {deck_section}')
            for card in cards[deck_section].items():
                card[1][2] = int(round(card[1][2], 0))
                if card[1][1] >= min_decks:
                    nb_cards = nb_cards + card[1][2]
            if deck_section != 'SIDEBOARDS':
                main_total_cards += nb_cards
            else:
                side_total_cards += nb_cards
            if print_with_details:
                print(f'{deck_section} x{int(round(nb_cards, 0))}')
                print('//--------------------------------------------------')
            for card in sorted(cards[deck_section].items(), key=lambda x:x[1][1], reverse=True):
                if card[1][1] >= min_decks:
                    if print_with_details:
                        print(f'{card[1][2]}x {card[0]} - used in {card[1][1]}/{n-1} decks')
                    else:
                        print(f'{card[1][2]} {card[0]}')
        print(f'Total of {main_total_cards} cards in main deck and {side_total_cards} in sideboard')
    else:
        # Main deck
        min_decks_main = 12
        main_total_cards = 0
        main_target_delta = abs(main_target-main_total_cards)
        while True:
            previous_main_total_cards = main_total_cards
            main_total_cards = 0
            # Count number of cards we can add to main deck
            for deck_section in sorted_cards.keys():
                if deck_section != 'SIDEBOARDS':
                    nb_cards = 0
                    for card in cards[deck_section].items():
                        card[1][2] = int(round(card[1][2], 0))
                        if card[1][1] >= min_decks_main:
                            nb_cards += card[1][2]
                    main_total_cards += nb_cards
            previous_delta = main_target_delta
            main_target_delta = abs(main_target-main_total_cards)
            if main_target_delta == 0: # We reached the target, let's stop
                break
            if previous_delta < main_target_delta: # Previous search was better, we went to far
                min_decks_main = previous_min_decks_main # We keep the previous found optimal number of decks using each card
                main_total_cards = previous_main_total_cards # We keep the previous found optimal number of cards for main
                break # We break the loop
            elif previous_delta > main_target_delta: # This search is better
                if (main_target-main_total_cards) > 0: # We are lower than the target, let's decrease the minimum number of decks for next search
                    previous_min_decks_main = min_decks_main
                    min_decks_main -= 1
                else: # We are higher than the target, let's increase the minimum number of decks for next search
                    previous_min_decks_main = min_decks_main
                    min_decks_main += 1
            else: # This search is equal to the previous one
                if main_total_cards <= previous_main_total_cards: # We haven't increase the number of cards, let's continue
                    if (main_target-main_total_cards) > 0: # We are lower than the target, let's decrease the minimum number of decks for next search
                        previous_min_decks_main = min_decks_main
                        min_decks_main -= 1
                    else: # We are higher than the target, let's increase the minimum number of decks for next search
                        previous_min_decks_main = min_decks_main
                        min_decks_main += 1
                else: # We increased the number of cards, let's stop
                    break
        # Sideboard
        min_decks_side = 12
        side_total_cards = 0
        side_target_delta = abs(side_target-side_total_cards)
        while True:
            previous_side_total_cards = side_total_cards
            side_total_cards = 0
            # Count number of cards we can add to sideboard
            for deck_section in sorted_cards.keys():
                if deck_section == 'SIDEBOARDS':
                    nb_cards = 0
                    for card in cards[deck_section].items():
                        card[1][2] = int(round(card[1][2], 0))
                        if card[1][1] >= min_decks_side:
                            nb_cards += card[1][2]
                    side_total_cards += nb_cards
            previous_delta = side_target_delta
            side_target_delta = abs(side_target-side_total_cards)
            if side_target_delta == 0: # We reached the target, let's stop
                break
            elif previous_delta < side_target_delta: # Previous search was better, we went to far
                min_decks_side = previous_min_decks_side # We keep the previous found optimal number of decks using each card
                side_total_cards = previous_side_total_cards # We keep the previous found optimal number of cards for side
                break # We break the loop
            elif previous_delta > side_target_delta: # This search is better
                if (side_target-side_total_cards) > 0: # We are lower than the target, let's decrease the minimum number of decks for next search
                    previous_min_decks_side = min_decks_side
                    min_decks_side -= 1
                else: # We are higher than the target, let's increase the minimum number of decks for next search
                    previous_min_decks_side = min_decks_side
                    min_decks_side += 1
            else: # This search is equal to the previous one
                if side_total_cards <= previous_side_total_cards: # We haven't increase the number of cards, let's continue
                    if (side_target-side_total_cards) > 0: # We are lower than the target, let's decrease the minimum number of decks for next search
                        previous_min_decks_side = min_decks_side
                        min_decks_side -= 1
                    else: # We are higher than the target, let's increase the minimum number of decks for next search
                        previous_min_decks_side = min_decks_side
                        min_decks_side += 1
                else: # We increased the number of cards, let's stop
                    break
        # Print the cards
        for deck_section in sorted_cards.keys():
            nb_cards = 0
            if print_with_details:
                print(f'//--------------------------------------------------')
            if (not print_with_details) and (deck_section == 'SIDEBOARDS'):
                print(f'// {deck_section}')
            for card in cards[deck_section].items():
                if deck_section != 'SIDEBOARDS':
                    if card[1][1] >= min_decks_main:
                        card[1][2] = int(round(card[1][2], 0))
                        nb_cards = nb_cards + card[1][2]
                else:
                    if card[1][1] >= min_decks_side:
                        card[1][2] = int(round(card[1][2], 0))
                        nb_cards = nb_cards + card[1][2]
            if print_with_details:
                print(f'// {deck_section} x{int(round(nb_cards, 0))}')
                print(f'//--------------------------------------------------')
            for card in sorted(cards[deck_section].items(), key=lambda x:x[1][1], reverse=True):
                if deck_section != 'SIDEBOARDS':
                    if card[1][1] >= min_decks_main:
                        if print_with_details:
                            print(f'{card[1][2]}x {card[0]} - used in {card[1][1]}/{n-1} decks')
                        else:
                            print(f'{card[1][2]} {card[0]}')
                else:
                    if card[1][1] >= min_decks_side:
                        if print_with_details:
                            print(f'{card[1][2]}x {card[0]} - used in {card[1][1]}/{n-1} decks')
                        else:
                            print(f'{card[1][2]} {card[0]}')
        print(f'\nTotal of {main_total_cards} cards in main deck and {side_total_cards} in sideboard\n')
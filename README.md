# mtgdeckbuild
A Magic: The Gathering format archetype average deck building tool based on tournament results from MTGTOP8.

# MTGDeckBuild
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)  
---  
A Magic: The Gathering format archetype average deck building tool based on tournaments results from MTGTOP8. Deck building is based on currently played archetypes and most used cards in tournaments decks. Several options are available to fine tune your deck building.

## Features

* Support of [MTGTOP8](https://mtgtop8.com) as website data source.
* By default, interactive mode to chose the format with automatic format discovery.
* Interactive mode to chose the archetype(s) with automatic archetype discovery and possibility to only list a number of top played archetype.
* By default, possibility to specify the format and archetype as an option to avoid interactive mode.
* Possibility to specify the maximum number of decks to analyze (default: 20).
* Filtering available to only consider competitive decks.
* Filtering available to only consider decks including given card names in main deck and/or sideboard.
* Filtering available to only consider decks including given deck names.
* Filtering available to only consider decks over the last given months.
* Two methods available to determine the quantity of each card in the average deck: average quantity (default) or top chosen quantity amongst analyzed decks (except when last cards are added in order to avoid going over the deck limits).
* Possibility to target a number of cards per section in the average deck based on the average number of cards per section in the analyzed decks while locking the lands section target.
* Possibility to display a Maybeboard section with all the cards that are tied or minus a number (analyzed decks / 4) in terms of number of decks using them for main deck and sideboard.
* Simple or detailed printing of the average decklist available.

## Requirements

Make sure you have [Python 3.10 or higher](https://www.python.org/downloads/) and [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) installed.  

## Installation 

#### Clone the repository to your working directory 
```
$ git clone https://github.com/thibaut-probst/mtgdeckbuild.git
$ cd mtgdeckbuild/
```
#### Install the dependencies
```
$ pip install -r requirements.txt
```

## Usage 

You can display ***MTGDeckBuild*** startup parameters information by using the --help argument: 

```
$ python3 mtgdeckbuild.py -h
usage: mtgdeckbuild.py [-h] [--top-archetypes TOP_ARCHETYPES] [--format FORMAT] [--archetype ARCHETYPE] [--decks DECKS] [--print-details] [--competitive-only]
                       [--name NAME] [--include-cards INCLUDE_CARDS] [--main-include] [--side-include] [--last-months LAST_MONTHS] [--since SINCE]
                       [--top-quantity] [--balance] [--balance-lands] [--maybeboard]

options:
  -h, --help            show this help message and exit
  --top-archetypes TOP_ARCHETYPES, -t TOP_ARCHETYPES
                        The number of top archetypes to parse (default: all archetypes)
  --format FORMAT, -f FORMAT
                        The format to analyze (default: interactive mode)
  --archetype ARCHETYPE, -a ARCHETYPE
                        The archetype to analyze (default: interactive mode, must be used along with --format/-f)
  --decks DECKS, -d DECKS
                        The maximum number of decks to analyze (default: 25)
  --print-details, -p   Print deck with details: sections and number of decks using each card
  --competitive-only, -c
                        Only consider competitive decks
  --name NAME, -n NAME  Only consider decks including given deck name
  --include-cards INCLUDE_CARDS, -i INCLUDE_CARDS
                        Only consider decks including given cards (use dash-separated card names if passing multiple cards, must be used with --main-deck/-m, --sideboard/-s arguments or both)
  --main-include, -m    Consider cards to include for the main deck (must be used with --include-cards/-i)
  --side-include, -s    Consider cards to include for the sideboard (must be used with --include-cards/-i)
  --last-months LAST_MONTHS, -l LAST_MONTHS
                        Only consider decks from the last given months
  --since SINCE, -S SINCE
                        Only consider decks since the given start date (DD-MM-YYYY)
  --top-quantity, -T    Build average deck based on the top used quantity for each most used card in analyzed decks (default: based on the average quantity)
  --balance, -b         Balance the number of cards for each section (lands, creatures, other spells) based on the average number of cards per section in the analyzed decks (default: do not balance and just retain the most used cards)
  --balance-lands, -B   Balance the number of cards for the lands section based on the average number of lands in the analyzed decks (default: do not balance and just retain the most used cards)
  --maybeboard, -M      Print Maybeboard (additional cards that are tied or minus a number (analyzed decks / 4) in terms of number of decks using them for main deck and sideboard)
```

## Examples
Legacy Burn average deck with interactive mode:
```
$ python3 mtgdeckbuild.py 
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian Highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - cEDH
16 - Duel Commander
17 - Premodern
: 12
Select an archetype:
0 - All archetypes
1 - 4/5c Control
2 - Affinity
3 - All my Spells
4 - Arclight Phoenix
5 - Artifacts Blue
6 - BUG Control
7 - BUG Midrange
8 - Bant Control
9 - Boros Aggro
10 - Burn
11 - Cascade Crash
12 - Cephalid Breakfast
13 - Cloudpost Ramp
14 - Cradle Control
15 - Dark Depths
16 - Death & Taxes
17 - Death's Shadow
18 - Delver (Other)
19 - Dimir Tempo
20 - Doomsday
21 - Dragon Stompy
22 - Dredge
23 - Eldrazi Aggro
24 - Esper Vial
25 - Goblins
26 - Grixis Aggro
27 - High Tide
28 - Infect
29 - Initiative Stompy
30 - Jund
31 - Lands
32 - Landstill
33 - MUD
34 - Merfolk
35 - Mississippi River
36 - Mono Black Aggro
37 - Mono Black Combo
38 - Mono Red Combo
39 - Mystic Forge
40 - Nadu
41 - Nic Fit 
42 - Ninja
43 - Other - Aggro
44 - Other - Combo
45 - Other - Control
46 - Painter
47 - Patriot Aggro
48 - Rakdos Aggro
49 - Reanimator
50 - Show and Tell
51 - Stiflenought
52 - Stoneblade
53 - Storm
54 - Turbo Necro
55 - UR Aggro
56 - UWx Control
: 10


// MAIN DECK
13 Mountain
2 Arid Mesa
2 Wooded Foothills
2 Bloodstained Mire
4 Monastery Swiftspear
4 Eidolon of the Great Revel
4 Goblin Guide
4 Chain Lightning
4 Fireblast
4 Lava Spike
4 Lightning Bolt
4 Rift Bolt
4 Price of Progress
3 Skewer the Critics
2 Roiling Vortex
// SIDEBOARD
3 Smash to Smithereens
2 Pyroblast
2 Red Elemental Blast
2 Faerie Macabre
2 Grafdigger's Cage
2 Ensnaring Bridge
1 Meltdown
1 Leyline of the Void
```
Legacy Burn average deck with detailed printing and top quantity for each card:
```
$ python3 mtgdeckbuild.py -f LE -a Burn -T -p


//----------------------------------------------------------------------
// LANDS - 18 cards
//----------------------------------------------------------------------
9 Mountain - Used by 25/25 decks (100%)
2 Arid Mesa - Used by 15/25 decks (60%)
2 Barbarian Ring - Used by 12/25 decks (48%)
2 Bloodstained Mire - Used by 11/25 decks (44%)
2 Scalding Tarn - Used by 9/25 decks (36%)
1 Wooded Foothills - Used by 13/25 decks (52%)
//----------------------------------------------------------------------
// CREATURES - 12 cards
//----------------------------------------------------------------------
4 Monastery Swiftspear - Used by 25/25 decks (100%)
4 Eidolon of the Great Revel - Used by 24/25 decks (96%)
4 Goblin Guide - Used by 21/25 decks (84%)
//----------------------------------------------------------------------
// OTHER SPELLS - 30 cards
//----------------------------------------------------------------------
4 Chain Lightning - Used by 25/25 decks (100%)
4 Fireblast - Used by 25/25 decks (100%)
4 Lava Spike - Used by 25/25 decks (100%)
4 Lightning Bolt - Used by 25/25 decks (100%)
4 Rift Bolt - Used by 25/25 decks (100%)
4 Price of Progress - Used by 24/25 decks (96%)
4 Skewer the Critics - Used by 23/25 decks (92%)
2 Roiling Vortex - Used by 17/25 decks (68%)
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Leyline of the Void - Used by 10/25 decks (40%)
2 Smash to Smithereens - Used by 25/25 decks (100%)
2 Pyroblast - Used by 15/25 decks (60%)
2 Faerie Macabre - Used by 11/25 decks (44%)
2 Exquisite Firecraft - Used by 7/25 decks (28%)
1 Red Elemental Blast - Used by 12/25 decks (48%)
1 Grafdigger's Cage - Used by 11/25 decks (44%)
1 Ensnaring Bridge - Used by 9/25 decks (36%)
```
Legacy Burn average deck considering only competitive decks with detailed printing and top quantity for each card:
```
$ python3 mtgdeckbuild.py -f LE -a Burn -c -T -p


//----------------------------------------------------------------------
// LANDS - 18 cards
//----------------------------------------------------------------------
18 Mountain - Used by 24/25 decks (96%)
//----------------------------------------------------------------------
// CREATURES - 12 cards
//----------------------------------------------------------------------
4 Goblin Guide - Used by 23/25 decks (92%)
4 Monastery Swiftspear - Used by 23/25 decks (92%)
4 Eidolon of the Great Revel - Used by 20/25 decks (80%)
//----------------------------------------------------------------------
// OTHER SPELLS - 30 cards
//----------------------------------------------------------------------
4 Lightning Bolt - Used by 25/25 decks (100%)
4 Chain Lightning - Used by 24/25 decks (96%)
4 Fireblast - Used by 24/25 decks (96%)
4 Lava Spike - Used by 24/25 decks (96%)
4 Price of Progress - Used by 23/25 decks (92%)
4 Rift Bolt - Used by 23/25 decks (92%)
4 Skewer the Critics - Used by 20/25 decks (80%)
2 Roiling Vortex - Used by 14/25 decks (56%)
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Smash to Smithereens - Used by 21/25 decks (84%)
4 Leyline of the Void - Used by 14/25 decks (56%)
4 Exquisite Firecraft - Used by 9/25 decks (36%)
2 Faerie Macabre - Used by 9/25 decks (36%)
1 Pyroblast - Used by 14/25 decks (56%)
```
Modern UB Mill average deck considering only competitive decks using the 50 last decks with detailed printing:
```
$ python3 mtgdeckbuild.py -f MO -a "UB Mill" -c -d 50 -p


//----------------------------------------------------------------------
// LANDS - 25 cards
//----------------------------------------------------------------------
4 Field of Ruin - Used by 49/50 decks (98%)
4 Island - Used by 47/50 decks (94%)
4 Polluted Delta - Used by 43/50 decks (86%)
3 Flooded Strand - Used by 30/50 decks (60%)
2 Misty Rainforest - Used by 28/50 decks (56%)
2 Scalding Tarn - Used by 27/50 decks (54%)
1 Oboro, Palace in the Clouds - Used by 46/50 decks (92%)
1 Watery Grave - Used by 46/50 decks (92%)
1 Otawara, Soaring City - Used by 42/50 decks (84%)
1 Shelldock Isle - Used by 40/50 decks (80%)
1 Undercity Sewers - Used by 34/50 decks (68%)
1 Swamp - Used by 33/50 decks (66%)
//----------------------------------------------------------------------
// CREATURES - 8 cards
//----------------------------------------------------------------------
4 Hedron Crab - Used by 50/50 decks (100%)
4 Ruin Crab - Used by 50/50 decks (100%)
//----------------------------------------------------------------------
// OTHER SPELLS - 27 cards
//----------------------------------------------------------------------
4 Archive Trap - Used by 50/50 decks (100%)
4 Fractured Sanity - Used by 49/50 decks (98%)
4 Fatal Push - Used by 34/50 decks (68%)
4 Drown in the Loch - Used by 32/50 decks (64%)
3 Surgical Extraction - Used by 49/50 decks (98%)
3 Visions of Beyond - Used by 46/50 decks (92%)
3 Tasha's Hideous Laughter - Used by 44/50 decks (88%)
2 Jace, the Perfected Mind - Used by 38/50 decks (76%)
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
3 Ensnaring Bridge - Used by 40/50 decks (80%)
3 Soul-Guide Lantern - Used by 35/50 decks (70%)
3 Extirpate - Used by 29/50 decks (57%)
2 Crypt Incursion - Used by 34/50 decks (68%)
2 Consign to Memory - Used by 23/50 decks (46%)
1 Engineered Explosives - Used by 21/50 decks (42%)
1 Toxic Deluge - Used by 15/50 decks (30%)
```
Duel-Commander Phelia, the Exuberant Shepherd average deck considering only competitive decks over the last month:
```
$ python3 mtgdeckbuild.py -f DC -a Phelia -c -l 1 -p
Archetype not found: Phelia
Did you mean Phelia, Exuberant Shepherd? [y/n] (y): 


//----------------------------------------------------------------------
// LANDS - 39 cards
//----------------------------------------------------------------------
23 Snow-Covered Plains - Used by 13/15 decks (87%)
1 Eiganjo, Seat of the Empire - Used by 14/15 decks (93%)
1 Flagstones of Trokair - Used by 14/15 decks (93%)
1 Tectonic Edge - Used by 14/15 decks (93%)
1 Dust Bowl - Used by 13/15 decks (87%)
1 Crystal Vein - Used by 12/15 decks (80%)
1 Eiganjo Castle - Used by 12/15 decks (80%)
1 Urza's Saga - Used by 12/15 decks (80%)
1 Rishadan Port - Used by 12/15 decks (80%)
1 Mishra's Factory - Used by 11/15 decks (73%)
1 War Room - Used by 11/15 decks (73%)
1 Gemstone Caverns - Used by 10/15 decks (67%)
1 Mutavault - Used by 10/15 decks (67%)
1 City of Traitors - Used by 9/15 decks (60%)
1 Castle Ardenvale - Used by 8/15 decks (53%)
1 Scavenger Grounds - Used by 8/15 decks (53%)
1 Talon Gates of Madara - Used by 7/15 decks (47%)
//----------------------------------------------------------------------
// CREATURES - 32 cards
//----------------------------------------------------------------------
1 Giver of Runes - Used by 15/15 decks (100%)
1 Mother of Runes - Used by 15/15 decks (100%)
1 Recruiter of the Guard - Used by 15/15 decks (100%)
1 Solitude - Used by 15/15 decks (100%)
1 Steel Seraph - Used by 15/15 decks (100%)
1 Stoneforge Mystic - Used by 15/15 decks (100%)
1 White Plume Adventurer - Used by 15/15 decks (100%)
1 Containment Priest - Used by 14/15 decks (93%)
1 Elite Spellbinder - Used by 14/15 decks (93%)
1 Esper Sentinel - Used by 14/15 decks (93%)
1 Guide of Souls - Used by 14/15 decks (93%)
1 Novice Inspector - Used by 14/15 decks (93%)
1 Palace Jailer - Used by 14/15 decks (93%)
1 Seasoned Dungeoneer - Used by 14/15 decks (93%)
1 Skrelv, Defector Mite - Used by 14/15 decks (93%)
1 Skyclave Apparition - Used by 14/15 decks (93%)
1 Thraben Inspector - Used by 14/15 decks (93%)
1 Witch Enchanter - Used by 14/15 decks (93%)
1 Blade Splicer - Used by 13/15 decks (87%)
1 Drannith Magistrate - Used by 13/15 decks (87%)
1 Restoration Angel - Used by 11/15 decks (73%)
1 Serra Paragon - Used by 10/15 decks (67%)
1 Benevolent Bodyguard - Used by 10/15 decks (67%)
1 Cathar Commando - Used by 9/15 decks (60%)
1 Flickerwisp - Used by 9/15 decks (60%)
1 Samwise the Stouthearted - Used by 9/15 decks (60%)
1 Sanctifier en-Vec - Used by 8/15 decks (53%)
1 Thalia, Guardian of Thraben - Used by 8/15 decks (53%)
1 Toby, Beastie Befriender - Used by 8/15 decks (53%)
1 Ocelot Pride - Used by 7/15 decks (47%)
1 Overlord of the Mistmoors - Used by 7/15 decks (47%)
1 Astrid Peth - Used by 6/15 decks (40%)
//----------------------------------------------------------------------
// OTHER SPELLS - 28 cards
//----------------------------------------------------------------------
1 Ephemerate - Used by 15/15 decks (100%)
1 Invasion of Gobakhan - Used by 15/15 decks (100%)
1 Ossification - Used by 15/15 decks (100%)
1 Parallax Wave - Used by 15/15 decks (100%)
1 Skullclamp - Used by 15/15 decks (100%)
1 Swords to Plowshares - Used by 15/15 decks (100%)
1 Cataclysm - Used by 14/15 decks (93%)
1 Pre-War Formalwear - Used by 14/15 decks (93%)
1 Razorgrass Ambush - Used by 14/15 decks (93%)
1 Static Prison - Used by 14/15 decks (93%)
1 Arcum's Astrolabe - Used by 13/15 decks (87%)
1 Council's Judgment - Used by 13/15 decks (87%)
1 Mana Tithe - Used by 13/15 decks (87%)
1 On Thin Ice - Used by 13/15 decks (87%)
1 Reverent Mantra - Used by 13/15 decks (87%)
1 Staff of the Storyteller - Used by 13/15 decks (87%)
1 Swift Reconfiguration - Used by 13/15 decks (87%)
1 The Wandering Emperor - Used by 13/15 decks (87%)
1 March of Otherworldly Light - Used by 12/15 decks (80%)
1 Portable Hole - Used by 12/15 decks (80%)
1 Oust - Used by 11/15 decks (73%)
1 Reprieve - Used by 11/15 decks (73%)
1 Shadowspear - Used by 11/15 decks (73%)
1 Unexpectedly Absent - Used by 10/15 decks (67%)
1 Umezawa's Jitte - Used by 9/15 decks (60%)
1 Enlightened Tutor - Used by 8/15 decks (53%)
1 Batterskull - Used by 7/15 decks (47%)
1 Tangle Wire - Used by 7/15 decks (47%)
//----------------------------------------------------------------------
// SIDEBOARD - 1 cards
//----------------------------------------------------------------------
1 Phelia, Exuberant Shepherd - Used by 15/15 decks (100%)
```
Duel-Commander Yoshimaru, Ever Faithful average deck considering only competitive decks and a selected partner with interactive mode suggesting only top 10 archetypes and detailed printing:
```
$ python3 mtgdeckbuild.py -t 10 -c -p
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian Highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - cEDH
16 - Duel Commander
17 - Premodern
: 16
Select an archetype:
0 - All archetypes
1 - Aragorn, King Of Gondor
2 - Atraxa, Grand Unifier
3 - Ertai Resurrected
4 - Feldon, Ronom Excavator
5 - Partner WR
6 - Phelia, Exuberant Shepherd
7 - Phlage, Titan Of Fire's Fury
8 - Satya, Aetherflux Genius
9 - Slimefoot And Squee
10 - Tamiyo, Inquisitive Student
: 5
Different commanders are used in analyzed decks. Select those you want to keep. If you want to select multiple commanders, use comma-separated choices (e.g. "1, 2")
0 - Any
1 - Dargo, the Shipwrecker
2 - Gut, True Soul Zealot
3 - Yoshimaru, Ever Faithful
4 - Bruse Tarl, Boorish Herder
5 - Veteran Soldier
: 3


//----------------------------------------------------------------------
// LANDS - 38 cards
//----------------------------------------------------------------------
5 Snow-Covered Plains - Used by 15/24 decks (62%)
1 Arid Mesa - Used by 24/24 decks (100%)
1 Bloodstained Mire - Used by 24/24 decks (100%)
1 Command Tower - Used by 24/24 decks (100%)
1 Eiganjo, Seat of the Empire - Used by 24/24 decks (100%)
1 Flooded Strand - Used by 24/24 decks (100%)
1 Inspiring Vantage - Used by 24/24 decks (100%)
1 Marsh Flats - Used by 24/24 decks (100%)
1 Minas Tirith - Used by 24/24 decks (100%)
1 Sacred Foundry - Used by 24/24 decks (100%)
1 Sokenzan, Crucible of Defiance - Used by 24/24 decks (100%)
1 Windswept Heath - Used by 24/24 decks (100%)
1 Wooded Foothills - Used by 24/24 decks (100%)
1 Battlefield Forge - Used by 23/24 decks (96%)
1 Eiganjo Castle - Used by 23/24 decks (96%)
1 Flagstones of Trokair - Used by 23/24 decks (96%)
1 Plateau - Used by 23/24 decks (96%)
1 Plaza of Heroes - Used by 23/24 decks (96%)
1 Shinka, the Bloodsoaked Keep - Used by 23/24 decks (96%)
1 Prismatic Vista - Used by 22/24 decks (92%)
1 Scalding Tarn - Used by 22/24 decks (92%)
1 Hammerheim - Used by 22/24 decks (92%)
1 Sunbaked Canyon - Used by 21/24 decks (88%)
1 Urza's Saga - Used by 21/24 decks (88%)
1 Clifftop Retreat - Used by 20/24 decks (83%)
1 Mines of Moria - Used by 20/24 decks (83%)
1 Rugged Prairie - Used by 20/24 decks (83%)
1 Den of the Bugbear - Used by 19/24 decks (79%)
1 Needleverge Pathway - Used by 18/24 decks (75%)
1 Snow-Covered Mountain - Used by 15/24 decks (62%)
1 Sundown Pass - Used by 15/24 decks (62%)
1 Arena of Glory - Used by 14/24 decks (57%)
1 Gemstone Caverns - Used by 14/24 decks (57%)
1 Elegant Parlor - Used by 13/24 decks (54%)
//----------------------------------------------------------------------
// CREATURES - 39 cards
//----------------------------------------------------------------------
1 Broadside Bombardiers - Used by 24/24 decks (100%)
1 Fury - Used by 24/24 decks (100%)
1 Headliner Scarlett - Used by 24/24 decks (100%)
1 Kari Zev, Skyship Raider - Used by 24/24 decks (100%)
1 Laelia, the Blade Reforged - Used by 24/24 decks (100%)
1 Merry, Esquire of Rohan - Used by 24/24 decks (100%)
1 Mother of Runes - Used by 24/24 decks (100%)
1 Phelia, Exuberant Shepherd - Used by 24/24 decks (100%)
1 Solitude - Used by 24/24 decks (100%)
1 White Plume Adventurer - Used by 24/24 decks (100%)
1 Adeline, Resplendent Cathar - Used by 23/24 decks (96%)
1 Ajani, Nacatl Pariah - Used by 23/24 decks (96%)
1 Feldon, Ronom Excavator - Used by 23/24 decks (96%)
1 Phlage, Titan of Fire's Fury - Used by 23/24 decks (96%)
1 Loyal Apprentice - Used by 22/24 decks (92%)
1 Thalia, Guardian of Thraben - Used by 22/24 decks (92%)
1 Skyclave Apparition - Used by 22/24 decks (92%)
1 Baird, Argivian Recruiter - Used by 21/24 decks (88%)
1 Seasoned Dungeoneer - Used by 21/24 decks (88%)
1 Senu, Keen-Eyed Protector - Used by 21/24 decks (88%)
1 Giver of Runes - Used by 20/24 decks (83%)
1 Inti, Seneschal of the Sun - Used by 20/24 decks (83%)
1 Skrelv, Defector Mite - Used by 20/24 decks (83%)
1 Arbaaz Mir - Used by 20/24 decks (83%)
1 Pyrogoyf - Used by 20/24 decks (83%)
1 Samwise the Stouthearted - Used by 19/24 decks (79%)
1 Stoneforge Mystic - Used by 19/24 decks (79%)
1 Tajic, Legion's Edge - Used by 19/24 decks (79%)
1 Thalia, Heretic Cathar - Used by 19/24 decks (79%)
1 Squee, Dubious Monarch - Used by 18/24 decks (75%)
1 Anim Pakal, Thousandth Moon - Used by 16/24 decks (67%)
1 Mabel, Heir to Cragflame - Used by 16/24 decks (67%)
1 Boromir, Warden of the Tower - Used by 16/24 decks (67%)
1 Zurgo Bellstriker - Used by 15/24 decks (62%)
1 Drannith Magistrate - Used by 14/24 decks (57%)
1 Ash, Party Crasher - Used by 14/24 decks (57%)
1 Cathar Commando - Used by 12/24 decks (50%)
1 Palace Jailer - Used by 12/24 decks (50%)
1 Sanctifier en-Vec - Used by 10/24 decks (42%)
//----------------------------------------------------------------------
// OTHER SPELLS - 21 cards
//----------------------------------------------------------------------
1 Chain Lightning - Used by 24/24 decks (100%)
1 Flowering of the White Tree - Used by 24/24 decks (100%)
1 Lightning Bolt - Used by 24/24 decks (100%)
1 Parallax Wave - Used by 24/24 decks (100%)
1 Pyrokinesis - Used by 24/24 decks (100%)
1 Swords to Plowshares - Used by 24/24 decks (100%)
1 Shadowspear - Used by 23/24 decks (96%)
1 Forth Eorlingas! - Used by 22/24 decks (92%)
1 Galadriel's Dismissal - Used by 20/24 decks (83%)
1 Embercleave - Used by 19/24 decks (79%)
1 Reverent Mantra - Used by 18/24 decks (75%)
1 Pre-War Formalwear - Used by 17/24 decks (71%)
1 Skullclamp - Used by 17/24 decks (71%)
1 Sundering Eruption - Used by 17/24 decks (71%)
1 Flame Slash - Used by 17/24 decks (71%)
1 Swift Reconfiguration - Used by 16/24 decks (67%)
1 Static Prison - Used by 15/24 decks (62%)
1 Ghostfire Slice - Used by 14/24 decks (57%)
1 Galvanic Discharge - Used by 12/24 decks (50%)
1 On Thin Ice - Used by 12/24 decks (50%)
1 Enlightened Tutor - Used by 11/24 decks (46%)
//----------------------------------------------------------------------
// SIDEBOARD - 2 cards
//----------------------------------------------------------------------
1 Yoshimaru, Ever Faithful - Used by 24/24 decks (100%)
1 Bruse Tarl, Boorish Herder - Used by 19/24 decks (79%)
```
Standard Gruul Aggro average deck where the deck names includes "Dino" considering only decks over the last 1 month:
```
$ python3 mtgdeckbuild.py -n Dino -l 1
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian Highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - cEDH
16 - Duel Commander
17 - Premodern
: 9
Select an archetype:
1 - 4/5C Control
2 - 4/5c Aggro
3 - Abzan Aggro
4 - Angels
5 - Azorius Aggro
6 - Bant Aggro
7 - Bant Control
8 - Boros Aggro
9 - Dimir Aggro
10 - Dimir Control
11 - Esper Aggro
12 - Esper Control
13 - Golgari Aggro
14 - Grixis Aggro
15 - Grixis Control
16 - Gruul Aggro
17 - Izzet Control
18 - Jeskai Aggro
19 - Jeskai Control
20 - Jund
21 - Mono Black Aggro
22 - Mono Black Control
23 - Mono Blue Aggro
24 - Mono Green Aggro
25 - Mono Red Control
26 - Mono White Control 
27 - Naya Aggro
28 - Naya Control
29 - Orzhov Aggro
30 - Orzhov Control
31 - Other - Aggro
32 - Other - Control
33 - Rakdos Aggro
34 - Rakdos Control
35 - Reanimator
36 - Red Deck Wins
37 - Selesnya Aggro
38 - Simic Aggro
39 - Sultai Aggro
40 - Sultai Control
41 - UR Aggro
42 - UW Control
43 - Weenie White 
: 16


// MAIN DECK
7 Forest
3 Karplusan Forest
3 Cavern of Souls
2 Copperline Gorge
4 Mountain
2 Rockfall Vale
2 Restless Ridgeline
1 Sokenzan, Crucible of Defiance
1 Boseiju, Who Endures
4 Hulking Raptor
4 Intrepid Paleontologist
3 Trumpeting Carnosaur
3 Bonehoard Dracosaur
4 Ixalli's Lorekeeper
4 Pugnacious Hammerskull
2 Itzquinth, Firstborn of Gishath
4 Palani's Hatcher
3 Huatli, Poet of Unity
4 Triumphant Chomp
// SIDEBOARD
4 Scytheclaw Raptor
2 Itzquinth, Firstborn of Gishath
3 Tamiyo's Safekeeping
4 Thrashing Brontodon
2 Earthshaker Dreadmaw
```
Standard Gruul Aggro average deck using the 100 last decks:
```
$ python3 mtgdeckbuild.py -f ST -a Gruul -d 100
Archetype not found: Gruul
Did you mean Gruul Aggro? [y/n] (y): 


// MAIN DECK
4 Copperline Gorge
4 Karplusan Forest
6 Mountain
4 Thornspire Verge
2 Restless Ridgeline
2 Rockface Village
4 Emberheart Challenger
4 Heartfire Hero
4 Monastery Swiftspear
4 Slickshot Show-Off
3 Manifold Mouse
1 Questing Druid
4 Monstrous Rage
2 Snakeskin Veil
4 Might of the Meek
4 Shock
4 Turn Inside Out
// SIDEBOARD
3 Urabrask's Forge
2 Obliterating Bolt
3 Torch the Tower
2 Pawpatch Formation
2 Scorching Shot
2 Pick Your Poison
1 Ghost Vacuum
```
Standard Gruul Aggro average deck considering only the last 50 decks with maybeboard, balance of the deck section, top quantity for each card and detailed printing:
```
$ python3 mtgdeckbuild.py -f ST -a "Gruul Aggro" -d 50 -M -T -b -p


//----------------------------------------------------------------------
// LANDS - 21 cards
//----------------------------------------------------------------------
6 Mountain - Used by 50/50 decks (100%)
4 Copperline Gorge - Used by 50/50 decks (100%)
4 Karplusan Forest - Used by 50/50 decks (100%)
4 Thornspire Verge - Used by 49/50 decks (98%)
2 Restless Ridgeline - Used by 35/50 decks (70%)
1 Rockface Village - Used by 34/50 decks (68%)
//----------------------------------------------------------------------
// CREATURES - 21 cards
//----------------------------------------------------------------------
4 Emberheart Challenger - Used by 47/50 decks (94%)
4 Heartfire Hero - Used by 46/50 decks (92%)
4 Monastery Swiftspear - Used by 46/50 decks (92%)
4 Slickshot Show-Off - Used by 41/50 decks (82%)
4 Manifold Mouse - Used by 40/50 decks (80%)
1 Questing Druid - Used by 35/50 decks (70%)
//----------------------------------------------------------------------
// OTHER SPELLS - 18 cards
//----------------------------------------------------------------------
4 Monstrous Rage - Used by 47/50 decks (94%)
4 Might of the Meek - Used by 40/50 decks (80%)
4 Shock - Used by 32/50 decks (64%)
3 Innkeeper's Talent - Used by 35/50 decks (70%)
2 Snakeskin Veil - Used by 44/50 decks (88%)
1 Turn Inside Out - Used by 17/50 decks (34%)
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Torch the Tower - Used by 43/50 decks (86%)
3 Urabrask's Forge - Used by 48/50 decks (96%)
2 Pawpatch Formation - Used by 40/50 decks (80%)
2 Pick Your Poison - Used by 36/50 decks (72%)
2 Scorching Shot - Used by 36/50 decks (72%)
1 Obliterating Bolt - Used by 40/50 decks (80%)
1 Ghost Vacuum - Used by 31/50 decks (62%)
//----------------------------------------------------------------------
// MAYBEBOARD - 17 cards
//----------------------------------------------------------------------
4 Cacophony Scamp - Used by 14/50 decks (28%)
4 Leyline of Resonance - Used by 13/50 decks (26%)
4 Torch the Tower - Used by 7/50 decks (14%)
2 Witch's Mark - Used by 7/50 decks (14%)
2 Callous Sell-Sword - Used by 6/50 decks (12%)
1 Forest - Used by 5/50 decks (10%)
```
Duel-Commander Aminatou, The Fateshifter average deck considering decks since a specific date, including a specific card in the main deck, with maybeboard, balance of the deck sections and detailed printing:
```
$ python3 mtgdeckbuild.py -f DC -a Aminatou -b -M -S 28-09-2024 -m -i "Archon of Cruelty" -p
Archetype not found: Aminatou
Did you mean Aminatou, The Fateshifter? [y/n] (y): 


//----------------------------------------------------------------------
// LANDS - 36 cards
//----------------------------------------------------------------------
1 Arid Mesa - Used by 24/24 decks (100%)
1 Bloodstained Mire - Used by 24/24 decks (100%)
1 Command Tower - Used by 24/24 decks (100%)
1 Darkslick Shores - Used by 24/24 decks (100%)
1 Flooded Strand - Used by 24/24 decks (100%)
1 Godless Shrine - Used by 24/24 decks (100%)
1 Hallowed Fountain - Used by 24/24 decks (100%)
1 Misty Rainforest - Used by 24/24 decks (100%)
1 Polluted Delta - Used by 24/24 decks (100%)
1 Scalding Tarn - Used by 24/24 decks (100%)
1 Scrubland - Used by 24/24 decks (100%)
1 Shadowy Backstreet - Used by 24/24 decks (100%)
1 Swamp - Used by 24/24 decks (100%)
1 Tundra - Used by 24/24 decks (100%)
1 Verdant Catacombs - Used by 24/24 decks (100%)
1 Watery Grave - Used by 24/24 decks (100%)
1 Windswept Heath - Used by 24/24 decks (100%)
1 Drowned Catacomb - Used by 23/24 decks (96%)
1 Marsh Flats - Used by 23/24 decks (96%)
1 Meticulous Archive - Used by 23/24 decks (96%)
1 Seachrome Coast - Used by 23/24 decks (96%)
1 Island - Used by 22/24 decks (92%)
1 Isolated Chapel - Used by 22/24 decks (92%)
1 Prismatic Vista - Used by 22/24 decks (92%)
1 Undercity Sewers - Used by 22/24 decks (92%)
1 Underground Sea - Used by 22/24 decks (92%)
1 Glacial Fortress - Used by 21/24 decks (88%)
1 Underground River - Used by 20/24 decks (83%)
1 Plains - Used by 19/24 decks (79%)
1 Reflecting Pool - Used by 18/24 decks (75%)
1 Gloomlake Verge - Used by 17/24 decks (71%)
1 Adarkar Wastes - Used by 16/24 decks (67%)
1 Snow-Covered Island - Used by 13/24 decks (54%)
1 Tomb Fortress - Used by 13/24 decks (54%)
1 Snow-Covered Swamp - Used by 12/24 decks (50%)
1 Floodfarm Verge - Used by 11/24 decks (46%)
//----------------------------------------------------------------------
// CREATURES - 19 cards
//----------------------------------------------------------------------
1 Archon of Cruelty - Used by 24/24 decks (100%)
1 Ashen Rider - Used by 24/24 decks (100%)
1 Spellseeker - Used by 24/24 decks (100%)
1 Agent of Treachery - Used by 23/24 decks (96%)
1 Lord of Change - Used by 23/24 decks (96%)
1 Magister of Worth - Used by 21/24 decks (88%)
1 Metamorphosis Fanatic - Used by 21/24 decks (88%)
1 Psychic Frog - Used by 21/24 decks (88%)
1 Grief - Used by 20/24 decks (83%)
1 Tivit, Seller of Secrets - Used by 20/24 decks (83%)
1 Hoarding Broodlord - Used by 18/24 decks (75%)
1 Troll of Khazad-dûm - Used by 18/24 decks (75%)
1 Overlord of the Floodpits - Used by 17/24 decks (71%)
1 Fallaji Archaeologist - Used by 15/24 decks (62%)
1 Rune-Scarred Demon - Used by 14/24 decks (57%)
1 Astral Dragon - Used by 14/24 decks (57%)
1 Overlord of the Balemurk - Used by 12/24 decks (50%)
1 Overlord of the Mistmoors - Used by 12/24 decks (50%)
1 Griselbrand - Used by 11/24 decks (46%)
//----------------------------------------------------------------------
// OTHER SPELLS - 44 cards
//----------------------------------------------------------------------
1 Balance - Used by 24/24 decks (100%)
1 Demonic Tutor - Used by 24/24 decks (100%)
1 Exhume - Used by 24/24 decks (100%)
1 Necromancy - Used by 24/24 decks (100%)
1 Persist - Used by 24/24 decks (100%)
1 Animate Dead - Used by 23/24 decks (96%)
1 Dance of the Dead - Used by 23/24 decks (96%)
1 Flash - Used by 23/24 decks (96%)
1 Force of Will - Used by 23/24 decks (96%)
1 Frantic Search - Used by 23/24 decks (96%)
1 Reanimate - Used by 23/24 decks (96%)
1 Tainted Indulgence - Used by 23/24 decks (96%)
1 Tainted Pact - Used by 23/24 decks (96%)
1 Unmarked Grave - Used by 23/24 decks (96%)
1 Bitter Triumph - Used by 22/24 decks (92%)
1 Collective Brutality - Used by 22/24 decks (92%)
1 Fatal Push - Used by 22/24 decks (92%)
1 Shallow Grave - Used by 22/24 decks (92%)
1 Swords to Plowshares - Used by 22/24 decks (92%)
1 Teferi, Time Raveler - Used by 22/24 decks (92%)
1 Daze - Used by 21/24 decks (88%)
1 Inquisition of Kozilek - Used by 21/24 decks (88%)
1 Intuition - Used by 21/24 decks (88%)
1 Thoughtseize - Used by 21/24 decks (88%)
1 Careful Study - Used by 20/24 decks (83%)
1 Corpse Dance - Used by 20/24 decks (83%)
1 Brainstorm - Used by 19/24 decks (79%)
1 Force Spike - Used by 19/24 decks (79%)
1 Tithing Blade - Used by 19/24 decks (79%)
1 Mana Tithe - Used by 18/24 decks (75%)
1 Unburial Rites - Used by 18/24 decks (75%)
1 Bone Shards - Used by 16/24 decks (67%)
1 Faithful Mending - Used by 16/24 decks (67%)
1 Ponder - Used by 16/24 decks (67%)
1 Wash Away - Used by 16/24 decks (67%)
1 Counterspell - Used by 15/24 decks (62%)
1 Mental Misstep - Used by 14/24 decks (57%)
1 Prismatic Ending - Used by 14/24 decks (57%)
1 Show and Tell - Used by 14/24 decks (57%)
1 Cling to Dust - Used by 13/24 decks (54%)
1 Oath of Kaya - Used by 12/24 decks (50%)
1 Currency Converter - Used by 11/24 decks (46%)
1 Lose Focus - Used by 11/24 decks (46%)
1 Preordain - Used by 10/24 decks (42%)
//----------------------------------------------------------------------
// SIDEBOARD - 1 cards
//----------------------------------------------------------------------
1 Aminatou, the Fateshifter - Used by 24/24 decks (100%)
//----------------------------------------------------------------------
// MAYBEBOARD - 40 cards
//----------------------------------------------------------------------
1 Concealed Courtyard - Used by 11/24 decks (46%)
1 Priest of Fell Rites - Used by 11/24 decks (46%)
1 Beza, the Bounding Spring - Used by 10/24 decks (42%)
1 Enlightened Tutor - Used by 10/24 decks (42%)
1 Spell Pierce - Used by 9/24 decks (38%)
1 Duress - Used by 9/24 decks (38%)
1 Snow-Covered Plains - Used by 8/24 decks (33%)
1 Orcish Bowmasters - Used by 8/24 decks (33%)
1 Buried Alive - Used by 8/24 decks (33%)
1 Mana Leak - Used by 7/24 decks (28%)
1 Spell Snare - Used by 7/24 decks (28%)
1 Emperor of Bones - Used by 7/24 decks (28%)
1 Snapcaster Mage - Used by 7/24 decks (28%)
1 Memory Lapse - Used by 7/24 decks (28%)
1 Shipwreck Marsh - Used by 7/24 decks (28%)
1 Clearwater Pathway - Used by 7/24 decks (28%)
1 Baleful Strix - Used by 6/24 decks (25%)
1 Barrowgoyf - Used by 6/24 decks (25%)
1 Drown in the Loch - Used by 6/24 decks (25%)
1 Sevinne's Reclamation - Used by 6/24 decks (25%)
1 Occult Epiphany - Used by 6/24 decks (25%)
1 Urborg, Tomb of Yawgmoth - Used by 6/24 decks (25%)
1 Dihada's Ploy - Used by 6/24 decks (25%)
1 Boggart Trawler - Used by 5/24 decks (21%)
1 Sauron's Ransom - Used by 5/24 decks (21%)
1 Abhorrent Oculus - Used by 5/24 decks (21%)
1 Deserted Beach - Used by 5/24 decks (21%)
1 Valgavoth, Terror Eater - Used by 5/24 decks (21%)
1 Ephemerate - Used by 5/24 decks (21%)
1 Personal Tutor - Used by 5/24 decks (21%)
1 Witch Enchanter - Used by 4/24 decks (17%)
1 Lim-Dûl's Vault - Used by 4/24 decks (17%)
1 Damn - Used by 4/24 decks (17%)
1 Otawara, Soaring City - Used by 4/24 decks (17%)
1 Consider - Used by 4/24 decks (17%)
1 Force of Negation - Used by 4/24 decks (17%)
1 Crabomination - Used by 4/24 decks (17%)
1 From the Catacombs - Used by 4/24 decks (17%)
1 Omen of the Sea - Used by 4/24 decks (17%)
1 Harvester of Misery - Used by 4/24 decks (17%)
```
```
Duel-Commander Aminatou, The Fateshifter average deck considering decks since a specific date, including a specific card in the main deck, with maybeboard, balance of the land section and detailed printing:
```
$ python3 mtgdeckbuild.py -f DC -a Aminatou -B -M -S 28-09-2024 -m -i "Archon of Cruelty" -p
Archetype not found: Aminatou
Did you mean Aminatou, The Fateshifter? [y/n] (y): 


//----------------------------------------------------------------------
// LANDS - 36 cards
//----------------------------------------------------------------------
1 Arid Mesa - Used by 24/24 decks (100%)
1 Bloodstained Mire - Used by 24/24 decks (100%)
1 Command Tower - Used by 24/24 decks (100%)
1 Darkslick Shores - Used by 24/24 decks (100%)
1 Flooded Strand - Used by 24/24 decks (100%)
1 Godless Shrine - Used by 24/24 decks (100%)
1 Hallowed Fountain - Used by 24/24 decks (100%)
1 Misty Rainforest - Used by 24/24 decks (100%)
1 Polluted Delta - Used by 24/24 decks (100%)
1 Scalding Tarn - Used by 24/24 decks (100%)
1 Scrubland - Used by 24/24 decks (100%)
1 Shadowy Backstreet - Used by 24/24 decks (100%)
1 Swamp - Used by 24/24 decks (100%)
1 Tundra - Used by 24/24 decks (100%)
1 Verdant Catacombs - Used by 24/24 decks (100%)
1 Watery Grave - Used by 24/24 decks (100%)
1 Windswept Heath - Used by 24/24 decks (100%)
1 Drowned Catacomb - Used by 23/24 decks (96%)
1 Marsh Flats - Used by 23/24 decks (96%)
1 Meticulous Archive - Used by 23/24 decks (96%)
1 Seachrome Coast - Used by 23/24 decks (96%)
1 Island - Used by 22/24 decks (92%)
1 Isolated Chapel - Used by 22/24 decks (92%)
1 Prismatic Vista - Used by 22/24 decks (92%)
1 Undercity Sewers - Used by 22/24 decks (92%)
1 Underground Sea - Used by 22/24 decks (92%)
1 Glacial Fortress - Used by 21/24 decks (88%)
1 Underground River - Used by 20/24 decks (83%)
1 Plains - Used by 19/24 decks (79%)
1 Reflecting Pool - Used by 18/24 decks (75%)
1 Gloomlake Verge - Used by 17/24 decks (71%)
1 Adarkar Wastes - Used by 16/24 decks (67%)
1 Snow-Covered Island - Used by 13/24 decks (54%)
1 Tomb Fortress - Used by 13/24 decks (54%)
1 Snow-Covered Swamp - Used by 12/24 decks (50%)
1 Floodfarm Verge - Used by 11/24 decks (46%)
//----------------------------------------------------------------------
// CREATURES - 20 cards
//----------------------------------------------------------------------
1 Archon of Cruelty - Used by 24/24 decks (100%)
1 Ashen Rider - Used by 24/24 decks (100%)
1 Spellseeker - Used by 24/24 decks (100%)
1 Agent of Treachery - Used by 23/24 decks (96%)
1 Lord of Change - Used by 23/24 decks (96%)
1 Magister of Worth - Used by 21/24 decks (88%)
1 Metamorphosis Fanatic - Used by 21/24 decks (88%)
1 Psychic Frog - Used by 21/24 decks (88%)
1 Grief - Used by 20/24 decks (83%)
1 Tivit, Seller of Secrets - Used by 20/24 decks (83%)
1 Hoarding Broodlord - Used by 18/24 decks (75%)
1 Troll of Khazad-dûm - Used by 18/24 decks (75%)
1 Overlord of the Floodpits - Used by 17/24 decks (71%)
1 Fallaji Archaeologist - Used by 15/24 decks (62%)
1 Rune-Scarred Demon - Used by 14/24 decks (57%)
1 Astral Dragon - Used by 14/24 decks (57%)
1 Overlord of the Balemurk - Used by 12/24 decks (50%)
1 Overlord of the Mistmoors - Used by 12/24 decks (50%)
1 Griselbrand - Used by 11/24 decks (46%)
1 Priest of Fell Rites - Used by 11/24 decks (46%)
//----------------------------------------------------------------------
// OTHER SPELLS - 43 cards
//----------------------------------------------------------------------
1 Balance - Used by 24/24 decks (100%)
1 Demonic Tutor - Used by 24/24 decks (100%)
1 Exhume - Used by 24/24 decks (100%)
1 Necromancy - Used by 24/24 decks (100%)
1 Persist - Used by 24/24 decks (100%)
1 Animate Dead - Used by 23/24 decks (96%)
1 Dance of the Dead - Used by 23/24 decks (96%)
1 Flash - Used by 23/24 decks (96%)
1 Force of Will - Used by 23/24 decks (96%)
1 Frantic Search - Used by 23/24 decks (96%)
1 Reanimate - Used by 23/24 decks (96%)
1 Tainted Indulgence - Used by 23/24 decks (96%)
1 Tainted Pact - Used by 23/24 decks (96%)
1 Unmarked Grave - Used by 23/24 decks (96%)
1 Bitter Triumph - Used by 22/24 decks (92%)
1 Collective Brutality - Used by 22/24 decks (92%)
1 Fatal Push - Used by 22/24 decks (92%)
1 Shallow Grave - Used by 22/24 decks (92%)
1 Swords to Plowshares - Used by 22/24 decks (92%)
1 Teferi, Time Raveler - Used by 22/24 decks (92%)
1 Daze - Used by 21/24 decks (88%)
1 Inquisition of Kozilek - Used by 21/24 decks (88%)
1 Intuition - Used by 21/24 decks (88%)
1 Thoughtseize - Used by 21/24 decks (88%)
1 Careful Study - Used by 20/24 decks (83%)
1 Corpse Dance - Used by 20/24 decks (83%)
1 Brainstorm - Used by 19/24 decks (79%)
1 Force Spike - Used by 19/24 decks (79%)
1 Tithing Blade - Used by 19/24 decks (79%)
1 Mana Tithe - Used by 18/24 decks (75%)
1 Unburial Rites - Used by 18/24 decks (75%)
1 Bone Shards - Used by 16/24 decks (67%)
1 Faithful Mending - Used by 16/24 decks (67%)
1 Ponder - Used by 16/24 decks (67%)
1 Wash Away - Used by 16/24 decks (67%)
1 Counterspell - Used by 15/24 decks (62%)
1 Mental Misstep - Used by 14/24 decks (57%)
1 Prismatic Ending - Used by 14/24 decks (57%)
1 Show and Tell - Used by 14/24 decks (57%)
1 Cling to Dust - Used by 13/24 decks (54%)
1 Oath of Kaya - Used by 12/24 decks (50%)
1 Currency Converter - Used by 11/24 decks (46%)
1 Lose Focus - Used by 11/24 decks (46%)
//----------------------------------------------------------------------
// SIDEBOARD - 1 cards
//----------------------------------------------------------------------
1 Aminatou, the Fateshifter - Used by 24/24 decks (100%)
//----------------------------------------------------------------------
// MAYBEBOARD - 30 cards
//----------------------------------------------------------------------
1 Concealed Courtyard - Used by 11/24 decks (46%)
1 Beza, the Bounding Spring - Used by 10/24 decks (42%)
1 Preordain - Used by 10/24 decks (42%)
1 Enlightened Tutor - Used by 10/24 decks (42%)
1 Spell Pierce - Used by 9/24 decks (38%)
1 Duress - Used by 9/24 decks (38%)
1 Snow-Covered Plains - Used by 8/24 decks (33%)
1 Orcish Bowmasters - Used by 8/24 decks (33%)
1 Buried Alive - Used by 8/24 decks (33%)
1 Mana Leak - Used by 7/24 decks (28%)
1 Spell Snare - Used by 7/24 decks (28%)
1 Emperor of Bones - Used by 7/24 decks (28%)
1 Snapcaster Mage - Used by 7/24 decks (28%)
1 Memory Lapse - Used by 7/24 decks (28%)
1 Shipwreck Marsh - Used by 7/24 decks (28%)
1 Clearwater Pathway - Used by 7/24 decks (28%)
1 Baleful Strix - Used by 6/24 decks (25%)
1 Barrowgoyf - Used by 6/24 decks (25%)
1 Drown in the Loch - Used by 6/24 decks (25%)
1 Sevinne's Reclamation - Used by 6/24 decks (25%)
1 Occult Epiphany - Used by 6/24 decks (25%)
1 Urborg, Tomb of Yawgmoth - Used by 6/24 decks (25%)
1 Dihada's Ploy - Used by 6/24 decks (25%)
1 Boggart Trawler - Used by 5/24 decks (21%)
1 Sauron's Ransom - Used by 5/24 decks (21%)
1 Abhorrent Oculus - Used by 5/24 decks (21%)
1 Deserted Beach - Used by 5/24 decks (21%)
1 Valgavoth, Terror Eater - Used by 5/24 decks (21%)
1 Ephemerate - Used by 5/24 decks (21%)
1 Personal Tutor - Used by 5/24 decks (21%)
```
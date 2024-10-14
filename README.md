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
* Possibility to display a Maybeboard section with all the cards that are tied or minus a number (analyzed decks / 5) in terms of number of decks using them for main deck and sideboard.
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
                       [--name NAME] [--include-cards INCLUDE_CARDS] [--main-include] [--side-include] [--last-months LAST_MONTHS] [--top-quantity] [--balance]
                       [--maybeboard]

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
  --top-quantity, -T    Build average deck based on the top used quantity for each most used card in analyzed decks (default: based on the average quantity)
  --balance, -b         Balance the number of cards for each section (lands, creatures, other spells) based on the average number of cards per section in then analyzed decks (default: do not balance and just retain the most used cards)
  --maybeboard, -M      Print Maybeboard (additional cards that are tied or minus one in terms of number of decks using them)
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
9 Mountain - Used by 19/20 decks
2 Arid Mesa - Used by 11/20 decks
2 Bloodstained Mire - Used by 9/20 decks
2 Barbarian Ring - Used by 9/20 decks
2 Scalding Tarn - Used by 8/20 decks
1 Wooded Foothills - Used by 11/20 decks
//----------------------------------------------------------------------
// CREATURES - 12 cards
//----------------------------------------------------------------------
4 Monastery Swiftspear - Used by 20/20 decks
4 Eidolon of the Great Revel - Used by 19/20 decks
4 Goblin Guide - Used by 17/20 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 30 cards
//----------------------------------------------------------------------
4 Chain Lightning - Used by 20/20 decks
4 Fireblast - Used by 20/20 decks
4 Lava Spike - Used by 20/20 decks
4 Lightning Bolt - Used by 20/20 decks
4 Rift Bolt - Used by 20/20 decks
4 Price of Progress - Used by 19/20 decks
4 Skewer the Critics - Used by 19/20 decks
2 Roiling Vortex - Used by 14/20 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Leyline of the Void - Used by 7/20 decks
2 Smash to Smithereens - Used by 20/20 decks
2 Pyroblast - Used by 13/20 decks
2 Faerie Macabre - Used by 9/20 decks
2 Grafdigger's Cage - Used by 9/20 decks
1 Red Elemental Blast - Used by 11/20 decks
1 Ensnaring Bridge - Used by 8/20 decks
1 Meltdown - Used by 7/20 decks
```
Legacy Burn average deck considering only competitive decks with detailed printing and top quantity for each card:
```
$ python3 mtgdeckbuild.py -f LE -a Burn -c -T -p


//----------------------------------------------------------------------
// LANDS - 18 cards
//----------------------------------------------------------------------
18 Mountain - Used by 15/20 decks
//----------------------------------------------------------------------
// CREATURES - 12 cards
//----------------------------------------------------------------------
4 Goblin Guide - Used by 19/20 decks
4 Monastery Swiftspear - Used by 19/20 decks
4 Eidolon of the Great Revel - Used by 15/20 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 30 cards
//----------------------------------------------------------------------
4 Lightning Bolt - Used by 20/20 decks
4 Chain Lightning - Used by 19/20 decks
4 Fireblast - Used by 19/20 decks
4 Lava Spike - Used by 19/20 decks
4 Price of Progress - Used by 19/20 decks
4 Rift Bolt - Used by 18/20 decks
4 Skewer the Critics - Used by 16/20 decks
2 Roiling Vortex - Used by 12/20 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Leyline of the Void - Used by 13/20 decks
3 Smash to Smithereens - Used by 16/20 decks
2 Faerie Macabre - Used by 7/20 decks
2 Red Elemental Blast - Used by 7/20 decks
1 Pyroblast - Used by 13/20 decks
1 Exquisite Firecraft - Used by 8/20 decks
1 Ensnaring Bridge - Used by 6/20 decks
1 Tormod's Crypt - Used by 4/20 decks
```
Modern UB Mill average deck considering only competitive decks using the 50 last decks with detailed printing:
```
$ python3 mtgdeckbuild.py -f MO -a "UB Mill" -c -d 50 -p


//----------------------------------------------------------------------
// LANDS - 25 cards
//----------------------------------------------------------------------
4 Field of Ruin - Used by 49/50 decks
4 Island - Used by 47/50 decks
4 Polluted Delta - Used by 43/50 decks
3 Flooded Strand - Used by 31/50 decks
2 Misty Rainforest - Used by 27/50 decks
2 Scalding Tarn - Used by 27/50 decks
1 Oboro, Palace in the Clouds - Used by 46/50 decks
1 Watery Grave - Used by 46/50 decks
1 Otawara, Soaring City - Used by 42/50 decks
1 Shelldock Isle - Used by 39/50 decks
1 Undercity Sewers - Used by 34/50 decks
1 Swamp - Used by 33/50 decks
//----------------------------------------------------------------------
// CREATURES - 8 cards
//----------------------------------------------------------------------
4 Hedron Crab - Used by 50/50 decks
4 Ruin Crab - Used by 50/50 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 27 cards
//----------------------------------------------------------------------
4 Archive Trap - Used by 50/50 decks
4 Fractured Sanity - Used by 49/50 decks
4 Fatal Push - Used by 33/50 decks
4 Drown in the Loch - Used by 31/50 decks
3 Surgical Extraction - Used by 49/50 decks
3 Visions of Beyond - Used by 46/50 decks
3 Tasha's Hideous Laughter - Used by 44/50 decks
2 Jace, the Perfected Mind - Used by 38/50 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
3 Ensnaring Bridge - Used by 39/50 decks
3 Soul-Guide Lantern - Used by 34/50 decks
3 Extirpate - Used by 28/50 decks
2 Crypt Incursion - Used by 33/50 decks
2 Consign to Memory - Used by 22/50 decks
1 Engineered Explosives - Used by 21/50 decks
1 Toxic Deluge - Used by 14/50 decks
```
Duel-Commander Phelia, the Exuberant Shepherd average deck considering only competitive decks over the last month:
```
$ python3 mtgdeckbuild.py -f DC -a Phelia -c -l 1 -p
Archetype not found: Phelia
Did you mean Phelia, Exuberant Shepherd? [y/n] (y): 


//----------------------------------------------------------------------
// LANDS - 38 cards
//----------------------------------------------------------------------
23 Snow-Covered Plains - Used by 8/11 decks
1 Eiganjo, Seat of the Empire - Used by 10/11 decks
1 Flagstones of Trokair - Used by 10/11 decks
1 Tectonic Edge - Used by 10/11 decks
1 Eiganjo Castle - Used by 9/11 decks
1 Urza's Saga - Used by 9/11 decks
1 Dust Bowl - Used by 9/11 decks
1 Rishadan Port - Used by 9/11 decks
1 War Room - Used by 8/11 decks
1 Crystal Vein - Used by 8/11 decks
1 Gemstone Caverns - Used by 7/11 decks
1 Mishra's Factory - Used by 7/11 decks
1 Scavenger Grounds - Used by 7/11 decks
1 City of Traitors - Used by 6/11 decks
1 Castle Ardenvale - Used by 6/11 decks
1 Mutavault - Used by 6/11 decks
//----------------------------------------------------------------------
// CREATURES - 30 cards
//----------------------------------------------------------------------
1 Esper Sentinel - Used by 11/11 decks
1 Giver of Runes - Used by 11/11 decks
1 Mother of Runes - Used by 11/11 decks
1 Recruiter of the Guard - Used by 11/11 decks
1 Skrelv, Defector Mite - Used by 11/11 decks
1 Solitude - Used by 11/11 decks
1 Stoneforge Mystic - Used by 11/11 decks
1 White Plume Adventurer - Used by 11/11 decks
1 Containment Priest - Used by 10/11 decks
1 Drannith Magistrate - Used by 10/11 decks
1 Elite Spellbinder - Used by 10/11 decks
1 Guide of Souls - Used by 10/11 decks
1 Novice Inspector - Used by 10/11 decks
1 Palace Jailer - Used by 10/11 decks
1 Seasoned Dungeoneer - Used by 10/11 decks
1 Skyclave Apparition - Used by 10/11 decks
1 Steel Seraph - Used by 10/11 decks
1 Thraben Inspector - Used by 10/11 decks
1 Witch Enchanter - Used by 10/11 decks
1 Blade Splicer - Used by 9/11 decks
1 Benevolent Bodyguard - Used by 8/11 decks
1 Restoration Angel - Used by 8/11 decks
1 Serra Paragon - Used by 8/11 decks
1 Thalia, Guardian of Thraben - Used by 8/11 decks
1 Samwise the Stouthearted - Used by 7/11 decks
1 Flickerwisp - Used by 7/11 decks
1 Cathar Commando - Used by 6/11 decks
1 Extraction Specialist - Used by 5/11 decks
1 Sanctifier en-Vec - Used by 5/11 decks
1 Loran of the Third Path - Used by 5/11 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 31 cards
//----------------------------------------------------------------------
1 Ephemerate - Used by 11/11 decks
1 Ossification - Used by 11/11 decks
1 Parallax Wave - Used by 11/11 decks
1 Skullclamp - Used by 11/11 decks
1 Static Prison - Used by 11/11 decks
1 Swords to Plowshares - Used by 11/11 decks
1 Council's Judgment - Used by 10/11 decks
1 Invasion of Gobakhan - Used by 10/11 decks
1 Mana Tithe - Used by 10/11 decks
1 Portable Hole - Used by 10/11 decks
1 Razorgrass Ambush - Used by 10/11 decks
1 On Thin Ice - Used by 9/11 decks
1 Pre-War Formalwear - Used by 9/11 decks
1 Shadowspear - Used by 9/11 decks
1 Staff of the Storyteller - Used by 9/11 decks
1 The Wandering Emperor - Used by 9/11 decks
1 Cataclysm - Used by 9/11 decks
1 Reprieve - Used by 9/11 decks
1 Arcum's Astrolabe - Used by 8/11 decks
1 Reverent Mantra - Used by 8/11 decks
1 Swift Reconfiguration - Used by 8/11 decks
1 Unexpectedly Absent - Used by 8/11 decks
1 March of Otherworldly Light - Used by 8/11 decks
1 Enlightened Tutor - Used by 7/11 decks
1 Oust - Used by 7/11 decks
1 Tangle Wire - Used by 7/11 decks
1 Aether Vial - Used by 6/11 decks
1 Umezawa's Jitte - Used by 6/11 decks
1 Soul-Guide Lantern - Used by 6/11 decks
1 Glimmer Lens - Used by 5/11 decks
1 Batterskull - Used by 5/11 decks
//----------------------------------------------------------------------
// SIDEBOARD - 1 cards
//----------------------------------------------------------------------
1 Phelia, Exuberant Shepherd - Used by 11/11 decks
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
Yoshimaru, Ever Faithful is used in all analyzed decks as Commander.
Different commanders are used in analyzed decks. Select those you want to keep. If you want to select multiple commanders, use comma-separated choices (e.g. "1, 2")
0 - Any
1 - Dargo, the Shipwrecker
2 - Bruse Tarl, Boorish Herder
: 2


//----------------------------------------------------------------------
// LANDS - 39 cards
//----------------------------------------------------------------------
5 Snow-Covered Plains - Used by 13/20 decks
2 Snow-Covered Mountain - Used by 13/20 decks
1 Arid Mesa - Used by 20/20 decks
1 Bloodstained Mire - Used by 20/20 decks
1 Command Tower - Used by 20/20 decks
1 Eiganjo, Seat of the Empire - Used by 20/20 decks
1 Flooded Strand - Used by 20/20 decks
1 Inspiring Vantage - Used by 20/20 decks
1 Marsh Flats - Used by 20/20 decks
1 Minas Tirith - Used by 20/20 decks
1 Sacred Foundry - Used by 20/20 decks
1 Shinka, the Bloodsoaked Keep - Used by 20/20 decks
1 Sokenzan, Crucible of Defiance - Used by 20/20 decks
1 Windswept Heath - Used by 20/20 decks
1 Wooded Foothills - Used by 20/20 decks
1 Battlefield Forge - Used by 19/20 decks
1 Eiganjo Castle - Used by 19/20 decks
1 Flagstones of Trokair - Used by 19/20 decks
1 Hammerheim - Used by 19/20 decks
1 Plaza of Heroes - Used by 19/20 decks
1 Plateau - Used by 19/20 decks
1 Scalding Tarn - Used by 18/20 decks
1 Prismatic Vista - Used by 18/20 decks
1 Clifftop Retreat - Used by 17/20 decks
1 Rugged Prairie - Used by 17/20 decks
1 Sunbaked Canyon - Used by 17/20 decks
1 Urza's Saga - Used by 17/20 decks
1 Den of the Bugbear - Used by 16/20 decks
1 Mines of Moria - Used by 16/20 decks
1 Needleverge Pathway - Used by 15/20 decks
1 Arena of Glory - Used by 12/20 decks
1 Sundown Pass - Used by 12/20 decks
1 Gemstone Caverns - Used by 11/20 decks
1 Elegant Parlor - Used by 10/20 decks
//----------------------------------------------------------------------
// CREATURES - 38 cards
//----------------------------------------------------------------------
1 Broadside Bombardiers - Used by 20/20 decks
1 Fury - Used by 20/20 decks
1 Headliner Scarlett - Used by 20/20 decks
1 Kari Zev, Skyship Raider - Used by 20/20 decks
1 Laelia, the Blade Reforged - Used by 20/20 decks
1 Merry, Esquire of Rohan - Used by 20/20 decks
1 Mother of Runes - Used by 20/20 decks
1 Phelia, Exuberant Shepherd - Used by 20/20 decks
1 Solitude - Used by 20/20 decks
1 White Plume Adventurer - Used by 20/20 decks
1 Adeline, Resplendent Cathar - Used by 19/20 decks
1 Ajani, Nacatl Pariah - Used by 19/20 decks
1 Feldon, Ronom Excavator - Used by 19/20 decks
1 Phlage, Titan of Fire's Fury - Used by 19/20 decks
1 Skyclave Apparition - Used by 19/20 decks
1 Loyal Apprentice - Used by 18/20 decks
1 Thalia, Guardian of Thraben - Used by 18/20 decks
1 Arbaaz Mir - Used by 17/20 decks
1 Baird, Argivian Recruiter - Used by 17/20 decks
1 Giver of Runes - Used by 17/20 decks
1 Pyrogoyf - Used by 17/20 decks
1 Seasoned Dungeoneer - Used by 17/20 decks
1 Senu, Keen-Eyed Protector - Used by 17/20 decks
1 Inti, Seneschal of the Sun - Used by 16/20 decks
1 Skrelv, Defector Mite - Used by 16/20 decks
1 Stoneforge Mystic - Used by 16/20 decks
1 Thalia, Heretic Cathar - Used by 16/20 decks
1 Samwise the Stouthearted - Used by 16/20 decks
1 Squee, Dubious Monarch - Used by 15/20 decks
1 Tajic, Legion's Edge - Used by 15/20 decks
1 Boromir, Warden of the Tower - Used by 13/20 decks
1 Anim Pakal, Thousandth Moon - Used by 12/20 decks
1 Mabel, Heir to Cragflame - Used by 12/20 decks
1 Zurgo Bellstriker - Used by 12/20 decks
1 Ash, Party Crasher - Used by 12/20 decks
1 Drannith Magistrate - Used by 11/20 decks
1 Selfless Spirit - Used by 10/20 decks
1 Cathar Commando - Used by 9/20 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 21 cards
//----------------------------------------------------------------------
1 Chain Lightning - Used by 20/20 decks
1 Flowering of the White Tree - Used by 20/20 decks
1 Lightning Bolt - Used by 20/20 decks
1 Parallax Wave - Used by 20/20 decks
1 Pyrokinesis - Used by 20/20 decks
1 Swords to Plowshares - Used by 20/20 decks
1 Forth Eorlingas! - Used by 19/20 decks
1 Shadowspear - Used by 19/20 decks
1 Embercleave - Used by 17/20 decks
1 Galadriel's Dismissal - Used by 17/20 decks
1 Pre-War Formalwear - Used by 15/20 decks
1 Reverent Mantra - Used by 15/20 decks
1 Skullclamp - Used by 14/20 decks
1 Sundering Eruption - Used by 14/20 decks
1 Flame Slash - Used by 14/20 decks
1 Swift Reconfiguration - Used by 13/20 decks
1 Static Prison - Used by 12/20 decks
1 Ghostfire Slice - Used by 12/20 decks
1 On Thin Ice - Used by 11/20 decks
1 Enlightened Tutor - Used by 10/20 decks
1 Galvanic Discharge - Used by 10/20 decks
//----------------------------------------------------------------------
// SIDEBOARD - 2 cards
//----------------------------------------------------------------------
1 Yoshimaru, Ever Faithful - Used by 20/20 decks
1 Bruse Tarl, Boorish Herder - Used by 15/20 decks
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
7 Mountain
2 Restless Ridgeline
2 Rockface Village
2 Forest
4 Emberheart Challenger
4 Heartfire Hero
4 Monastery Swiftspear
3 Slickshot Show-Off
4 Manifold Mouse
2 Questing Druid
4 Monstrous Rage
2 Snakeskin Veil
4 Shock
4 Might of the Meek
2 Innkeeper's Talent
2 Witchstalker Frenzy
// SIDEBOARD
4 Urabrask's Forge
2 Obliterating Bolt
2 Torch the Tower
3 Tectonic Hazard
3 Pawpatch Formation
1 Scorching Shot
```
Standard Gruul Aggro average deck considering only the last 15 decks with maybeboard, balance of the deck section, top quantity for each card and detailed printing:
```
$ python3 mtgdeckbuild.py -f ST -a "Gruul Aggro" -d 15 -M -T -b -p


//----------------------------------------------------------------------
// LANDS - 20 cards
//----------------------------------------------------------------------
8 Mountain - Used by 15/15 decks
4 Copperline Gorge - Used by 15/15 decks
4 Karplusan Forest - Used by 15/15 decks
4 Thornspire Verge - Used by 14/15 decks
//----------------------------------------------------------------------
// CREATURES - 20 cards
//----------------------------------------------------------------------
4 Emberheart Challenger - Used by 13/15 decks
4 Heartfire Hero - Used by 13/15 decks
4 Monastery Swiftspear - Used by 13/15 decks
4 Cacophony Scamp - Used by 9/15 decks
3 Picnic Ruiner - Used by 8/15 decks
1 Slickshot Show-Off - Used by 5/15 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 20 cards
//----------------------------------------------------------------------
4 Monstrous Rage - Used by 13/15 decks
4 Might of the Meek - Used by 12/15 decks
4 Turn Inside Out - Used by 11/15 decks
4 Leyline of Resonance - Used by 9/15 decks
2 Snakeskin Veil - Used by 13/15 decks
2 Witch's Mark - Used by 8/15 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Torch the Tower - Used by 12/15 decks
3 Urabrask's Forge - Used by 13/15 decks
3 Pawpatch Formation - Used by 12/15 decks
3 Obliterating Bolt - Used by 12/15 decks
2 Twisted Fealty - Used by 5/15 decks
//----------------------------------------------------------------------
// MAYBEBOARD - 18 cards
//----------------------------------------------------------------------
4 Shock - Used by 5/15 decks
1 Restless Ridgeline - Used by 4/15 decks
4 Manifold Mouse - Used by 4/15 decks
2 Questing Druid - Used by 3/15 decks
1 Forest - Used by 3/15 decks
2 Rockface Village - Used by 3/15 decks
4 Innkeeper's Talent - Used by 3/15 decks
2 Audacity - Used by 2/15 decks
2 Callous Sell-Sword - Used by 2/15 decks
2 Royal Treatment - Used by 2/15 decks
1 Commercial District - Used by 2/15 decks
4 Fear of Missing Out - Used by 2/15 decks
4 Inti, Seneschal of the Sun - Used by 2/15 decks
4 Omnivorous Flytrap - Used by 2/15 decks
4 Wildfire Wickerfolk - Used by 2/15 decks
4 Break Out - Used by 2/15 decks
4 Torch the Tower - Used by 2/15 decks
1 Witchstalker Frenzy - Used by 2/15 decks
```
Duel-Commander Aminatou, The Fateshifter average deck considering decks since a specific date, including a specific card in the main deck, with maybeboard, balance of the deck section and detailed printing:
```
$ python3 mtgdeckbuild.py -f DC -a Aminatou -b -M -S 30-09-2024 -m -i "Archon of Cruelty" -p
Archetype not found: Aminatou
Did you mean Aminatou, The Fateshifter? [y/n] (y): 


//----------------------------------------------------------------------
// LANDS - 36 cards
//----------------------------------------------------------------------
1 Arid Mesa - Used by 6/6 decks (100%)
1 Bloodstained Mire - Used by 6/6 decks (100%)
1 Command Tower - Used by 6/6 decks (100%)
1 Darkslick Shores - Used by 6/6 decks (100%)
1 Drowned Catacomb - Used by 6/6 decks (100%)
1 Flooded Strand - Used by 6/6 decks (100%)
1 Godless Shrine - Used by 6/6 decks (100%)
1 Hallowed Fountain - Used by 6/6 decks (100%)
1 Island - Used by 6/6 decks (100%)
1 Marsh Flats - Used by 6/6 decks (100%)
1 Meticulous Archive - Used by 6/6 decks (100%)
1 Misty Rainforest - Used by 6/6 decks (100%)
1 Plains - Used by 6/6 decks (100%)
1 Polluted Delta - Used by 6/6 decks (100%)
1 Prismatic Vista - Used by 6/6 decks (100%)
1 Scalding Tarn - Used by 6/6 decks (100%)
1 Scrubland - Used by 6/6 decks (100%)
1 Seachrome Coast - Used by 6/6 decks (100%)
1 Shadowy Backstreet - Used by 6/6 decks (100%)
1 Swamp - Used by 6/6 decks (100%)
1 Tundra - Used by 6/6 decks (100%)
1 Undercity Sewers - Used by 6/6 decks (100%)
1 Underground River - Used by 6/6 decks (100%)
1 Verdant Catacombs - Used by 6/6 decks (100%)
1 Watery Grave - Used by 6/6 decks (100%)
1 Windswept Heath - Used by 6/6 decks (100%)
1 Adarkar Wastes - Used by 5/6 decks (83%)
1 Glacial Fortress - Used by 5/6 decks (83%)
1 Isolated Chapel - Used by 5/6 decks (83%)
1 Reflecting Pool - Used by 5/6 decks (83%)
1 Underground Sea - Used by 5/6 decks (83%)
1 Floodfarm Verge - Used by 4/6 decks (67%)
1 Gloomlake Verge - Used by 4/6 decks (67%)
1 Tomb Fortress - Used by 4/6 decks (67%)
1 Snow-Covered Island - Used by 3/6 decks (50%)
1 Snow-Covered Swamp - Used by 2/6 decks (33%)
//----------------------------------------------------------------------
// CREATURES - 19 cards
//----------------------------------------------------------------------
1 Agent of Treachery - Used by 6/6 decks (100%)
1 Archon of Cruelty - Used by 6/6 decks (100%)
1 Ashen Rider - Used by 6/6 decks (100%)
1 Lord of Change - Used by 6/6 decks (100%)
1 Metamorphosis Fanatic - Used by 6/6 decks (100%)
1 Spellseeker - Used by 6/6 decks (100%)
1 Hoarding Broodlord - Used by 5/6 decks (83%)
1 Overlord of the Floodpits - Used by 5/6 decks (83%)
1 Psychic Frog - Used by 5/6 decks (83%)
1 Rune-Scarred Demon - Used by 5/6 decks (83%)
1 Tivit, Seller of Secrets - Used by 5/6 decks (83%)
1 Troll of Khazad-dûm - Used by 5/6 decks (83%)
1 Overlord of the Balemurk - Used by 4/6 decks (67%)
1 Magister of Worth - Used by 4/6 decks (67%)
1 Astral Dragon - Used by 3/6 decks (50%)
1 Fallaji Archaeologist - Used by 3/6 decks (50%)
1 Grief - Used by 3/6 decks (50%)
1 Orcish Bowmasters - Used by 3/6 decks (50%)
1 Griselbrand - Used by 2/6 decks (33%)
//----------------------------------------------------------------------
// OTHER SPELLS - 44 cards
//----------------------------------------------------------------------
1 Animate Dead - Used by 6/6 decks (100%)
1 Balance - Used by 6/6 decks (100%)
1 Careful Study - Used by 6/6 decks (100%)
1 Collective Brutality - Used by 6/6 decks (100%)
1 Dance of the Dead - Used by 6/6 decks (100%)
1 Daze - Used by 6/6 decks (100%)
1 Demonic Tutor - Used by 6/6 decks (100%)
1 Exhume - Used by 6/6 decks (100%)
1 Fatal Push - Used by 6/6 decks (100%)
1 Flash - Used by 6/6 decks (100%)
1 Force of Will - Used by 6/6 decks (100%)
1 Frantic Search - Used by 6/6 decks (100%)
1 Inquisition of Kozilek - Used by 6/6 decks (100%)
1 Intuition - Used by 6/6 decks (100%)
1 Necromancy - Used by 6/6 decks (100%)
1 Persist - Used by 6/6 decks (100%)
1 Reanimate - Used by 6/6 decks (100%)
1 Shallow Grave - Used by 6/6 decks (100%)
1 Swords to Plowshares - Used by 6/6 decks (100%)
1 Tainted Indulgence - Used by 6/6 decks (100%)
1 Tainted Pact - Used by 6/6 decks (100%)
1 Teferi, Time Raveler - Used by 6/6 decks (100%)
1 Thoughtseize - Used by 6/6 decks (100%)
1 Unmarked Grave - Used by 6/6 decks (100%)
1 Bitter Triumph - Used by 5/6 decks (83%)
1 Brainstorm - Used by 5/6 decks (83%)
1 Corpse Dance - Used by 5/6 decks (83%)
1 Counterspell - Used by 5/6 decks (83%)
1 Force Spike - Used by 5/6 decks (83%)
1 Mental Misstep - Used by 5/6 decks (83%)
1 Ponder - Used by 5/6 decks (83%)
1 Tithing Blade - Used by 5/6 decks (83%)
1 Unburial Rites - Used by 5/6 decks (83%)
1 Currency Converter - Used by 4/6 decks (67%)
1 Mana Tithe - Used by 4/6 decks (67%)
1 Prismatic Ending - Used by 4/6 decks (67%)
1 Spell Snare - Used by 4/6 decks (67%)
1 Duress - Used by 4/6 decks (67%)
1 Faithful Mending - Used by 4/6 decks (67%)
1 Wash Away - Used by 4/6 decks (67%)
1 Sevinne's Reclamation - Used by 3/6 decks (50%)
1 Bone Shards - Used by 3/6 decks (50%)
1 Buried Alive - Used by 3/6 decks (50%)
1 Dihada's Ploy - Used by 3/6 decks (50%)
//----------------------------------------------------------------------
// SIDEBOARD - 1 cards
//----------------------------------------------------------------------
1 Aminatou, the Fateshifter - Used by 6/6 decks (100%)
//----------------------------------------------------------------------
// MAYBEBOARD - 40 cards
//----------------------------------------------------------------------
1 Oath of Kaya - Used by 2/6 decks (33%)
1 Show and Tell - Used by 2/6 decks (33%)
1 Clearwater Pathway - Used by 2/6 decks (33%)
1 Concealed Courtyard - Used by 2/6 decks (33%)
1 Urborg, Tomb of Yawgmoth - Used by 2/6 decks (33%)
1 Spell Pierce - Used by 2/6 decks (33%)
1 Malcolm, Alluring Scoundrel - Used by 1/6 decks (17%)
1 Triumph of Saint Katherine - Used by 1/6 decks (17%)
1 Temporal Mastery - Used by 1/6 decks (17%)
1 Snow-Covered Plains - Used by 1/6 decks (17%)
1 Beza, the Bounding Spring - Used by 1/6 decks (17%)
1 Grave Titan - Used by 1/6 decks (17%)
1 Sun Titan - Used by 1/6 decks (17%)
1 Force of Negation - Used by 1/6 decks (17%)
1 Elesh Norn, Grand Cenobite - Used by 1/6 decks (17%)
1 Harvester of Misery - Used by 1/6 decks (17%)
1 Three Steps Ahead - Used by 1/6 decks (17%)
1 Eiganjo, Seat of the Empire - Used by 1/6 decks (17%)
1 Fetid Heath - Used by 1/6 decks (17%)
1 Hengegate Pathway - Used by 1/6 decks (17%)
1 Mystic Gate - Used by 1/6 decks (17%)
1 Sunken Ruins - Used by 1/6 decks (17%)
1 Baleful Strix - Used by 1/6 decks (17%)
1 Valgavoth, Terror Eater - Used by 1/6 decks (17%)
1 Enlightened Tutor - Used by 1/6 decks (17%)
1 Jace, Wielder of Mysteries - Used by 1/6 decks (17%)
1 Liliana of the Veil - Used by 1/6 decks (17%)
1 Port of Karfell - Used by 1/6 decks (17%)
1 River of Tears - Used by 1/6 decks (17%)
1 Shipwreck Marsh - Used by 1/6 decks (17%)
1 Crabomination - Used by 1/6 decks (17%)
1 Brainsurge - Used by 1/6 decks (17%)
1 Consider - Used by 1/6 decks (17%)
1 Lim-Dûl's Vault - Used by 1/6 decks (17%)
1 Mana Leak - Used by 1/6 decks (17%)
1 Omen of the Sea - Used by 1/6 decks (17%)
1 Profane Tutor - Used by 1/6 decks (17%)
1 Ripples of Undeath - Used by 1/6 decks (17%)
1 Serum Visions - Used by 1/6 decks (17%)
1 Wrath of the Skies - Used by 1/6 decks (17%)
```
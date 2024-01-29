# mtgdeckbuild
A Magic: The Gathering format archetype average deck building tool based on tournament results.

# MTGDeckBuild
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)  
---  
A Magic: The Gathering format archetype average deck building tool based on tournaments results. Deck building is based on currently played archetypes and most used cards in tournaments decks. Generally, the last 25 decks are used but some filter may affect the number of analyzed decks.

## Features

* Support of [MTGTOP8](https://mtgtop8.com) and [MTGDECKS](https://mtgdecks.net) as website data sources.
* Support of all formats with automatic discovery.
* Support of all archetypes with automatic discovery and possibility to only parse a given number of top archetypes.
* Possibility to specify the maximum number of decks to analyze (default: 25).
* Filtering available to only consider competitive decks (only for MTGTOP8).
* Filtering available to only consider decks including given card names in main deck and/or sideboard.
* Filtering available to only consider decks including given names (only for MTGTOP8).
* Filtering available to only consider decks over the last given months (only for MTGTOP8).
* Possibility to display a Maybeboard section with all the cards that are tied or minus one in terms of number of decks using them for main deck and sideboard.
* Interactive mode when executing the script.
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
usage: mtgdeckbuild.py [-h] [--website-source WEBSITE_SOURCE] [--top-archetypes TOP_ARCHETYPES] [--decks DECKS] [--print-details] [--competitive-only] [--name NAME]
                       [--include-cards INCLUDE_CARDS] [--main-include] [--side-include] [--last-months LAST_MONTHS] [--maybeboard]

options:
  -h, --help            show this help message and exit
  --website-source WEBSITE_SOURCE, -w WEBSITE_SOURCE
                        Website data source to use (mtgtop8 or mtgdecks ; default: mtgtop8)
  --top-archetypes TOP_ARCHETYPES, -t TOP_ARCHETYPES
                        The number of top archetypes to parse (default: all archetypes)
  --decks DECKS, -d DECKS
                        The maximum number of decks to analyze (default: 25)
  --print-details, -p   Print deck with details: sections and number of decks using each card
  --competitive-only, -c
                        Only consider competitive decks (only for MTGTOP8)
  --name NAME, -n NAME  Only consider decks including given deck name (only for MTGTOP8)
  --include-cards INCLUDE_CARDS, -i INCLUDE_CARDS
                        Only consider decks including given cards (use dash-separated card names if passing multiple cards, must be used with --main-deck/-m, --sideboard/-s arguments or both)
  --main-include, -m    Consider cards to include for the main deck (must be used with --include-cards/-i, also include cards for the sideboard for MTGDECKS)
  --side-include, -s    Consider cards to include for the sideboard (must be used with --include-cards/-i)
  --last-months LAST_MONTHS, -l LAST_MONTHS
                        Only consider decks from the last given months (only for MTGTOP8)
  --maybeboard          Print Maybeboard (additional cards that are tied or minus one in terms of number of decks using them)
```

## Examples
Legacy Burn average deck from MTGTOP8:
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
1 - 4/5c Control
2 - Affinity
3 - All my Spells
4 - Aluren
5 - Arclight Phoenix
6 - Artifacts Blue
7 - Artifacts Prison
8 - BUG Control
9 - BUG Midrange
10 - Bant Aggro
11 - Bant Control
12 - Bomberman
13 - Burn
14 - Canadian Threshold
15 - Cascade Crash
16 - Cephalid Breakfast
17 - Cloudpost Ramp
18 - Curses
19 - Dark Depths
20 - Deadguy Ale
21 - Death & Taxes
22 - Death's Shadow
23 - Delver (Other)
24 - Dimir Aggro
25 - Doomsday
26 - Dragon Stompy
27 - Dredge
28 - Eldrazi Aggro
29 - Elves
30 - Esper Aggro
31 - Esper Vial
32 - Faeries
33 - Food Chain
34 - Goblins
35 - Grixis Aggro
36 - Grixis Control
37 - High Tide
38 - Hive Mind
39 - Hogaak
40 - Hollow One Madness
41 - Infect
42 - Initiative Stompy
43 - Jund
44 - Lands
45 - Landstill
46 - Loam
47 - MUD
48 - Maverick
49 - Merfolk
50 - Mississippi River
51 - Mono Black Aggro
52 - Mono Black Combo
53 - Mystic Forge
54 - Nic Fit 
55 - Ninja
56 - Other - Aggro
57 - Other - Combo
58 - Painter
59 - Patriot Aggro
60 - Pox
61 - Reanimator
62 - Show and Tell
63 - Slivers
64 - Stiflenought
65 - Stoneblade
66 - Storm
67 - Thassa's Oracle
68 - The Rock (Junk)
69 - UR Aggro
70 - UWx Control
: 13


// MAIN DECK
12 Mountain
3 Arid Mesa
2 Bloodstained Mire
1 Wooded Foothills
4 Goblin Guide
4 Monastery Swiftspear
4 Eidolon of the Great Revel
4 Lightning Bolt
4 Chain Lightning
4 Fireblast
4 Lava Spike
4 Price of Progress
4 Rift Bolt
3 Skewer the Critics
2 Roiling Vortex
1 Exquisite Firecraft
// SIDEBOARD
3 Smash to Smithereens
2 Ensnaring Bridge
2 Pyroblast
4 Leyline of the Void
3 Searing Blood
1 Faerie Macabre
```
Legacy Burn average deck from MTGTOP8 with detailed printing:
```
$ python3 mtgdeckbuild.py -p
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
1 - 4/5c Control
2 - Affinity
3 - All my Spells
4 - Aluren
5 - Arclight Phoenix
6 - Artifacts Blue
7 - Artifacts Prison
8 - BUG Control
9 - BUG Midrange
10 - Bant Aggro
11 - Bant Control
12 - Bomberman
13 - Burn
14 - Canadian Threshold
15 - Cascade Crash
16 - Cephalid Breakfast
17 - Cloudpost Ramp
18 - Curses
19 - Dark Depths
20 - Deadguy Ale
21 - Death & Taxes
22 - Death's Shadow
23 - Delver (Other)
24 - Dimir Aggro
25 - Doomsday
26 - Dragon Stompy
27 - Dredge
28 - Eldrazi Aggro
29 - Elves
30 - Esper Aggro
31 - Esper Vial
32 - Faeries
33 - Food Chain
34 - Goblins
35 - Grixis Aggro
36 - Grixis Control
37 - High Tide
38 - Hive Mind
39 - Hogaak
40 - Hollow One Madness
41 - Infect
42 - Initiative Stompy
43 - Jund
44 - Lands
45 - Landstill
46 - Loam
47 - MUD
48 - Maverick
49 - Merfolk
50 - Mississippi River
51 - Mono Black Aggro
52 - Mono Black Combo
53 - Mystic Forge
54 - Nic Fit 
55 - Ninja
56 - Other - Aggro
57 - Other - Combo
58 - Painter
59 - Patriot Aggro
60 - Pox
61 - Reanimator
62 - Show and Tell
63 - Slivers
64 - Stiflenought
65 - Stoneblade
66 - Storm
67 - Thassa's Oracle
68 - The Rock (Junk)
69 - UR Aggro
70 - UWx Control
: 13


//----------------------------------------------------------------------
// LANDS - 18 cards
//----------------------------------------------------------------------
12 Mountain - Used by 24/25 decks
3 Arid Mesa - Used by 12/25 decks
2 Bloodstained Mire - Used by 9/25 decks
1 Wooded Foothills - Used by 8/25 decks
//----------------------------------------------------------------------
// CREATURES - 12 cards
//----------------------------------------------------------------------
4 Goblin Guide - Used by 24/25 decks
4 Monastery Swiftspear - Used by 24/25 decks
4 Eidolon of the Great Revel - Used by 23/25 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 30 cards
//----------------------------------------------------------------------
4 Lightning Bolt - Used by 25/25 decks
4 Chain Lightning - Used by 24/25 decks
4 Fireblast - Used by 24/25 decks
4 Lava Spike - Used by 24/25 decks
4 Price of Progress - Used by 24/25 decks
4 Rift Bolt - Used by 24/25 decks
3 Skewer the Critics - Used by 18/25 decks
2 Roiling Vortex - Used by 11/25 decks
1 Exquisite Firecraft - Used by 10/25 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Leyline of the Void - Used by 12/25 decks
3 Smash to Smithereens - Used by 23/25 decks
3 Searing Blood - Used by 9/25 decks
2 Ensnaring Bridge - Used by 13/25 decks
2 Pyroblast - Used by 13/25 decks
1 Faerie Macabre - Used by 8/25 decks
```
Legacy Burn average deck from MTGTOP8 considering only competitive decks with detailed printing:
```
$ python3 mtgdeckbuild.py -c -p
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
1 - 4/5c Control
2 - Affinity
3 - All my Spells
4 - Aluren
5 - Arclight Phoenix
6 - Artifacts Blue
7 - Artifacts Prison
8 - BUG Control
9 - BUG Midrange
10 - Bant Aggro
11 - Bant Control
12 - Bomberman
13 - Burn
14 - Canadian Threshold
15 - Cascade Crash
16 - Cephalid Breakfast
17 - Cloudpost Ramp
18 - Curses
19 - Dark Depths
20 - Deadguy Ale
21 - Death & Taxes
22 - Death's Shadow
23 - Delver (Other)
24 - Dimir Aggro
25 - Doomsday
26 - Dragon Stompy
27 - Dredge
28 - Eldrazi Aggro
29 - Elves
30 - Esper Aggro
31 - Esper Vial
32 - Faeries
33 - Food Chain
34 - Goblins
35 - Grixis Aggro
36 - Grixis Control
37 - High Tide
38 - Hive Mind
39 - Hogaak
40 - Hollow One Madness
41 - Infect
42 - Initiative Stompy
43 - Jund
44 - Lands
45 - Landstill
46 - Loam
47 - MUD
48 - Maverick
49 - Merfolk
50 - Mississippi River
51 - Mono Black Aggro
52 - Mono Black Combo
53 - Mystic Forge
54 - Nic Fit 
55 - Ninja
56 - Other - Aggro
57 - Other - Combo
58 - Painter
59 - Patriot Aggro
60 - Pox
61 - Reanimator
62 - Show and Tell
63 - Slivers
64 - Stiflenought
65 - Stoneblade
66 - Storm
67 - Thassa's Oracle
68 - The Rock (Junk)
69 - UR Aggro
70 - UWx Control
: 13


//----------------------------------------------------------------------
// LANDS - 19 cards
//----------------------------------------------------------------------
13 Mountain - Used by 17/25 decks
3 Arid Mesa - Used by 11/25 decks
2 Bloodstained Mire - Used by 9/25 decks
1 Barbarian Ring - Used by 9/25 decks
//----------------------------------------------------------------------
// CREATURES - 12 cards
//----------------------------------------------------------------------
4 Monastery Swiftspear - Used by 23/25 decks
4 Eidolon of the Great Revel - Used by 22/25 decks
4 Goblin Guide - Used by 22/25 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 29 cards
//----------------------------------------------------------------------
4 Lightning Bolt - Used by 25/25 decks
4 Chain Lightning - Used by 24/25 decks
4 Fireblast - Used by 24/25 decks
4 Lava Spike - Used by 24/25 decks
4 Rift Bolt - Used by 24/25 decks
4 Skewer the Critics - Used by 16/25 decks
3 Price of Progress - Used by 23/25 decks
2 Roiling Vortex - Used by 14/25 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Leyline of the Void - Used by 12/25 decks
3 Smash to Smithereens - Used by 19/25 decks
2 Pyroblast - Used by 16/25 decks
2 Red Elemental Blast - Used by 9/25 decks
2 Ensnaring Bridge - Used by 9/25 decks
2 Exquisite Firecraft - Used by 7/25 decks
```
Modern UB Mill average deck from MTGTOP8 considering only competitive decks using the 50 last decks with detailed printing:
```
$ python3 mtgdeckbuild.py -c -d 50 -p
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
: 11
Select an archetype:
1 - 4/5c Aggro
2 - 4c Control
3 - Affinity
4 - Amulet Titan
5 - Aura Hexproof
6 - Big Red
7 - Breach
8 - Cascade Crash
9 - CopyCat
10 - Creativity
11 - Creatures Toolbox
12 - Death And Taxes
13 - Death's Shadow
14 - Dimir Control
15 - Dredge
16 - Elementals
17 - Esper Control
18 - Grixis Control
19 - Hammer Time
20 - Hardened Scales
21 - Heliod Life
22 - Instant Reanimator
23 - Jund
24 - Landless
25 - Living End
26 - Loam
27 - Mardu Midrange
28 - Martyr Life
29 - Merfolk
30 - Mono Black Aggro
31 - Mono Black Control
32 - Other - Aggro
33 - Other - Combo
34 - Other - Control
35 - Rakdos Aggro
36 - Red Deck Wins
37 - Temur Aggro
38 - The One Ring Control
39 - The Rock
40 - The Underworld Cookbook
41 - UB Mill
42 - UR Aggro
43 - UR Control
44 - UW Control
45 - Urza
46 - UrzaTron
: 41


//----------------------------------------------------------------------
// LANDS - 22 cards
//----------------------------------------------------------------------
4 Field of Ruin - Used by 50/50 decks
4 Polluted Delta - Used by 49/50 decks
3 Island - Used by 49/50 decks
2 Watery Grave - Used by 46/50 decks
2 Shelldock Isle - Used by 43/50 decks
2 Scalding Tarn - Used by 32/50 decks
1 Oboro, Palace in the Clouds - Used by 49/50 decks
1 Otawara, Soaring City - Used by 46/50 decks
1 Swamp - Used by 44/50 decks
1 Mikokoro, Center of the Sea - Used by 24/50 decks
1 Flooded Strand - Used by 21/50 decks
//----------------------------------------------------------------------
// CREATURES - 8 cards
//----------------------------------------------------------------------
4 Hedron Crab - Used by 50/50 decks
4 Ruin Crab - Used by 50/50 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 30 cards
//----------------------------------------------------------------------
4 Archive Trap - Used by 50/50 decks
4 Fractured Sanity - Used by 50/50 decks
4 Tasha's Hideous Laughter - Used by 48/50 decks
4 Drown in the Loch - Used by 45/50 decks
4 Fatal Push - Used by 45/50 decks
3 Visions of Beyond - Used by 47/50 decks
3 Surgical Extraction - Used by 43/50 decks
2 Jace, the Perfected Mind - Used by 48/50 decks
1 Murderous Cut - Used by 25/50 decks
1 Baleful Mastery - Used by 24/50 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
3 Extirpate - Used by 43/50 decks
3 Soul-Guide Lantern - Used by 39/50 decks
2 Ensnaring Bridge - Used by 44/50 decks
2 Crypt Incursion - Used by 43/50 decks
2 Engineered Explosives - Used by 34/50 decks
2 Ghost Quarter - Used by 20/50 decks
1 Go for the Throat - Used by 21/50 decks
```
Duel-Commander Weenie White average deck from MTGTOP8 considering only competitive decks and selected commanders with detailed printing:
```
$ python3 mtgdeckbuild.py -p -c
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
1 - Aminatou, the Fateshifter
2 - Animar, Soul of Elements
3 - Aragorn, King Of Gondor
4 - Aragorn, The Uniter
5 - Arwen, Mortal Queen
6 - Atraxa, Grand Unifier
7 - Atraxa, Praetors' Voice
8 - Azusa, Lost But Seeking
9 - Balmor, Battlemage Captain
10 - Dennick, Pious Apprentice
11 - Elminster
12 - Emmara, Soul Of The Accord
13 - Ertai Resurrected
14 - Ghyrson Starn, Kelermorph
15 - Golos, Tireless Pilgrim
16 - Greasefang, Okiba Boss
17 - Grenzo, Dungeon Warden
18 - Grist, The Hunger Tide
19 - Gut, True Soul Zealot
20 - Indoraptor, the Perfect Hybrid
21 - Jirina Kudro
22 - Judith, the Scourge Diva
23 - Juri, Master Of The Revue
24 - Kelsien, the Plague
25 - Kess, Dissident Mage
26 - Kinnan, Bonder Prodigy
27 - Klothys, God Of Destiny
28 - Kroxa, Titan Of Death's Hunger
29 - Kyodai, Soul Of Kamigawa
30 - Leovold, Emissary of Trest
31 - Light-Paws, Emperor's Voice
32 - Maelstrom Wanderer
33 - Marath, Will of the Wild
34 - Migloz, Maze Crusher
35 - Minsc, Beloved Ranger
36 - Mono Black Control
37 - Narset, Enlightened Master
38 - Niv-Mizzet Reborn
39 - Niv-Mizzet, Parun
40 - Octavia, Living Thesis
41 - Old Rutstein
42 - Old Stickfingers
43 - Other - Aggro
44 - Other - Combo
45 - Other - Control
46 - Other Partner Aggro
47 - Other Partner Combo
48 - Other Partner Control
49 - Prossh, Skyraider of Kher
50 - Queen Marchesa
51 - Raffine, Scheming Seer
52 - Red Deck Wins
53 - Slimefoot And Squee
54 - Soul of Windgrace
55 - Sygg, River Cutthroat
56 - Sythis, Harvest's Hand
57 - Teferi, Temporal Archmage
58 - The Beamtown Bullies
59 - The Gitrog Monster
60 - The Ur-Dragon
61 - Tivit, Seller Of Secrets
62 - Weenie White
63 - Will 11
64 - Yoshimaru
: 62
Different commanders are used in analyzed decks. Select those you want to keep. If you want to select multiple commanders, use comma-separated choices (e.g. "1, 2")
1 - Ratchet, Field Medic
2 - Kytheon, Hero of Akros
3 - Skrelv, Defector Mite
4 - Adeline, Resplendent Cathar
5 - Isamaru, Hound of Konda
: 2, 3, 4, 5


//----------------------------------------------------------------------
// LANDS - 36 cards
//----------------------------------------------------------------------
22 Snow-Covered Plains - Used by 20/24 decks
1 Eiganjo, Seat of the Empire - Used by 22/24 decks
1 Flagstones of Trokair - Used by 20/24 decks
1 Eiganjo Castle - Used by 19/24 decks
1 Mishra's Factory - Used by 19/24 decks
1 Castle Ardenvale - Used by 18/24 decks
1 Mutavault - Used by 18/24 decks
1 Shefet Dunes - Used by 18/24 decks
1 Blinkmoth Nexus - Used by 15/24 decks
1 Rishadan Port - Used by 14/24 decks
1 Tectonic Edge - Used by 14/24 decks
1 Urza's Saga - Used by 14/24 decks
1 Cave of the Frost Dragon - Used by 14/24 decks
1 Ghost Quarter - Used by 13/24 decks
1 War Room - Used by 12/24 decks
//----------------------------------------------------------------------
// CREATURES - 42 cards
//----------------------------------------------------------------------
1 Mother of Runes - Used by 24/24 decks
1 Thalia, Heretic Cathar - Used by 24/24 decks
1 Thalia, Guardian of Thraben - Used by 23/24 decks
1 Drannith Magistrate - Used by 21/24 decks
1 Giver of Runes - Used by 21/24 decks
1 Lion Sash - Used by 21/24 decks
1 Luminarch Aspirant - Used by 21/24 decks
1 Palace Jailer - Used by 21/24 decks
1 Skyclave Apparition - Used by 21/24 decks
1 Stoneforge Mystic - Used by 21/24 decks
1 Adeline, Resplendent Cathar - Used by 20/24 decks
1 Esper Sentinel - Used by 20/24 decks
1 Leonin Arbiter - Used by 20/24 decks
1 Cathar Commando - Used by 19/24 decks
1 Giant Killer - Used by 19/24 decks
1 Benevolent Bodyguard - Used by 19/24 decks
1 Sanctifier en-Vec - Used by 19/24 decks
1 Bounty Agent - Used by 18/24 decks
1 Brimaz, King of Oreskos - Used by 18/24 decks
1 Selfless Spirit - Used by 18/24 decks
1 Tithe Taker - Used by 18/24 decks
1 Weathered Wayfarer - Used by 18/24 decks
1 Archon of Emeria - Used by 17/24 decks
1 Solitude - Used by 17/24 decks
1 White Plume Adventurer - Used by 17/24 decks
1 Elite Spellbinder - Used by 17/24 decks
1 Recruiter of the Guard - Used by 16/24 decks
1 Phyrexian Revoker - Used by 15/24 decks
1 Reidane, God of the Worthy - Used by 15/24 decks
1 Ranger-Captain of Eos - Used by 15/24 decks
1 Welcoming Vampire - Used by 15/24 decks
1 Kytheon, Hero of Akros - Used by 13/24 decks
1 Seasoned Dungeoneer - Used by 13/24 decks
1 Knight of the White Orchid - Used by 13/24 decks
1 Guardian of Faith - Used by 13/24 decks
1 Archivist of Oghma - Used by 12/24 decks
1 Grand Abolisher - Used by 12/24 decks
1 Mirran Crusader - Used by 12/24 decks
1 Anointed Peacekeeper - Used by 11/24 decks
1 Sungold Sentinel - Used by 11/24 decks
1 Anafenza, Kin-Tree Spirit - Used by 11/24 decks
1 Selfless Savior - Used by 11/24 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 21 cards
//----------------------------------------------------------------------
1 Swords to Plowshares - Used by 24/24 decks
1 Umezawa's Jitte - Used by 24/24 decks
1 March of Otherworldly Light - Used by 22/24 decks
1 Council's Judgment - Used by 21/24 decks
1 Mana Tithe - Used by 20/24 decks
1 Parallax Wave - Used by 20/24 decks
1 Portable Hole - Used by 20/24 decks
1 Gideon Blackblade - Used by 20/24 decks
1 Armageddon - Used by 19/24 decks
1 On Thin Ice - Used by 19/24 decks
1 Reverent Mantra - Used by 18/24 decks
1 Brave the Elements - Used by 18/24 decks
1 Flawless Maneuver - Used by 17/24 decks
1 Enlightened Tutor - Used by 16/24 decks
1 Unexpectedly Absent - Used by 16/24 decks
1 Smuggler's Copter - Used by 15/24 decks
1 Skullclamp - Used by 14/24 decks
1 The Wandering Emperor - Used by 14/24 decks
1 Mox Amber - Used by 13/24 decks
1 Fateful Absence - Used by 12/24 decks
1 Sword of Fire and Ice - Used by 11/24 decks
//----------------------------------------------------------------------
// SIDEBOARD - 1 cards
//----------------------------------------------------------------------
1 Isamaru, Hound of Konda - Used by 15/24 decks
```
Duel-Commander Yoshimaru average deck from MTGTOP8 considering only competitive decks and a selected partner with detailed printing:
```
$ python3 mtgdeckbuild.py -p -c
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
1 - Aminatou, the Fateshifter
2 - Animar, Soul of Elements
3 - Aragorn, King Of Gondor
4 - Aragorn, The Uniter
5 - Arwen, Mortal Queen
6 - Atraxa, Grand Unifier
7 - Atraxa, Praetors' Voice
8 - Azusa, Lost But Seeking
9 - Balmor, Battlemage Captain
10 - Dennick, Pious Apprentice
11 - Elminster
12 - Emmara, Soul Of The Accord
13 - Ertai Resurrected
14 - Ghyrson Starn, Kelermorph
15 - Golos, Tireless Pilgrim
16 - Greasefang, Okiba Boss
17 - Grenzo, Dungeon Warden
18 - Grist, The Hunger Tide
19 - Gut, True Soul Zealot
20 - Indoraptor, the Perfect Hybrid
21 - Jirina Kudro
22 - Judith, the Scourge Diva
23 - Juri, Master Of The Revue
24 - Kelsien, the Plague
25 - Kess, Dissident Mage
26 - Kinnan, Bonder Prodigy
27 - Klothys, God Of Destiny
28 - Kroxa, Titan Of Death's Hunger
29 - Kyodai, Soul Of Kamigawa
30 - Leovold, Emissary of Trest
31 - Light-Paws, Emperor's Voice
32 - Maelstrom Wanderer
33 - Marath, Will of the Wild
34 - Migloz, Maze Crusher
35 - Minsc, Beloved Ranger
36 - Mono Black Control
37 - Narset, Enlightened Master
38 - Niv-Mizzet Reborn
39 - Niv-Mizzet, Parun
40 - Octavia, Living Thesis
41 - Old Rutstein
42 - Old Stickfingers
43 - Other - Aggro
44 - Other - Combo
45 - Other - Control
46 - Other Partner Aggro
47 - Other Partner Combo
48 - Other Partner Control
49 - Prossh, Skyraider of Kher
50 - Queen Marchesa
51 - Raffine, Scheming Seer
52 - Red Deck Wins
53 - Slimefoot And Squee
54 - Soul of Windgrace
55 - Sygg, River Cutthroat
56 - Sythis, Harvest's Hand
57 - Teferi, Temporal Archmage
58 - The Beamtown Bullies
59 - The Gitrog Monster
60 - The Ur-Dragon
61 - Tivit, Seller Of Secrets
62 - Weenie White
63 - Will 11
64 - Yoshimaru
: 64
Yoshimaru, Ever Faithful is used in all analyzed decks as Commander.
Different commanders are used in analyzed decks. Select those you want to keep. If you want to select multiple commanders, use comma-separated choices (e.g. "1, 2")
1 - Bruse Tarl, Boorish Herder
2 - Ludevic, Necro-Alchemist
3 - Tana, the Bloodsower
4 - Reyhan, Last of the Abzan
5 - Tymna the Weaver
: 1


//----------------------------------------------------------------------
// LANDS - 39 cards
//----------------------------------------------------------------------
4 Plains - Used by 16/25 decks
2 Mountain - Used by 17/25 decks
1 Arid Mesa - Used by 25/25 decks
1 Bloodstained Mire - Used by 25/25 decks
1 Command Tower - Used by 25/25 decks
1 Eiganjo Castle - Used by 25/25 decks
1 Eiganjo, Seat of the Empire - Used by 25/25 decks
1 Flooded Strand - Used by 25/25 decks
1 Marsh Flats - Used by 25/25 decks
1 Flagstones of Trokair - Used by 24/25 decks
1 Minas Tirith - Used by 24/25 decks
1 Windswept Heath - Used by 24/25 decks
1 Wooded Foothills - Used by 24/25 decks
1 Plaza of Heroes - Used by 23/25 decks
1 Plateau - Used by 23/25 decks
1 Sacred Foundry - Used by 23/25 decks
1 Scalding Tarn - Used by 23/25 decks
1 Sokenzan, Crucible of Defiance - Used by 23/25 decks
1 Prismatic Vista - Used by 22/25 decks
1 Battlefield Forge - Used by 22/25 decks
1 Shinka, the Bloodsoaked Keep - Used by 22/25 decks
1 Sunbaked Canyon - Used by 21/25 decks
1 Urza's Saga - Used by 19/25 decks
1 Inspiring Vantage - Used by 18/25 decks
1 Clifftop Retreat - Used by 18/25 decks
1 Rugged Prairie - Used by 17/25 decks
1 Hammerheim - Used by 17/25 decks
1 Mines of Moria - Used by 17/25 decks
1 Den of the Bugbear - Used by 13/25 decks
1 Mishra's Factory - Used by 13/25 decks
1 Mana Confluence - Used by 12/25 decks
1 Needleverge Pathway - Used by 12/25 decks
1 The Grey Havens - Used by 11/25 decks
1 Sundown Pass - Used by 11/25 decks
1 Gemstone Caverns - Used by 10/25 decks
//----------------------------------------------------------------------
// CREATURES - 40 cards
//----------------------------------------------------------------------
1 Thalia, Guardian of Thraben - Used by 25/25 decks
1 Solitude - Used by 24/25 decks
1 White Plume Adventurer - Used by 24/25 decks
1 Mother of Runes - Used by 23/25 decks
1 Thalia, Heretic Cathar - Used by 23/25 decks
1 Fury - Used by 23/25 decks
1 Kari Zev, Skyship Raider - Used by 23/25 decks
1 Merry, Esquire of Rohan - Used by 23/25 decks
1 Adeline, Resplendent Cathar - Used by 22/25 decks
1 Baird, Argivian Recruiter - Used by 22/25 decks
1 Feldon, Ronom Excavator - Used by 22/25 decks
1 Laelia, the Blade Reforged - Used by 22/25 decks
1 Loyal Apprentice - Used by 22/25 decks
1 Seasoned Dungeoneer - Used by 21/25 decks
1 Skyclave Apparition - Used by 21/25 decks
1 Giver of Runes - Used by 20/25 decks
1 Skrelv, Defector Mite - Used by 20/25 decks
1 Tajic, Legion's Edge - Used by 20/25 decks
1 Zurgo Bellstriker - Used by 20/25 decks
1 Palace Jailer - Used by 19/25 decks
1 Selfless Spirit - Used by 19/25 decks
1 Stoneforge Mystic - Used by 19/25 decks
1 Ash, Party Crasher - Used by 19/25 decks
1 Squee, Dubious Monarch - Used by 19/25 decks
1 Caves of Chaos Adventurer - Used by 19/25 decks
1 Drannith Magistrate - Used by 18/25 decks
1 Kytheon, Hero of Akros - Used by 16/25 decks
1 Magus of the Moon - Used by 16/25 decks
1 Boromir, Warden of the Tower - Used by 15/25 decks
1 Brimaz, King of Oreskos - Used by 14/25 decks
1 Goro-Goro, Disciple of Ryusei - Used by 14/25 decks
1 Samwise the Stouthearted - Used by 13/25 decks
1 Ardoz, Cobbler of War - Used by 13/25 decks
1 Isamaru, Hound of Konda - Used by 13/25 decks
1 Cathar Commando - Used by 13/25 decks
1 Benevolent Bodyguard - Used by 13/25 decks
1 Giada, Font of Hope - Used by 11/25 decks
1 Bonecrusher Giant - Used by 11/25 decks
1 Winota, Joiner of Forces - Used by 10/25 decks
1 Kellan, the Fae-Blooded - Used by 9/25 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 19 cards
//----------------------------------------------------------------------
1 Flowering of the White Tree - Used by 25/25 decks
1 Shadowspear - Used by 25/25 decks
1 Swords to Plowshares - Used by 25/25 decks
1 Parallax Wave - Used by 24/25 decks
1 Skullclamp - Used by 23/25 decks
1 Lightning Bolt - Used by 23/25 decks
1 Chain Lightning - Used by 22/25 decks
1 Embercleave - Used by 22/25 decks
1 Pyrokinesis - Used by 21/25 decks
1 Forth Eorlingas! - Used by 20/25 decks
1 Blood Moon - Used by 19/25 decks
1 Flame Slash - Used by 18/25 decks
1 Lightning Helix - Used by 16/25 decks
1 Lithomantic Barrage - Used by 16/25 decks
1 Umezawa's Jitte - Used by 13/25 decks
1 Reverent Mantra - Used by 13/25 decks
1 Oust - Used by 10/25 decks
1 Bessie, the Doctor's Roadster - Used by 10/25 decks
1 Gideon Blackblade - Used by 10/25 decks
//----------------------------------------------------------------------
// SIDEBOARD - 2 cards
//----------------------------------------------------------------------
1 Yoshimaru, Ever Faithful - Used by 25/25 decks
1 Bruse Tarl, Boorish Herder - Used by 16/25 decks
```
Standard Gruul Aggro average deck from MTGTOP8 where the deck names includes "Dino" considering onlydecks over the last 1 month:
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
Modern Affinity average deck from MTGTOP8 including some specific cards in the main deck with detailed printing:
```
$python3 mtgdeckbuild.py -i "Galvanic Blast - Haywire Mite" -m -p
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
: 11
Select an archetype:
1 - 4/5c Aggro
2 - 4c Control
3 - Affinity
4 - Amulet Titan
5 - Calibrated Blast
6 - Cascade Crash
7 - CopyCat
8 - Creativity
9 - Creatures Toolbox
10 - Death And Taxes
11 - Death's Shadow
12 - Dredge
13 - Enchantress
14 - Faeries
15 - Goblins
16 - Grixis Control
17 - Gruul Aggro
18 - Hammer Time
19 - Hardened Scales
20 - Heliod Life
21 - Humans
22 - Instant Reanimator
23 - Jeskai Aggro
24 - Jund
25 - Living End
26 - Mardu Midrange
27 - Martyr Life
28 - Merfolk
29 - Mono Black Aggro
30 - Mono Black Control
31 - Orzhov Midrange
32 - Other - Aggro
33 - Other - Combo
34 - Other - Control
35 - Rakdos Aggro
36 - Red Deck Wins
37 - Scapeshift
38 - Teaching Control
39 - Temur Aggro
40 - The One Ring Control
41 - The Rock
42 - The Underworld Cookbook
43 - UB Mill
44 - UR Aggro
45 - UR Control
46 - UW Control
47 - Urza
48 - UrzaTron
49 - Valakut
: 3


//----------------------------------------------------------------------
// LANDS - 17 cards
//----------------------------------------------------------------------
4 Darksteel Citadel - Used by 8/8 decks
4 Urza's Saga - Used by 8/8 decks
4 Silverbluff Bridge - Used by 6/8 decks
2 Treasure Vault - Used by 6/8 decks
2 Tanglepool Bridge - Used by 4/8 decks
1 Island - Used by 8/8 decks
//----------------------------------------------------------------------
// CREATURES - 25 cards
//----------------------------------------------------------------------
4 Memnite - Used by 8/8 decks
4 Ornithopter - Used by 8/8 decks
4 Thought Monitor - Used by 8/8 decks
4 Frogmite - Used by 6/8 decks
4 Patchwork Automaton - Used by 6/8 decks
3 Sojourner's Companion - Used by 6/8 decks
1 Haywire Mite - Used by 8/8 decks
1 Gingerbrute - Used by 5/8 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 18 cards
//----------------------------------------------------------------------
4 Springleaf Drum - Used by 8/8 decks
4 Thoughtcast - Used by 8/8 decks
3 Cranial Plating - Used by 8/8 decks
3 Galvanic Blast - Used by 8/8 decks
1 Shadowspear - Used by 8/8 decks
1 Welding Jar - Used by 8/8 decks
1 Aether Spellbomb - Used by 6/8 decks
1 Nettlecyst - Used by 5/8 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
3 Metallic Rebuke - Used by 8/8 decks
2 Damping Sphere - Used by 5/8 decks
2 Etched Champion - Used by 4/8 decks
2 Soulless Jailer - Used by 4/8 decks
2 Hurkyl's Recall - Used by 4/8 decks
1 Pithing Needle - Used by 8/8 decks
1 Haywire Mite - Used by 7/8 decks
1 Grafdigger's Cage - Used by 4/8 decks
1 Boom / Bust - Used by 3/8 decks
```
Duel-Commander Red Deck Wins average deck from MTGTOP8 including a specific card in the sideboard (commander) and considering only competitive decks:
```
$python3 mtgdeckbuild.py -i "Feldon, Ronom Excavator" -c -s
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
1 - Aminatou, the Fateshifter
2 - Animar, Soul of Elements
3 - Aragorn, King Of Gondor
4 - Aragorn, The Uniter
5 - Arwen, Mortal Queen
6 - Atraxa, Grand Unifier
7 - Atraxa, Praetors' Voice
8 - Azusa, Lost But Seeking
9 - Balmor, Battlemage Captain
10 - Dennick, Pious Apprentice
11 - Elminster
12 - Emmara, Soul Of The Accord
13 - Ertai Resurrected
14 - Esika, God Of The Tree
15 - Ghyrson Starn, Kelermorph
16 - Greasefang, Okiba Boss
17 - Grist, The Hunger Tide
18 - Gut, True Soul Zealot
19 - Heliod, Sun-Crowned
20 - Indoraptor, the Perfect Hybrid
21 - Judith, the Scourge Diva
22 - Juri, Master Of The Revue
23 - Karlov Of The Ghost Council
24 - Kelsien, the Plague
25 - Kess, Dissident Mage
26 - Kinnan, Bonder Prodigy
27 - Klothys, God Of Destiny
28 - Kroxa, Titan Of Death's Hunger
29 - Leovold, Emissary of Trest
30 - Light-Paws, Emperor's Voice
31 - Maelstrom Wanderer
32 - Magda, Brazen Outlaw
33 - Marath, Will of the Wild
34 - Migloz, Maze Crusher
35 - Minsc, Beloved Ranger
36 - Mono Black Control
37 - Narset, Enlightened Master
38 - Niv-Mizzet Reborn
39 - Niv-Mizzet, Parun
40 - Octavia, Living Thesis
41 - Old Rutstein
42 - Old Stickfingers
43 - Other - Aggro
44 - Other - Combo
45 - Other - Control
46 - Other Partner Aggro
47 - Other Partner Combo
48 - Other Partner Control
49 - Prossh, Skyraider of Kher
50 - Queen Marchesa
51 - Raffine, Scheming Seer
52 - Red Deck Wins
53 - Saskia the Unyielding
54 - Slimefoot And Squee
55 - Soul of Windgrace
56 - Sythis, Harvest's Hand
57 - Teferi, Temporal Archmage
58 - The Beamtown Bullies
59 - The Gitrog Monster
60 - The Ur-Dragon
61 - Tivit, Seller Of Secrets
62 - Weenie White
63 - Will 11
64 - Yoshimaru
: 52


// MAIN DECK
1 Ramunap Ruins
1 Mutavault
1 Den of the Bugbear
1 Mishra's Factory
1 Sokenzan, Crucible of Defiance
1 Barbarian Ring
24 Snow-Covered Mountain
1 Arid Mesa
1 Bloodstained Mire
1 Scalding Tarn
1 Wooded Foothills
1 War Room
1 Prismatic Vista
1 Shinka, the Bloodsoaked Keep
1 Castle Embereth
1 Bomat Courier
1 Laelia, the Blade Reforged
1 Monastery Swiftspear
1 Soul-Scar Mage
1 Zurgo Bellstriker
1 Goblin Guide
1 Loyal Apprentice
1 Magus of the Moon
1 Falkenrath Pit Fighter
1 Bonecrusher Giant
1 Fury
1 Ahn-Crop Crasher
1 Grim Lavamancer
1 Dragon's Rage Channeler
1 Falkenrath Gorger
1 Icehide Golem
1 Embereth Veteran
1 Phoenix of Ash
1 Eidolon of the Great Revel
1 Stromkirk Noble
1 Slicer, Hired Muscle
1 Squee, Dubious Monarch
1 Arc Trail
1 Fiery Confluence
1 Fireblast
1 Incinerate
1 Lightning Bolt
1 Lightning Strike
1 Pyrokinesis
1 Chain Lightning
1 Exquisite Firecraft
1 Light Up the Stage
1 Play with Fire
1 Rift Bolt
1 Seal of Fire
1 Searing Blaze
1 Searing Spear
1 Skewer the Critics
1 Wild Slash
1 Blood Moon
1 Forked Bolt
1 Kumano Faces Kakkazan
1 Lava Spike
1 Slaying Fire
1 Burst Lightning
1 Galvanic Blast
1 Sulfuric Vortex
1 Tarfire
1 Flames of the Blood Hand
1 Roil Eruption
1 Skullcrack
1 Incendiary Flow
1 Invasion of Regatha
1 Shock
1 Volcanic Hammer
1 Reckless Impulse
1 Wrenn's Resolve
1 Flame Javelin
1 Chandra, Torch of Defiance
1 Flame Slash
1 Force of Rage
// SIDEBOARD
1 Feldon, Ronom Excavator
```
Duel-Commander Atraxa, Grand Unifier average deck from MTGDECKS displaying only the top 15 archetypes in the interactive mode selection menu and with detailed printing:
```
$ python3 mtgdeckbuild.py -w mtgdecks -t 15 -p
Select a format:
1 - Standard
2 - Pioneer
3 - Modern
4 - Pauper
5 - Alchemy
6 - Explorer
7 - Historic
8 - Timeless
9 - Commander
10 - Duel-Commander
11 - Brawl
12 - Historic-Brawl
13 - Legacy
14 - Vintage
15 - Premodern
16 - Old-School
: 10
Select an archetype:
1 - Aminatou, the Fateshifter
2 - Aragorn, King of Gondor
3 - Atraxa, Grand Unifier
4 - Bruse Tarl, Boorish Herder
5 - Dihada, Binder of Wills
6 - Ertai Resurrected
7 - Feldon, Ronom Excavator
8 - Ghyrson Starn, Kelermorph
9 - Grist, the Hunger Tide
10 - Raffine, Scheming Seer
11 - Slimefoot and Squee
12 - Tana, the Bloodsower
13 - Tivit, Seller of Secrets
14 - Tymna the Weaver
15 - Yoshimaru, Ever Faithful
: 3


//----------------------------------------------------------------------
// LANDS - 41 cards
//----------------------------------------------------------------------
1 Arid Mesa - Used by 25/25 decks
1 Command Tower - Used by 25/25 decks
1 Hallowed Fountain - Used by 25/25 decks
1 Marsh Flats - Used by 25/25 decks
1 Misty Rainforest - Used by 25/25 decks
1 Otawara, Soaring City - Used by 25/25 decks
1 Raffine's Tower - Used by 25/25 decks
1 Scalding Tarn - Used by 25/25 decks
1 Verdant Catacombs - Used by 25/25 decks
1 Watery Grave - Used by 25/25 decks
1 Windswept Heath - Used by 25/25 decks
1 Zagoth Triome - Used by 25/25 decks
1 Bayou - Used by 24/25 decks
1 Flooded Strand - Used by 24/25 decks
1 Glacial Fortress - Used by 24/25 decks
1 Polluted Delta - Used by 24/25 decks
1 Reflecting Pool - Used by 24/25 decks
1 Spara's Headquarters - Used by 24/25 decks
1 Wooded Foothills - Used by 24/25 decks
1 Bloodstained Mire - Used by 23/25 decks
1 Deserted Beach - Used by 23/25 decks
1 Drowned Catacomb - Used by 23/25 decks
1 Savannah - Used by 23/25 decks
1 Scrubland - Used by 23/25 decks
1 Temple of the False God - Used by 23/25 decks
1 Tropical Island - Used by 23/25 decks
1 Underground Sea - Used by 23/25 decks
1 Boseiju, Who Endures - Used by 22/25 decks
1 Mystic Sanctuary - Used by 22/25 decks
1 Prismatic Vista - Used by 22/25 decks
1 Shipwreck Marsh - Used by 22/25 decks
1 Tundra - Used by 22/25 decks
1 Island - Used by 22/25 decks
1 Plains - Used by 22/25 decks
1 Swamp - Used by 22/25 decks
1 Forest - Used by 21/25 decks
1 Path of Ancestry - Used by 20/25 decks
1 Hinterland Harbor - Used by 18/25 decks
1 Seachrome Coast - Used by 17/25 decks
1 Hengegate Pathway - Used by 16/25 decks
1 Mystic Gate - Used by 16/25 decks
//----------------------------------------------------------------------
// CREATURES - 5 cards
//----------------------------------------------------------------------
1 Baleful Strix - Used by 25/25 decks
1 Snapcaster Mage - Used by 25/25 decks
1 Solitude - Used by 25/25 decks
1 Orcish Bowmasters - Used by 23/25 decks
1 Emrakul, the Promised End - Used by 21/25 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 53 cards
//----------------------------------------------------------------------
1 Abrupt Decay - Used by 25/25 decks
1 Brainstorm - Used by 25/25 decks
1 Cut Down - Used by 25/25 decks
1 Dark Ritual - Used by 25/25 decks
1 Memory Lapse - Used by 25/25 decks
1 Swords to Plowshares - Used by 25/25 decks
1 Demonic Tutor - Used by 25/25 decks
1 Supreme Verdict - Used by 25/25 decks
1 Toxic Deluge - Used by 25/25 decks
1 Teferi, Time Raveler - Used by 25/25 decks
1 Shorikai, Genesis Engine - Used by 24/25 decks
1 Cling to Dust - Used by 24/25 decks
1 Counterspell - Used by 24/25 decks
1 Fatal Push - Used by 24/25 decks
1 Force of Will - Used by 24/25 decks
1 Mana Leak - Used by 24/25 decks
1 Sauron's Ransom - Used by 24/25 decks
1 Damn - Used by 24/25 decks
1 Preordain - Used by 24/25 decks
1 Leyline Binding - Used by 24/25 decks
1 Oko, Thief of Crowns - Used by 24/25 decks
1 Force Spike - Used by 23/25 decks
1 Kaya's Guile - Used by 23/25 decks
1 Lose Focus - Used by 23/25 decks
1 Memory Deluge - Used by 23/25 decks
1 Tainted Pact - Used by 23/25 decks
1 Void Rend - Used by 23/25 decks
1 Wash Away - Used by 23/25 decks
1 Ponder - Used by 23/25 decks
1 Dream Halls - Used by 23/25 decks
1 Spell Snare - Used by 23/25 decks
1 Cryptic Command - Used by 22/25 decks
1 Drown in the Loch - Used by 22/25 decks
1 Force of Negation - Used by 22/25 decks
1 Mana Tithe - Used by 22/25 decks
1 Mystic Confluence - Used by 22/25 decks
1 Stern Scolding - Used by 22/25 decks
1 Tale's End - Used by 22/25 decks
1 Prismatic Ending - Used by 22/25 decks
1 The Wandering Emperor - Used by 22/25 decks
1 Evasive Action - Used by 21/25 decks
1 Jace, the Mind Sculptor - Used by 21/25 decks
1 Arcane Signet - Used by 20/25 decks
1 Cosmic Rebirth - Used by 20/25 decks
1 Growth Spiral - Used by 20/25 decks
1 Lórien Revealed - Used by 20/25 decks
1 Teferi, Hero of Dominaria - Used by 20/25 decks
1 Archmage's Charm - Used by 19/25 decks
1 Remand - Used by 18/25 decks
1 Reprieve - Used by 16/25 decks
1 Unexpectedly Absent - Used by 15/25 decks
1 Oust - Used by 14/25 decks
1 Sunset Revelry - Used by 13/25 decks
//----------------------------------------------------------------------
// SIDEBOARD - 1 cards
//----------------------------------------------------------------------
1 Atraxa, Grand Unifier - Used by 25/25 decks
```
Standard Gruul Dinosaurs average deck from MTGDECKS using the 200 last decks:
```
$ python3 mtgdeckbuild.py -w mtgdecks -d 200
Select a format:
1 - Standard
2 - Pioneer
3 - Modern
4 - Pauper
5 - Alchemy
6 - Explorer
7 - Historic
8 - Timeless
9 - Commander
10 - Duel-Commander
11 - Brawl
12 - Historic-Brawl
13 - Legacy
14 - Vintage
15 - Premodern
16 - Old-School
: 1
Select an archetype:
1 - 4 Color Angels
2 - 4 Color Beanstalk
3 - 4 Color Dragons
4 - 4 Color Emergence
5 - 4 Color Isshin
6 - 4 Color Legends
7 - 4 Color Pia
8 - 4 Color Reanimator
9 - 4 Color Rona
10 - 4 Color Superfriends
11 - 5 Color Humans
12 - 5 Color Legends
13 - 5 Color Midrange
14 - Abzan Angels
15 - Abzan Control
16 - Abzan Humans
17 - Abzan Lifegain
18 - Abzan Midrange
19 - Abzan Phyrexians
20 - Abzan Ratadrabik
21 - Abzan Rigging
22 - Abzan Sacrifice
23 - Azorius Adventures
24 - Azorius Artifacts
25 - Azorius Awakening
26 - Azorius Blink
27 - Azorius Calendar
28 - Azorius Control
29 - Azorius Convoke
30 - Azorius Craft
31 - Azorius Flash
32 - Azorius Justice
33 - Azorius Mentor
34 - Azorius Midrange
35 - Azorius Mill
36 - Azorius Powerstones
37 - Azorius Prototypes
38 - Azorius Reconstruction
39 - Azorius Schooner
40 - Azorius Soldiers
41 - Azorius Spirits
42 - Azorius Superfriends
43 - Azorius Tempo
44 - Azorius Tezzeret
45 - Azorius Toxic
46 - Bant Aggro
47 - Bant Angels
48 - Bant Artifacts
49 - Bant Beanstalk
50 - Bant Cauldron
51 - Bant Control
52 - Bant Midrange
53 - Bant Ramp
54 - Bant Tokens
55 - Bant Toxic
56 - Big Red
57 - Boros Aggro
58 - Boros Artifacts
59 - Boros Blink
60 - Boros Bombardment
61 - Boros Burn
62 - Boros Calendar
63 - Boros Control
64 - Boros Convoke
65 - Boros Counters
66 - Boros Discover
67 - Boros Enchantments
68 - Boros Equipments
69 - Boros Humans
70 - Boros Mentor
71 - Boros Midrange
72 - Boros Pia
73 - Boros Powerstones
74 - Boros Soldiers
75 - Boros Tokens
76 - Boros Virtuoso
77 - Caves
78 - Chaotic Transformation
79 - Dimir Caves
80 - Dimir Control
81 - Dimir Crime
82 - Dimir Descend
83 - Dimir Faeries
84 - Dimir Midrange
85 - Dimir Mill
86 - Dimir Mindlink
87 - Dimir Proliferate
88 - Dimir Schooner
89 - Dimir Tempo
90 - Domain Adventures
91 - Domain Alara
92 - Domain Discover
93 - Domain Leyline
94 - Domain Ramp
95 - Domain Singularity
96 - Elves
97 - Esper Adventures
98 - Esper Aggro
99 - Esper Awakening
100 - Esper Control
101 - Esper Faeries
102 - Esper Flash
103 - Esper Grounds
104 - Esper Incubate
105 - Esper Mentor
106 - Esper Midrange
107 - Esper Proliferate
108 - Esper Reanimator
109 - Esper Roles
110 - Esper Rona
111 - Esper Soldiers
112 - Esper Superfriends
113 - Esper Tempo
114 - Esper Tokens
115 - Goblins
116 - Golgari Aggro
117 - Golgari Cauldron
118 - Golgari Emergence
119 - Golgari Enchantments
120 - Golgari Food
121 - Golgari Midrange
122 - Golgari Phyrexians
123 - Golgari Ramp
124 - Golgari Rigging
125 - Golgari Zombies
126 - Grixis Adventures
127 - Grixis Anvil
128 - Grixis Control
129 - Grixis Descend
130 - Grixis Discover
131 - Grixis Dragons
132 - Grixis Hellraiser
133 - Grixis Midrange
134 - Grixis Pirates
135 - Grixis Ramp
136 - Grixis Reanimator
137 - Grixis Singularity
138 - Grixis Throne
139 - Grixis Vampires
140 - Gruul Aggro
141 - Gruul Artifacts
142 - Gruul Calendar
143 - Gruul Cauldron
144 - Gruul Counters
145 - Gruul Dinosaurs
146 - Gruul Disguise
147 - Gruul Food
148 - Gruul Midrange
149 - Gruul Midrange
150 - Gruul Ramp
151 - Gruul Ramp
152 - Gruul Werewolves
153 - Izzet Artifacts
154 - Izzet Control
155 - Izzet Mindlink
156 - Izzet Pirates
157 - Izzet Powerstones
158 - Izzet Spellslinger
159 - Jeskai Artifact
160 - Jeskai Calendar
161 - Jeskai Control
162 - Jeskai Discover
163 - Jeskai Dragons
164 - Jeskai Equipments
165 - Jeskai Humans
166 - Jeskai Mentor
167 - Jeskai Midrange
168 - Jeskai Pia
169 - Jeskai Soldiers
170 - Jeskai Spells
171 - Jund Aggro
172 - Jund Anvil
173 - Jund Cauldron
174 - Jund Dinosaurs
175 - Jund Discover
176 - Jund Emergence
177 - Jund Graveyard
178 - Jund Land Destruction
179 - Jund Midrange
180 - Jund Ramp
181 - Jund Reanimator
182 - Jund Rigging
183 - Jund Throne
184 - MTGA decklists
185 - Mardu Calendar
186 - Mardu Discover
187 - Mardu Greasefang
188 - Mardu Humans
189 - Mardu Lifegain
190 - Mardu Midrange
191 - Mardu Ratadrabik
192 - Mardu Reanimator
193 - Mardu Sacrifice
194 - Mardu Tokens
195 - Mardu Vampires
196 - Mono Black
197 - Mono Black Rats
198 - Mono Black Toxic
199 - Mono Blue Artifacts
200 - Mono Blue Crime
201 - Mono Blue Ninjas
202 - Mono Blue Tempo
203 - Mono Green
204 - Mono Red Calendar
205 - Mono White Angels
206 - Mono White Artifacts
207 - Mono White Control
208 - Mono White Craft
209 - Mono White Lifegain
210 - Mono White Midrange
211 - Mono White Tokens
212 - Mono White Toxic
213 - Naya Artifacts
214 - Naya Break Out
215 - Naya Calendar
216 - Naya Cascade
217 - Naya Counters
218 - Naya Dinosaurs
219 - Naya Discover
220 - Naya Domain
221 - Naya Humans
222 - Naya Midrange
223 - Naya Pia
224 - Naya Ramp
225 - Naya Throne
226 - Naya Tokens
227 - Naya Virtuoso
228 - Naya Werewolves
229 - Niv-Mizzet Control
230 - Orzhov Angels
231 - Orzhov Artifacts
232 - Orzhov Blink
233 - Orzhov Control
234 - Orzhov Enchantments
235 - Orzhov Humans
236 - Orzhov Justice
237 - Orzhov Lifegain
238 - Orzhov Midrange
239 - Orzhov Ratadrabik
240 - Orzhov Reanimator
241 - Orzhov Sacrifice
242 - Orzhov Scam
243 - Orzhov Superfriends
244 - Orzhov Tokens
245 - Rainbow Humans
246 - Rakdos Aggro
247 - Rakdos Anvil
248 - Rakdos Bombardment
249 - Rakdos Conquest
250 - Rakdos Discover
251 - Rakdos Dragons
252 - Rakdos Inti
253 - Rakdos Midrange
254 - Rakdos Ramp
255 - Rakdos Reanimator
256 - Rakdos Sacrifice
257 - Rakdos Vampires
258 - Red Deck Wins
259 - Red Deck Wins
260 - Rogue
261 - Selesnya Angels
262 - Selesnya Artifacts
263 - Selesnya Blink
264 - Selesnya Counters
265 - Selesnya Enchantments
266 - Selesnya Festival
267 - Selesnya Humans
268 - Selesnya Legends
269 - Selesnya Midrange
270 - Selesnya Ramp
271 - Selesnya Tokens
272 - Selesnya Toxic
273 - Simic Auras
274 - Simic Beanstalk
275 - Simic Cauldron
276 - Simic Counters
277 - Simic Food
278 - Simic Grounds
279 - Simic Merfolks
280 - Simic Ramp
281 - Simic Tempo
282 - Simic Tezzeret
283 - Sultai Cauldron
284 - Sultai Emergence
285 - Sultai Graveyard
286 - Sultai Midrange
287 - Sultai Rigging
288 - Sultai Self Mill
289 - Sultai Slogurk
290 - Sultai Tokens
291 - Sultai Toxic
292 - Temur Cauldron
293 - Temur Counters
294 - Temur Discover
295 - Temur Treasures
296 - White Weenie
: 145


// MAIN DECK
5 Forest
3 Mountain
4 Karplusan Forest
4 Copperline Gorge
2 Restless Ridgeline
3 Cavern of Souls
1 Boseiju, Who Endures
1 Sokenzan, Crucible of Defiance
3 Rockfall Vale
4 Pugnacious Hammerskull
4 Ixalli's Lorekeeper
3 Itzquinth, Firstborn of Gishath
3 Bonehoard Dracosaur
3 Intrepid Paleontologist
3 Trumpeting Carnosaur
3 Hulking Raptor
3 Palani's Hatcher
4 Belligerent Yearling
1 Etali, Primal Conqueror
3 Triumphant Chomp
// SIDEBOARD
3 Lithomantic Barrage
2 Tranquil Frillback
3 Urabrask's Forge
2 Nissa, Ascended Animist
2 Witchstalker Frenzy
2 Brotherhood's End
1 End the Festivities
```
Standard White Weenie average deck from MTGDECKS including a specific card in the sideboard with detailed printing:
```
$ python3 mtgdeckbuild.py -w mtgdecks -s -i "Get Lost" -p
Select a format:
1 - Standard
2 - Pioneer
3 - Modern
4 - Pauper
5 - Alchemy
6 - Explorer
7 - Historic
8 - Timeless
9 - Commander
10 - Duel-Commander
11 - Brawl
12 - Historic-Brawl
13 - Legacy
14 - Vintage
15 - Premodern
16 - Old-School
: 1
Select an archetype:
1 - 4 Color Angels
2 - 4 Color Beanstalk
3 - 4 Color Dragons
4 - 4 Color Emergence
5 - 4 Color Isshin
6 - 4 Color Legends
7 - 4 Color Pia
8 - 4 Color Reanimator
9 - 4 Color Rona
10 - 4 Color Superfriends
11 - 5 Color Humans
12 - 5 Color Legends
13 - 5 Color Midrange
14 - Abzan Angels
15 - Abzan Control
16 - Abzan Humans
17 - Abzan Lifegain
18 - Abzan Midrange
19 - Abzan Phyrexians
20 - Abzan Ratadrabik
21 - Abzan Rigging
22 - Abzan Sacrifice
23 - Azorius Adventures
24 - Azorius Artifacts
25 - Azorius Awakening
26 - Azorius Blink
27 - Azorius Calendar
28 - Azorius Control
29 - Azorius Convoke
30 - Azorius Craft
31 - Azorius Flash
32 - Azorius Justice
33 - Azorius Mentor
34 - Azorius Midrange
35 - Azorius Mill
36 - Azorius Powerstones
37 - Azorius Prototypes
38 - Azorius Reconstruction
39 - Azorius Schooner
40 - Azorius Soldiers
41 - Azorius Spirits
42 - Azorius Superfriends
43 - Azorius Tempo
44 - Azorius Tezzeret
45 - Azorius Toxic
46 - Bant Aggro
47 - Bant Angels
48 - Bant Artifacts
49 - Bant Beanstalk
50 - Bant Cauldron
51 - Bant Control
52 - Bant Midrange
53 - Bant Ramp
54 - Bant Tokens
55 - Bant Toxic
56 - Big Red
57 - Boros Aggro
58 - Boros Artifacts
59 - Boros Blink
60 - Boros Bombardment
61 - Boros Burn
62 - Boros Calendar
63 - Boros Control
64 - Boros Convoke
65 - Boros Counters
66 - Boros Discover
67 - Boros Enchantments
68 - Boros Equipments
69 - Boros Humans
70 - Boros Mentor
71 - Boros Midrange
72 - Boros Pia
73 - Boros Powerstones
74 - Boros Soldiers
75 - Boros Tokens
76 - Boros Virtuoso
77 - Caves
78 - Chaotic Transformation
79 - Dimir Caves
80 - Dimir Control
81 - Dimir Crime
82 - Dimir Descend
83 - Dimir Faeries
84 - Dimir Midrange
85 - Dimir Mill
86 - Dimir Mindlink
87 - Dimir Proliferate
88 - Dimir Schooner
89 - Dimir Tempo
90 - Domain Adventures
91 - Domain Alara
92 - Domain Discover
93 - Domain Leyline
94 - Domain Ramp
95 - Domain Singularity
96 - Elves
97 - Esper Adventures
98 - Esper Aggro
99 - Esper Awakening
100 - Esper Control
101 - Esper Faeries
102 - Esper Flash
103 - Esper Grounds
104 - Esper Incubate
105 - Esper Mentor
106 - Esper Midrange
107 - Esper Proliferate
108 - Esper Reanimator
109 - Esper Roles
110 - Esper Rona
111 - Esper Soldiers
112 - Esper Superfriends
113 - Esper Tempo
114 - Esper Tokens
115 - Goblins
116 - Golgari Aggro
117 - Golgari Cauldron
118 - Golgari Emergence
119 - Golgari Enchantments
120 - Golgari Food
121 - Golgari Midrange
122 - Golgari Phyrexians
123 - Golgari Ramp
124 - Golgari Rigging
125 - Golgari Zombies
126 - Grixis Adventures
127 - Grixis Anvil
128 - Grixis Control
129 - Grixis Descend
130 - Grixis Discover
131 - Grixis Dragons
132 - Grixis Hellraiser
133 - Grixis Midrange
134 - Grixis Pirates
135 - Grixis Ramp
136 - Grixis Reanimator
137 - Grixis Singularity
138 - Grixis Throne
139 - Grixis Vampires
140 - Gruul Aggro
141 - Gruul Artifacts
142 - Gruul Calendar
143 - Gruul Cauldron
144 - Gruul Counters
145 - Gruul Dinosaurs
146 - Gruul Disguise
147 - Gruul Food
148 - Gruul Midrange
149 - Gruul Midrange
150 - Gruul Ramp
151 - Gruul Ramp
152 - Gruul Werewolves
153 - Izzet Artifacts
154 - Izzet Control
155 - Izzet Mindlink
156 - Izzet Pirates
157 - Izzet Powerstones
158 - Izzet Spellslinger
159 - Jeskai Artifact
160 - Jeskai Calendar
161 - Jeskai Control
162 - Jeskai Discover
163 - Jeskai Dragons
164 - Jeskai Equipments
165 - Jeskai Humans
166 - Jeskai Mentor
167 - Jeskai Midrange
168 - Jeskai Pia
169 - Jeskai Soldiers
170 - Jeskai Spells
171 - Jund Aggro
172 - Jund Anvil
173 - Jund Cauldron
174 - Jund Dinosaurs
175 - Jund Discover
176 - Jund Emergence
177 - Jund Graveyard
178 - Jund Land Destruction
179 - Jund Midrange
180 - Jund Ramp
181 - Jund Reanimator
182 - Jund Rigging
183 - Jund Throne
184 - MTGA decklists
185 - Mardu Calendar
186 - Mardu Discover
187 - Mardu Greasefang
188 - Mardu Humans
189 - Mardu Lifegain
190 - Mardu Midrange
191 - Mardu Ratadrabik
192 - Mardu Reanimator
193 - Mardu Sacrifice
194 - Mardu Tokens
195 - Mardu Vampires
196 - Mono Black
197 - Mono Black Rats
198 - Mono Black Toxic
199 - Mono Blue Artifacts
200 - Mono Blue Crime
201 - Mono Blue Ninjas
202 - Mono Blue Tempo
203 - Mono Green
204 - Mono Red Calendar
205 - Mono White Angels
206 - Mono White Artifacts
207 - Mono White Control
208 - Mono White Craft
209 - Mono White Lifegain
210 - Mono White Midrange
211 - Mono White Tokens
212 - Mono White Toxic
213 - Naya Artifacts
214 - Naya Break Out
215 - Naya Calendar
216 - Naya Cascade
217 - Naya Counters
218 - Naya Dinosaurs
219 - Naya Discover
220 - Naya Domain
221 - Naya Humans
222 - Naya Midrange
223 - Naya Pia
224 - Naya Ramp
225 - Naya Throne
226 - Naya Tokens
227 - Naya Virtuoso
228 - Naya Werewolves
229 - Niv-Mizzet Control
230 - Orzhov Angels
231 - Orzhov Artifacts
232 - Orzhov Blink
233 - Orzhov Control
234 - Orzhov Enchantments
235 - Orzhov Humans
236 - Orzhov Justice
237 - Orzhov Lifegain
238 - Orzhov Midrange
239 - Orzhov Ratadrabik
240 - Orzhov Reanimator
241 - Orzhov Sacrifice
242 - Orzhov Scam
243 - Orzhov Superfriends
244 - Orzhov Tokens
245 - Rainbow Humans
246 - Rakdos Aggro
247 - Rakdos Anvil
248 - Rakdos Bombardment
249 - Rakdos Conquest
250 - Rakdos Discover
251 - Rakdos Dragons
252 - Rakdos Inti
253 - Rakdos Midrange
254 - Rakdos Ramp
255 - Rakdos Reanimator
256 - Rakdos Sacrifice
257 - Rakdos Vampires
258 - Red Deck Wins
259 - Red Deck Wins
260 - Rogue
261 - Selesnya Angels
262 - Selesnya Artifacts
263 - Selesnya Blink
264 - Selesnya Counters
265 - Selesnya Enchantments
266 - Selesnya Festival
267 - Selesnya Humans
268 - Selesnya Legends
269 - Selesnya Midrange
270 - Selesnya Ramp
271 - Selesnya Tokens
272 - Selesnya Toxic
273 - Simic Auras
274 - Simic Beanstalk
275 - Simic Cauldron
276 - Simic Counters
277 - Simic Food
278 - Simic Grounds
279 - Simic Merfolks
280 - Simic Ramp
281 - Simic Tempo
282 - Simic Tezzeret
283 - Sultai Cauldron
284 - Sultai Emergence
285 - Sultai Graveyard
286 - Sultai Midrange
287 - Sultai Rigging
288 - Sultai Self Mill
289 - Sultai Slogurk
290 - Sultai Tokens
291 - Sultai Toxic
292 - Temur Cauldron
293 - Temur Counters
294 - Temur Discover
295 - Temur Treasures
296 - White Weenie
: 296


//----------------------------------------------------------------------
// LANDS - 20 cards
//----------------------------------------------------------------------
18 Plains - Used by 3/3 decks
2 Eiganjo, Seat of the Empire - Used by 3/3 decks
//----------------------------------------------------------------------
// CREATURES - 39 cards
//----------------------------------------------------------------------
4 Recruitment Officer - Used by 3/3 decks
4 Thalia, Guardian of Thraben - Used by 3/3 decks
4 Warden of the Inner Sky - Used by 2/3 decks
4 Hopeful Initiate - Used by 2/3 decks
4 Kellan, Daring Traveler - Used by 2/3 decks
4 Coppercoat Vanguard - Used by 2/3 decks
4 Resolute Reinforcements - Used by 2/3 decks
4 Adeline, Resplendent Cathar - Used by 2/3 decks
4 Knight-Errant of Eos - Used by 2/3 decks
3 Sanguine Evangelist - Used by 2/3 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 1 cards
//----------------------------------------------------------------------
1 Lay Down Arms - Used by 1/3 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
3 Invasion of Gobakhan - Used by 3/3 decks
3 Wedding Announcement - Used by 1/3 decks
3 Kutzil's Flanker - Used by 1/3 decks
2 Get Lost - Used by 3/3 decks
2 Extraction Specialist - Used by 2/3 decks
1 Werefox Bodyguard - Used by 2/3 decks
1 Lantern Flare - Used by 1/3 decks
```
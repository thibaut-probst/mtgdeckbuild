# mtgdeckbuild
A Magic: The Gathering format archetype average deck building tool based on tournaments results.

# MTGDeckBuild
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)  
---  
A Magic: The Gathering format archetype average deck building tool based on tournaments results. Deck building is based on currently played archetypes and most used cards in tournaments decks. Generally, the last 25 decks are used but some filter may affect the number of analyzed decks.

## Features

* Support of [MTGTOP8](https://mtgtop8.com) and [MTGDECKS](https://mtgdecks.net) as website data sources.
* Support of all formats with automatic discovery.
* Support of all archetypes with automatic discovery and possibility to only parse a given number of top archetypes.
* Filtering available to only consider competitive decks (only for MTGTOP8).
* Filtering available to only consider decks including given card names in main deck and/or sideboard.
* Filtering available to only consider decks including given names (only for MTGTOP8).
* Filtering available to only consider decks over the last given months (only for MTGTOP8).
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
usage: mtgdeckbuild.py [-h] [--website-source WEBSITE_SOURCE] [--top-archetypes TOP_ARCHETYPES] [--details]
                       [--competitive-only] [--name NAME] [--include-cards INCLUDE_CARDS] [--main-include]
                       [--side-include] [--last-months LAST_MONTHS]

options:
  -h, --help            show this help message and exit
  --website-source WEBSITE_SOURCE, -w WEBSITE_SOURCE
                        Website data source to use (mtgtop8 or mtgdecks ; default: mtgtop8)
  --top-archetypes TOP_ARCHETYPES, -t TOP_ARCHETYPES
                        The number of top archetypes to parse (default: all archetypes)
  --details, -d         Print deck with details: sections and number of decks using each card
  --competitive-only, -c
                        Only consider competitive decks (only for MTGTOP8)
  --name NAME, -n NAME  Only consider decks including given deck name (only for MTGTOP8)
  --include-cards INCLUDE_CARDS, -i INCLUDE_CARDS
                        Only consider decks including given cards (use dash-separated card names if passing multiple cards, must be used with --main-deck/-m, --sideboard/-s arguments or both)
  --main-include, -m    Consider cards to include for the main deck (must be used with --include-cards/-i, also include cards for the sideboard for MTGDECKS)
  --side-include, -s    Consider cards to include for the sideboard (must be used with --include-cards/-i)
  --last-months LAST_MONTHS, -l LAST_MONTHS
                        Only consider decks from the last given months (only for MTGTOP8)
```

## Examples
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
12 - Belcher
13 - Bomberman
14 - Burn
15 - Canadian Threshold
16 - Cascade Crash
17 - Cephalid Breakfast
18 - Cloudpost Ramp
19 - Curses
20 - Dark Depths
21 - Deadguy Ale
22 - Death & Taxes
23 - Death's Shadow
24 - Delver (Other)
25 - Dimir Aggro
26 - Doomsday
27 - Dragon Stompy
28 - Dredge
29 - Eldrazi Aggro
30 - Elves
31 - Enchantress
32 - Esper Aggro
33 - Food Griffin
34 - Goblins
35 - Grixis Aggro
36 - Grixis Control
37 - Hammer Time
38 - High Tide
39 - Hive Mind
40 - Hogaak
41 - Hollow One Madness
42 - Humans
43 - Infect
44 - Initiative Stompy
45 - Jund
46 - Lands
47 - Landstill
48 - Loam
49 - Maverick
50 - Merfolk
51 - Mississippi River
52 - Mono Black Aggro
53 - Mono Black Combo
54 - Mono Red Combo
55 - Mystic Forge
56 - Nic Fit 
57 - Ninja
58 - Other - Aggro
59 - Other - Combo
60 - Other - Control
61 - Painter
62 - Patriot Aggro
63 - Pox
64 - Reanimator
65 - Shoal Infect
66 - Show and Tell
67 - Slivers
68 - Stiflenought
69 - Stoneblade
70 - Storm
71 - The Rock (Junk)
72 - UR Aggro
73 - UWx Control
: 14


// MAIN DECK
12 Mountain
3 Arid Mesa
2 Barbarian Ring
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
2 Exquisite Firecraft
2 Roiling Vortex
// SIDEBOARD
3 Smash to Smithereens
2 Roiling Vortex
2 Pyroblast
2 Ensnaring Bridge
4 Leyline of the Void
2 Searing Blood
```
```
$ python3 mtgdeckbuild.py -d
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
12 - Belcher
13 - Bomberman
14 - Burn
15 - Canadian Threshold
16 - Cascade Crash
17 - Cephalid Breakfast
18 - Cloudpost Ramp
19 - Curses
20 - Dark Depths
21 - Deadguy Ale
22 - Death & Taxes
23 - Death's Shadow
24 - Delver (Other)
25 - Dimir Aggro
26 - Doomsday
27 - Dragon Stompy
28 - Dredge
29 - Eldrazi Aggro
30 - Elves
31 - Enchantress
32 - Esper Aggro
33 - Food Griffin
34 - Goblins
35 - Grixis Aggro
36 - Grixis Control
37 - Hammer Time
38 - High Tide
39 - Hive Mind
40 - Hogaak
41 - Hollow One Madness
42 - Humans
43 - Infect
44 - Initiative Stompy
45 - Jund
46 - Lands
47 - Landstill
48 - Loam
49 - Maverick
50 - Merfolk
51 - Mississippi River
52 - Mono Black Aggro
53 - Mono Black Combo
54 - Mono Red Combo
55 - Mystic Forge
56 - Nic Fit 
57 - Ninja
58 - Other - Aggro
59 - Other - Combo
60 - Other - Control
61 - Painter
62 - Patriot Aggro
63 - Pox
64 - Reanimator
65 - Shoal Infect
66 - Show and Tell
67 - Slivers
68 - Stiflenought
69 - Stoneblade
70 - Storm
71 - The Rock (Junk)
72 - UR Aggro
73 - UWx Control
: 14


//----------------------------------------------------------------------
// LANDS - 17 cards
//----------------------------------------------------------------------
12 Mountain - Used by 22/25 decks
3 Arid Mesa - Used by 10/25 decks
2 Barbarian Ring - Used by 7/25 decks
//----------------------------------------------------------------------
// CREATURES - 12 cards
//----------------------------------------------------------------------
4 Goblin Guide - Used by 23/25 decks
4 Monastery Swiftspear - Used by 23/25 decks
4 Eidolon of the Great Revel - Used by 21/25 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 31 cards
//----------------------------------------------------------------------
4 Lightning Bolt - Used by 25/25 decks
4 Chain Lightning - Used by 23/25 decks
4 Fireblast - Used by 23/25 decks
4 Lava Spike - Used by 23/25 decks
4 Price of Progress - Used by 23/25 decks
4 Rift Bolt - Used by 23/25 decks
3 Skewer the Critics - Used by 18/25 decks
2 Exquisite Firecraft - Used by 10/25 decks
2 Roiling Vortex - Used by 9/25 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
4 Leyline of the Void - Used by 12/25 decks
3 Smash to Smithereens - Used by 23/25 decks
2 Roiling Vortex - Used by 15/25 decks
2 Pyroblast - Used by 13/25 decks
2 Ensnaring Bridge - Used by 12/25 decks
2 Searing Blood - Used by 8/25 decks
```
```
$ python3 mtgdeckbuild.py -c
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
12 - Belcher
13 - Bomberman
14 - Burn
15 - Canadian Threshold
16 - Cascade Crash
17 - Cephalid Breakfast
18 - Cloudpost Ramp
19 - Curses
20 - Dark Depths
21 - Deadguy Ale
22 - Death & Taxes
23 - Death's Shadow
24 - Delver (Other)
25 - Dimir Aggro
26 - Doomsday
27 - Dragon Stompy
28 - Dredge
29 - Eldrazi Aggro
30 - Elves
31 - Enchantress
32 - Esper Aggro
33 - Food Griffin
34 - Goblins
35 - Grixis Aggro
36 - Grixis Control
37 - Hammer Time
38 - High Tide
39 - Hive Mind
40 - Hogaak
41 - Hollow One Madness
42 - Humans
43 - Infect
44 - Initiative Stompy
45 - Jund
46 - Lands
47 - Landstill
48 - Loam
49 - Maverick
50 - Merfolk
51 - Mississippi River
52 - Mono Black Aggro
53 - Mono Black Combo
54 - Mono Red Combo
55 - Mystic Forge
56 - Nic Fit 
57 - Ninja
58 - Other - Aggro
59 - Other - Combo
60 - Other - Control
61 - Painter
62 - Patriot Aggro
63 - Pox
64 - Reanimator
65 - Shoal Infect
66 - Show and Tell
67 - Slivers
68 - Stiflenought
69 - Stoneblade
70 - Storm
71 - The Rock (Junk)
72 - UR Aggro
73 - UWx Control
: 14


// MAIN DECK
14 Mountain
3 Arid Mesa
2 Bloodstained Mire
4 Monastery Swiftspear
4 Eidolon of the Great Revel
4 Goblin Guide
4 Lightning Bolt
4 Chain Lightning
4 Fireblast
4 Lava Spike
4 Rift Bolt
3 Price of Progress
4 Skewer the Critics
2 Roiling Vortex
// SIDEBOARD
3 Smash to Smithereens
2 Pyroblast
2 Roiling Vortex
4 Leyline of the Void
2 Ensnaring Bridge
2 Red Elemental Blast
```
```
$ python3 mtgdeckbuild.py -d -c
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
5 - Boros Aggro
6 - Calibrated Blast
7 - Cascade Beanstalk
8 - Cascade Crash
9 - CopyCat
10 - Creativity
11 - Creatures Toolbox
12 - Death And Taxes
13 - Death's Shadow
14 - Dredge
15 - Eldrazi Aggro
16 - Enchantress
17 - Faeries
18 - Glimpse of Tomorrow
19 - Goblins
20 - Grixis Control
21 - Gruul Aggro
22 - Gruul Utopia
23 - Hammer Time
24 - Hardened Scales
25 - Heliod Life
26 - Humans
27 - Instant Reanimator
28 - Jeskai Aggro
29 - Jund
30 - Living End
31 - Martyr Life
32 - Merfolk
33 - Mono Black Control
34 - Orzhov Midrange
35 - Other - Aggro
36 - Other - Combo
37 - Other - Control
38 - Rakdos Aggro
39 - Red Deck Wins
40 - Scapeshift
41 - Smallpox
42 - Tameshi Bloom
43 - Teaching Control
44 - Temur Aggro
45 - The One Ring Control
46 - The Rock
47 - The Underworld Cookbook
48 - UB Mill
49 - UR Aggro
50 - UR Control
51 - UW Control
52 - UrzaTron
: 48


//----------------------------------------------------------------------
// LANDS - 23 cards
//----------------------------------------------------------------------
4 Field of Ruin - Used by 25/25 decks
4 Polluted Delta - Used by 24/25 decks
3 Island - Used by 25/25 decks
2 Watery Grave - Used by 24/25 decks
2 Shelldock Isle - Used by 22/25 decks
2 Scalding Tarn - Used by 19/25 decks
2 Flooded Strand - Used by 12/25 decks
1 Oboro, Palace in the Clouds - Used by 25/25 decks
1 Otawara, Soaring City - Used by 24/25 decks
1 Swamp - Used by 23/25 decks
1 Mikokoro, Center of the Sea - Used by 13/25 decks
//----------------------------------------------------------------------
// CREATURES - 8 cards
//----------------------------------------------------------------------
4 Hedron Crab - Used by 25/25 decks
4 Ruin Crab - Used by 25/25 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 29 cards
//----------------------------------------------------------------------
4 Archive Trap - Used by 25/25 decks
4 Fractured Sanity - Used by 25/25 decks
4 Drown in the Loch - Used by 23/25 decks
4 Fatal Push - Used by 23/25 decks
3 Visions of Beyond - Used by 24/25 decks
3 Tasha's Hideous Laughter - Used by 23/25 decks
3 Surgical Extraction - Used by 21/25 decks
2 Jace, the Perfected Mind - Used by 25/25 decks
1 Baleful Mastery - Used by 15/25 decks
1 Murderous Cut - Used by 14/25 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
2 Ensnaring Bridge - Used by 22/25 decks
2 Extirpate - Used by 21/25 decks
2 Engineered Explosives - Used by 17/25 decks
2 Soul-Guide Lantern - Used by 17/25 decks
2 Ghost Quarter - Used by 9/25 decks
1 Crypt Incursion - Used by 22/25 decks
1 Eliminate - Used by 9/25 decks
1 Go for the Throat - Used by 9/25 decks
1 Echoing Truth - Used by 6/25 decks
1 Leyline of the Void - Used by 6/25 decks
```
```
$ python3 mtgdeckbuild.py -d -c
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
```
$ python3 mtgdeckbuild.py -d -c
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
```
$python3 mtgdeckbuild.py -i "Galvanic Blast - Haywire Mite" -m -d
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
```
$ python3 mtgdeckbuild.py -w mtgdecks -t 15 -d
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
```
$ python3 mtgdeckbuild.py -w mtgdecks 
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
3 - 4 Color Control
4 - 4 Color Discover
5 - 4 Color Dragons
6 - 4 Color Emergence
7 - 4 Color Legends
8 - 4 Color Midrange
9 - 4 Color Pia
10 - 4 Color Reanimator
11 - 4 Color Rona
12 - 4 Color Superfriends
13 - 4 Color Tokens
14 - 4 Color Vampires
15 - 4 Color Werewolves
16 - 5 Color Humans
17 - 5 Color Legends
18 - 5 Color Praetors
19 - 5 Color Reanimator
20 - Abzan Angels
21 - Abzan Control
22 - Abzan Humans
23 - Abzan Lifegain
24 - Abzan Midrange
25 - Abzan Phyrexians
26 - Abzan Ramp
27 - Abzan Rigging
28 - Abzan Sacrifice
29 - Abzan Toxic
30 - Azorius Adventures
31 - Azorius Angels
32 - Azorius Apparatus
33 - Azorius Artifacts
34 - Azorius Awakening
35 - Azorius Blink
36 - Azorius Calendar
37 - Azorius Control
38 - Azorius Convoke
39 - Azorius Craft
40 - Azorius Flash
41 - Azorius Justice
42 - Azorius Mentor
43 - Azorius Midrange
44 - Azorius Mill
45 - Azorius Powerstones
46 - Azorius Prototypes
47 - Azorius Schooner
48 - Azorius Soldiers
49 - Azorius Spirits
50 - Azorius Superfriends
51 - Azorius Tempo
52 - Azorius Tezzeret
53 - Azorius Toxic
54 - Bant Aggro
55 - Bant Angels
56 - Bant Beanstalk
57 - Bant Control
58 - Bant Midrange
59 - Bant Ramp
60 - Bant Superfriends
61 - Bant Tokens
62 - Bant Toxic
63 - Big Boros
64 - Big Red
65 - Boros Aggro
66 - Boros Artifacts
67 - Boros Blink
68 - Boros Calendar
69 - Boros Control
70 - Boros Convoke
71 - Boros Counters
72 - Boros Craft
73 - Boros Discover
74 - Boros Equipments
75 - Boros Humans
76 - Boros Justice
77 - Boros Mentor
78 - Boros Midrange
79 - Boros Ojer Pingers
80 - Boros Pia
81 - Boros Powerstones
82 - Boros Soldiers
83 - Boros Tokens
84 - Boros Virtuoso
85 - Brass Reclamation
86 - Caves
87 - Chaotic Transformation
88 - Dimir Breach
89 - Dimir Caves
90 - Dimir Control
91 - Dimir Convoke
92 - Dimir Descend
93 - Dimir Faeries
94 - Dimir Midrange
95 - Dimir Mill
96 - Dimir Mindlink
97 - Dimir Ninjas
98 - Dimir Proliferate
99 - Dimir Proxy
100 - Dimir Reanimator
101 - Dimir Schooner
102 - Dimir Tempo
103 - Dimir Throne
104 - Dimir Wizards
105 - Dimir Zombies
106 - Domain Adventures
107 - Domain Alara
108 - Domain Discover
109 - Domain Ramp
110 - Esper Adventures
111 - Esper Aggro
112 - Esper Angels
113 - Esper Awakening
114 - Esper Control
115 - Esper Faeries
116 - Esper Flash
117 - Esper Greasefang
118 - Esper Justice
119 - Esper Midrange
120 - Esper Poison
121 - Esper Roles
122 - Esper Rona
123 - Esper Sacrifice
124 - Esper Soldiers
125 - Esper Superfriends
126 - Esper Tempo
127 - Esper Tezzeret
128 - Esper Tokens
129 - Esper Zur
130 - Goblins
131 - Golgari Cauldron
132 - Golgari Descend
133 - Golgari Emergence
134 - Golgari Food
135 - Golgari Midrange
136 - Golgari Phyrexians
137 - Golgari Ramp
138 - Golgari Rigging
139 - Golgari Zombies
140 - Grixis Adventures
141 - Grixis Anvil
142 - Grixis Casualty Combo
143 - Grixis Control
144 - Grixis Descend
145 - Grixis Discover
146 - Grixis Dragons
147 - Grixis Hellraiser
148 - Grixis Midrange
149 - Grixis Olivia
150 - Grixis Pirates
151 - Grixis Ramp
152 - Grixis Reanimator
153 - Grixis Sacrifice
154 - Grixis Singularity
155 - Grixis Throne
156 - Gruul Aggro
157 - Gruul Calendar
158 - Gruul Counters
159 - Gruul Dinosaurs
160 - Gruul Discover
161 - Gruul Food
162 - Gruul Midrange
163 - Gruul Powerstones
164 - Gruul Ramp
165 - Gruul Ramp
166 - Gruul Werewolves
167 - Izzet Artifacts
168 - Izzet Calendar
169 - Izzet Control
170 - Izzet Midrange
171 - Izzet Mindlink
172 - Izzet Pirates
173 - Izzet Ramp
174 - Izzet Schooner
175 - Izzet Spellslinger
176 - Jeskai Artifact
177 - Jeskai Control
178 - Jeskai Discover
179 - Jeskai Dragons
180 - Jeskai Humans
181 - Jeskai Mentor
182 - Jeskai Midrange
183 - Jeskai Pia
184 - Jeskai Soldiers
185 - Jeskai Tezzeret
186 - Jund Aggro
187 - Jund Anvil
188 - Jund Bombardment
189 - Jund Cauldron
190 - Jund Dinosaurs
191 - Jund Discover
192 - Jund Emergence
193 - Jund Graveyard
194 - Jund Midrange
195 - Jund Ramp
196 - Jund Reanimator
197 - Jund Rigging
198 - Jund Throne
199 - MTGA decklists
200 - Mardu Anvil
201 - Mardu Calendar
202 - Mardu Discover
203 - Mardu Greasefang
204 - Mardu Humans
205 - Mardu Kirin
206 - Mardu Midrange
207 - Mardu Ratadrabik
208 - Mardu Reanimator
209 - Mardu Sacrifice
210 - Mardu Vampires
211 - Mono Black
212 - Mono Black Rats
213 - Mono Blue Artifacts
214 - Mono Blue Ninjas
215 - Mono Blue Tempo
216 - Mono Green
217 - Mono Red Calendar
218 - Mono Red Dragons
219 - Mono White Angels
220 - Mono White Control
221 - Mono White Craft
222 - Mono White Midrange
223 - Mono White Ramp
224 - Mono White Toxic
225 - Naya Artifacts
226 - Naya Calendar
227 - Naya Cascade
228 - Naya Counters
229 - Naya Dinosaurs
230 - Naya Discover
231 - Naya Gnomes
232 - Naya Humans
233 - Naya Legends
234 - Naya Midrange
235 - Naya Pia
236 - Naya Ramp
237 - Naya Throne
238 - Naya Tokens
239 - Naya Virtuoso
240 - Naya Werewolves
241 - Orzhov Angels
242 - Orzhov Artifacts
243 - Orzhov Blink
244 - Orzhov Control
245 - Orzhov Convoke
246 - Orzhov Humans
247 - Orzhov Justice
248 - Orzhov Lifegain
249 - Orzhov Midrange
250 - Orzhov Roles
251 - Orzhov Sacrifice
252 - Orzhov Scam
253 - Orzhov Superfriends
254 - Orzhov Tokens
255 - Orzhov Toxic
256 - Orzhov Vampires
257 - Rainbow Humans
258 - Rakdos Aggro
259 - Rakdos Anvil
260 - Rakdos Beseech
261 - Rakdos Bombardment
262 - Rakdos Conquest
263 - Rakdos Discover
264 - Rakdos Inti
265 - Rakdos Kingpin
266 - Rakdos Midrange
267 - Rakdos Ramp
268 - Rakdos Rats
269 - Rakdos Reanimator
270 - Rakdos Sacrifice
271 - Rakdos Vampires
272 - Red Deck Wins
273 - Red Deck Wins
274 - Rogue
275 - Selesnya Angels
276 - Selesnya Artifacts
277 - Selesnya Cats
278 - Selesnya Counters
279 - Selesnya Enchantments
280 - Selesnya Humans
281 - Selesnya Midrange
282 - Selesnya Ramp
283 - Selesnya Reconstruction
284 - Selesnya Rootpriest
285 - Selesnya Tokens
286 - Selesnya Toxic
287 - Simic Beanstalk
288 - Simic Cauldron
289 - Simic Food
290 - Simic Grounds
291 - Simic Merfolks
292 - Simic Ramp
293 - Simic Tempo
294 - Simic Tezzeret
295 - Sultai Calendar
296 - Sultai Cauldron
297 - Sultai Drawing
298 - Sultai Emergence
299 - Sultai Graveyard
300 - Sultai Midrange
301 - Sultai Rigging
302 - Sultai Slogurk
303 - Sultai Toxic
304 - Temur Cauldron
305 - Temur Counters
306 - Temur Discover
307 - Temur Prowess
308 - Temur Throne
309 - Temur Treasures
310 - White Weenie
: 229


// MAIN DECK
4 Forest
3 Cavern of Souls
2 Mountain
4 Copperline Gorge
3 Karplusan Forest
4 Rockfall Vale
2 Restless Ridgeline
1 Boseiju, Who Endures
2 Plains
2 Gishath, Sun's Avatar
4 Pugnacious Hammerskull
3 Trumpeting Carnosaur
3 Etali, Primal Conqueror
4 Ixalli's Lorekeeper
2 Bonehoard Dracosaur
2 Ghalta, Stampede Tyrant
3 Intrepid Paleontologist
2 Bramble Familiar
3 Hulking Raptor
4 Fight Rigging
3 Glimpse the Core
// SIDEBOARD
3 Lithomantic Barrage
3 Scytheclaw Raptor
1 Burn Down the House
2 Tyrranax Rex
2 Abrade
2 Get Lost
2 Tranquil Frillback
```
```
$ python3 mtgdeckbuild.py -w mtgdecks -s -i "Get Lost" -d
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
: 2
Select an archetype:
1 - 4 Color Adventures
2 - 4 Color Ascendancy
3 - 4 Color Greasefang
4 - 4 Color Gyruda
5 - 4 Color Knights
6 - 4 Color Omnath
7 - 4 Color Rona
8 - 5 Color Midrange
9 - 5 Color Niv-Mizzet
10 - 5 Color Superfriends
11 - 5 Color Transmogrify
12 - Abzan Amalia
13 - Abzan Company
14 - Abzan Deathtouch
15 - Abzan Greasefang
16 - Abzan Midrange
17 - Acererak Combo
18 - Angels
19 - Archfiend Alteration
20 - Atarka Red
21 - Azorius Auras
22 - Azorius Control
23 - Azorius Craft
24 - Azorius Devotion
25 - Azorius Enigma
26 - Azorius Flash
27 - Azorius Lotus Field
28 - Azorius Powerstones
29 - Azorius Soldiers
30 - Azorius Spirits
31 - Bant Auras
32 - Bant Company
33 - Bant Control
34 - Bant Flash
35 - Bant Lotus Field
36 - Bant Spirits
37 - Boros Aggro
38 - Boros Convoke
39 - Boros Flash
40 - Boros Heroic
41 - Boros Humans
42 - Boros Mentor
43 - Boros Pia
44 - Boros Prowess
45 - Boros Transmogrify
46 - Boros Vehicles
47 - Bring to Beanstalk
48 - Bring to Light
49 - Cats
50 - Death and Taxes
51 - Dimir Control
52 - Dimir Delver
53 - Dimir Faeries
54 - Dimir Mindlink
55 - Dimir Narset-Thief
56 - Dimir Pirates
57 - Dimir Rogues
58 - Dinosaurs
59 - Discover Evolution
60 - Domain Ramp
61 - Dredge
62 - Eldrazi Ramp
63 - Elementals
64 - Elves
65 - Enigmatic Incarnation
66 - Ensoul Artifacts
67 - Esper Control
68 - Esper Greasefang
69 - Esper Superfriends
70 - Esper Yorion
71 - Gates
72 - Goblins
73 - Gods Tree
74 - Golgari Company
75 - Golgari Midrange
76 - Golgari Rigging
77 - Golgari Seasons Past
78 - Golgari Toxic
79 - Golgari Vampires
80 - Golgari Vehicles
81 - Green Devotion
82 - Grinning Ignus Combo
83 - Grixis Bolas
84 - Grixis Drake
85 - Grixis Midrange
86 - Grixis Phoenix
87 - Grixis Reanimator
88 - Grixis Spells
89 - Grixis Transmogrify
90 - Grixis Vampires
91 - Gruul Aggro
92 - Gruul Bard Class
93 - Gruul Company
94 - Gruul Convoke
95 - Gruul Dragons
96 - Gruul Gods Scapeshift
97 - Gruul Midrange
98 - Gruul Obosh
99 - Gruul Prowess
100 - Gruul Ramp
101 - Gruul Vehicles
102 - Hammer Time
103 - Hardened Scales
104 - Izzet Control
105 - Izzet Copter
106 - Izzet Creativity
107 - Izzet Delver
108 - Izzet Drakes
109 - Izzet Emerge
110 - Izzet Narset Undoing
111 - Izzet Phoenix
112 - Izzet Spells
113 - Izzet Transmogrify
114 - Jeskai Ascendancy
115 - Jeskai Creativity
116 - Jeskai Cycling
117 - Jeskai Fires
118 - Jeskai Mentor
119 - Jeskai Narset Undoing
120 - Jeskai Phoenix
121 - Jeskai Superfriends
122 - Jeskai Transmogrify
123 - Jeskai Vehicles
124 - Jund Dinosaurs
125 - Jund Land Destruction
126 - Jund Lukka
127 - Jund Midrange
128 - Jund Rigging
129 - Jund Sacrifice
130 - Jund Transmogrify
131 - Lotus Field Combo
132 - Mardu Beseech Sacrifice
133 - Mardu Doom
134 - Mardu Greasefang
135 - Merfolks
136 - Metalwork Colossus
137 - Mill
138 - Minotaurs
139 - Mono Black
140 - Mono Black Devotion
141 - Mono Blue Devotion
142 - Mono Blue Flash
143 - Mono Blue Mill
144 - Mono Blue Spirits
145 - Mono Blue Tempo
146 - Mono Blue Wizards
147 - Mono Green Copter
148 - Mono Green Stompy
149 - Mono Red Artifacts
150 - Mono Red Fires
151 - Mono White Artifacts
152 - Mono White Colossus
153 - Mono White Humans
154 - Mono White Midrange
155 - Naya Adventures
156 - Naya Aggro
157 - Naya Pia
158 - Naya Transmogrify
159 - Neoform
160 - Orzhov Auras
161 - Orzhov Greasefang
162 - Orzhov Humans
163 - Orzhov Midrange
164 - Orzhov Yorion
165 - Possibility Storm
166 - Quintorius Combo
167 - Rainbow Humans
168 - Rakdos Aggro
169 - Rakdos Anvil
170 - Rakdos Beseech
171 - Rakdos Copter
172 - Rakdos Creativity
173 - Rakdos Madness
174 - Rakdos Midrange
175 - Rakdos Reanimator
176 - Rakdos Sacrifice
177 - Rakdos Transmogrify
178 - Red Deck Wins
179 - Rogue
180 - Selesnya Chord
181 - Selesnya Company
182 - Selesnya Counters
183 - Selesnya Enchantments
184 - Selesnya Midrange
185 - Selesnya Vehicles
186 - Simic Cauldron
187 - Simic Flash
188 - Simic Midrange
189 - Song of Creation
190 - Soulflayer Time
191 - Storm Herald
192 - Sultai Beanstalk
193 - Sultai Bring to Light
194 - Sultai Emergence
195 - Sultai Gyruda
196 - Sultai Rona
197 - Sultai Toxic
198 - Temur Adventures
199 - Temur Marvel
200 - Temur Phoenix
201 - Thassa's Bargain
202 - Vampires
203 - Vannifar Combo
: 153


//----------------------------------------------------------------------
// LANDS - 22 cards
//----------------------------------------------------------------------
11 Plains - Used by 25/25 decks
4 Mutavault - Used by 25/25 decks
3 Cavern of Souls - Used by 16/25 decks
2 Eiganjo, Seat of the Empire - Used by 25/25 decks
2 Castle Ardenvale - Used by 19/25 decks
//----------------------------------------------------------------------
// CREATURES - 34 cards
//----------------------------------------------------------------------
4 Recruitment Officer - Used by 25/25 decks
4 Thalia's Lieutenant - Used by 25/25 decks
4 Adeline, Resplendent Cathar - Used by 25/25 decks
4 Thalia, Guardian of Thraben - Used by 25/25 decks
4 Hopeful Initiate - Used by 24/25 decks
4 Coppercoat Vanguard - Used by 23/25 decks
3 Dauntless Bodyguard - Used by 24/25 decks
3 Brutal Cathar - Used by 20/25 decks
2 Luminarch Aspirant - Used by 13/25 decks
1 Giant Killer - Used by 17/25 decks
1 Kytheon, Hero of Akros - Used by 16/25 decks
//----------------------------------------------------------------------
// OTHER SPELLS - 4 cards
//----------------------------------------------------------------------
2 Brave the Elements - Used by 17/25 decks
2 Get Lost - Used by 17/25 decks
//----------------------------------------------------------------------
// SIDEBOARD - 15 cards
//----------------------------------------------------------------------
3 Wedding Announcement - Used by 24/25 decks
3 Portable Hole - Used by 21/25 decks
2 Get Lost - Used by 25/25 decks
2 Rest in Peace - Used by 21/25 decks
2 Reidane, God of the Worthy - Used by 20/25 decks
2 Invasion of Gobakhan - Used by 10/25 decks
1 Containment Priest - Used by 7/25 decks
```
# mtgdeckbuild
A Magic: The Gathering format archetype deck building tool based on TOP 8 tournaments results.

# MTGDeckBuild
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)  
---  
A Magic: The Gathering format archetype average deck building tool based on TOP 8 tournaments results. Deck building is based on currently played archetypes and most used cards in tournaments decks. Generally, the last 25 decks are used but some filter may affect the number of analyzed decks.

## Features

* Support of [MTGTOP8](https://mtgtop8.com) as tournament data source.
* Support of all formats with automatic discovery.
* Support of all archetypes with automatic discovery.
* Support of a filter to only consider competitive decks.
* Support of a filter to only consider decks including given names.
* Support of a filter to only consider decks over the last given months.
* Support of an interactive mode when executing the script.
* Support of simple or detailed printing of the average decklist.

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
usage: mtgdeckbuild.py [-h] [--details] [--competitive-only] [--name NAME] [--last-months LAST_MONTHS]

options:
  -h, --help            show this help message and exit
  --details, -d         Print deck with details: sections and number of decks using each card
  --competitive-only, -c
                        Only consider competitive decks
  --name NAME, -n NAME  Only consider decks including given deck name
  --last-months LAST_MONTHS, -l LAST_MONTHS
                        Only consider decks from the last given months
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
TOLA320005770:mtgdeckbuild to126816$ 
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
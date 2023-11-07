# mtgdeckbuild
A Magic: The Gathering format archetype deck building tool based on TOP 8 tournaments results.

# MTGDeckBuild
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue)  
---  
A Magic: The Gathering format archetype deck building tool based on TOP 8 tournaments results. Deck building is based on currently played archetypes and most used cards in tournaments decks. Generally, the last 25 decks are used. A proposal with a number of cards as close as possible to the format target number of cards is then proposed.

## Features

* Support of [MTGTOP8](https://mtgtop8.com) as tournament data source.
* Support of all formats with automatic discovery.
* Support of autodiscovery of archetypes.
* Support of simple or detailed printing of the decklist.
* Support of automatic adjustment of minimum number of decks using each card to generate a decklist closer to format's target number of card in main deck and sideboard. The decklist number of card will be as closed as possible to the format's target while considering the average playset value of each card.
* Support of manual submission of the minimum number of decks using each card to generate a decklist accordingly. The decklist number of cards will depend on this parameter while considering the average playset value of each card.

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
usage: mtgdeckbuild.py [-h] [--details] [--minimum-number-of-decks MINIMUM_NUMBER_OF_DECKS] [--competitive-only]

options:
  -h, --help            show this help message and exit
  --details, -d         Print deck with details: sections and number of decks using each card
  --minimum-number-of-decks MINIMUM_NUMBER_OF_DECKS, -m MINIMUM_NUMBER_OF_DECKS
                        Minimum number of decks playing each card (default: automatically adjust the result to match the deck format's number of cards)
  --competitive-only, -c
                        Only consider competitive decks
```

## Examples
```
$ python3 mtgdeckbuild.py 
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - Cedh
16 - Duel commander
17 - Premodern
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17]: 12
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
10 - Bant Control
11 - Belcher
12 - Bomberman
13 - Burn
14 - Canadian Threshold
15 - Cascade Crash
16 - Cephalid Breakfast
17 - Cloudpost Ramp
18 - Dark Depths
19 - Deadguy Ale
20 - Death & Taxes
21 - Death's Shadow
22 - Delver (Other)
23 - Dimir Aggro
24 - Doomsday
25 - Dragon Stompy
26 - Dredge
27 - Eldrazi Aggro
28 - Elves
29 - Enchantress
30 - Esper Aggro
31 - Esper Vial
32 - Food Griffin
33 - Goblins
34 - Grixis Aggro
35 - Grixis Control
36 - Hammer Time
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
47 - Maverick
48 - Merfolk
49 - Mississippi River
50 - Mono Black Aggro
51 - Mono Black Combo
52 - Mono Red Combo
53 - Mystic Forge
54 - Nic Fit 
55 - Ninja
56 - Other - Aggro
57 - Other - Combo
58 - Other - Control
59 - Painter
60 - Patriot Aggro
61 - Pox
62 - Reanimator
63 - Show and Tell
64 - Slivers
65 - Stiflenought
66 - Stoneblade
67 - Storm
68 - The Rock (Junk)
69 - UR Aggro
70 - UWx Control
71 - Zoo
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57/58/59/60/61
/62/63/64/65/66/67/68/69/70/71]: 13


12 Mountain
1 Barbarian Ring
3 Bloodstained Mire
3 Wooded Foothills
4 Goblin Guide
4 Monastery Swiftspear
4 Eidolon of the Great Revel
4 Lightning Bolt
4 Chain Lightning
4 Fireblast
4 Price of Progress
4 Rift Bolt
4 Lava Spike
3 Skewer the Critics
2 Roiling Vortex
// SIDEBOARDS
4 Smash to Smithereens
2 Pyroblast
2 Ensnaring Bridge
4 Leyline of the Void
2 Roiling Vortex
2 Red Elemental Blast

Total of 60 cards in main deck and 16 in sideboard
```
```
$ python3 mtgdeckbuild.py -d
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - Cedh
16 - Duel commander
17 - Premodern
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17]: 12
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
10 - Bant Control
11 - Belcher
12 - Bomberman
13 - Burn
14 - Canadian Threshold
15 - Cascade Crash
16 - Cephalid Breakfast
17 - Cloudpost Ramp
18 - Dark Depths
19 - Deadguy Ale
20 - Death & Taxes
21 - Death's Shadow
22 - Delver (Other)
23 - Dimir Aggro
24 - Doomsday
25 - Dragon Stompy
26 - Dredge
27 - Eldrazi Aggro
28 - Elves
29 - Enchantress
30 - Esper Aggro
31 - Esper Vial
32 - Food Griffin
33 - Goblins
34 - Grixis Aggro
35 - Grixis Control
36 - Hammer Time
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
47 - Maverick
48 - Merfolk
49 - Mississippi River
50 - Mono Black Aggro
51 - Mono Black Combo
52 - Mono Red Combo
53 - Mystic Forge
54 - Nic Fit 
55 - Ninja
56 - Other - Aggro
57 - Other - Combo
58 - Other - Control
59 - Painter
60 - Patriot Aggro
61 - Pox
62 - Reanimator
63 - Show and Tell
64 - Slivers
65 - Stiflenought
66 - Stoneblade
67 - Storm
68 - The Rock (Junk)
69 - UR Aggro
70 - UWx Control
71 - Zoo
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57/58/59/60/61
/62/63/64/65/66/67/68/69/70/71]: 13


//--------------------------------------------------
// LANDS x19
//--------------------------------------------------
12x Mountain - used in 24/25 decks
1x Barbarian Ring - used in 12/25 decks
3x Bloodstained Mire - used in 11/25 decks
3x Wooded Foothills - used in 10/25 decks
//--------------------------------------------------
// CREATURES x12
//--------------------------------------------------
4x Goblin Guide - used in 23/25 decks
4x Monastery Swiftspear - used in 23/25 decks
4x Eidolon of the Great Revel - used in 21/25 decks
//--------------------------------------------------
// OTHER SPELLS x29
//--------------------------------------------------
4x Lightning Bolt - used in 25/25 decks
4x Chain Lightning - used in 23/25 decks
4x Fireblast - used in 23/25 decks
4x Price of Progress - used in 23/25 decks
4x Rift Bolt - used in 23/25 decks
4x Lava Spike - used in 22/25 decks
3x Skewer the Critics - used in 19/25 decks
2x Roiling Vortex - used in 12/25 decks
//--------------------------------------------------
// SIDEBOARDS x16
//--------------------------------------------------
4x Smash to Smithereens - used in 24/25 decks
2x Pyroblast - used in 16/25 decks
2x Ensnaring Bridge - used in 14/25 decks
4x Leyline of the Void - used in 12/25 decks
2x Roiling Vortex - used in 10/25 decks
2x Red Elemental Blast - used in 9/25 decks

Total of 60 cards in main deck and 16 in sideboard
```
```
$ python3 mtgdeckbuild.py -c
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - Cedh
16 - Duel commander
17 - Premodern
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17]: 12
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
10 - Bant Control
11 - Belcher
12 - Bomberman
13 - Burn
14 - Canadian Threshold
15 - Cascade Crash
16 - Cephalid Breakfast
17 - Cloudpost Ramp
18 - Dark Depths
19 - Deadguy Ale
20 - Death & Taxes
21 - Death's Shadow
22 - Delver (Other)
23 - Dimir Aggro
24 - Doomsday
25 - Dragon Stompy
26 - Dredge
27 - Eldrazi Aggro
28 - Elves
29 - Enchantress
30 - Esper Aggro
31 - Esper Vial
32 - Food Griffin
33 - Goblins
34 - Grixis Aggro
35 - Grixis Control
36 - Hammer Time
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
47 - Maverick
48 - Merfolk
49 - Mississippi River
50 - Mono Black Aggro
51 - Mono Black Combo
52 - Mono Red Combo
53 - Mystic Forge
54 - Nic Fit 
55 - Ninja
56 - Other - Aggro
57 - Other - Combo
58 - Other - Control
59 - Painter
60 - Patriot Aggro
61 - Pox
62 - Reanimator
63 - Show and Tell
64 - Slivers
65 - Stiflenought
66 - Stoneblade
67 - Storm
68 - The Rock (Junk)
69 - UR Aggro
70 - UWx Control
71 - Zoo
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57/58/59/60/61
/62/63/64/65/66/67/68/69/70/71]: 13


13 Mountain
3 Arid Mesa
1 Barbarian Ring
3 Wooded Foothills
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
// SIDEBOARDS
3 Smash to Smithereens
2 Pyroblast
2 Roiling Vortex
4 Leyline of the Void
2 Ensnaring Bridge
2 Red Elemental Blast

Total of 61 cards in main deck and 15 in sideboard
```
```
$ python3 mtgdeckbuild.py -m 11 -d -c
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - Cedh
16 - Duel commander
17 - Premodern
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17]: 16
Select an archetype:
1 - Abzan Tempo
2 - Adeliz, The Cinder Wind
3 - Aminatou, the Fateshifter
4 - Animar, Soul of Elements
5 - Anje Falkenrath
6 - Aragorn, King Of Gondor
7 - Aragorn, The Uniter
8 - Atraxa, Grand Unifier
9 - Atraxa, Praetors' Voice
10 - Azusa, Lost But Seeking
11 - Balmor, Battlemage Captain
12 - Braids, Cabal Minion
13 - Dennick, Pious Apprentice
14 - Elminster
15 - Ertai Resurrected
16 - Esika, God Of The Tree
17 - Golos, Tireless Pilgrim
18 - Grist, The Hunger Tide
19 - Gut, True Soul Zealot
20 - Juri, Master Of The Revue
21 - Karlov Of The Ghost Council
22 - Kelsien, the Plague
23 - Kess, Dissident Mage
24 - Kroxa, Titan Of Death's Hunger
25 - Leovold, Emissary of Trest
26 - Light-Paws, Emperor's Voice
27 - Magda, Brazen Outlaw
28 - Marath, Will of the Wild
29 - Minsc, Beloved Ranger
30 - Mono Black Control
31 - Niv-Mizzet Reborn
32 - Octavia, Living Thesis
33 - Old Rutstein
34 - Other - Aggro
35 - Other - Combo
36 - Other - Control
37 - Other Partner Aggro
38 - Other Partner Combo
39 - Other Partner Control
40 - Prossh, Skyraider of Kher
41 - Raffine, Scheming Seer
42 - Red Deck Wins
43 - Sai, Master Thopterist
44 - Saskia the Unyielding
45 - Selesnya Aggro
46 - Slimefoot And Squee
47 - Soul of Windgrace
48 - Surrak Dragonclaw
49 - Sythis, Harvest's Hand
50 - Teferi, Temporal Archmage
51 - The Beamtown Bullies
52 - The Mimeoplasm
53 - The Ur-Dragon
54 - Titania, Protector of Argoth
55 - Tivit, Seller Of Secrets
56 - Weenie White
57 - Yoshimaru
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57]: 56


Minimum number of decks using each card: 11

//--------------------------------------------------
LANDS x36
//--------------------------------------------------
22x Snow-Covered Plains - used in 24/25 decks
1x Eiganjo, Seat of the Empire - used in 23/25 decks
1x Flagstones of Trokair - used in 21/25 decks
1x Eiganjo Castle - used in 20/25 decks
1x Mishra's Factory - used in 20/25 decks
1x Castle Ardenvale - used in 19/25 decks
1x Mutavault - used in 19/25 decks
1x Shefet Dunes - used in 19/25 decks
1x Blinkmoth Nexus - used in 16/25 decks
1x Rishadan Port - used in 15/25 decks
1x Tectonic Edge - used in 15/25 decks
1x Urza's Saga - used in 15/25 decks
1x Cave of the Frost Dragon - used in 14/25 decks
1x Ghost Quarter - used in 14/25 decks
1x War Room - used in 12/25 decks
//--------------------------------------------------
CREATURES x43
//--------------------------------------------------
1x Mother of Runes - used in 25/25 decks
1x Thalia, Heretic Cathar - used in 25/25 decks
1x Thalia, Guardian of Thraben - used in 24/25 decks
1x Drannith Magistrate - used in 22/25 decks
1x Giver of Runes - used in 22/25 decks
1x Lion Sash - used in 22/25 decks
1x Luminarch Aspirant - used in 22/25 decks
1x Palace Jailer - used in 22/25 decks
1x Skyclave Apparition - used in 22/25 decks
1x Stoneforge Mystic - used in 22/25 decks
1x Adeline, Resplendent Cathar - used in 21/25 decks
1x Esper Sentinel - used in 21/25 decks
1x Leonin Arbiter - used in 21/25 decks
1x Benevolent Bodyguard - used in 20/25 decks
1x Cathar Commando - used in 20/25 decks
1x Giant Killer - used in 20/25 decks
1x Bounty Agent - used in 19/25 decks
1x Brimaz, King of Oreskos - used in 19/25 decks
1x Sanctifier en-Vec - used in 19/25 decks
1x Selfless Spirit - used in 19/25 decks
1x Weathered Wayfarer - used in 19/25 decks
1x Archon of Emeria - used in 18/25 decks
1x Elite Spellbinder - used in 18/25 decks
1x Solitude - used in 18/25 decks
1x Tithe Taker - used in 18/25 decks
1x White Plume Adventurer - used in 18/25 decks
1x Recruiter of the Guard - used in 17/25 decks
1x Phyrexian Revoker - used in 16/25 decks
1x Ranger-Captain of Eos - used in 16/25 decks
1x Reidane, God of the Worthy - used in 16/25 decks
1x Welcoming Vampire - used in 15/25 decks
1x Kytheon, Hero of Akros - used in 14/25 decks
1x Seasoned Dungeoneer - used in 14/25 decks
1x Archivist of Oghma - used in 13/25 decks
1x Guardian of Faith - used in 13/25 decks
1x Knight of the White Orchid - used in 13/25 decks
1x Mirran Crusader - used in 13/25 decks
1x Grand Abolisher - used in 12/25 decks
1x Selfless Savior - used in 12/25 decks
1x Anafenza, Kin-Tree Spirit - used in 11/25 decks
1x Anointed Peacekeeper - used in 11/25 decks
1x Sungold Sentinel - used in 11/25 decks
1x Tomik, Distinguished Advokist - used in 11/25 decks
//--------------------------------------------------
OTHER SPELLS x21
//--------------------------------------------------
1x Swords to Plowshares - used in 25/25 decks
1x Umezawa's Jitte - used in 25/25 decks
1x March of Otherworldly Light - used in 23/25 decks
1x Council's Judgment - used in 22/25 decks
1x Mana Tithe - used in 21/25 decks
1x Parallax Wave - used in 21/25 decks
1x Portable Hole - used in 21/25 decks
1x Gideon Blackblade - used in 20/25 decks
1x On Thin Ice - used in 20/25 decks
1x Armageddon - used in 19/25 decks
1x Brave the Elements - used in 19/25 decks
1x Reverent Mantra - used in 19/25 decks
1x Flawless Maneuver - used in 18/25 decks
1x Enlightened Tutor - used in 17/25 decks
1x Unexpectedly Absent - used in 17/25 decks
1x Smuggler's Copter - used in 16/25 decks
1x Skullclamp - used in 15/25 decks
1x The Wandering Emperor - used in 15/25 decks
1x Mox Amber - used in 14/25 decks
1x Fateful Absence - used in 13/25 decks
1x Sword of Fire and Ice - used in 12/25 decks
//--------------------------------------------------
SIDEBOARDS x1
//--------------------------------------------------
1x Isamaru, Hound of Konda - used in 16/25 decks
Total of 100 cards in main deck and 1 in sideboard
```
```
$ python3 mtgdeckbuild.py -m 11 -c
Select a format:
1 - Peasant
2 - Block
3 - Extended
4 - Highlander
5 - Canadian highlander
6 - Explorer
7 - Historic
8 - Alchemy
9 - Standard
10 - Pioneer
11 - Modern
12 - Legacy
13 - Vintage
14 - Pauper
15 - Cedh
16 - Duel commander
17 - Premodern
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17]: 11
Select an archetype:
1 - 4/5c Aggro
2 - 4c Control
3 - Ad Nauseam
4 - Affinity
5 - Amulet Titan
6 - Bant Control
7 - Big Red
8 - Breach
9 - Calibrated Blast
10 - Cascade Beanstalk
11 - Cascade Crash
12 - Creativity
13 - Creatures Toolbox
14 - Death And Taxes
15 - Death's Shadow
16 - Elementals
17 - Esper Control
18 - Grixis Control
19 - Hammer Time
20 - Hardened Scales
21 - Heliod Life
22 - Humans
23 - Infect
24 - Instant Reanimator
25 - Jeskai Control
26 - Jund
27 - Landless
28 - Living End
29 - Martyr Life
30 - Merfolk
31 - Mono Black Control
32 - Orzhov Midrange
33 - Other - Aggro
34 - Other - Combo
35 - Rakdos Aggro
36 - Reanimator
37 - Red Deck Wins
38 - Scapeshift
39 - Temur Aggro
40 - The One Ring Control
41 - The Rock
42 - The Underworld Cookbook
43 - Tooth and Nail
44 - UB Mill
45 - UR Aggro
46 - UR Control
47 - Urza
48 - UrzaTron
49 - Valakut
 [1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49]: 44


Minimum number of decks using each card: 11

4 Field of Ruin
1 Oboro, Palace in the Clouds
3 Island
4 Polluted Delta
2 Watery Grave
1 Otawara, Soaring City
1 Swamp
2 Shelldock Isle
2 Scalding Tarn
1 Mikokoro, Center of the Sea
4 Hedron Crab
4 Ruin Crab
4 Archive Trap
4 Fractured Sanity
2 Jace, the Perfected Mind
4 Drown in the Loch
4 Fatal Push
4 Tasha's Hideous Laughter
3 Visions of Beyond
3 Surgical Extraction
1 Baleful Mastery
1 Murderous Cut
1 Echoing Truth
// SIDEBOARDS
1 Crypt Incursion
2 Ensnaring Bridge
3 Extirpate
2 Soul-Guide Lantern
2 Engineered Explosives
1 Eliminate
2 Ghost Quarter
1 Go for the Throat
Total of 60 cards in main deck and 14 in sideboard
```
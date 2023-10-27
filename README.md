# mtgdeckbuild
A Magic: The Gathering format archetype deck building tool based on TOP 8 tournaments results.

# MTGRank
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue)  
---  
A Magic: The Gathering format archetype deck building tool based on TOP 8 tournaments results. Building is based on currently played archetypes and most used cards in tournaments decks. Generally, the last 25 decks are used.

## Features

* Support of [MTGTOP8](https://mtgtop8.com) as tournament data source.
* Support of 4 formats: Modern, Legacy, Duel Commander, and Pioneer.
* Support of autodiscovery of archetypes.
* Support of simple or detailed printing of the decklist.
* Support of automatic adjustment of minimum number of decks using each card to generate a decklist closer to format's target number of card in main deck and sideboard. The decklist number of card will be as closed as possible to the format's target while considering the average playset value of each card.
* Support of manual submission of minimum number of decks using each card to generate a decklist accordingly. The decklist number of cards will depend on this parameter while considering the average playset value of each card..

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
        1 Legacy
        2 Modern
        3 Duel Commander
        4 Pioneer
 [1/2/3/4]: 1
Select an archetype:
1 4/5c Control
2 Affinity
3 All my Spells
4 Aluren
5 Arclight Phoenix
6 Artifacts Blue
7 Artifacts Prison
8 BUG Control
9 BUG Midrange
10 Bant Control
11 Belcher
12 Bomberman
13 Burn
14 Canadian Threshold
15 Cascade Crash
16 Cephalid Breakfast
17 Cloudpost Ramp
18 Dark Depths
19 Deadguy Ale
20 Death & Taxes
21 Death's Shadow
22 Delver (Other)
23 Dimir Aggro
24 Doomsday
25 Dragon Stompy
26 Dredge
27 Eldrazi Aggro
28 Elves
29 Enchantress
30 Esper Aggro
31 Esper Vial
32 Food Griffin
33 Goblins
34 Grixis Aggro
35 Grixis Control
36 Hammer Time
37 High Tide
38 Hive Mind
39 Hogaak
40 Hollow One Madness
41 Infect
42 Initiative Stompy
43 Jund
44 Lands
45 Landstill
46 Loam
47 Maverick
48 Merfolk
49 Mississippi River
50 Mono Black Aggro
51 Mono Black Combo
52 Mono Red Combo
53 Mystic Forge
54 Nic Fit 
55 Ninja
56 Other - Aggro
57 Other - Combo
58 Other - Control
59 Painter
60 Patriot Aggro
61 Pox
62 Reanimator
63 Show and Tell
64 Slivers
65 Stiflenought
66 Stoneblade
67 Storm
68 The Rock (Junk)
69 UR Aggro
70 UWx Control
71 Zoo
 [0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49
/50/51/52/53/54/55/56/57/58/59/60/61/62/63/64/65/66/67/68/69/70]: 13


13x Mountain
2x Barbarian Ring
3x Bloodstained Mire
4x Goblin Guide
4x Monastery Swiftspear
4x Eidolon of the Great Revel
4x Lightning Bolt
4x Chain Lightning
4x Fireblast
4x Price of Progress
4x Rift Bolt
4x Lava Spike
3x Skewer the Critics
2x Roiling Vortex
// SIDEBOARDS
4x Smash to Smithereens
2x Ensnaring Bridge
3x Pyroblast
2x Roiling Vortex
4x Leyline of the Void

Total of 59 cards in main deck and 15 in sideboard
```
```
$ python3 mtgdeckbuild.py -d
Select a format:
        1 Legacy
        2 Modern
        3 Duel Commander
        4 Pioneer
 [1/2/3/4]: 1
Select an archetype:
1 4/5c Control
2 Affinity
3 All my Spells
4 Aluren
5 Arclight Phoenix
6 Artifacts Blue
7 Artifacts Prison
8 BUG Control
9 BUG Midrange
10 Bant Control
11 Belcher
12 Bomberman
13 Burn
14 Canadian Threshold
15 Cascade Crash
16 Cephalid Breakfast
17 Cloudpost Ramp
18 Dark Depths
19 Deadguy Ale
20 Death & Taxes
21 Death's Shadow
22 Delver (Other)
23 Dimir Aggro
24 Doomsday
25 Dragon Stompy
26 Dredge
27 Eldrazi Aggro
28 Elves
29 Enchantress
30 Esper Aggro
31 Esper Vial
32 Food Griffin
33 Goblins
34 Grixis Aggro
35 Grixis Control
36 Hammer Time
37 High Tide
38 Hive Mind
39 Hogaak
40 Hollow One Madness
41 Infect
42 Initiative Stompy
43 Jund
44 Lands
45 Landstill
46 Loam
47 Maverick
48 Merfolk
49 Mississippi River
50 Mono Black Aggro
51 Mono Black Combo
52 Mono Red Combo
53 Mystic Forge
54 Nic Fit 
55 Ninja
56 Other - Aggro
57 Other - Combo
58 Other - Control
59 Painter
60 Patriot Aggro
61 Pox
62 Reanimator
63 Show and Tell
64 Slivers
65 Stiflenought
66 Stoneblade
67 Storm
68 The Rock (Junk)
69 UR Aggro
70 UWx Control
71 Zoo
 [0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49
/50/51/52/53/54/55/56/57/58/59/60/61/62/63/64/65/66/67/68/69/70]: 13


//--------------------------------------------------
// LANDS x18
//--------------------------------------------------
13x Mountain - used in 24/25 decks
2x Barbarian Ring - used in 13/25 decks
3x Bloodstained Mire - used in 10/25 decks
//--------------------------------------------------
// CREATURES x12
//--------------------------------------------------
4x Goblin Guide - used in 24/25 decks
4x Monastery Swiftspear - used in 24/25 decks
4x Eidolon of the Great Revel - used in 21/25 decks
//--------------------------------------------------
// OTHER SPELLS x29
//--------------------------------------------------
4x Lightning Bolt - used in 25/25 decks
4x Chain Lightning - used in 24/25 decks
4x Fireblast - used in 24/25 decks
4x Price of Progress - used in 24/25 decks
4x Rift Bolt - used in 24/25 decks
4x Lava Spike - used in 23/25 decks
3x Skewer the Critics - used in 21/25 decks
2x Roiling Vortex - used in 12/25 decks
//--------------------------------------------------
// SIDEBOARDS x15
//--------------------------------------------------
4x Smash to Smithereens - used in 22/25 decks
2x Ensnaring Bridge - used in 14/25 decks
3x Pyroblast - used in 14/25 decks
2x Roiling Vortex - used in 10/25 decks
4x Leyline of the Void - used in 9/25 decks

Total of 59 cards in main deck and 15 in sideboard
```
```
$ python3 mtgdeckbuild.py -c
Select a format:
        1 Legacy
        2 Modern
        3 Duel Commander
        4 Pioneer
 [1/2/3/4]: 1
Select an archetype:
1 4/5c Control
2 Affinity
3 All my Spells
4 Aluren
5 Arclight Phoenix
6 Artifacts Blue
7 Artifacts Prison
8 BUG Control
9 BUG Midrange
10 Bant Control
11 Belcher
12 Bomberman
13 Burn
14 Canadian Threshold
15 Cascade Crash
16 Cephalid Breakfast
17 Cloudpost Ramp
18 Dark Depths
19 Deadguy Ale
20 Death & Taxes
21 Death's Shadow
22 Delver (Other)
23 Dimir Aggro
24 Doomsday
25 Dragon Stompy
26 Dredge
27 Eldrazi Aggro
28 Elves
29 Enchantress
30 Esper Aggro
31 Esper Vial
32 Food Griffin
33 Goblins
34 Grixis Aggro
35 Grixis Control
36 Hammer Time
37 High Tide
38 Hive Mind
39 Hogaak
40 Hollow One Madness
41 Infect
42 Initiative Stompy
43 Jund
44 Lands
45 Landstill
46 Loam
47 Maverick
48 Merfolk
49 Mississippi River
50 Mono Black Aggro
51 Mono Black Combo
52 Mono Red Combo
53 Mystic Forge
54 Nic Fit 
55 Ninja
56 Other - Aggro
57 Other - Combo
58 Other - Control
59 Painter
60 Patriot Aggro
61 Pox
62 Reanimator
63 Show and Tell
64 Slivers
65 Stiflenought
66 Stoneblade
67 Storm
68 The Rock (Junk)
69 UR Aggro
70 UWx Control
71 Zoo
 [0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49
/50/51/52/53/54/55/56/57/58/59/60/61/62/63/64/65/66/67/68/69/70]: 13


14x Mountain
3x Arid Mesa
1x Barbarian Ring
4x Monastery Swiftspear
4x Eidolon of the Great Revel
4x Goblin Guide
4x Lightning Bolt
4x Chain Lightning
4x Fireblast
4x Lava Spike
4x Rift Bolt
3x Price of Progress
4x Skewer the Critics
2x Roiling Vortex
2x Exquisite Firecraft
// SIDEBOARDS
3x Smash to Smithereens
2x Pyroblast
2x Roiling Vortex
2x Red Elemental Blast
2x Ensnaring Bridge
4x Leyline of the Void

Total of 61 cards in main deck and 15 in sideboard
```
```
$ python3 mtgdeckbuild.py -m 11 -d -c
Select a format:
        1 Legacy
        2 Modern
        3 Duel Commander
        4 Pioneer
 [1/2/3/4]: 3
Select an archetype:
1 Abzan Tempo
2 Aminatou, the Fateshifter
3 Animar, Soul of Elements
4 Aragorn, King Of Gondor
5 Aragorn, The Uniter
6 Atraxa, Grand Unifier
7 Atraxa, Praetors' Voice
8 Azusa, Lost But Seeking
9 Balmor, Battlemage Captain
10 Braids, Cabal Minion
11 Dennick, Pious Apprentice
12 Elminster
13 Ertai Resurrected
14 Esika, God Of The Tree
15 Ghyrson Starn, Kelermorph
16 Golos, Tireless Pilgrim
17 Grenzo, Dungeon Warden
18 Grist, The Hunger Tide
19 Gut, True Soul Zealot
20 Juri, Master Of The Revue
21 Kelsien, the Plague
22 Kess, Dissident Mage
23 Klothys, God Of Destiny
24 Kroxa, Titan Of Death's Hunger
25 Leovold, Emissary of Trest
26 Light-Paws, Emperor's Voice
27 Magda, Brazen Outlaw
28 Marath, Will of the Wild
29 Minsc, Beloved Ranger
30 Mono Black Control
31 Niv-Mizzet Reborn
32 Octavia, Living Thesis
33 Old Rutstein
34 Other - Aggro
35 Other - Control
36 Other Partner Aggro
37 Other Partner Combo
38 Other Partner Control
39 Prossh, Skyraider of Kher
40 Raffine, Scheming Seer
41 Red Deck Wins
42 Sai, Master Thopterist
43 Saskia the Unyielding
44 Slimefoot And Squee
45 Soul of Windgrace
46 Surrak Dragonclaw
47 Sythis, Harvest's Hand
48 Teferi, Temporal Archmage
49 The Beamtown Bullies
50 The Mimeoplasm
51 The Ur-Dragon
52 Titania, Protector of Argoth
53 Tivit, Seller Of Secrets
54 Vendilion Clique
55 Weenie White
56 Yoshimaru
 [0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49
/50/51/52/53/54/55]: 55


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
TOTAL x100 + x1
```
```
$ python3 mtgdeckbuild.py -m 11 -c
Select a format:
        1 Legacy
        2 Modern
        3 Duel Commander
        4 Pioneer
 [1/2/3/4]: 2
Select an archetype:
1 4/5c Aggro
2 4c Control
3 Abzan Aggro
4 Ad Nauseam
5 Affinity
6 Allosaurus Combo
7 Amulet Titan
8 Bant Control
9 Big Red
10 Breach
11 Calibrated Blast
12 Cascade Beanstalk
13 Cascade Crash
14 CopyCat
15 Creativity
16 Creatures Toolbox
17 Death And Taxes
18 Death's Shadow
19 Dredge
20 Enchantress
21 Goblins
22 Grixis Control
23 Gruul Utopia
24 Hammer Time
25 Hardened Scales
26 Heliod Life
27 Hollow One
28 Humans
29 Instant Reanimator
30 Jeskai Control
31 Jund
32 Landless
33 Lantern Control
34 Living End
35 Martyr Life
36 Merfolk
37 Mono Black Control
38 Other - Aggro
39 Other - Combo
40 Rakdos Aggro
41 Red Deck Wins
42 Scapeshift
43 Tameshi Bloom
44 Temur Aggro
45 The One Ring Control
46 The Rock
47 The Underworld Cookbook
48 UB Mill
49 UR Aggro
50 UR Control
51 UR Storm
52 UW Control
53 UWx Midrange
54 Urza
55 UrzaTron
56 Valakut
57 Zoo
 [0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49
/50/51/52/53/54/55/56]: 48


Minimum number of decks using each card: 11

4x Field of Ruin
3x Island
1x Oboro, Palace in the Clouds
4x Polluted Delta
2x Watery Grave
1x Otawara, Soaring City
2x Shelldock Isle
1x Swamp
2x Scalding Tarn
1x Mikokoro, Center of the Sea
4x Hedron Crab
4x Ruin Crab
4x Archive Trap
4x Fractured Sanity
2x Jace, the Perfected Mind
4x Tasha's Hideous Laughter
3x Visions of Beyond
4x Drown in the Loch
4x Fatal Push
3x Surgical Extraction
1x Baleful Mastery
1x Murderous Cut
1x Echoing Truth
// SIDEBOARDS
2x Extirpate
1x Crypt Incursion
2x Ensnaring Bridge
3x Soul-Guide Lantern
2x Engineered Explosives
2x Ghost Quarter
1x Eliminate
1x Go for the Throat
TOTAL x60 + x14
```
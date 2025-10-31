# Defeat-The-Evil-Wizard

⚔️ Python Battle Arena Game

-A turn-based Python text adventure game showcasing Object-Oriented Programming (OOP) principles — inheritance, polymorphism, encapsulation, and dynamic gameplay mechanics.

-Battle as a Warrior, Mage, Archer, or Paladin against the powerful Evil Wizard, using strategy, special abilities, and healing to survive!


Project Overview

This game demonstrates:

-Object-Oriented Programming Concepts

-Classes, inheritance, and method overriding

-Interactive Console Gameplay

-Choose actions, cast spells, block attacks, and heal

-Dynamic Combat System

-Randomized attacks, regeneration, and health tracking

-Polymorphism

-Each class has unique special abilities and defensive tactics


Project Structure
battle_arena.py        # Main game file (contains all logic and classes)

How to Run the Game

-Clone the repository

-git clone https://github.com/your-username/python-battle-arena.git
cd python-battle-arena


Run the game

-python battle_arena.py


Play the game!

-Choose your class

-Select your battle actions (attack, special, heal, view stats)

-Defeat the Evil Wizard 👑

Character Classes
-Class	Health	Attack	Special Ability	Defensive Move
-Warrior	140	25	Power Strike (35–50 dmg)	Defend (block next attack)
-Mage	100	35	Fireball (30–45 dmg)	Arcane Shield (block next attack)
-Archer	120	30	Quick Shot (2 hits, 10–20 dmg each)	Evade (block next attack)
-Paladin	160	20	Holy Strike (25–40 dmg)	Divine Shield (block next attack)
-Evil Wizard	150	15	Regenerate (+5 HP each turn)	—
Gameplay Example
=== Welcome to the Battle Arena! ===
Choose your character class:
1. Warrior
2. Mage
3. Archer
4. Paladin
Enter the number of your class choice: 2
Enter your character's name: Eldrin

Battle Start! Eldrin vs The Dark Wizard

--- Your Turn ---
1. Attack
2. Use Special Ability
3. Heal
4. View Stats
Choose an action: 2
1. Fireball  2. Arcane Shield: 1
Eldrin casts Fireball on The Dark Wizard for 42 damage!

--- Wizard's Turn ---
The Dark Wizard regenerates 5 health!
The Dark Wizard attacks Eldrin for 14 damage!

OOP Concepts Demonstrated
✅ Inheritance

Each character subclass (Warrior, Mage, Archer, Paladin) inherits from the base Character class.

✅ Polymorphism

Each subclass implements unique special and defensive methods.

✅ Encapsulation

Health, attack power, and state (blocking, healing) are managed inside each class.

✅ Abstraction

The player interacts only with high-level methods like attack(), heal(), or display_stats().

Features to Try:

-Play multiple rounds using different classes

-Experiment with different ability combinations

-Observe how defense blocks attacks

-Try to finish with full health for a perfect victory

Requirements:

-Python 3.8 or higher

-No external dependencies (only uses the built-in random module)

 Future Enhancements:

-Add multiplayer or AI opponents

-Introduce mana or stamina systems

-Implement leveling and experience gain

-Save player stats between games

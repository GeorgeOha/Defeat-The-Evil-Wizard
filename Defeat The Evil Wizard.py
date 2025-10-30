import random

# -------------------------------
# Base Character class
# -------------------------------
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.block_next = False  # Used for defensive abilities

    def attack(self, opponent):
        """Deals randomized attack damage to an opponent."""
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        if opponent.block_next:
            print(f"{opponent.name} blocked the attack!")
            opponent.block_next = False
            damage = 0
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        """Restores a random amount of health without exceeding the maximum."""
        heal_amount = random.randint(10, 25)
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount}! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        """Displays current stats."""
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# -------------------------------
# Warrior class
# -------------------------------
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_strike(self, opponent):
        """High-damage attack."""
        damage = random.randint(35, 50)
        opponent.health -= damage
        print(f"{self.name} uses Power Strike on {opponent.name} for {damage} damage!")

    def defend(self):
        """Block next attack."""
        self.block_next = True
        print(f"{self.name} raises a shield to block the next attack!")

# -------------------------------
# Mage class
# -------------------------------
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def fireball(self, opponent):
        """Heavy attack with chance to burn."""
        damage = random.randint(30, 45)
        opponent.health -= damage
        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")

    def arcane_shield(self):
        """Block next attack using magic."""
        self.block_next = True
        print(f"{self.name} conjures an Arcane Shield to block the next attack!")

# -------------------------------
# Archer class
# -------------------------------
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)

    def quick_shot(self, opponent):
        """Two fast arrow shots."""
        total_damage = 0
        for i in range(2):
            dmg = random.randint(10, 20)
            opponent.health -= dmg
            total_damage += dmg
        print(f"{self.name} fires Quick Shot, hitting twice for {total_damage} total damage!")

    def evade(self):
        """Avoid the next attack."""
        self.block_next = True
        print(f"{self.name} prepares to Evade the next attack!")

# -------------------------------
# Paladin class
# -------------------------------
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

    def holy_strike(self, opponent):
        """Bonus light-infused attack."""
        damage = random.randint(25, 40)
        opponent.health -= damage
        print(f"{self.name} smites {opponent.name} with a Holy Strike for {damage} damage!")

    def divine_shield(self):
        """Blocks the next attack."""
        self.block_next = True
        print(f"{self.name} activates Divine Shield to block the next attack!")

# -------------------------------
# Evil Wizard class
# -------------------------------
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        """Regenerates small health each turn."""
        self.health = min(self.max_health, self.health + 5)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}")

# -------------------------------
# Character Creation
# -------------------------------
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# -------------------------------
# Battle System
# -------------------------------
def battle(player, wizard):
    print(f"\nBattle Start! {player.name} vs {wizard.name}\n")

    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Choose ability based on character type
            if isinstance(player, Warrior):
                ability = input("1. Power Strike  2. Defend: ")
                if ability == '1':
                    player.power_strike(wizard)
                elif ability == '2':
                    player.defend()
            elif isinstance(player, Mage):
                ability = input("1. Fireball  2. Arcane Shield: ")
                if ability == '1':
                    player.fireball(wizard)
                elif ability == '2':
                    player.arcane_shield()
            elif isinstance(player, Archer):
                ability = input("1. Quick Shot  2. Evade: ")
                if ability == '1':
                    player.quick_shot(wizard)
                elif ability == '2':
                    player.evade()
            elif isinstance(player, Paladin):
                ability = input("1. Holy Strike  2. Divine Shield: ")
                if ability == '1':
                    player.holy_strike(wizard)
                elif ability == '2':
                    player.divine_shield()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice. Try again.")
            continue

        # Wizard's Turn
        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"\n💀 {player.name} has been defeated by {wizard.name}! Game Over.")
            break

    if wizard.health <= 0:
        print(f"\n🎉 Victory! {player.name} has defeated the evil wizard {wizard.name}!")

# -------------------------------
# Main Function
# -------------------------------
def main():
    print("=== Welcome to the Battle Arena! ===")
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()

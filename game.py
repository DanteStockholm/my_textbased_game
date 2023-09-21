import random
import sys

import creatures
import weapons
import actions

# Global variables
number_of_visits = 0

class Character:

    def __init__(self, name, health, level, active_weapon, inventory, location, creature, \
                 creature_hp, creature_xp, creature_spoils, enemies, xp, status):
        self.name = name
        self.health = health
        self.level = level
        self.active_weapon = active_weapon
        self.inventory = inventory
        self.location = location
        self.creature = creature
        self.creature_hp = creature_hp
        self.creature_xp = creature_xp
        self.creature_spoils = creature_spoils
        self.xp = xp
        self.enemies = enemies
        self.status = "Alive"


    def bow_shot(self):
        modified_roll = (random.randint(1,20) - self.level)
        if modified_roll < 8:
            print("Good shot!")
            hit_points = weapons.short_bow()
            self.attack_phase2(hit_points)

        if modified_roll >= 8:
            print("You missed")
            self.creature_attack()

    def attack(self):
        if self.enemies > 0:
            if self.active_weapon == "unarmed":
                hit_points = weapons.unarmed()
                self.attack_phase2(hit_points)

            elif self.active_weapon == "dagger":
                hit_points = weapons.dagger()
                self.attack_phase2(hit_points)

            elif self.active_weapon == "knife":
                hit_points = weapons.dagger()
                self.attack_phase2(hit_points)

            elif self.active_weapon == "sledgehammer":
                hit_points = weapons.sledgehammer()
                self.attack_phase2(hit_points)

            elif self.active_weapon == "longsword":
                hit_points = weapons.long_sword()
                self.attack_phase2(hit_points)

            elif self.active_weapon == "shortsword":
                hit_points = weapons.short_sword()
                self.attack_phase2(hit_points)

            elif self.active_weapon == "two-handed sword":
                hit_points = weapons.two_handed_sword()
                self.attack_phase2(hit_points)

            elif self.active_weapon == "shortbow" or self.active_weapon == "longbow":
                    self.bow_shot()

            else:
                text = self.active_weapon
                capitalized_text = text.capitalize()

                print(f"{capitalized_text} is not a valid weapon. Now you have to trust your boxing skills")
                self.active_weapon = "unarmed"
                hit_points = weapons.unarmed()
                self.attack_phase2(hit_points)


        else:
            print("""You cannot see any enemies to attack.
            """)

    def attack_phase2(self, hit_points):

        if self.active_weapon == "unarmed":
            print(f"""{self.name} attacked {self.creature} with his fists and kicks and caused {hit_points} of damage.""")

        else:
            print(f"""{self.name} attacked {self.creature} with {self.active_weapon} and caused {hit_points} of damage.
        """)

        self.creature_hp -= hit_points
        if self.creature_hp < 1:
            self.enemies = 0
            self.xp += self.creature_xp
            self.check_xp()
            spoils = self.creature_spoils[random.randint(0, 3)]
            if spoils not in self.inventory:
                self.inventory.append(spoils)
            print(f"""{self.creature} was defeated by your attack.
You found {spoils} and earned {self.creature_xp}xp.""")
            print("")


        else:
            self.creature_attack()

    def creature_attack(self):
        roll_result = 0
        if self.creature == "Goblin":
            hit_points = creatures.goblin_attack()
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"

        elif self.creature == "Troll":
            hit_points = creatures.troll_attack()
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"

        elif self.creature == "Goblin Bowman":
            hit_points = creatures.goblin_bowman()
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"

        elif self.creature == "Death knight":
            #hit_points = creatures.death_knight() not woriking
            for i in range(2):
                roll_result += random.randint(1, 6)  # = 3x D6
            hit_points = roll_result
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"

        elif self.creature == "Dragon":
            for i in range(3):
                roll_result += random.randint(1, 6)  # = 4x D6
            hit_points = roll_result
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"

        elif self.creature == "Minotaur":
            for i in range(1):
                roll_result += random.randint(1, 6)  # = 2x D6
            hit_points = roll_result
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"

        elif self.creature == "Bandit":
            hit_points = creatures.bandit()
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"

        elif self.creature == "Skeleton":
            hit_points = creatures.skeleton()
            self.health -= hit_points
            print(f"{self.creature} attacks and hit you by {hit_points} of damage. You health is now {self.health}.")
            print("")
            if self.health < 1:
                self.status = "Dead"



    def check_xp(self):
        if self.level == 1:
            if self.xp > 149:
                self.level = 2
                self.health += 10
                self.levelup_message()

        if self.level == 2:
            if self.xp > 299:
                self.level = 3
                self.health += 20
                self.levelup_message()

        if self.level == 3:
            if self.xp > 499:
                self.level = 4
                self.health += 30
                self.levelup_message()

        if self.level == 4:
            if self.xp > 799:
                self.level = 5
                self.health += 40
                self.levelup_message()

        if self.level == 5:
            if self.xp > 1249:
                self.level = 6
                self.health += 50
                self.levelup_message()

        if self.level == 6:
            if self.xp > 1999:
                self.level = 7
                self.health += 60
                self.levelup_message()

        if self.level == 7:
            if self.xp > 2649:
                self.level = 8
                self.health += 70
                self.levelup_message()

        if self.level == 8:
            if self.xp > 3649:
                self.level = 9
                self.health += 80
                self.levelup_message()

        if self.level == 9:
            if self.xp > 4999:
                self.level = 10
                print("You have reached level 10 and won the game!")
                sys.exit()



    def levelup_message(self):
        print(f"Level up! You are now on level {self.level} and {self.health}HP.")


    def action_golbin_cave(self):
        print("On your right side, you see a cave. At the entrance, you see three goblins quarreling about something.")
        go_to_cave = input("Do you want to enter the cave? Y/N: ")
        if go_to_cave.upper() == "Y":
            self.location = 4
            self.action_goblin_cave_entrance()

        else:
            self.location = 5
            self.move() # This will be 6 due to +1 in method.

    def action_goblin_cave_entrance(self): #location is now 3
        print("Two goblins ran away and left the lonely bastard alone to meet his destiny!")
        print("Goblin attacks you!")
        self.create_goblin()
        self.creature_attack()

    def action_troll_and_treasure(self):

        while True:
            print("""You stand at the entrance of the cave.
Do you want to go inside or continue walking on the forest path?""")
            choice = input("Choose: cave/forest: ")

            if choice.upper() == "CAVE":
                self.troll_and_treasure_part2()
                break

            elif choice.upper() == "FOREST":
                self.location = 5  # Becomes 6 after the move method, i.e., go to the forest.
                self.move()
                break

            else:
                print("Invalid choice. Please type cave or forest.")

    def troll_and_treasure_part2(self):
        print("You see a troll and he looks pretty mad!")
        self.create_troll()
        self.creature_attack()




    def move(self):
        self.location += 1

        if self.location == 2:  # Sees the Goblin Cave
            self.action_golbin_cave()

            # 3 and 4 is part of an action

        elif self.location == 5:
            self.action_troll_and_treasure()

        elif self.location == 6:  # North Forest
            print("North Forest. You see a Goblin without any weapons.")
            self.create_goblin()

        elif self.location == 7:  # Trees
            print("Forest. You see a Goblin holding a bow.")
            self.create_goblin_bowman()

        else:
            self.old_dark_forest() # Last location, The old and dark forest


    def old_dark_forest(self):
        global number_of_visits
        number_of_visits += 1

        if number_of_visits < 2:
            print("You are entering an old and dark forest. A small path takes you deeper in the forest. Who knows what dangers hides in there?!")

        else:
            print("The dark and old forest")

        if self.level < 3:
            random_creature = random.randint(1,4)
            if random_creature == 1:
                self.create_goblin_bowman()
            else:
                self.create_goblin()

        if self.level == 3 or self.level == 4:
            random_creature = random.randint(1, 4)
            if random_creature < 3:
                self.create_goblin()
            elif random_creature == 3:
                self.create_goblin_bowman()
            else:
                self.create_troll()

        if self.level == 5:
            random_creature = random.randint(1, 4)
            if random_creature == 1:
                self.create_goblin_bowman()
            elif random_creature == 2:
                self.create_troll()
            elif random_creature == 3:
                self.create_bandit()
            else:
                self.create_skeleton()

        if self.level == 6 or self.level == 7:
            random_creature = random.randint(1, 4)
            if random_creature == 1:
                self.create_skeleton()
            elif random_creature == 2:
                self.create_bandit()
            elif random_creature == 3:
                self.create_minotaur()
            else:
                self.create_death_knight()

            if self.level == 8 or self.level == 9:
                random_creature = random.randint(1, 4)
                if random_creature == 1:
                    self.create_dragon()
                elif random_creature == 2:
                    self.create_bandit()
                elif random_creature == 3:
                    self.create_minotaur()
                else:
                    self.create_death_knight()

        print(f"You see a {self.creature}.")


    def create_bandit(self):
        self.creature = "Bandit"
        self.creature_hp = 10
        self.creature_xp = 200
        self.creature_spoils = ["dried meat", "knife", "beer bottle", "shortsword"]
        self.enemies = 1

    def create_death_knight(self):
        self.creature = "Death Knight"
        self.creature_hp = 30
        self.creature_xp = 425
        self.creature_spoils = ["spell book", "sledgehammer", "two-handed sword", "helmet"]
        self.enemies = 1

    def create_dragon(self):
        self.creature = "Dragon"
        self.creature_hp = 100
        self.creature_xp = 600
        self.creature_spoils = ["gold coins", "dragon tooth", "two-handed sword", "jewelry"]
        self.enemies = 1

    def create_goblin(self):
        self.creature = "Goblin"
        self.creature_hp = 3
        self.creature_xp = 50
        self.creature_spoils = ["dried meat", "dagger", "stone", "water bottle"]
        self.enemies = 1

    def create_goblin_bowman(self):
        self.creature = "Goblin Bowman"
        self.creature_hp = 3
        self.creature_xp = 75
        self.creature_spoils = ["dried meat", "quiver", "arrow", "shortbow"]
        self.enemies = 1

    def create_minotaur(self):
        self.creature = "Minotaur"
        self.creature_hp = 20
        self.creature_xp = 300
        self.creature_spoils = ["empty bottle", "knife", "longsword", "broken shield"]
        self.enemies = 1

    def create_skeleton(self):
        self.creature = "Skeleton"
        self.creature_hp = 15
        self.creature_xp = 200
        self.creature_spoils = ["empty bottle", "knife", "shortsword", "broken shield"]
        self.enemies = 1

    def create_troll(self):
        self.creature = "Troll"
        self.creature_hp = 10
        self.creature_xp = 150
        self.creature_spoils = ["dried meat", "knife", "damaged shirt", "sledgehammer"]
        self.enemies = 1



    def backpack(self):
        print(self.inventory)
        print("Please type the weapon you want to use or 'unarmed' to test your luck with your fists.")
        print("")
        self.equip()

    def equip(self):
        new_weapon = input()
        if new_weapon in self.inventory:
            self.active_weapon = new_weapon

        elif new_weapon == "unarmed":
            self.active_weapon = "unarmed"

        else:
            print("Could not find that weapon.")

    def check_health_and_xp(self):
        print(f"Your health is {self.health} and you have {self.xp}xp.")
        print("")

    def is_alive(self):
        return self.health > 0


class Game:


    def __init__(self):
        self.player = Character(health=10, level=1, active_weapon="unarmed", inventory=["backpack"], status="Alive", \
                                creature="Goblin", creature_hp=3, enemies=1, location=1, creature_xp=0, xp=0,\
                                creature_spoils= {""}, \
                                name=input("Welcome to Forest Path! An adventure game for brave heroes. Enter the name of your character: "))

        self.player.create_goblin() #Starting Goblin
        print("""
You are in a forest not far from home. You see a goblin wandering around by himself. He seems to be unarmed.
        """)

    def end_game(self):
        sys.exit()

    def start(self):
        while self.player.is_alive():
            self.event()
        print("You are dead and lost the game.")
        game.end_game()

    def event(self):

        print("""Choose an action:
(A) Attack (C) Check Health/XP (I) Inventory (M) Move (Q) Quit (R) Rules""")

        choice = input("Enter your choice: ")

        if choice.upper() == "A":
            self.player.attack()

        if choice.upper() == "C":
            self.player.check_health_and_xp()

        if choice.upper() == "I":
            self.player.backpack()

        if choice.upper() == "M":
            self.player.move()

        if choice.upper() == "R":
            self.rules()

        if choice.upper() == "Q":
            print("Goodbye! Thank you for playing.")
            game.end_game()

        if choice.upper() == "R": #Rules text
            pass

        print("")

    def rules(self):
        dice_rolls_weapons = {
"Dagger": "d6",
"Knife": "d6",
"Longbow": "d12 + 2",
"Shortbow": "d8 + 2",
"Short Sword": "d8",
"Sledgehammer": "d8",
"Two-handed sword": "3xd6",
"Unarmed attack": "d4"
        }

        print("""
        RULES
        
        To win the game you have to reach level 10. To go up a level you need experience points(xp) which you will get
        when you destroy your enemies such as goblins, trolls etc.
        You loose the game if you get killed.
        
        All damage from attacks in the game are made by dice rolls. In list below you can see the dice roll for a specific weapon.
        For example: the damage from a dagger is a six side die (abbreviated d6). Some weapons are modified by a number e.g. longbow (D12 + 2).
        That means a longbow can make as minimum 3 of damage (1 by the roll plus 2).
        Ranged attacks may not always succeed. If you hit or not depends on a dice roll that is modified by your level.
        Better level = better chance to hit your target.
        
        """)

        print("Weapons in the game:")
        print(dice_rolls_weapons)




if __name__ == "__main__":
    game = Game()
    game.start()

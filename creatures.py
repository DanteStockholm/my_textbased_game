import random

def bandit():
    damage = random.randint(1, 8)
    return damage

'''def death_knight(roll_result): FUNCTION NOT WORKING. TRY ANOTHER SOLUTION.
    for i in range(2):
        roll_result += random.randint(1, 6)  # = 3x D6
    damage = roll_result
    return damage

def dragon(roll_result):
    for i in range(3):
        roll_result += random.randint(1, 6)  # = 4x D6
    damage = roll_result
    return damage'''

def goblin_attack():
    damage = random.randint(1, 4)
    return damage

def goblin_bowman():
    damage = random.randint(1, 8)
    return damage

'''def minotaur(roll_result):
    for i in range(1):
        roll_result += random.randint(1, 6)  # = 2x D6
    damage = roll_result + 2
    return damage'''

def skeleton():
    damage = random.randint(1, 8)
    return damage


def troll_attack():
    damage = random.randint(1, 6)
    return damage
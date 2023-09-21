# Weapons and other attack possibilites in the game
import random

def dagger(): # Also knife.
    damage = random.randint(1,6)
    return damage

def long_bow():
    damage = (random.randint(1, 12)) + 2
    return damage

def long_sword():
    damage = (random.randint(1, 8) + 2)
    return damage

def short_bow():
    damage = (random.randint(1, 8) + 2)
    return damage

def short_sword():
    damage = random.randint(1, 8)
    return damage

def sledgehammer():
    damage = (random.randint(1, 8) +1)
    return damage

def two_handed_sword(roll_result):
    for i in range(2):
        roll_result += random.randint(1,6)  # = 3x D6
    damage = roll_result
    return damage

def unarmed():
    damage = random.randint(1,4)
    return damage
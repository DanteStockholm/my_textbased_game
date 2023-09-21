# Actions


'''def hollow_tree():
    print("You see a big hollow tree. Looks like something is glowing inside the tree.")
    choice = input("Do you want to take a look? Y/N: ")
    if choice.upper() == "Y":
        hollow_tree_look()

    else:
        print("The tree stands still with all it's beauty. What do you want to do now?")'''


def goblin_cave():
    print("On your right side, you see a cave. At the entrance, you see three goblins quarreling about something")
    print("")
    go_to_cave = int(input("Do you want to go to the cave? Y/N: "))
    if go_to_cave.upper() == "Y":
        user_choice = 3
        return user_choice  # pass this as the location number, i.e. go to Goblin Cave

    elif go_to_cave.upper() == "N":
        user_choice = 5
        return user_choice  # pass this as the location number, i.e. go to North Forest

    else:
        print("Invalid answer. Please type 'Y' to enter the cave or 'N' to continue forward")
        user_choice = 5
        return user_choice  # Invalid answer, go to North Forest by default





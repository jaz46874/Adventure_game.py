import time
import random


def print_pause(x):
    print(x)
    time.sleep(2)


def castle(items):

    print_pause("Welcome to the Willy's Magical Castle.\n")
    print_pause("You find yourself stood in the hall of a wizard's castle.\n")
    print_pause("A dusty window casts a dark shadow in front of your body, "
                "stretching the length of the room.\n")
    time.sleep(1)
    print_pause("A dim chandelier provides enough light to glance "
                "around the room and see dust covered chests and troves.\n")
    time.sleep(1)
    print_pause("The wizard is on holiday and the castle is empty...\n")
    time.sleep(3)
    print_pause("or so it seems...\n")
    print_pause("On the left, you see a gloomy looking passage way.\n"
                "On the right is a tarnished wooden door.\n")


def passage(items):
    print_pause("As you walk the passage way gets darker and darker.\n")
    print_pause("You start to hear strange voices whispering "
                "encantations and chants.\n")

    if object in items:
        print_pause("Using the light from your new treasure, "
                    "you scan the room for danger.\n")
        print_pause("You step around the large hole in front of you.\n")
        print_pause("At the far end of the passage you find a locked door.\n")
        print_pause("'Unlock!' you exclaim and the door flies open.\n")
        print_pause("You step through the doorway to fresh air.\n")
        print_pause("Willy the curious wizard greets you outside "
                    "with a cheeky grin.\n")
        time.sleep(1)
        print_pause("Reaching into his backpocket, "
                    "he produces a certificate glowing with ruby writing "
                    "that reads:\n\n")
        print("\033[1;31;48m'Congratulation my child,\n"
              " you have passed the final test.\n"
              " Go forth and conquer!'\n\n")
        print("\033[30;0;48mYou Win!")
        play_again()

    else:
        print_pause("In the darkness, you trip and fall into a large hole.\n")
        print_pause("Your soul is lost forever!\n")
        print_pause("You Lose!")

        play_again()


def room(items):

    print_pause("The door creeks as you pull it open.\n")

    if object in items:
        print_pause("It doesn't seem like there is much else here for you!\n")
        print_pause("You walk back into the wizard's hall.\n")
        choose_room(items)

    else:

        objects = random.choice(["It's a Magic Wand!!!",
                                 "It's a Mystical Stone!!!",
                                 "It's an enchanted locket!!!"])

        print_pause("You step cautiously into the darkness.\n")
        print_pause("Suddenly, you come across a strange object.\n")
        print_pause(objects)
        print_pause("\nYou remember a 'magic spell' the wizard "
                    "taught you...\n")
        print_pause("Wibble Wabble, Scribb-ly Scrobble, Light My Way!\n")
        time.sleep(2)
        print_pause("A bright light begins to shine from your treasure.\n")
        print_pause("You walk back into the wizard's hall.\n")
        items.append(object)
        choose_room(items)


def choose_room(items):

    choice = input("1.Enter 'passage' to walk through the passage way. \n\n"
                   "2.Enter 'room' to open the door. \n\n")

    if "p" in choice:
        passage(items)

    elif "r" in choice:
        room(items)

    else:
        print_pause("\nUh oh, there are only two ways out!\n")
        choose_room(items)


def play_again():
    print_pause("\n\n-------------------GAME OVER-------------------")
    again = input("\n\nWould you like to play again? (enter 'yes' or 'no')\n")

    if "y" in again:
        play_game()

    else:
        print_pause("Have an enchanted day!")


def play_game():
    items = []
    castle(items)
    choose_room(items)


play_game()

# Python Text RPG - Ben Griffin

# Imports
import cmd
import textwrap
import sys
import os
import time
import random

# Our screen width
screen_width = 100

#### Player Class Setup ####


class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


# Initialize a player
myPlayer = Player()

#### Title Screen ####


def title_screen_selections():
    # select menu options and lowercase it
    option = input("~~> ")

    if option.lower() == ("play"):
        setup_game()  # TODO - placeholder
    elif option.lower() == ("help"):
        help_menu()   # TODO - placeholder
    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("~~> ")

        if option.lower() == ("play"):
            setup_game()  # TODO - placeholder
        elif option.lower() == ("help"):
            help_menu()   # TODO - placeholder
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('######################################')
    print('# Welcome to the Text RPG!')
    print('######################################')
    print('               -Play-                 ')
    print('               -Help-                 ')
    print('               -Quit-                 ')
    print('        Copyright Ben Griffin         ')
    title_screen_selections()


def help_menu():
    os.system('clear')
    print('######################################')
    print('# Welcome to the Text RPG!')
    print('######################################')
    print('- Use up, down, left, right to move   ')
    print('- Type your commands to run them      ')
    print('- Good luck and have fun              ')
    title_screen_selections()

#### Game Interactivity ####


def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zone_map[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print("\n" + "===============")
    print("What would you like to do?")
    action = input("~~> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit',
                          'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Please use a known action")
        action = input("~~> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())     # TODO
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())  # TODO


def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zone_map[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zone_map[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zone_map[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zone_map[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print(f"\n You have moved to the {destination}.")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zone_map[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print("You can trigger puzzle here.")

#### Game Functionality ####


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # here handle if puzzles have been solved, boss defeated, explored etc.


#### MAP ####
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up, north'
DOWN = 'down, south'
LEFT = 'left, west'
RIGHT = 'right, east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

zone_map = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home.',
        EXAMINATION: 'Your home looks the same - nothing has changed.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    # TODO map remainder of map
}


def setup_game():
    os.system('clear')

    # name collecting
    question1 = "Hello Whats your name?\n"
    for char in question1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    player_name = input("~~> ")
    myPlayer.name = player_name

    # job collecting
    question2 = "Hello, what role do you want to play?\n"
    question2added = "You can play as 'warrior', 'mage', 'priest'.\n"
    for char in question2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for char2 in question2added:
        sys.stdout.write(char2)
        sys.stdout.flush()
        time.sleep(0.10)
    player_job = input("~~> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print(f"You are now a {player_job}\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("~~> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print(f"You are now a {player_job}\n")
    # PLayer stats
    if myPlayer.job == 'warrior':
        myPlayer.hp = 100
        myPlayer.mp = 15
    elif myPlayer.job == 'mage':
        myPlayer.hp = 95
        myPlayer.mp = 65
    elif myPlayer.job == 'priest':
        myPlayer.hp = 50
        myPlayer.mp = 50
    # Introduction
    question3 = f"Weclome {player_name} the {player_job}.\n"
    for char in question3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

    speech1 = "Welcome to this fantasy world.\n"
    speech2 = "Enjoy the adventure.\n"
    speech3 = "Just make sure to not lose your way...\n"

    for char in speech1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    for char in speech2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    for char in speech3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    os.system('clear')
    print("#############")
    print("Let's start now.")
    print("#############")
    main_game_loop()


title_screen()

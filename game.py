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
        self.hp = 0
        self.mp = 0
        self.status_effects = []


# Initialize a player
myPlayer = Player()

#### Title Screen ####


def title_screen_selections():
    # select menu options and lowercase it
    option = input("~~> ")

    if option.lower() == ("play"):
        start_game()  # TODO - placeholder
    elif option.lower() == ("help"):
        help_menu()   # TODO - placeholder
    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("~~> ")

        if option.lower() == ("play"):
            start_game()  # TODO - placeholder
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


def start_game():

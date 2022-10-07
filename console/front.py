# Imports
import back
import os
from termcolor import colored
# Get text from user, depending on mode


def get_text_from_user(mode: str, system_text: str) -> str:
    """
    Show message asking text input mode, and gets the text.

    Arguments
    mode -- Mode of input
    system_text -- Text for user interaction
    """
    ret = None
    if (mode == 1):
        while (ret == None):
            path = input(system_text)
            ret = back.get_raw_text_from_file(path)
    else:
        ret = input(system_text)
    return ret


def handle_lan_error(value: str):
    """
    Handle when the value inputed from the user is not valid.

    Argument
    value -- User inputed value
    """

    # tell the user why the input is wrong
    return


def simple_input(system_txt) -> int:
    return input(system_txt)


def get_lan(system_txt: str) -> int:
    """
    Gets the system language

    Arguments
    system_text -- System text for input
    """
    return simple_input(system_txt)


def get_mode(system_txt: str) -> int:
    """
    Gets the input mode 

    Arguments
    system_text -- System text for input
    """
    return simple_input(system_txt)


def display_options(suggestion_list: tuple):
    """
    Shows options to user

    Arguments
    suggestion_list: tuple of suggestions
    """
    for i in range(len(suggestion_list)-1):
        print(f"[{i+1}]: {suggestion_list[i]}")
    print(f"[{len(suggestion_list)}]: OOV")
    print("")  # print an empty line


def get_option(system_text: str) -> int:
    """
    Gets the user option 

    Arguments
    system_text -- System text for input
    """
    # Get option
    return simple_input(system_text)

# Display text


def display_text(index: int, sliced_words: list, color: str):
    """
    Show text with highlighted word.

    Arguments
    index -- Index of word
    sliced_words -- Text with words sliced
    color -- Color to use
    """
    clear_terminal()
    for x in range(index):
        print(sliced_words[x], end="")
    print(colored(sliced_words[index], color), end="")
    for x in range(index+1, len(sliced_words)):
        print(sliced_words[x], end=""),
    print("")

# Final print message


def finalprint(message: str, system_text: str):
    """
    Shows the resulting text.

    Arguments
    message -- Text to display
    system_text -- System text for input
    """
    print(system_text)
    print(colored(message, "green"))

# Clear terminal


def clear_terminal():
    """
    Clear the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def easter_egg():
    """
    Amogus!!

    Lore: https://knowyourmeme.com/memes/amogus
    """
    amongus = """           ⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁"""
    print(colored(amongus, "cyan"),)

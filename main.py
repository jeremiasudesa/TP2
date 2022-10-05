#Imports
from time import sleep
import front
import back
import text_suggestion
#Ask system language
def get_system_language() -> str:
    """
    Define system language based on an input value
    """
    language = None
    # pedir lenguaje al usuario hasta que de correcto
    while ((language == None) or (not back.check_lan_input(language))):
        language = int(input(
            "Choose interaction language - Elegir lenguaje de interacción (English: 1, Español: 2): "))
    return language

#Ask text processing mode and returns the words sliced
def ask_text_from_user(system_text1: str, system_text2: tuple) -> tuple:
    """
    Define system mode of text input based on an input value, and handles the text (slicing) then returns it.

    Arguments:
    system_text1 -- Provides text for inputs
    system_text2 -- Provides text for inputs
    """
    mode = int(input(system_text1))
    #Validate mode
    raw = front.get_text_from_user(mode, system_text2[mode-1])
    #Get words
    return back.separe(raw)

#Get top 5 words
def get_top_5(word: str, bktree: text_suggestion.bk_tree) -> list:
    """
    Get top five words for a given string using Levenshtein distance.

    Arguments
    word -- Word to calculate top five values.
    bktree - Instance of B.K. Tree.
    """
    ret = []
    #Retrieve words from BK Tree for a given word
    bktree.retrieve_words(2, bktree.root, word, ret)
    if (len(ret) > 0):
        ret.sort()
    return [x[1] for x in list(ret[:5])]

#Fix errors
def fix_error(word_index: int, sliced_words: list, bk_tree: text_suggestion.bk_tree, system_text1: str, system_text2: str, system_text3: str):
    """
    For a given word index shows the word and provides interactions for the user to edit.

    Arguments
    word_index -- Word index
    sliced_words -- List of sliced words
    bk_tree -- Instance of B.K. Tree
    system_text1 -- System text
    system_text2 -- System text
    system_text3 -- System text
    """
    #Terminal clear
    front.clear_terminal()
    #Display words
    front.display_text(word_index, sliced_words, "red")
    #Display options
    suggestion_list = get_top_5(sliced_words[word_index], bk_tree)
    suggestion_list.append(sliced_words[word_index])
    print(system_text1)
    for i in range(len(suggestion_list)-1):
        print(f"[{i+1}]: {suggestion_list[i]}")
    print(f"[{len(suggestion_list)+1}]: OOV")
    print("")
    #When user selects option perform editing
    option = front.get_option(len(suggestion_list), system_text2)
    back.replace_text(option, word_index, sliced_words, suggestion_list)
    front.display_text(word_index, sliced_words, "green")
    #"Next" user interaction
    anykey = input(system_text3)
    return

#Thrid language
def do_not_read_shhh(language: str):
    if (language == 3):
        front.easter_egg()
        exit()

#Main function
def main():
    #Clear terminal
    front.clear_terminal()
    #Get text for the system interction
    language = get_system_language()
    #Shhhhhh
    do_not_read_shhh(language)
    #Get interaction text from database
    interaction_text = back.get_system_texts(language)
    #Get dictionary for the corresponding language
    dictionary = back.get_dict(language)
    #Ask text from user
    parts = ask_text_from_user(interaction_text[0], (interaction_text[1], interaction_text[2]))
    #Caculate five words with Levenshtein distance ≤ 2
    words_outside = back.not_in_dict(parts, dictionary)
    #Caculate top 3 levi distances for each word
    bktree = text_suggestion.bk_tree_singleton(dictionary, language)
    #Fix error in words
    for wo in words_outside:
        fix_error(wo, parts, bktree, interaction_text[3], interaction_text[4], interaction_text[5])
    front.clear_terminal()
    ft = ""
    for x in parts:
        ft += x
    front.finalprint(ft, interaction_text[6])


if __name__ == "__main__":
    main()
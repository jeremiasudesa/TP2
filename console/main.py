# Imports
import front
import back
import text_suggestion
# Ask system language


def get_system_language() -> int:
    """
    Get system language from user
    """
    language = "-1"
    # ask language until check is True
    while not back.check_lan_input(language):
        system_text_lan = "Choose interaction language - Elegir lenguaje de interacción (English: 1, Español: 2): "
        language = front.get_lan(system_text_lan)
    return int(language)


def get_mode_from_user(system_text: str) -> int:
    """
    Get input mode from user
    """
    mode = "-1"
    # ask mode until check is True
    while not back.check_mode_input(mode):
        mode = front.get_mode(system_text)
    return int(mode)


def get_text_from_user(mode: int, system_texts: tuple) -> list:
    """
    Gets text from user, based on mode

    Arguments:
    mode -- input mode
    system_texts -- user interaction strings
    """
    raw = front.get_text_from_user(mode, system_texts[mode-1])
    # Get words
    return back.separe(raw)


def get_option_from_user(len_sug: int, system_text: str) -> int:
    """
    Get option from user

    Arguments
    len_sug -- lenght of suggestion list
    system_text -- user interaction string
    """
    opt = "-1"
    # ask mode until check is True
    while not back.check_opt_input(opt, len_sug):
        opt = front.get_option(system_text)
    return int(opt)


def get_top_5(word: str, bktree: text_suggestion.bk_tree) -> tuple:
    """
    Get top five words for a given string using Levenshtein distance.

    Arguments
    word -- Word to calculate top five values.
    bktree - Instance of B.K. Tree.
    """
    ret = []
    # Retrieve words from BK Tree for a given word
    bktree.retrieve_words(2, bktree.root, word, ret)
    if (len(ret) > 0):
        ret.sort()
    return tuple([x[1] for x in list(ret[:5])])


def fix_error(word_index: int, sliced_words: list, bk_tree: text_suggestion.bk_tree, system_texts: tuple):
    """
    For a given word index shows the word and provides interactions for the user to edit.

    Arguments
    word_index -- Word index
    sliced_words -- List of sliced words
    bk_tree -- Instance of BK Tree
    system_texts -- Texts for user interaction
    """
    # Display words
    front.display_text(word_index, sliced_words, "red")
    # Get options
    suggestion_list = get_top_5(sliced_words[word_index], bk_tree)
    suggestion_list += sliced_words[word_index]
    # Display options
    front.display_options(suggestion_list)
    # When user selects option perform editing
    option = get_option_from_user(len(suggestion_list), system_texts[1])-1
    # OOV
    if option == len(suggestion_list)-1:
        alt = front.get_OOV()
        suggestion_list[option] = alt if alt != "" else suggestion_list[option]
    # Replace text
    back.replace_text(option, word_index, sliced_words, suggestion_list)
    front.display_text(word_index, sliced_words, "green")
    # The users presses any key, the program continues
    anykey = input(system_texts[2])
    return


def do_not_read_shhh(language: int):
    if (language == 3):
        front.easter_egg()
        exit()


def main():
    # Clear terminal
    front.clear_terminal()
    # Get text for the system interction
    language = get_system_language()
    # Shhhhhh
    do_not_read_shhh(language)
    # Get interaction text from database
    interaction_text = back.get_system_texts(language)
    # Get wordset for the corresponding language
    wordset = back.get_wordset(language)
    # Ask text from user
    mode = get_mode_from_user(interaction_text[0])
    parts = get_text_from_user(mode, interaction_text[1:3])
    # Caculate five words with Levenshtein distance ≤ 2
    words_outside = back.not_in_wordset(parts, wordset)
    # Caculate top 3 levi distances for each word
    bktree = text_suggestion.bk_tree_singleton(wordset, language)
    # Fix error in words
    for word_outside in words_outside:
        fix_error(word_outside, parts, bktree, interaction_text[3:6])
    # Show final text
    front.clear_terminal()
    ft = back.final_text(parts)
    front.finalprint(ft, interaction_text[6])
    if (mode == 1):
        back.writefile(input(interaction_text[7])+".txt", ft)


if __name__ == "__main__":
    main()

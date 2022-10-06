# Imports
from os import path
# Absolut path


def abspath(relative_path: str) -> str:
    """
    Create a absolute path with a relative path

    Arguments
    relative_path -- Relative path
    """
    script_dir = path.dirname(__file__)  # get absolute path of context
    file_path = path.join(script_dir, relative_path)  # join with realtive path
    return file_path


# Check if path exist


def path_name_exists(path_name: str) -> bool:
    """
    Check if path exist

    Arguments
    path_name -- Path to check
    """
    return path.exists(path_name)

# Get raw text from file


def get_raw_text_from_file(path_name: str) -> str:
    """
    Get the raw text from a given file

    Arguments
    path_name -- Path to access the file
    """
    file_path = abspath(path_name)  # get absolute path
    if (not path_name_exists(file_path)):  # wait until path exists
        return None
    f = open(file_path)
    ret = f.read()
    f.close()
    return ret

# Get system texts


def get_system_texts(language: str) -> tuple:
    """
    For a given language gets system texts

    Arguments
    language -- Language specified from user
    """
    path = "source/textos_interaccion_" + str(language) + ".txt"
    raw_text = get_raw_text_from_file(path)
    return raw_text.split("|")

# Get wordset for the selected language


def get_wordset(language: str) -> set:
    """
    For a given language gets wordset

    Arguments
    language -- Language specified from user
    """
    path = "source/diccionario_" + str(language) + ".txt"
    raw_text = get_raw_text_from_file(path)
    if (raw_text == None):
        return None
    dic = set()
    striped = raw_text.split("\n")
    for x in striped:
        dic.add(x)
    return dic

# Checks language input


def check_lan_input(language: int) -> bool:
    """
    Checks if language option is valid.

    Arguments 
    language -- Language selected
    """
    return (language in range(1, 4))

# Check input option


def check_opt_input(opt: int, lenop) -> bool:
    """
    Checks if option is valid.

    Arguments 
    option -- option selected
    """
    return (opt in range(1, lenop+1))

# Get splited words from text


def get_words_from_raw(raw_text: str) -> list:
    """
    Get splited tuple of words

    Arguments
    raw_text -- Raw text to get words
    """
    return raw_text.split()

# Clean words


def clean_word(word: str) -> str:
    """
    Get only words from a given string.

    Arguments
    word -- String to clean
    """
    return str([x for x in word if (x in range('a', 'z'))])

#Words not in wordset


def not_in_wordset(words_list: list, wordset: set) -> tuple:
    """
    Get words not in wordset

    Arguments
    words_list -- List of words to check
    wordset -- Wordset 
    """
    ret = []
    for ind in range(len(words_list)):
        if (not (words_list[ind][0].isalpha())):
            continue
        if not (words_list[ind] in wordset):
            ret.append(ind)
    return ret

# Separe words from characters


def separe(text: str) -> list:
    """
    Separe text from characters

    Arguments
    text -- String of text to check
    """
    ret = []
    idx = 0
    b = text[0].isalpha()
    for i in range(len(text)):
        if (b != (text[i].isalpha()) or text[i] == " "):
            ret.append(text[idx:i])
            idx = i
        b = text[i].isalpha()
    ret.append(text[idx:])
    return ret

# Replace text


def replace_text(option_number: int, index: int, words_list: list, suggestion_list: list) -> None:
    """
    Replace text inside list of words

    Arguments
    option_number -- Number of selected option
    index -- Index of the word to change
    words_list -- List of words
    suggestion_list -- List of word suggestion    
    """
    words_list[index] = suggestion_list[option_number-1]


def writefile(path: str, content: str):
    path = abspath(path)
    with open(path, 'w') as f:
        f.write(content)

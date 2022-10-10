from os import path
import typing


def abspath(relative_path: str) -> str:
    """
    Create a absolute path with a relative path

    Arguments
    relative_path -- Relative path
    """
    script_dir = path.dirname(__file__)  # get absolute path of context
    file_path = path.join(script_dir, relative_path)  # join with realtive path
    return file_path


def path_name_exists(path_name: str) -> bool:
    """
    Check if path exist

    Arguments
    path_name -- Path to check
    """
    return path.exists(path_name)


def check_file_type(path_name: str, desired_types: tuple) -> bool:
    """
    Return true if correct file type

    Arguments
    path_name -- Path to access the file
    desired_types -- Valid file
    """
    return path_name.lower().endswith(desired_types)


def get_raw_text_from_file(path_name: str) -> typing.Union[str, None]:
    """
    Get the raw text from a given file if file is as desired

    Arguments
    path_name -- Path to access the file
    """
    file_path = abspath(path_name)  # get absolute path
    if (not path_name_exists(file_path)):  # wait until path exists
        return None
    extensions = tuple(".txt")
    if (not check_file_type(file_path, extensions)):
        return None
    f = open(file_path,  encoding='utf-8')
    ret = f.read()
    f.close()
    return ret


def get_system_texts(language: int) -> tuple:
    """
    For a given language gets system texts

    Arguments
    language -- Language specified from user
    """
    path = "source/textos_interaccion_" + str(language) + ".txt"
    raw_text = get_raw_text_from_file(path)
    if (raw_text == None):
        raise Exception("Internal Error: System Text Retrieval Fail")
    return tuple(raw_text.split("|"))


def get_wordset(language: int) -> typing.Union[set, None]:
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


def try_positive_int(param: str) -> int:
    """
    Tries casting string to int, otherwise returns a negative number.

    Arguments
    param -- any string
    """
    try:
        return int(param)
    except:
        return -1


def check(x: str, maxi: int) -> bool:
    """
    Try casting string to int, check if inside range.

    Arguments
    x -- String to be checked
    """
    x_int = try_positive_int(x)
    return x_int in range(1, maxi)


def check_lan_input(language: str) -> bool:
    """
    Checks if language option is valid.

    Arguments
    language -- Language selected
    """
    return check(language, 4)


def check_mode_input(mode: str) -> bool:
    """
    Checks if mode option is valid.

    Arguments
    mode -- Mode selected
    """
    return check(mode, 3)


def check_opt_input(opt: str, len_sug: int) -> bool:
    """
    Checks if option is valid.

    Arguments
    option -- option selected
    """
    return check(opt, len_sug+1)


def get_words_from_raw(raw_text: str) -> list:
    """
    Get splited tuple of words

    Arguments
    raw_text -- Raw text to get words
    """
    return raw_text.split()


def clean_word(word: str) -> str:
    """
    Get only words from a given string.

    Arguments
    word -- String to clean
    """
    return str([x for x in word if (x in range('a', 'z'))])


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
    return tuple(ret)


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


def replace_text(option_number: int, index: int, words_list: list, suggestion_list: list) -> None:
    """
    Replace text inside list of words

    Arguments
    option_number -- Number of selected option
    index -- Index of the word to change
    words_list -- List of words
    suggestion_list -- List of word suggestion
    """
    words_list[index] = suggestion_list[option_number]


def writefile(path: str, content: str):
    """
    Creates file

    Arguments
    path -- pathname
    content -- file content
    """
    path = abspath(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def final_text(parts: list) -> str:
    """
    joins string segments
    """
    return "".join(parts)

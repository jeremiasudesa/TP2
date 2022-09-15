import os.path
from os import path


def path_name_exists(pathstr: str) -> bool:
    return path.exists(pathstr)


def get_raw_text_from_file(pathstr: str) -> str:
    if (not path_name_exists(pathstr)):
        return None
    f = open(pathstr)
    ret = f.read()
    f.close()
    return ret


def get_interaction_text_from_DB(lan: str) -> tuple:
    grtff = get_raw_text_from_file(
        "source/textos_interaccion_" + str(lan) + ".txt")
    if (grtff == None):
        return None
    return grtff.split("|")


def get_dict(lan: str) -> set:
    grtff = get_raw_text_from_file("source/diccionario_" + str(lan) + ".txt")
    if (grtff == None):
        return None
    dic = {}
    striped = grtff.split("\n")
    for x in striped:
        dic.add(x)
    return x


def check_lan_input(lan: int) -> bool:
    # TODO check if int, check if easter egg, else wrong
    return (lan == 1 or lan == 2)


def get_words_from_raw(raw: str) -> tuple:
    return raw.split()


def check_text_input(text: str) -> bool:
    return True


def clean_word(word: str) -> str:
    return str([x for x in word if (x in range('a', 'z'))])


def not_in_dict(wrds: str, dict: str) -> tuple:
    # posiblemente se podria hacer mejor con una funcion nativa
    ret = []
    for i in range(len(wrds)):
        if (clean_word(wrds[i]) not in dict):
            ret.append(i)
    return ret

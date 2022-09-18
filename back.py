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
    dic = set()
    striped = grtff.split("\n")
    for x in striped:
        dic.add(x)
    return dic


def check_lan_input(lan: int) -> bool:
    # TODO check if int, check if easter egg, else wrong
    return (lan == 1 or lan == 2)


def get_words_from_raw(raw: str) -> tuple:
    return raw.split()


def clean_word(word: str) -> str:
    return str([x for x in word if (x in range('a', 'z'))])


def not_in_dict(wrds: str, dic: set) -> tuple:
    # posiblemente se podria hacer mejor con una funcion nativa
    ret = []
    for w in wrds:
        if not (w in dic):
            ret.append(w)
    return ret

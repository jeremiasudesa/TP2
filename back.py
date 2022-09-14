def get_raw_text_from_file(path: str) -> str:
    f = open(path)
    ret = f.read()
    f.close()
    return ret


def get_interaction_text_from_DB(len: str) -> tuple:
    return get_raw_text_from_file("source/textos_interaccion_" + str(len) + ".txt").split("|")


def get_dict(len: str) -> tuple:
    return get_raw_text_from_file("source/diccionario_" + str(len) + ".txt").split()


def check_lan_input(lan: str) -> bool:
    # TODO check if int, check if easter egg, else wrong
    return False


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

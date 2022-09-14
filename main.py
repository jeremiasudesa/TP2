def get_raw_text_from_file(path: str) -> str:
    f = open(path)
    ret = f.read()
    f.close()
    return ret


def get_interaction_text_from_DB(len: str) -> tuple:
    return get_raw_text_from_file("source/textos_interaccion_" + str(len) + ".txt").split("|")


def get_dict(len: str) -> tuple:
    return get_raw_text_from_file("source/diccionario_" + str(len) + ".txt").split()


def get_text_from_user(way: str) -> str:
    return ""


def check_lan_input(lan: str) -> bool:
    # TODO check if int, check if easter egg, else wrong
    return False


def handle_lan_error(txt: str):
    # tell the user why the input is wrong
    return


def ask_lan_from_user() -> str:
    lan = None
    # pedir lenguaje al usuario hasta que de correcto
    while (not check_lan_input(lan)):
        lan = int(input(
            "choose interaction language // elegi lenguaje de interaccion (en: 1, es: 2): "))
    return lan


def get_words_from_raw(raw: str) -> tuple:
    return raw.split()


def handle_text_error(txt: str):
    # tell the user why the input is wrong
    return


def ask_text_from_user(input_txt: str) -> tuple:
    # conseguir raw
    way = input(input_txt)
    raw = None
    while (not check_text_input(raw)):
        handle_text_error(raw)
        raw = get_text_from_user(way)
    # conseguir palabras
    words = get_words_from_raw(raw)
    return words


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


def main():
    # conseguir lenguaje
    len = ask_lan_from_user()
    # conseguir textos de interaccion
    itxt = get_interaction_text_from_DB(len)
    # conseguir diccionario
    dict = get_dict(len)
    # conseguir palabras no limpias
    words = ask_text_from_user(itxt[0])
    # conseguir indices de palabras no pertenecientes al diccionario
    words_outside = not_in_dict(words, dict)


if __name__ == "__main__":
    main()

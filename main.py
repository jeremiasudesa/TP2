def get_interaction_language_from_DB(len: str) -> str:
    f = None
    if (len == "en"):
        f = open("textos/textos_interaccion_en.txt")
    else:
        f = open("textos/textos_interaccion_es.txt")
    ret = f.read()
    f.close()
    return ret


def handle_len_input(len: str) -> str:
    # TODO implement check
    return len


def get_interaction_language_from_user() -> str:
    #input / validation
    len = input(
        "choose interaction language // elegi lenguaje de interaccion (en, es): ")
    len = handle_len_input(len)
    # get interaction texts
    itxt = get_interaction_language_from_DB(len)
    return itxt


def main():
    itxt = get_interaction_language_from_user()


if __name__ == "__main__":
    main()

import front
import back
import text_suggestion


def ask_lan_from_user() -> str:
    lan = None
    # pedir lenguaje al usuario hasta que de correcto
    while ((lan == None) or (not back.check_lan_input(lan))):
        lan = int(input(
            "choose interaction language // elegi lenguaje de interaccion (en: 1, es: 2): "))
    return lan


def ask_text_from_user(input_txt: str) -> tuple:
    # conseguir raw
    way = input(input_txt)
    # validar way
    raw = front.get_text_from_user(way)
    # conseguir palabras
    words = back.get_words_from_raw(raw)
    return words


def main():
    # conseguir lenguaje
    len = ask_lan_from_user()
    # conseguir textos de interaccion
    itxt = back.get_interaction_text_from_DB(len)
    # conseguir diccionario
    dictionary = back.get_dict(len)
    # calculate top 3 levi for each word
    # add check with dictionary
    # for each word offer options to user and make him able to change
    # conseguir palabras no limpias
    words = ask_text_from_user(itxt[0])
    # conseguir indices de palabras no pertenecientes al diccionario
    words_outside = back.not_in_dict(words, dictionary)
    # caculate top 3 levi distances for each word
    bktree = text_suggestion.bk_tree(dictionary)
    # print(bktree.tree[bktree.root][1])
    ret = []
    print(bktree.root)
    print(bktree.retrieve_words(10, bktree.root, "pollerx", ret))


if __name__ == "__main__":
    main()

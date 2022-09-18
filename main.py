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
    lan = ask_lan_from_user()
    # conseguir textos de interaccion
    itxt = back.get_interaction_text_from_DB(lan)
    # conseguir diccionario
    dictionary = back.get_dict(lan)
    # calculate top 3 levi for each word
    # add check with dictionary
    # for each word offer options to user and make him able to change
    # conseguir palabras no limpias
    words = ask_text_from_user(itxt[0])
    # conseguir indices de palabras no pertenecientes al diccionario
    words_outside = back.not_in_dict(words, dictionary)
    # caculate top 3 levi distances for each word
    bktree = text_suggestion.bk_tree_singleton(dictionary, lan)
    # print(bktree.tree[bktree.root][1])
    ret = []
    print("buscando palabras...")
    bktree.retrieve_words(2, bktree.root, words[0], ret)
    if (len(ret) > 0):
        ret.sort()
    for x in range(min(5, len(ret))):
        print(ret[x][1])


if __name__ == "__main__":
    main()

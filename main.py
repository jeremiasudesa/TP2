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
    return back.separe(raw)


def get_top_5(wrd: str, bktree: text_suggestion.bk_tree) -> list:
    ret = []
    bktree.retrieve_words(2, bktree.root, wrd, ret)
    if (len(ret) > 0):
        ret.sort()
    return [x[1] for x in list(ret[:5])]


def fix_error(wrd: int, parts: list, bkt: text_suggestion.bk_tree):
    suggestion_list = get_top_5(parts[wrd], bkt)
    suggestion_list.append("OOV")
    print("elegir opcion: ")
    for i in range(len(suggestion_list)):
        print(f"[{i+1}]: {suggestion_list[i]}")
    print("//////////")
    option = front.get_option(len(suggestion_list))
    print(option)
    back.replace_text(option, wrd, parts, suggestion_list)
    front.display_text(parts)
    return


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
    parts = ask_text_from_user(itxt[0])
    # conseguir indices de palabras no pertenecientes al diccionario
    words_outside = back.not_in_dict(parts, dictionary)
    # caculate top 3 levi distances for each word
    bktree = text_suggestion.bk_tree_singleton(dictionary, lan)
    for wo in words_outside:
        fix_error(wo, parts, bktree)


if __name__ == "__main__":
    main()

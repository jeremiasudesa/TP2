from time import sleep
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


def ask_text_from_user(input_txt1: str, input_txt2: tuple) -> tuple:
    # conseguir raw
    way = int(input(input_txt1))
    # validar way
    raw = front.get_text_from_user(way, input_txt2[way-1])
    # conseguir palabras
    return back.separe(raw)


def get_top_5(wrd: str, bktree: text_suggestion.bk_tree) -> list:
    ret = []
    bktree.retrieve_words(2, bktree.root, wrd, ret)
    if (len(ret) > 0):
        ret.sort()
    return [x[1] for x in list(ret[:5])]


def fix_error(wrd: int, parts: list, bkt: text_suggestion.bk_tree, interaction_txt1: str, interaction_txt2: str, interaction_txt3: str):
    front.clear_terminal()
    front.display_text(wrd, parts, "red")
    suggestion_list = get_top_5(parts[wrd], bkt)
    print(interaction_txt1)
    for i in range(len(suggestion_list)):
        print(f"[{i+1}]: {suggestion_list[i]}")
    print(f"[{len(suggestion_list)+1}]: OOV")
    print("//////////")
    suggestion_list.append(parts[wrd])
    option = front.get_option(len(suggestion_list), interaction_txt2)
    back.replace_text(option, wrd, parts, suggestion_list)
    front.display_text(wrd, parts, "green")
    anykey = input(interaction_txt3)
    return


def third_language(lan: str):
    if (lan == 3):
        front.easter_egg()
        exit()


def main():
    front.clear_terminal()
    # conseguir lenguaje
    lan = ask_lan_from_user()
    third_language(lan)
    # conseguir textos de interaccion
    itxt = back.get_interaction_text_from_DB(lan)
    # conseguir diccionario
    dictionary = back.get_dict(lan)
    # calculate top 3 levi for each word
    # add check with dictionary
    # for each word offer options to user and make him able to change
    # conseguir palabras no limpias
    parts = ask_text_from_user(itxt[0], (itxt[1], itxt[2]))
    # conseguir indices de palabras no pertenecientes al diccionario
    words_outside = back.not_in_dict(parts, dictionary)
    # caculate top 3 levi distances for each word
    bktree = text_suggestion.bk_tree_singleton(dictionary, lan)
    for wo in words_outside:
        fix_error(wo, parts, bktree, itxt[3], itxt[4], itxt[5])
    front.clear_terminal()
    ft = ""
    for x in parts:
        ft += x
    front.finalprint(ft, itxt[6])


if __name__ == "__main__":
    main()

from os import path


def abspath(relative_path: str) -> str:
    script_dir = path.dirname(__file__)  # <-- absolute dir the script is in
    file_path = path.join(script_dir, relative_path)
    return file_path


def path_name_exists(pathstr: str) -> bool:
    return path.exists(pathstr)


def get_raw_text_from_file(pathstr: str) -> str:
    # TODO: abrir con with
    # TODO: correjir en el archivo mismo
    # commit thissss
    file_path = abspath(pathstr)
    if (not path_name_exists(file_path)):
        print("NO EXISTE")
        return None
    f = open(file_path)
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
    return (lan in range(1, 4))


def check_opt_input(opt: int, lenop) -> bool:
    return (opt in range(1, lenop+1))


def get_words_from_raw(raw: str) -> tuple:
    return raw.split()


def clean_word(word: str) -> str:
    return str([x for x in word if (x in range('a', 'z'))])


def not_in_dict(wrds: list, dic: set) -> tuple:
    # posiblemente se podria hacer mejor con una funcion nativa
    ret = []
    for ind in range(len(wrds)):
        if (not (wrds[ind][0].isalpha())):
            continue
        if not (wrds[ind] in dic):
            ret.append(ind)
    return ret


def separe(w: str) -> list:
    ret = []
    idx = 0
    b = w[0].isalpha()
    for i in range(len(w)):
        if (b != (w[i].isalpha()) or w[i] == " "):
            ret.append(w[idx:i])
            idx = i
        b = w[i].isalpha()
    ret.append(w[idx:])
    return ret


def replace_text(option: int, idx: int, parts: list, suggestion_list: list) -> None:
    parts[idx] = suggestion_list[option-1]

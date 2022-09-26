import back


def get_text_from_user(way: str) -> str:
    ret = None
    if (way == 1):
        while (ret == None):
            path = input("ingresar path del archivo: ")
            ret = back.get_raw_text_from_file(path)
    else:
        ret = input("ingresar texto: ")
    return ret


def handle_lan_error(txt: str):
    # tell the user why the input is wrong
    return


def get_option(cantop: int) -> str:
    ret = False
    while (not ret):
        opt = int(input("ingresar opcion: "))
        ret = back.check_opt_input(opt, cantop)
    return opt


def display_text(parts: list):
    fulltxt = ""
    for x in parts:
        fulltxt += x
    print(fulltxt)

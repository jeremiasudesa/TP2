
from back import get_raw_text_from_file


def get_text_from_user(way: str) -> str:
    ret = None
    if (way == 1):
        while (ret == None):
            path = input("ingresar path del archivo: ")
            ret = get_raw_text_from_file(path)
    else:
        ret = input("ingresar texto: ")
    return ""


def handle_lan_error(txt: str):
    # tell the user why the input is wrong
    return


def handle_text_error(txt: str):
    # tell the user why the input is wrong
    return

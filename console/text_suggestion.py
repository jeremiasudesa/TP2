import functools
from functools import lru_cache
import pickle
import back


class bk_tree:
    def __init__(self, D: set, lan: int):
        self.tree = {}
        self.root = ""
        self.Dictionary = D
        self.init_dictionary()
        # store instance

    def init_dictionary(self):
        print("creando diccionario...")
        for w in self.Dictionary:
            self.insert_word(self.root, w)
        print("diccionario creado.")

    @lru_cache
    def levenshtein_recursive(self, word_a, word_b):
        len_b = len(word_b)
        len_a = len(word_a)

        if len_b == 0:
            return len_a

        if len_a == 0:
            return len_b

        tail_a = word_a[1:]
        tail_b = word_b[1:]

        if word_a[0] == word_b[0]:
            return self.levenshtein_recursive(tail_a, tail_b)

        return 1 + min(
            self.levenshtein_recursive(word_a, tail_b),
            self.levenshtein_recursive(tail_a, word_b),
            self.levenshtein_recursive(tail_a, tail_b)
        )

    def insert_word(self, curr: str, wrd: str):
        # print(f"{curr}, {wrd}")
        if self.root == "":
            self.root = wrd
            self.tree[self.root] = (self.root, {})
            return
        distance = self.levenshtein_recursive(curr, wrd)
        if (distance in self.tree[curr][1].keys()):
            self.insert_word(self.tree[curr][1][distance][0], wrd)
            return
        self.tree[wrd] = (wrd, {})
        self.tree[curr][1][distance] = self.tree[wrd]

    def retrieve_words(self, tol: int, curr: str, wrd: str, ret: list) -> list:
        D = self.levenshtein_recursive(curr, wrd)
        if (D <= tol):
            ret.append((D, curr))
        rb = D + tol
        lb = max(1, D - tol)
        parent = self.tree[curr]
        for dis in range(lb, rb+1):
            child = parent[1].get(dis)
            if (child == None):
                continue
            nd = self.levenshtein_recursive(child[0], wrd)
            self.retrieve_words(tol, child[0], wrd, ret)


def bk_tree_singleton(D: set, lan: int):
    # check if tree already exists
    file_path = back.abspath("source/class_" + str(lan)+".obj")
    if (back.path_name_exists(file_path)):
        # set class to class
        filehandler = open(file_path, 'rb')
        return pickle.load(filehandler)
    else:
        bktree = bk_tree(D, lan)
        file_pi = open(file_path, 'wb')
        pickle.dump(bktree, file_pi)
        return bktree

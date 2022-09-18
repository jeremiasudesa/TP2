import functools
from functools import lru_cache


class bk_tree:
    def __init__(self, D: set):
        self.tree = {}
        self.root = ""
        self.Dictionary = D
        self.init_dictionary()

    def init_dictionary(self):
        for w in self.Dictionary:
            self.insert_word(self.root, w)

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
        #print(f"{curr}, {wrd}")
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
        print(f"{curr}, {wrd}")
        min_child = None
        min_distance = tol+1
        if (self.levenshtein_recursive(curr, wrd) <= tol):
            ret.append(curr)
        for x in self.tree[curr][1].keys():
            node = self.tree[curr][1][x]
            curr_child = node[0]
            curr_distance = self.levenshtein_recursive(curr_child, wrd)
            if (curr_distance < min_distance):
                min_child = curr_child
                min_distance = curr_distance
        if (min_child != None):
            return self.retrieve_words(tol, min_child, wrd, ret)
        return ret

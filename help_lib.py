import string
import sys

TUPLE_ALL_SYMBOLS = tuple(string.ascii_letters) +                  tuple('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ') + \
                    tuple(string.punctuation)
SET_ALL_SYMBOLS = set(TUPLE_ALL_SYMBOLS)
LEN_ALL_SYMBOLS = len(TUPLE_ALL_SYMBOLS)
SYMBOL_TO_IND = {c: j for j, c in enumerate(TUPLE_ALL_SYMBOLS)}


def move_symbol(char, move):
    index = (SYMBOL_TO_IND[char] + move) % LEN_ALL_SYMBOLS
    return TUPLE_ALL_SYMBOLS[index]


class CleverOpenFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        if self.file_name is None:
            if self.mode == "r":
                return sys.stdin
            elif self.mode == "w":
                return sys.stdout
            else:
                raise ValueError
        else:
            self.file = open(self.file_name, self.mode)
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_name is not None:
            self.file.close()
        return False

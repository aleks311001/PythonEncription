import string
import sys

RUSSIAN_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
STR_ALL_SYMBOLS = str(string.ascii_letters) + \
                  RUSSIAN_ALPHABET.upper() + RUSSIAN_ALPHABET + ' ' + \
                  str(string.punctuation)
LEN_ALL_SYMBOLS = len(STR_ALL_SYMBOLS)
SYMBOL_TO_IND = {char: ind for ind, char in enumerate(STR_ALL_SYMBOLS)}


def move_symbol(char, move):
    index = (SYMBOL_TO_IND[char] + move) % LEN_ALL_SYMBOLS
    return STR_ALL_SYMBOLS[index]


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

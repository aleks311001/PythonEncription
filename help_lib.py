import string
import sys


all_symbols = tuple(string.ascii_letters) +\
              tuple('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ') +\
              tuple(string.punctuation)

len_all_symbols = len(all_symbols)
dict_symbols = {all_symbols[i]: i for i in range(len_all_symbols)}


def clever_open(file_name, mode):
    if file_name is None:
        if mode == "r":
            return sys.stdin
        elif mode == "w":
            return sys.stdout
        else:
            return None
    else:
        return open(file_name, mode)

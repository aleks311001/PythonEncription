from help_lib import *


def caesar(line, key):
    result = ''
    for char in line:
        if char in SET_ALL_SYMBOLS:
            index = (SYMBOL_TO_IND[char] + key) % LEN_ALL_SYMBOLS
            result += TUPLE_ALL_SYMBOLS[index]
        else:
            result += char
    return result


def vigenere(line, key):
    result = ''
    for index_char_in_line, char_lines in enumerate(line):
        if char_lines in SET_ALL_SYMBOLS:
            index_in_list_all_symbols = SYMBOL_TO_IND[char_lines]
            index_key_in_list_all_symbols = SYMBOL_TO_IND[key[index_char_in_line % len(key)]]
            index_char_in_encode = (index_in_list_all_symbols + index_key_in_list_all_symbols) % LEN_ALL_SYMBOLS

            result += TUPLE_ALL_SYMBOLS[index_char_in_encode]
        else:
            result += char_lines
    return result


def encode_file(input_file, output_file, key, func_for_encode):
    for line in input_file:
        new_line = func_for_encode(line, key)
        output_file.write(new_line)


def encode(args):
    with CleverOpenFile(args.input_file, "r") as input_file:
        with CleverOpenFile(args.output_file, "w") as output_file:
            if args.cipher == 'caesar':
                encode_file(input_file, output_file, int(args.key), caesar)
            elif args.cipher == 'vigenere':
                encode_file(input_file, output_file, args.key, vigenere)

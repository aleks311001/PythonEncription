from help_lib import SYMBOL_TO_IND, CleverOpenFile, move_symbol


def transform_caesar_char(char, key):
    if char in SYMBOL_TO_IND:
        return move_symbol(char, key)
    else:
        return char


def caesar(line, key):
    return "".join(transform_caesar_char(char, key) for char in line)


def transform_vigenere_char(char, index_char, key):
    if char in SYMBOL_TO_IND:
        index_key_in_list_all_symbols = SYMBOL_TO_IND[key[index_char % len(key)]]

        return move_symbol(char, index_key_in_list_all_symbols)
    else:
        return char


def vigenere(line, key):
    return "".join(transform_vigenere_char(char, index_char, key) for index_char, char in enumerate(line))


def encode_file(input_file, output_file, key, func_for_encode):
    for line in input_file:
        new_line = func_for_encode(line, key)
        output_file.write(new_line)


def encode(args):
    with CleverOpenFile(args.input_file, "r") as input_file, CleverOpenFile(args.output_file, "w") as output_file:
        if args.cipher == 'caesar':
            encode_file(input_file, output_file, int(args.key), caesar)
        elif args.cipher == 'vigenere':
            encode_file(input_file, output_file, args.key, vigenere)
        else:
            raise ValueError

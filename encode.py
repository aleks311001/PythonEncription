from help_lib import SYMBOL_TO_IND, CleverOpenFile, move_symbol


def transform_caesar_char(char, key, index_char):
    if char in SYMBOL_TO_IND:
        return move_symbol(char, key)
    else:
        return char

def transform_vigenere_char(char, key, index_char):
    if char in SYMBOL_TO_IND:
        index_key_in_list_all_symbols = SYMBOL_TO_IND[key[index_char % len(key)]]

        return move_symbol(char, index_key_in_list_all_symbols)
    else:
        return char


def encrypt(transform_char, line, key):
    return "".join(transform_char(char, key, index_char) for index_char, char in enumerate(line))


def encode_file(input_file, output_file, key, func_for_encode_char):
    for line in input_file:
        new_line = encrypt(func_for_encode_char, line, key)
        output_file.write(new_line)


def encode(args):
    with CleverOpenFile(args.input_file, "r") as input_file, CleverOpenFile(args.output_file, "w") as output_file:
        if args.cipher == 'caesar':
            encode_file(input_file, output_file, int(args.key), transform_caesar_char)
        elif args.cipher == 'vigenere':
            encode_file(input_file, output_file, args.key, transform_vigenere_char)
        else:
            raise ValueError("invalid cipher")

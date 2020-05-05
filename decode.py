from help_lib import STR_ALL_SYMBOLS, SYMBOL_TO_IND, LEN_ALL_SYMBOLS, CleverOpenFile
import encode


def made_inverse_key(key):
    return "".join(STR_ALL_SYMBOLS[-SYMBOL_TO_IND[char] % LEN_ALL_SYMBOLS] for char in key)


def decode(args):
    with CleverOpenFile(args.input_file, "r") as input_file, CleverOpenFile(args.output_file, "w") as output_file:
        if args.cipher == 'caesar':
            encode.encode_file(input_file, output_file, -int(args.key), encode.transform_caesar_char)
        elif args.cipher == 'vigenere':
            key = made_inverse_key(args.key)
            encode.encode_file(input_file, output_file, key, encode.transform_vigenere_char)

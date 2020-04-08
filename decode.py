import help_lib
import encode


def made_inverse_key(key):
    result = ''
    for char in key:
        result += help_lib.all_symbols[help_lib.len_all_symbols - help_lib.dict_symbols[char]]
    return result


def decode(args):
    print(help_lib.len_all_symbols)
    input_file = help_lib.clever_open(args.input_file, "r")
    output_file = help_lib.clever_open(args.output_file, "w")

    if args.cipher == 'caesar':
        encode.encode_file(input_file, output_file, -int(args.key), encode.caesar)
    elif args.cipher == 'vigenere':
        key = made_inverse_key(args.key)
        encode.encode_file(input_file, output_file, key, encode.vigenere)

    input_file.close()
    output_file.close()

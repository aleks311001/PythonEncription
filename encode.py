import help_lib


def caesar(line, key):
    result = ''
    for char in line:
        if char in help_lib.all_symbols:
            index = (help_lib.dict_symbols[char] + key) % help_lib.len_all_symbols
            result += help_lib.all_symbols[index]
        else:
            result += char
    return result


def vigenere(line, key):
    result = ''
    for i in range(len(line)):
        if line[i] in help_lib.all_symbols:
            index_line = help_lib.dict_symbols[line[i]]
            index_key = help_lib.dict_symbols[key[i % len(key)]]
            index = (index_line + index_key) % help_lib.len_all_symbols

            result += help_lib.all_symbols[index]
        else:
            result += line[i]
    return result


def encode_file(input_file, output_file, key, func_for_encode):
    for line in input_file:
        new_line = func_for_encode(line, key)
        output_file.write(new_line)


def encode(args):
    input_file = help_lib.clever_open(args.input_file, "r")
    output_file = help_lib.clever_open(args.output_file, "w")

    if args.cipher == 'caesar':
        encode_file(input_file, output_file, int(args.key), caesar)
    elif args.cipher == 'vigenere':
        encode_file(input_file, output_file, str(args.key), vigenere)

    input_file.close()
    output_file.close()

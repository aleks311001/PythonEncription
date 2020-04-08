import json
import help_lib


def calc_chars_in_str(dict_prob, strings):
    strings = strings
    for char in strings:
        if char in help_lib.all_symbols:
            dict_prob[char] += 1


def make_probability_from_numbers(dict_prob):
    summary = 0
    for num in dict_prob.values():
        summary += num

    for char in dict_prob.keys():
        dict_prob[char] /= summary


def calc_probability(args):
    dict_prob = dict()
    for char in help_lib.all_symbols:
        dict_prob[char] = 0

    with open(args.input_file, 'r') as file:
        for strings in file:
            calc_chars_in_str(dict_prob, strings)

    make_probability_from_numbers(dict_prob)
    with open(args.output_file, 'w') as file:
        json.dump(dict_prob, file, indent=4)

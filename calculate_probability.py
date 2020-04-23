import json
from help_lib import SET_ALL_SYMBOLS
from collections import defaultdict


def calc_only_correct_chars_in_line(dict_prob, strings):
    strings = strings
    for char in strings:
        if char in SET_ALL_SYMBOLS:
            dict_prob[char] += 1


def make_normalize_counts(dict_prob):
    num_all_chars_in_dict = sum(dict_prob.values())

    for char in dict_prob.keys():
        dict_prob[char] /= num_all_chars_in_dict


def calc_probability(args):
    dict_prob = defaultdict(float)

    with open(args.input_file, 'r') as file:
        for line in file:
            calc_only_correct_chars_in_line(dict_prob, line)

    make_normalize_counts(dict_prob)
    with open(args.output_file, 'w') as file:
        json.dump(dict_prob, file, indent=4)

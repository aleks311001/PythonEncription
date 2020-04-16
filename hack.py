import json
from help_lib import SET_ALL_SYMBOLS, LEN_ALL_SYMBOLS
from collections import defaultdict
import encode
import calculate_probability


def find_probability(input_file, key):
    dict_prob = defaultdict()
    for char in SET_ALL_SYMBOLS:
        dict_prob[char] = 0

    with open(input_file, 'r') as file:
        for strings in file:
            calculate_probability.calc_only_correct_chars_in_line(dict_prob, encode.caesar(strings, key))

    calculate_probability.make_normalize_counts(dict_prob)
    return dict_prob


def distance(real_prob, test_prob):
    dist = 0
    for coordinate_name in set(real_prob.keys()) | set(test_prob.keys()):
        dist += (real_prob[coordinate_name] - test_prob[coordinate_name]) ** 2
    return dist


def hack(args):
    with open(args.probability_file, 'r') as file:
        real_probability = defaultdict(float, json.load(file))

    min_dist = distance(real_probability, find_probability(args.input_file, 0))
    min_key = 0

    for key in range(1, LEN_ALL_SYMBOLS):
        dist = distance(real_probability, find_probability(args.input_file, key))
        if dist < min_dist:
            min_dist = dist
            min_key = key

    with open(args.input_file, 'r') as input_file, open(args.output_file, 'w') as output_file:
        encode.encode_file(input_file, output_file, min_key, encode.caesar)

import json
import math

from help_lib import LEN_ALL_SYMBOLS, move_symbol
from collections import defaultdict
import encode
import calculate_probability


def find_probability(input_file):
    dict_prob = defaultdict(float)

    with open(input_file, 'r') as file:
        for line in file:
            calculate_probability.calc_only_correct_chars_in_line(dict_prob, line)

    calculate_probability.make_normalize_counts(dict_prob)
    return dict_prob


def distance(real_prob, our_prob, key):
    dist = 0
    for coordinate_name in set(real_prob.keys()) | set(our_prob.keys()):
        coordinate_our_symbol = move_symbol(coordinate_name, key)
        dist += (real_prob.get(coordinate_name, 0) - our_prob.get(coordinate_our_symbol, 0)) ** 2
    return dist


def hack(args):
    with open(args.probability_file, 'r') as file:
        real_probability = json.load(file)

    our_probability = find_probability(args.input_file)

    min_dist = math.inf
    min_key = None

    for key in range(LEN_ALL_SYMBOLS):
        dist = distance(real_probability, our_probability, -key)
        if dist < min_dist:
            min_dist = dist
            min_key = key

    with open(args.input_file, 'r') as input_file, open(args.output_file, 'w') as output_file:
        encode.encode_file(input_file, output_file, min_key, encode.transform_caesar_char)

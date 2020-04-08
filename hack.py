import json
import help_lib
import encode
import calculate_probability


def find_probability(input_file, key):
    dict_prob = dict()
    for char in help_lib.all_symbols:
        dict_prob[char] = 0

    with open(input_file, 'r') as file:
        for strings in file:
            calculate_probability.calc_chars_in_str(dict_prob, encode.caesar(strings, key))

    calculate_probability.make_probability_from_numbers(dict_prob)
    return dict_prob


def distance(real_prob, test_prob):
    dist = 0
    for key in real_prob.keys():
        dist += (real_prob[key] - test_prob[key]) * (real_prob[key] - test_prob[key])
    return dist


def hack(args):
    with open(args.probability_file, 'r') as file:
        real_probability = json.load(file)

    min_dist = distance(real_probability, find_probability(args.input_file, 0))
    min_key = 0

    for key in range(1, help_lib.len_all_symbols):
        dist = distance(real_probability, find_probability(args.input_file, key))
        if dist < min_dist:
            min_dist = dist
            min_key = key

    input_file = open(args.input_file, 'r')
    output_file = open(args.output_file, 'w')

    encode.encode_file(input_file, output_file, min_key, encode.caesar)

    input_file.close()
    output_file.close()


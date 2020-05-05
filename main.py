import argparse
import calculate_probability
import encode
import decode
import hack


def main():
    parser = argparse.ArgumentParser(description='In this program, you can encode, decode, hack texts,\
                                                  and calculate the probability of the chars in text')
    subparsers = parser.add_subparsers()

    encode_parser = subparsers.add_parser('encode', help='Encode input text with the specified cipher')
    encode_parser.add_argument('--input_file', help="Enter file for encode")
    encode_parser.add_argument('--output_file', help="Enter file for save encode")
    encode_parser.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'],
                               help="Enter type of cipher for encode")
    encode_parser.add_argument('--key', required=True, help="Enter a number for caesar or text for vigenere")
    encode_parser.set_defaults(func=encode.encode)

    decode_parser = subparsers.add_parser('decode', help='Decode input text with the specified cipher')
    decode_parser.add_argument('--input_file', help="Enter file for decode")
    decode_parser.add_argument('--output_file', help="Enter file for save decode")
    decode_parser.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'],
                               help="Enter type of cipher for decode")
    decode_parser.add_argument('--key', required=True, help="Enter a number for caesar or text for vigenere")
    decode_parser.set_defaults(func=decode.decode)

    probability_parser = subparsers.add_parser('probability', help='Calculate probability chars')
    probability_parser.add_argument('--input_file', required=True, help="Enter file for calculate probability")
    probability_parser.add_argument('--output_file', required=True, help="Enter .json file for save probability")
    probability_parser.set_defaults(func=calculate_probability.calc_probability)

    hack_parser = subparsers.add_parser('hack', help="Hacking caesar cipher")
    hack_parser.add_argument('--input_file', help="Enter file for hack")
    hack_parser.add_argument('--output_file', help="Enter file for save")
    hack_parser.add_argument('--probability_file', required=True,
                             help="Enter .json file with probabilities, use 'probability' for create this file")
    hack_parser.set_defaults(func=hack.hack)

    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)


if __name__ == '__main__':
    main()

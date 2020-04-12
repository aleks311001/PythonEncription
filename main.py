import argparse
import calculate_probability
import encode
import decode
import hack


def main():
    parser = argparse.ArgumentParser(description='In this program, you can encode, decode, hack texts,\
                                                  and calculate the probability of the chars in text')
    subparsers = parser.add_subparsers()

    encode_parser = subparsers.add_parser('encode', help='encode input text with the specified cipher')
    encode_parser.add_argument('--input_file')
    encode_parser.add_argument('--output_file')
    encode_parser.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
    encode_parser.add_argument('--key', required=True)
    encode_parser.set_defaults(func=encode.encode)

    decode_parser = subparsers.add_parser('decode', help='decode input text with the specified cipher')
    decode_parser.add_argument('--input_file')
    decode_parser.add_argument('--output_file')
    decode_parser.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
    decode_parser.add_argument('--key', required=True)
    decode_parser.set_defaults(func=decode.decode)

    probability_parser = subparsers.add_parser('probability', help='calculate probability chars')
    probability_parser.add_argument('--input_file', required=True)
    probability_parser.add_argument('--output_file', required=True)
    probability_parser.set_defaults(func=calculate_probability.calc_probability)

    hack_parser = subparsers.add_parser('hack', help="hacking caesar cipher")
    hack_parser.add_argument('--input_file')
    hack_parser.add_argument('--output_file')
    hack_parser.add_argument('--probability_file', required=True)
    hack_parser.set_defaults(func=hack.hack)

    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)


main()

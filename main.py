import argparse
import calculate_probability
import encode
import decode
import hack


def main():
    parser = argparse.ArgumentParser(description='What do you want?')
    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='description')

    encode_parser = subparsers.add_parser('encode', help='encode')
    encode_parser.add_argument('--input_file', dest='input_file', default=None)
    encode_parser.add_argument('--output_file', dest='output_file', default=None)
    encode_parser.add_argument('--cipher', dest='cipher', required=True,
                               choices=['caesar', 'vigenere'])
    encode_parser.add_argument('--key', dest='key', required=True)
    encode_parser.set_defaults(func=encode.encode)

    decode_parser = subparsers.add_parser('decode', help='decode')
    decode_parser.add_argument('--input_file', dest='input_file', default=None)
    decode_parser.add_argument('--output_file', dest='output_file', default=None)
    decode_parser.add_argument('--cipher', dest='cipher', required=True,
                               choices=['caesar', 'vigenere'])
    decode_parser.add_argument('--key', dest='key', required=True)
    decode_parser.set_defaults(func=decode.decode)

    probability_parser = subparsers.add_parser('probability', help='calculate probability chars')
    probability_parser.add_argument('--input_file', dest='input_file', required=True)
    probability_parser.add_argument('--output_file', dest='output_file', required=True)
    probability_parser.set_defaults(func=calculate_probability.calc_probability)

    hack_parser = subparsers.add_parser('hack', help="hacking caesar cipher")
    hack_parser.add_argument('--input_file', dest='input_file', default=None)
    hack_parser.add_argument('--output_file', dest='output_file', default=None)
    hack_parser.add_argument('--probability_file', dest='probability_file', required=True)
    hack_parser.set_defaults(func=hack.hack)

    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)


main()

# python3 main.py encode --input_file test_read.txt --output_file code_file.txt --cipher caesar --key 10
# python3 main.py decode --input_file code_file.txt --output_file decode_file.txt --cipher caesar --key 10
# python3 main.py hack --input_file code_file.txt --output_file hack_file.txt --probability_file probability.json
# python3 main.py probability --input_file test_read.txt --output_file probability.json

# python3 main.py encode --input_file russian_for_encode.txt --output_file russian_encode.txt --cipher caesar --key 10
# python3 main.py decode --input_file russian_encode.txt --output_file russian_decode.txt --cipher caesar --key 10
# python3 main.py hack --input_file russian_encode.txt --output_file russian_hack.txt --probability_file russian_probability.json
# python3 main.py probability --input_file russian_file_for_prob.txt --output_file russian_probability.json

# python3 main.py encode --input_file russian_for_encode.txt --output_file russian_encode_vigenere.txt --cipher vigenere --key боба
# python3 main.py decode --input_file russian_encode_vigenere.txt --output_file russian_decode_vigenere.txt --cipher vigenere --key боба

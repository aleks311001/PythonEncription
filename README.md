Examples of commands to run the code:

1) python3 main.py encode --input_file test_read.txt --output_file code_file.txt --cipher caesar --key 10
2) python3 main.py decode --input_file code_file.txt --output_file decode_file.txt --cipher caesar --key 10
3) python3 main.py probability --input_file test_read.txt --output_file probability.json
4) python3 main.py hack --input_file code_file.txt --output_file hack_file.txt --probability_file probability.json

5) python3 main.py probability --input_file russian_file_for_prob.txt --output_file russian_probability.json
6) python3 main.py encode --input_file russian_for_encode.txt --output_file russian_encode.txt --cipher caesar --key 10
7) python3 main.py decode --input_file russian_encode.txt --output_file russian_decode.txt --cipher caesar --key 10
8) python3 main.py hack --input_file russian_encode.txt --output_file russian_hack.txt --probability_file russian_probability.json

9) python3 main.py encode --input_file russian_for_encode.txt --output_file russian_encode_vigenere.txt --cipher vigenere --key secret
10) python3 main.py decode --input_file russian_encode_vigenere.txt --output_file russian_decode_vigenere.txt --cipher vigenere --key secret

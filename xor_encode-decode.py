# a program that has an encode mode and a decode mode, can translate either through an XOR Cipher
def introchoose():
    mode = input("Welcome to the XOR Encoder/Decoder! Please select a mode (encode/decode): ")
    if mode == "encode":
        return 1
    elif mode == "decode":
        return 2
    else:
        print("invalid choice, please try again.")
        return introchoose()
mode = introchoose()
if mode == 1:
    input_string = input("Enter a string to be encoded: ")
    key_string = input("Enter a key to use to encode: ")
    input_ascii = [ord(char) for char in input_string]
    key_ascii = [ord(char) for char in key_string]
    encoded_list_ascii = []
    encoded_list_char = []
    for i in range(len(input_ascii)):
        encoded_char = int(input_ascii[i]) ^ int(key_ascii[i % len(key_ascii)])
        encoded_list_ascii.append(encoded_char)
    for i in range(len(encoded_list_ascii)):
        encoded_list_char.append(chr(encoded_list_ascii[i]))
    print("Encoded output (as ASCII values): ", encoded_list_ascii)
    print("Encoded output (as characters): ", encoded_list_char)
elif mode == 2:
    input_ascii_str = input("Enter a list of ASCII values to be decoded (separated by spaces): ")
    input_ascii = [int(num) for num in input_ascii_str.split()]
    key_string = input("Enter the key that was used to encode: ")
    key_ascii = [ord(char) for char in key_string]
    decoded_list_ascii = []
    decoded_list_char = []
    for i in range(len(input_ascii)):
        decoded_char = int(input_ascii[i]) ^ int(key_ascii[i % len(key_ascii)])
        decoded_list_ascii.append(decoded_char)
    for i in range(len(decoded_list_ascii)):
        decoded_list_char.append(chr(decoded_list_ascii[i]))
    print("Decoded output (as ASCII values): ", decoded_list_ascii)
    print("Decoded output (as characters): ", decoded_list_char)
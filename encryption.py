import random

def codification(input_message, encryption_key):
    encoded_message = ''
    random.seed(encryption_key)
    int(encryption_key)

    for character in input_message:
        dislocation = random.randint(1, 100)
        code = ord(character)
        new_code = code + dislocation
        encoded_message += chr(new_code)
    return encoded_message

def decodification(input_coded_message, decryption_key):
    decoded_result = ''
    random.seed(decryption_key)
    int(decryption_key)

    for character in input_coded_message:
        dislocation_decoded = random.randint(1, 100)
        code = ord(character)
        new_code = code - dislocation_decoded
        decoded_result += chr(new_code)
    return decoded_result

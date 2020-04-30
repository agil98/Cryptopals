import binascii

def decode(ciphertext):
    strings = []
    for char_value in range(65, 122):
        decoded = ''.join(chr(b ^ char_value) for b in ciphertext)
        if decoded.isprintable():
            strings.append(decoded)
    return strings
    
def main():
    hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ciphertext = binascii.unhexlify(hex_str)
    possible_strings = decode(ciphertext)
    sum = 0
    max = 0
    message = ''
    for s in possible_strings:
        sum = s.count(' ')
        if sum > max:
            max = sum
            message = s

    print(message)

if __name__ == '__main__':
    main()

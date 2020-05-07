import binascii

def decode(ciphertext):
    strings = []
    for char_value in range(0, 122):
        decoded = ''.join(chr(b ^ char_value) for b in ciphertext)
        decoded = decoded.strip('\n')
        if all(i.isalpha() or i.isspace() for i in decoded):
            strings.append(decoded)
    return strings
    
def main():
    total = 0
    max = 0
    message = ''

    char_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074
    }

    with open('input.txt', 'r') as fp:
        for line in fp:
            enconded_str =  line.strip()
            ciphertext = binascii.unhexlify(enconded_str)
            possible_strings = decode(ciphertext)
            for string in possible_strings:
                total = sum(char_frequencies.get(s.lower(), 0) for s in string)
                if total > max:
                    max = total
                    message = string
    print("score: ", max, "\n\message: ", message)

if __name__ == '__main__':
    main()

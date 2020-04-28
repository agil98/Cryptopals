def hex_xor(s1, s2):
  return hex(int(s1, 16) ^ int(s2, 16))

def main():
    hex_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")


if __name__ == '__main__':
    main()

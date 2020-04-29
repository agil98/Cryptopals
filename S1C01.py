import codecs

def hex_to_base64(s):
  return codecs.encode(codecs.decode(s, 'hex'), 'base64').decode()

def main():
    print(hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))


if __name__ == '__main__':
    main()
    

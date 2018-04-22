import sys
from cs50 import get_string
import string


def main():
    if len(sys.argv) == 2:
        k = sys.argv[1]
        if k.isalpha():
            plain_text = get_string("plaintext: ")
            s = cipher(plain_text,k)
            print(f"ciphertext:",end=" ")
            print(s)
        else:
            print("Usage: ./vigenere k")
            exit(1)
    else:
        print("Usage: ./vigenere k")
        exit(1)


def cipher(text, key):
    ciphered = ""
    n = len(text)
    k = len(key)
    offset = 0
    value = 0
    for i in range(n):
        if not((text[i] >= 'a' and text[i] <= 'z') or (text[i] >= 'A' and text[i] <= 'Z'))  :
            ciphered = ciphered + text[i]
        else:
            #print(f"{text[i]}", end=" ")
            char = key[offset]
            if char >= 'a' and char <= 'z':
                value = ord(char) - 97
            elif char >= 'A' and char <= 'Z':
                value = ord(char) - 65
            #print(f"{char}", end=" ")
            offset = offset + 1
            if offset == k:
                offset = 0
            if text[i] >= 'a' and text[i] <= 'z':
                #print(f"{value}", end=" ")
                new_char_value = ord(text[i]) + value
                #print(f"{new_char_value}", end=" ")
                if new_char_value > 122:
                    new_char_value = new_char_value - 26
                    #print(f"{new_char_value}", end=" ")
            elif text[i] >= 'A' and text[i] <= 'Z':
                #print(f"{value}", end=" ")
                new_char_value = ord(text[i]) + value
                #print(f"{new_char_value}", end=" ")
                if new_char_value > 90:
                    new_char_value = new_char_value - 26
                    #print(f"{new_char_value}", end=" ")
            new_char = chr(int(new_char_value))
            ciphered = ciphered + new_char
            #print(ciphered)
    return ciphered


if __name__ == "__main__":
    main()

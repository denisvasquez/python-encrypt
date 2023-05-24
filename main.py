from tk import *
import json

with open("./keys.json", "r") as f:
    keys = json.load(f)

def pass_to_ascii(text):
    ascii_values = [ord(char) for char in text]
    return ascii_values;

def encrypt(secuency_ascii, key, times, i):
    exp_private = key["exp_private"]
    public = key["public"]
    if i == times:
        return;

    i = i + 1

    text_encripted = [(item**exp_private) % public for item in secuency_ascii]
    encrypt(text_encripted, key, times, i)

    return text_encripted

def decoded(secuency_encrypted, keys):
    public, private = keys

    text_normal = [(item**private) % public for item in secuency_encrypted]

    return text_normal

def main():
    text = str(input("Insert the text to encript: "))
    key = int(input("Insert the key (1-3): ")) 
    times = int(input("Insert the times: "))
    if (key > 3 and key < 1):
        print("Invalid key")
        return

    encripted = encrypt(pass_to_ascii(text), keys[str(key)], times, 0)

    print("original: ", pass_to_ascii(text))
    print("encypted: ", encripted)
    

if __name__ == "__main__":
    main()
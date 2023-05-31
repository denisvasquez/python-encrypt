import json

with open("./keys.json", "r") as f:
        keys = json.load(f)

def pass_to_ascii(text):
    ascii_values = [ord(char) for char in text]
    return ascii_values;

def encode(array, key, times):
    exp_private = keys[key]["exp_private"]
    public = keys[key]["public"]

    if times == 0:
        return array;

    array = [(item**exp_private) % public for item in array]

    return encode(array, key, times-1)

def decode(secuency_encrypted, key, times, i = 0):
    private = keys[key]["private"]
    public = keys[key]["public"]

    i = i + 1

    text_normal = [(item**private) % public for item in secuency_encrypted]

    decode(text_normal, key, times, i)

    return text_normal


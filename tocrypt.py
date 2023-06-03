import json
import string, random
with open("./keys.json", "r") as f:
    keys = json.load(f)

def pass_to_ascii(text):
    ascii_values = [ord(char) for char in text]
    return ascii_values;

def encode(array, key, times):
    exp_private = keys[key]["exp_private"]
    public = keys[key]["public"]

    if times <= 1:
        _a = ""
        for char in array:
            rand = random.choice(string. ascii_letters)
            _a += str(char)+rand
        return _a[::-1]

    array = [(item**exp_private) % public for item in array]

    return encode(array, key, times-1)

def decode(array, key, times):
    private = keys[key]["private"]
    public = keys[key]["public"]

    if times <= 1:
        return array

    array = [(item**private) % public for item in array]

    return decode(array, key, times-1)

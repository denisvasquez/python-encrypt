import json

class to_crypt:
    def __init__(self):
        with open("./keys.json", "r") as f:
            self.keys = json.load(f)

    def pass_to_ascii(self, text):
        ascii_values = [ord(char) for char in text]
        return ascii_values;

    def encode(self, text, key, times, i = 0):
        secuency_ascii = self.pass_to_ascii(text)
        exp_private = self.keys[key]["exp_private"]
        public = self.keys[key]["public"]

        if i == times:
            return;

        i = i + 1

        text_encripted = [(item**exp_private) % public for item in secuency_ascii]
        self.encode(text_encripted, key, times, i)

        print(text_encripted)

        return text_encripted

    def decode(self, secuency_encrypted, key):
        private = self.keys[key]["private"]
        public = self.keys[key]["public"]

        text_normal = [(item**private) % public for item in secuency_encrypted]

        return text_normal


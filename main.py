import tkinter as tk
from tkinter import ttk
from tocrypt import encode, decode, pass_to_ascii

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Encriptador de texto") 
        self.master.resizable(False, False)
        self.buttons()
        self.labels()
        self.inputs();
        self.table()
    
    def buttons(self):
        self.btn = ttk.Button(self.master, text="Encriptar", command=lambda: self.encrypt(
            self.text_to_encrypt.get(),
            self.times_to_encrypt.get(),
            self.key_selected.get()
        ), width=50)
        self.btn.grid(row=4, column=2, sticky="w")
    
    def inputs(self):
        self.text_to_encrypt = ttk.Entry(self.master, width=50)
        self.times_to_encrypt = ttk.Entry(self.master, width=50)
        self.key_selected = ttk.Entry(self.master, width=50)

        self.text_to_encrypt.grid(row=1, column=2, pady=6)
        self.times_to_encrypt.grid(row=2, column=2, pady=6)
        self.key_selected.grid(row=3, column=2, pady=6)
    
    def labels(self):
        lbl_to_encrypt = ttk.Label(self.master, text="Texto a encriptar:")
        lbl_times = ttk.Label(self.master, text="Veces a encriptar:")
        lbl_keys = ttk.Label(self.master, text="Juego de llaves (1, 2, 3):")

        lbl_to_encrypt.grid(row=1, column=0)
        lbl_times.grid(row=2, column=0)
        lbl_keys.grid(row=3, column=0)
    
    def encrypt(self, text, times, key):
        if (text == "" or times == ""):
            print("Alguno de los campos estan vacios")
            return
        
        try:
            key = int(key)
            if (int(key) > 3 or int(key) < 1):
                print("La llave seleccionada no es valida")
                return
            try:
                times = int(times)
            except ValueError:
                print("NO SE PUEDE INGRESAR LETRAS EN EL NUMERO DE VECES")
                return
        except ValueError:
            print("NO SE PUEDE INGRESAR LETRAS EN EL JUEGO DE LLAVES")
            return

        encrypted = encode(pass_to_ascii(text), str(key), times)        
        datos = {
            "encrypted": encrypted,
            "times": times,
            "key": key
        }
        print(datos)

    def table(self):
        pass

if __name__ == "__main__":
    window = master = tk.Tk()
    app = App(window)
    window.mainloop()
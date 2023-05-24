import tocrypt
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.encryptor = tocrypt
        self.master = master
        self.master.title("Encriptador de texto") 
        self.buttons()
        self.labels()
        self.inputs();
        self.table()
        self.check_radios()
    
    def check_radios(self):
        self.radio1 = ttk.Radiobutton(self.master, text="Juego de llaves 1", value="1")
        self.radio2 = ttk.Radiobutton(self.master, text="Juego de llaves 2", value="2")
        self.radio3 = ttk.Radiobutton(self.master, text="Juego de llaves 3", value="3")

        self.radio1.grid(row=0, column=0)
        self.radio2.grid(row=0, column=1)
        self.radio3.grid(row=0, column=2)

    def buttons(self):
        self.btn = ttk.Button(self.master, text="Encriptar", command=lambda: self.encrypt(
            self.text_to_encrypt.get(),
            self.times_to_encrypt.get()
        ))
        self.btn.grid(row=3, column=2)
    
    def inputs(self):
        self.text_to_encrypt = ttk.Entry(self.master)
        self.times_to_encrypt = ttk.Entry(self.master)

        self.times_to_encrypt.grid(row=2, column=2)
        self.text_to_encrypt.grid(row=1, column=2)
    
    def labels(self):
        lbl_to_encrypt = ttk.Label(self.master, text="Texto a encriptar:")
        lbl_times = ttk.Label(self.master, text="Veces a encriptar:")

        lbl_to_encrypt.grid(row=1, column=0)
        lbl_times.grid(row=2, column=0)
    
    def encrypt(self, text, times):
        if (text == "" or times == ""):
            print("Alguno de los campos estan vacios")
            return
        
        try:
            if (int(times) > 3 or int(times) < 1):
                print("La llave seleccionada no es valida")
                return
        except ValueError:
            print("NO SE PUEDE INGRESAR LETRAS EN EL NUMERO DE VECES")
            return

        print("Informacion: ", text, times)

    def table(self):
        pass

# def main():
#     text = str(input("Insert the text to encript: "))
#     key = int(input("Insert the key (1-3): ")) 
#     times = int(input("Insert the times: "))
#     if (key > 3 and key < 1):
#         print("Invalid key")
#         return

#     encripted = encrypt(pass_to_ascii(text), keys[str(key)], times, 0)

#     print("original: ", pass_to_ascii(text))
#     print("encypted: ", encripted)

if __name__ == "__main__":
    window = master = tk.Tk()
    app = App(window)
    window.mainloop()
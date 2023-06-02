import tkinter as tk
from tkinter import ttk, Toplevel, StringVar, DISABLED
from tocrypt import encode, decode, pass_to_ascii

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Encriptador de texto") 
        self.master.resizable(False, False)
        self.buttons()
        self.labels()
        self.inputs()
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
        print("encripted", encrypted)
        datos = (
            encrypted,
            times,
            key
        )
        self.tree.insert("", tk.END, values=datos) 

    def table_item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item["values"]
            self.tmp = Toplevel(self.master)
            decoded = ""
            for char in decode([int(item) for item in str(record[0]).split(" ")], str(record[2]), record[1]):
                decoded += chr(char)

            self.LblTmp1 = ttk.Label(self.tmp, text="Texto desencriptado: ")
            self.LblTmp2 = ttk.Label(self.tmp, text="Numero de veces que se encripto: ")
            self.LblTmp3 = ttk.Label(self.tmp, text="Juego de llaves usado: ")
            self.LblTmp1.grid(row=0, column=0)
            self.LblTmp2.grid(row=1, column=0)
            self.LblTmp3.grid(row=2, column=0)

            tk.Entry(self.tmp, textvariable=StringVar(self.tmp, value=decoded), state='readonly').grid(row=0, column=1)
            tk.Entry(self.tmp, textvariable=StringVar(self.tmp, value=str(record[1])), state='readonly').grid(row=1, column=1)
            tk.Entry(self.tmp, textvariable=StringVar(self.tmp, value=str(record[2])), state='readonly').grid(row=2, column=1)

            print("decoded", decoded)

    def table(self):
        columns = ("Encriptado", "Encripciones", "Llave")

        self.tree = ttk.Treeview(self.master, columns=columns, show="headings")
        self.tree.heading("Encriptado", text="Encriptado")
        self.tree.heading("Encripciones", text="Encripciones")
        self.tree.heading("Llave", text="Llave")

        scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=5, column=3, sticky='ns')

        self.tree.bind('<<TreeviewSelect>>', self.table_item_selected)

        self.tree.grid(row=5, column=0, columnspan=3)

if __name__ == "__main__":
    window = master = tk.Tk()
    app = App(window)
    window.mainloop()

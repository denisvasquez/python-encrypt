import tkinter as tk
from tkinter import ttk, Toplevel, StringVar, END
from tocrypt import encode, decode, pass_to_ascii

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Encriptador de texto") 
        self.master.resizable(False, False)
        self.encryptions = []
        self.buttons()
        self.labels()
        self.inputs()
        self.table()
        self.insert_items()
    
    def buttons(self):
        ttk.Button(self.master, text="Encriptar", command=lambda: self.encrypt(
            self.text_to_encrypt.get(),
            self.times_to_encrypt.get(),
            self.key_selected.get()
        ), width=50).grid(row=4, column=2)

        # Eliminar de la tabla
        ttk.Button(self.master, text="Eliminar", command=self.delete_item,width=50).grid(row=5, column=2)

    def insert_items(self):
        records = self.tree.get_children()
        for item in records:
            self.tree.delete(item)
        
        for _, item in enumerate(self.encryptions):
            item = (item + (_,))
            self.tree.insert('', 'end', text = item[0], values=item)
    
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

        self.alert = ttk.Label(self.master, text="")
        self.alert.grid(row=6, column=0, columnspan=4)

        lbl_to_encrypt.grid(row=1, column=0)
        lbl_times.grid(row=2, column=0)
        lbl_keys.grid(row=3, column=0)
    
    def encrypt(self, text, times, key):
        self.alert["text"] = ""
        if (text == "" or times == ""):
            self.alert["text"] = "Alguno de los campos estan vacios"
            return
        
        try:
            key = int(key)
            if (int(key) > 3 or int(key) < 1):
                self.alert["text"] = "La llave seleccionada no es valida"
            try:
                times = int(times)
            except ValueError:
                self.alert["text"] = "NO SE PUEDE INGRESAR LETRAS EN EL NUMERO DE VECES"
                return
        except ValueError:
            self.alert["text"] = "NO SE PUEDE INGRESAR LETRAS EN EL JUEGO DE LLAVES"
            return
                
        encrypted = encode(pass_to_ascii(text), str(key), times)

        self.encryptions.append(( 
            encrypted,
            text,
            times,
            key
        ))

        self.text_to_encrypt.delete(0, END)
        self.times_to_encrypt.delete(0, END)
        self.key_selected.delete(0, END)

        self.insert_items()

    def delete_item(self):
        self.alert["text"] = ""
        try:
            self.tree.item(self.tree.selection())["values"][4]
        except IndexError as e:
            return;
        
        index = self.tree.item(self.tree.selection())["values"][4]
        
        self.encryptions.pop(index)

        self.insert_items();
        

    def table(self):
        columns = ("Encriptado", "Desencriptado", "Encripciones", "Llave")

        self.tree = ttk.Treeview(self.master, columns=columns, show="headings")
        self.tree.heading("Encriptado", text="Encriptado")
        self.tree.heading("Desencriptado", text="Desencriptado")
        self.tree.heading("Encripciones", text="Encripciones")
        self.tree.heading("Llave", text="Llave")

        scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=7, column=3, sticky='ns')

        self.tree.grid(row=7, column=0, columnspan=3)

if __name__ == "__main__":
    window = master = tk.Tk()
    app = App(window)
    window.mainloop()

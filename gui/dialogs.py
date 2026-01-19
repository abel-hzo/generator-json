import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from pathlib import Path
from .colors import *
import shutil
import json
import os

class Dialogs:

    def __init__(self):
        self.lang = ""
        self.fileorigin = tk.StringVar()
        self.filetarget = tk.StringVar()
        self.maxwidth = tk.StringVar()

    def __save_dialog_code(self, parent, codepathstringvar):
        pathcode = filedialog.asksaveasfile(
            parent=parent,
            initialdir=os.getcwd(),
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
            title="Guardar archivo como"
        )
        
        if pathcode:
            try:
                object_path = Path(pathcode.name)
                self.lang = object_path.name.split(".")[1]

                content = self.codeText.get(1.0, 'end-1c')
                contentreplaced = content.replace("<", "&lt;").replace(">", "&gt;")

                if pathcode.name.startswith(os.getcwd()):
                    pathcoderelative = pathcode.name.replace(os.getcwd(), ".")
                    codepathstringvar.set(pathcoderelative)

                    with open(pathcode.name, 'w', encoding='utf-8') as f:
                        f.write(contentreplaced)
                    messagebox.showinfo("Éxito", f"Archivo guardado en: {pathcode.name}", parent=parent)
                    parent.destroy()
                else:
                    os.remove(pathcode.name)
                    messagebox.showerror("Error", "Elija un subdirectorio!!!", parent=parent)        
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}", parent=parent)

    def open_window_code(self, root, codepathstringvar):
        window_code = tk.Toplevel(root, background=medium_blue)
        window_code.title("Codigo")
        window_code.resizable(False, False)
        window_code.geometry("400x500")

        self.codeText = scrolledtext.ScrolledText(
            window_code,
            font=("Monospace", 10, "bold"),
            foreground="white",
            background=dark_blue,
            wrap="none",
            width=1,
            height=1
        )

        self.codeText.vbar.config(
            bg=dark_blue
        )

        self.codeText.pack(
            expand=True,
            fill="both"
        )
                    
        codepathButton = tk.Button(
            window_code,
            text="Guardar",
            background=dark_blue,
            font=("Verdana", 11, "bold"),
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            width=10,
            command=lambda: self.__save_dialog_code(window_code, codepathstringvar)
        )

        codepathButton.pack(
            side="right",
            ipadx=0,
            ipady=0
        )

        # Si el campo codigo no esta vacio y tiene una dirección entonces
        # cargar el achivo codigo que se encuentra en esa ruta.
        if codepathstringvar.get():
            try:
                path = codepathstringvar.get()
                object_path = Path(path)
                self.lang = object_path.name.split(".")[1]

                with open(codepathstringvar.get(), '+r', encoding='utf-8') as f:
                    content = f.read()
                    contentreplaced = content.replace("&lt;", "<").replace("&gt;", ">")
                    self.codeText.insert(tk.INSERT, contentreplaced)
                    
            except Exception as e:
                content = "ARCHIVO INVALIDO O NO EXISTENTE"
                self.codeText.insert(tk.INSERT, content)


    # Apartir de aqui desarrollamos toda la logica para abrir y guardar imagenes
    # desde los cuadros de dialogos llamados desde una ventana secundaria.

    def open_dialog_image(self, parent, widget):
        pathopenimage = filedialog.askopenfile(
            parent=parent,
            defaultextension=".png",
            filetypes=[("Imagenes", ".png"), ("Todos los archivos", "*.*")],
            title="Abrir imagen"
        )

        print(os.getcwd())

        if pathopenimage:
            widget.set(pathopenimage.name)

    def save_dialog_image(self, parent, widget):
        pathsaveimage = filedialog.asksaveasfile(
            parent=parent,
            initialdir=os.getcwd(),
            defaultextension=".png",
            filetypes=[("Archivos de imagen", "*.png"), ("Todos los archivos", "*.*")],
            title="Guardar archivo como"
        )

        if pathsaveimage and pathsaveimage.name.startswith(os.getcwd()):
            pathfinal = pathsaveimage.name.replace(os.getcwd(), ".")
            widget.set(pathfinal)
        else:
            if pathsaveimage:
                os.remove(pathsaveimage.name)
            messagebox.showerror("Error", f"Elija un subdirectorio para guardar el archivo!!!", parent=parent)      
            
    def copy_image(self, parent, widget):
        if self.fileorigin.get() and self.filetarget.get():
            shutil.copy(self.fileorigin.get(),
                        self.filetarget.get())
            widget.set(self.filetarget.get())
            messagebox.showinfo("Éxito", f"Archivo guardado en: {self.filetarget.get()}", parent=parent)   
        parent.destroy()

    def open_window_image(self, parent, imagesrc, components):
        window_image = tk.Toplevel(parent) 
        window_image.title("Cargar Imagen") 
        window_image.geometry("600x150")
        window_image.resizable(False, False)

        framecomponents = tk.Frame(
            window_image, 
            background=medium_blue, 
            padx=10, 
            pady=10
        )

        framecomponents.columnconfigure(0, weight=1, uniform="a")
        framecomponents.columnconfigure(1, weight=4, uniform="a")
        framecomponents.columnconfigure(2, weight=1, uniform="a")

        buttonopenimage = {"text": "Abrir", "width": 7, "func": lambda: self.open_dialog_image(window_image, self.fileorigin)}
        buttonsaveimage = {"text": "Guardar", "width": 7, "func": lambda: self.save_dialog_image(window_image, self.filetarget)}

        components.add_row(framecomponents, 0, "Origen", self.fileorigin, buttonopenimage, True)
        components.add_row(framecomponents, 1, "Destino", self.filetarget, buttonsaveimage, True)
        components.add_row(framecomponents, 2, "Tam. Max.", self.maxwidth, None, True)

        framecomponents.rowconfigure(3, weight=1)
        framebuttons = tk.Frame(framecomponents, background=medium_blue)

        tk.Button(
            framebuttons,
            text="Guardar",
            background=dark_blue,
            font=("Verdana", 11, "bold"),
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            width=7,
            command=lambda:self.copy_image(window_image, imagesrc)
        ).pack(
            side=tk.RIGHT
        )  

        framebuttons.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="nsew"
        ) 

        framecomponents.pack(fill="both", expand=True)

    def window_preview_json(self, parent, operations):
        window_preview = tk.Toplevel(parent)
        window_preview.title("Preview JSON")
        window_preview.geometry("400x500")
        window_preview.resizable(False, False)

        # --- FRAME DEL TEXTO ---
        frame_text = tk.Frame(window_preview)
        frame_text.pack(fill="both", expand=True)

        jsonText = tk.Text(
            frame_text,
            font=("Monospace", 10, "bold"),
            foreground="white",
            background=dark_blue,
            wrap="none",
            width=1,
            height=1
        )

        scrollbar_horizontal = tk.Scrollbar(
            frame_text,
            width=10,
            orient=tk.HORIZONTAL,
            background=dark_blue,
            command=jsonText.xview)
        
        scrollbar_vertical = tk.Scrollbar(
            frame_text,
            width=10, 
            orient=tk.VERTICAL,
            background=dark_blue,
            command=jsonText.yview)

        jsonText.configure(xscrollcommand=scrollbar_horizontal.set,
                           yscrollcommand=scrollbar_vertical.set)
        
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")

        jsonText.pack(
            expand=True,
            fill="both"
        )

        result_json = json.dumps(operations.build_json(), indent=4)
        jsonText.insert(1.0, result_json)
        jsonText.configure(state="disabled")

        # --- FRAME DE BOTONES ---
        frame_buttons = tk.Frame(window_preview, background=medium_blue)
        frame_buttons.pack(fill="x")

        tk.Button(
            frame_buttons,
            text="Cerrar",
            background=dark_blue,
            font=("Verdana", 11, "bold"),
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            width=10,
            command=window_preview.destroy
        ).pack(
            side="right",
            ipadx=0,
            ipady=0
        )
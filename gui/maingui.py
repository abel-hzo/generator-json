import tkinter as tk
from .components import Components
from .contentblock import ContentBlock
from .dialogs import Dialogs
from .colors import *
from services.operations import Operations

class MainGui():
    def __init__(self):
        root = tk.Tk()
        root.title("Generador de posts")
        root.geometry("900x700")
        root.resizable(False, False)
        root.config(background=ligth_blue, padx=10, pady=10)

        self.dialogs = Dialogs()
        components = Components()
        self.operations = Operations(self)
        self.contentblocks = []

        labelframe = tk.LabelFrame(
            root,
            text="Datos Post",
            padx=10, 
            pady=10, 
            background=medium_blue,
            foreground="black",
            font=("Monospace", 13, "bold")
        )

        labelframe.place(x=0, y=0, relwidth=1, height=200)

        # Definimos un grid
        labelframe.columnconfigure(0, weight=1, uniform="a")
        labelframe.columnconfigure(1, weight=4, uniform="a")
        labelframe.columnconfigure(2, weight=1, uniform="a")

        # Definimos los textvariable
        self.header_title = tk.StringVar()
        self.header_image = tk.StringVar()
        self.title = tk.StringVar()
        self.author = tk.StringVar()

        # Agregamos los campos al grid
        buttonconfig = {"text": "Abrir", "width": 12, "func": lambda : self.dialogs.open_window_image(root, self.header_image, components)}
        components.add_row(labelframe, 0, "Supertitulo", self.header_title, None, True)
        components.add_row(labelframe, 1, "Imagen", self.header_image, buttonconfig, True)
        components.add_row(labelframe, 2, "Titulo", self.title, None, True)
        components.add_row(labelframe, 3, "Autor", self.author, None, True)

        framebuttons = tk.Frame(
            root,
            height=70,
            background=ligth_blue
        )
        
        framebuttons.pack(
            side="bottom",
            fill="x"
        )

        tk.Button(
            master=framebuttons,
            text="Generar",
            background=dark_blue,
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            font=("Verdana", 11, "bold"),
            command=self.operations.export_json
        ).place(
            relx=1,
            rely=0.3,
            width=140,
            relheight=0.5,
            anchor="ne"
        )

        self.frameblocks = self.createCanvasContent(root)

        tk.Button(
            master=framebuttons,
            text="Agregar",
            background=dark_blue,
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            font=("Verdana", 11, "bold"),
            command=lambda: self.add_content(self.frameblocks)
        ).place(
            relx=0.8,
            rely=0.3,
            width=140,
            relheight=0.5,
            anchor="ne"
        )

        tk.Button(
            framebuttons,
            text="Cargar",
            background=dark_blue,
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            font=("Verdana", 11, "bold"),
            command=self.operations.load_json
        ).place(
            relx=0.6,
            rely=0.3,
            width=140,
            relheight=0.5,
            anchor="ne"
        )

        tk.Button(
            framebuttons,
            text="Visualizar",
            background=dark_blue,
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            font=("Verdana", 11, "bold"),
            command=lambda: self.dialogs.window_preview_json(root, self.operations)
        ).place(
            relx=0,
            rely=0.3,
            width=140,
            relheight=0.5,
            anchor="nw"
        )

        root.mainloop()

    # Funcion que añadira un bloque de contenido
    def add_content(self, parent):
        dialogs = Dialogs()  # Cuadro de dialogo para cada contenido
        components = Components()  # Componentes para cada contenido
        contentgui = ContentBlock(parent, 
                             len(self.contentblocks) + 1, 
                             self.remove_content,
                             dialogs,
                             components)
        contentgui.pack(fill="x", pady=1, ipady=10)
        self.contentblocks.append(contentgui)
        return contentgui

    def remove_content(self, block):
        self.contentblocks.remove(block)

    # Creamos el frame que estara sobre un canvas para poder crear bloques de frames
    # y estos esten controlados con un Scroll.
    def createCanvasContent(self, parent):
        canvas = tk.Canvas(parent,
                           background=dark_blue)

        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview, background=dark_blue)   
        scrollbar.place(relx=1, y=220, width=10, height=400, anchor="ne")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.place(x=0, y=220, relwidth=1, height=400)

        frame = tk.Frame(canvas, 
                         background=dark_blue)

        canvas_window = canvas.create_window((0, 0), window=frame, anchor="nw")

        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")) 
        )

        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(tagOrId=canvas_window, width=e.width)
        )

        def on_mousewheel(event):
            if event.num == 4:      # Linux scroll up
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:    # Linux scroll down
                canvas.yview_scroll(1, "units")
            else:                   # Windows / MacOS
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)     # Windows / Mac
        canvas.bind_all("<Button-4>", on_mousewheel)       # Linux
        canvas.bind_all("<Button-5>", on_mousewheel)       # Linux

        return frame       
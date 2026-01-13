import tkinter as tk
from .colors import *

class ContentBlock(tk.LabelFrame):
    def __init__(self, parent, index, remove_content, dialogs, components):
        super().__init__(parent, 
                         text=f"Contenido #{index}", 
                         background=medium_blue,
                         padx=10,
                         pady=10,
                         font=("Verdana", 13, "bold"))
        
        self.remove_content = remove_content
        self.dialogs = dialogs
        self.components = components

        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=4, uniform="a")
        self.columnconfigure(2, weight=1, uniform="a")

        self.subtitle = tk.StringVar()
        self.codepath = tk.StringVar()
        self.imagesrc = tk.StringVar()

        buttoncode = {"text": "Cargar", "width": 12, "func": lambda: dialogs.open_window_code(self, self.codepath)}
        buttonimage = {"text": "Abrir", "width": 12, "func": lambda: dialogs.open_window_image(self, self.imagesrc, components)}

        self.components.add_row(self, 0, "Subtitulo", self.subtitle, None, True)
        self.components.add_row(self, 1, "Texto", None, None, False)
        self.components.add_row(self, 2, "Codigo", self.codepath, buttoncode, True)
        self.components.add_row(self, 3, "Image", self.imagesrc, buttonimage, True)

        self.rowconfigure(4, weight=1)

        buttonEliminar = tk.Button(
            self,
            text="Eliminar",
            background=dark_blue,
            font=("Verdana", 11, "bold"),
            foreground="white",
            activebackground=medium_blue,
            activeforeground="black",
            width=12,
            command=self.remove
        )

        buttonEliminar.grid(
            row=4,
            column=2,
            # ipadx=17,
            ipady=0,
            sticky="e"
        )

    def remove(self):
        self.remove_content(self)
        self.destroy()

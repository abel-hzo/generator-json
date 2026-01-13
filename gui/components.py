import tkinter as tk
from tkinter import scrolledtext
from .colors import *

class Components:
    def add_row(self, parent, index, texto, variable, buttonconfig, isEntry):
        parent.rowconfigure(index, weight=1)
        if buttonconfig:
            columnspanvar = 1
        else:
            columnspanvar = 2
        tk.Label(
            parent,
            text=texto,
            background=medium_blue,
            font=("Verdana", 11, "bold"),
            foreground="black",
            anchor="w"
        ).grid(
            row=index,
            column=0,
            ipadx=3,
            ipady=3,
            sticky="we"
        )

        if isEntry:
            tk.Entry(
                parent,
                background=dark_blue,
                font=("Verdana", 11, "bold"),
                foreground="white",
                justify="left",
                textvariable=variable
            ).grid(
                row=index,
                column=1,
                ipadx=2,
                ipady=3,
                columnspan=columnspanvar,
                sticky="we"
            )
        else:
            self.scrolltext = scrolledtext.ScrolledText(
                parent,
                background=dark_blue,
                font=("Verdana", 11, "bold"),
                foreground="white",
                width=1,
                height=5
            )

            self.scrolltext.vbar.config(
                # troughcolor=dark_blue,
                bg=dark_blue
            )

            self.scrolltext.grid(
                row=index,
                column=1,
                columnspan=columnspanvar,
                ipadx=0,
                ipady=1,
                sticky="ew"
            )

        if buttonconfig:
            tk.Button(
                parent,
                text=buttonconfig["text"],
                background=dark_blue,
                font=("Verdana", 11, "bold"),
                foreground="white",
                activebackground=medium_blue,
                activeforeground="black",
                width=buttonconfig["width"],
                command=buttonconfig["func"]
            ).grid(
                row=index,
                column=2,
                # ipadx=buttonconfig["ipadx"],
                ipady=0,
                sticky="e"
            )


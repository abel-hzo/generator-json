import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Creamos la ventana.
root = tk.Tk()
root.title("Generador de posts")
root.geometry("900x600") # Asignamos tamaño a la ventana
root.config(background="blue", padx=10, pady=10)

labelframe1 = tk.LabelFrame(
    root, 
    text="Datos generales", 
    padx=10, 
    pady=10, 
    background="green",
    foreground="white",
    font=("Monospace", 12)
)

labelframe1.place(x=0, y=0, relwidth=1, height=200)

# Creamos un frame
frame1 = tk.Frame(
    labelframe1, 
    background="green"
)

frame1.place(x=0, y=0, relwidth=1, relheight=1)

# Definimos el Grid
frame1.columnconfigure(0, weight=1, uniform="a")
frame1.columnconfigure(1, weight=4, uniform="a")
frame1.columnconfigure(2, weight=1, uniform="a")
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)
frame1.rowconfigure(2, weight=1)
frame1.rowconfigure(3, weight=1)

################## TITULO GENERICO ################## 
tituloGenLabel = tk.Label(     # Creamos el Label
    frame1,               # Le añadimos el parent
    text="Titulo Gen",     # Le colocamos un texto
    background="green",  # Fondo de color azul
    font=("Monospace", 12, "bold"), # Establecemos un tipo y tamaño de letra
    foreground="black",  # Establecemos un color de texto
    anchor="w"           # Alinear texto a la izquierda
)  

tituloGenLabel.grid(
    row=0,              # Posicionar en la fila 0
    column=0,           # Posicionar en la columna 0
    ipadx=3,            # Expandir el largo del elemento
    ipady=3,             # Expandir la altura del elemento
    sticky="we"
)

tituloGenField = tk.Entry(   # Creamos un elemento Entry 
    frame1,               # Lo asignamos a su elemento padre
    background="lightgreen", # 
    font=("Monospace", 12, "bold"),
    foreground="blue",
    justify="left"
)

tituloGenField.grid(      
    row=0,              # Posicionamos en la fila 0
    column=1,           # Posicionamos en la columna 1
    ipadx=2,            # Expandimos el largo del elemento
    ipady=2,            # Expandimos el alto del elemento
    padx=10,            # Definimos espacio alrededor del componente
    columnspan=2,
    sticky="we",
)

################## IMAGEN GENERICA ##################
imageGenLabel = tk.Label(
    frame1,
    text="Imagen",     # Le colocamos un texto
    background="green",  # Fondo de color azul
    font=("Monospace", 12, "bold"), # Establecemos un tipo y tamaño de letra
    foreground="black",  # Establecemos un color de texto
    anchor="w"           # Alinear texto a la izquierda
)

imageGenLabel.grid(
    row=1,              # Posicionar en la fila 0
    column=0,           # Posicionar en la columna 0
    ipadx=3,            # Expandir el largo del elemento
    ipady=3,             # Expandir la altura del elemento
    sticky="we" 
)

imageGenField = tk.Entry(
    frame1,
    background="lightgreen",        # 
    font=("Monospace", 12, "bold"), # Tipo de letra y tamaño
    foreground="blue",
    justify="left"
)

imageGenField.grid(      
    row=1,              # Posicionamos en la fila 0
    column=1,           # Posicionamos en la columna 1
    ipadx=2,            # Expandimos el largo del elemento
    ipady=2,            # Expandimos el alto del elemento
    padx=10,
    columnspan=1,
    sticky="we",
)

imageGenButton = tk.Button(
    frame1,
    text="Open",
    background="lightgreen",
    font=("Monospace", 10, "bold"),
    foreground="blue"
)

imageGenButton.grid(
    row=1,
    column=2,
    ipadx=0,
    ipady=0,
    padx=10,
    sticky="we"
)

################## TITLE ##################

titleLabel = tk.Label(
    frame1,
    text="Titulo",
    background="yellow",
    font=("Monospace", 12, "bold"),
    foreground="black",
    anchor="w"                     # Alinear texto a la izquierda
)

titleLabel.grid(
    row=2,
    column=0,
    ipadx=3,
    ipady=3,
    sticky="we"
)

tituloField = tk.Entry(
    frame1,
    background="lightgreen",
    font=("Monospace", 12, "bold"),
    foreground="blue",
    justify="left"
)

tituloField.grid(
    row=2,
    column=1,
    columnspan=2,
    ipadx=2,
    ipady=2,
    padx=10,
    sticky="we"
)

################## AUTOR ##################

autorLabel = tk.Label(
    frame1,
    background="green",
    text="Autor",
    font=("Monospace", 12, "bold"),
    foreground="black",
    anchor="w"
)

autorLabel.grid(
    row=3,
    column=0,
    ipadx=3,
    ipady=3,
    sticky="we"
)

autorField = tk.Entry(
    frame1,
    background="lightgreen",
    font=("Monospace", 12, "bold"),
    foreground="blue",
    justify="left"
)

autorField.grid(
    row=3,
    column=1,
    columnspan=2,
    ipadx=2,
    ipady=2,
    padx=10,
    sticky="we"
)

def content_block(parent, index):

    labelframe = tk.LabelFrame(
        parent, 
        text=f"Contenido {index}", 
        padx=10, 
        pady=10,
        background="green",
        font=("Monospace", 12)
    )

    labelframe.pack(fill="x", pady=5, padx=5)

    subtitle = tk.StringVar()
    text = tk.StringVar()
    list_path = tk.StringVar()
    code_path = tk.StringVar()
    image_src = tk.StringVar()

    labelframe.columnconfigure(0, weight=1, uniform="a")
    labelframe.columnconfigure(1, weight=4, uniform="a")
    labelframe.columnconfigure(2, weight=1, uniform="a")
    labelframe.rowconfigure(0, weight=1, pad=10)
    labelframe.rowconfigure(1, weight=1, pad=10)
    labelframe.rowconfigure(2, weight=1, pad=10)

    subtituloLabel = tk.Label(
        labelframe,
        background="green",
        text="Subtitulo",
        font=("Monospace", 12, "bold"),
        foreground="black",
        anchor="w"
    )

    subtituloLabel.grid(
        row=0,
        column=0,
        ipadx=3,
        ipady=3,
        sticky="we"
    )

    subtituloField = tk.Entry(
        labelframe,
        background="lightgreen",
        font=("Monospace", 12, "bold"),
        foreground="blue",
        justify="left"
    )

    subtituloField.grid(
        row=0,
        column=1,
        columnspan=2,
        ipadx=2,
        ipady=2,
        padx=10,
        sticky="we"
    )

    textoLabel = tk.Label(
        labelframe,
        text="Texto",
        background="green",
        font=("Monospace", 12, "bold"),
        foreground="black",
        anchor="w"
    )

    textoLabel.grid(
        row=1,
        column=0,
        ipadx=3,
        ipady=3,
        sticky="we"
    )

    textoField = scrolledtext.ScrolledText(
        labelframe,
        background="lightgreen",
        font=("Monospace", 12, "bold"),
        foreground="blue",
        width=1,
        height=5
    )

    textoField.grid(
        row=1,
        column=1,
        columnspan=2,
        ipadx=0,
        ipady=0,
        padx=10,
        sticky="ew"
    )

    codigoLabel = tk.Label(
        labelframe,
        background="green",
        text="Codigo",
        font=("Monospace", 12, "bold"),
        foreground="black",
        anchor="w"
    )

    codigoLabel.grid(
        row=2,
        column=0,
        ipadx=3,
        ipady=3,
        sticky="we"
    )

    codigoField = tk.Entry(
        labelframe,
        background="lightgreen",
        font=("Monospace", 12, "bold"),
        foreground="blue",
        justify="left"
    )

    codigoField.grid(
        row=2,
        column=1,
        columnspan=1,
        ipadx=2,
        ipady=2,
        padx=10,
        sticky="we"
    )

    codigoButton = tk.Button(
        labelframe,
        text="Codigo",
        background="lightgreen",
        font=("Monospace", 10, "bold"),
        foreground="blue",
        command=open_window_code
    )

    codigoButton.grid(
        row=2,
        column=2,
        ipadx=0,
        ipady=0,
        padx=10,
        sticky="we"
    )

def open_window_code():
    window_code = tk.Toplevel(root)
    window_code.title("Codigo")
    # window_code.resizable(False, False)
    #window_code.geometry("300x300")

    codeText = tk.Text(
        window_code,
        font=("Monospace", 10, "bold"),
        wrap="none"
    )

    codeText.pack(
        expand=True,
        fill="both"
    )

    codenameField = tk.Entry(
        window_code,
        background="lightgreen",
        font=("Monospace", 12, "bold"),
        foreground="blue",
        justify="left"
    )

    codenameField.pack(
        expand=True,
        fill="x",
        side="left"
    )

    def open_dialog_code():
        path = filedialog.asksaveasfile(
            defaultextension=".txt",
            filetypes=[("Archivois de texto", "*.txt"), ("Todos los archivos", "*.*")],
            title="Guardar archivo como"
        )
        
        if path:
            try:
                codetext = codeText.get(1.0, 'end-1c')
                with open(path.name, 'w', encoding='utf-8') as f:
                    f.write(codetext)
                messagebox.showinfo("Éxito", f"Archivo guardado en: {path.name}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    codepathButton = tk.Button(
        window_code,
        text="Guardar",
        background="lightgreen",
        font=("Monospace", 10, "bold"),
        foreground="blue",
        command=open_dialog_code
    )

    codepathButton.pack(
        side="right"
    )


canvas = tk.Canvas(root, highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.place(x=0, y=220, relwidth=1, height=300)
scrollbar.place(relx=1, y=220, width=10, height=300, anchor="ne")

frame2 = tk.Frame(canvas)

canvas_window = canvas.create_window((0, 0), window=frame2, anchor="nw")

frame2.bind(
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

# canvas.bind_all(
#     "<MouseWheel>",
#     lambda e: canvas.yview_scroll(number=int(-1 * (e.delta / 120)), what="units")
# )

# ---------- Manejo dinámico de bloques ----------
blocks = []

def add_block():
    block = content_block(frame2, len(blocks) + 1)
    blocks.append(block)

for i in range(5):
    add_block()


root.mainloop()
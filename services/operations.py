from tkinter import filedialog, messagebox
import json
# import sys
# import os
# sys.path.append(os.getcwd())
from dtos.content import Content, Codigo, Imagen
from dtos.post import Post

class Operations():
    def __init__(self, maingui):
        self.maingui = maingui

    def export_json(self):
        print("Generando JSON")
        if not self.maingui.contentblocks:
            messagebox.showerror("Error", "Agrega al menos un contenido.")
            return
        
        pathjson = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON", ".json")]
        )

        if not pathjson:
            return

        # Escribimos en el archivo, nuestro json.
        with open(pathjson, "w", encoding="utf-8") as f:
            json.dump(self.build_json(), f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Exito", "Archivo JSON generado correctamente.")

    def build_json(self):
        post = Post()
        post.header_title = self.maingui.header_title.get()
        post.header_image = self.maingui.header_image.get().replace(".", "", 1)
        post.title = self.maingui.title.get()
        post.author = self.maingui.author.get()

        for contentblock in self.maingui.contentblocks:
            content = Content()

            if contentblock.subtitle.get():
                content.subtitle = contentblock.subtitle.get()

            if contentblock.components.scrolltext.get(1.0, 'end-1c'):    
                cont = contentblock.components.scrolltext.get(1.0, 'end-1c')
                content.text = cont.replace("\n", "<br>")

            if contentblock.codepath.get():
                code = Codigo()
                code.path = contentblock.codepath.get().replace(".", "", 1)
                code.lang = contentblock.dialogs.lang
                content.code = code.__dict__

            if contentblock.imagesrc.get():
                image = Imagen()
                image.src = contentblock.imagesrc.get().replace(".", "", 1)
                image.maxwidth = contentblock.dialogs.maxwidth.get()
                content.image = image.__dict__


            # Limpiamos los campos que contengan null o None
            content_dict = {
                k: v for k, v in content.__dict__.items()
                if v is not None
            }    

            post.content.append(content_dict)

        return post.__dict__

    # Función que nos cargara un archivo JSON y lo establecera en el formulario
    def load_json(self):
        path = filedialog.askopenfilename(
            filetypes=[("JSON Files", "*.json")]
        )

        if not path:
            return
        
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.populate_from_json(data)

    def populate_from_json(self, data):
        self.maingui.header_title.set(data.get("header_title", ""))
        self.maingui.header_image.set(f".{data.get("header_image", "")}")
        self.maingui.dialogs.filetarget.set(f".{data.get("header_image", "")}")
        self.maingui.title.set(data.get("title", ""))
        self.maingui.author.set(data.get("author", ""))

        self.load_content_blocks(data.get("content", []))

    def load_content_blocks(self, content_list):

        # Quitamos los bloques que previemente estes creados.
        for block in self.maingui.contentblocks:
            block.destroy()

        self.maingui.contentblocks.clear()

        for i, data in enumerate(content_list, start=1):
            # Obtenemos la clase ContentGui que nos crea en la funcion add_content
            contentgui = self.maingui.add_content(self.maingui.frameblocks) 
            # Establecemos el valor de subtitle que viene del JSON
            contentgui.subtitle.set(data.get("subtitle", ""))
            # Establecemos el valor de text que viene del JSON
            text = data.get("text", "").replace("<br>", "\n")
            contentgui.components.scrolltext.insert(1.0, text)
            # Obtenemos el JSON de la propiedad code y después establecemos sus valores.
            codigo = data.get("code", {})
            if codigo.get("path", ""):
                contentgui.codepath.set(f".{codigo.get("path", "")}")
                contentgui.dialogs.lang = codigo.get("lang", "")
            # Obtenemos el JSON de la propiedad image y después establecemos sus valores.
            imagen = data.get("image", {})
            if imagen.get("src", ""):
                contentgui.imagesrc.set(f".{imagen.get("src", "")}")
                contentgui.dialogs.filetarget.set(f".{imagen.get("src", "")}")
                contentgui.dialogs.maxwidth.set(imagen.get("maxwidth", "-1px"))

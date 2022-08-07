"""
The windows from which the user will be able to choose an artwork or a church are identical in the format. Hence I created this class
to avoid creating twice the same file
"""

from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import os
from queries import find_names

class WindowWithCombobox():
    def __init__(self, title, bg_image_name, text, query, kb_path, x, y, root=None):
        self.bg_image_name = bg_image_name
        self.query = query
        self.text = text
        self.kb_path = kb_path
        self.x = x
        self.y = y
        if not root:
            root = Tk()
        self.root = root
        self.root.geometry("400x500")
        self.root.title(title)

    def retrieve(self):
        choose = self.box.get()
        for k in self.id_names.keys():
            if self.id_names[k] == choose:
                print(k)

    def create_window(self):
        frame = Frame(self.root)
        frame.pack(expand=True, fill=BOTH)

        canvas = Canvas(frame, width=400, height=500)
        canvas.pack()
        bg_image = ImageTk.PhotoImage(Image.open(os.path.join(self.bg_image_name)))
        canvas.create_image(self.x, self.y, image=bg_image)
        canvas.create_text(200, 100, text=self.text, font=('Helvetica bold', 15, 'bold'), fill='white')
        self.id_names = find_names(path=self.kb_path, query=self.query)
        self.box = Combobox(frame, values=sorted(list(self.id_names.values())), width=30)
        canvas.create_window(70, 200, window=self.box, anchor='nw')

        btn = Button(frame, text="Go!", width=5, height=1, background='black', fg='white', command=self.retrieve)
        canvas.create_window(170, 280, window=btn, anchor="nw")
        self.root.mainloop()


# Root and frame
'''root = Tk()
root.geometry("400x500")
root.resizable(False, False)
root.title("Artworks")
frame = Frame(root)
frame.pack(expand=True, fill=BOTH)

# Canvas
canvas = Canvas(frame, width=400, height=500)
canvas.pack()
bg_image = ImageTk.PhotoImage(Image.open(os.path.join("images", "art_window_bg.png")))
canvas.create_image(350, 80, image=bg_image)
canvas.create_text(200, 100, text="Choose the artwork", font=('Helvetica bold', 15, 'bold'), fill='white')
artworks_id_names = find_names(path="../kb", query="backward(fact(artwork, (ID, Name, _, _, _, _)))")

# Combobox
box = Combobox(frame, values=sorted(list(artworks_id_names.values())), width=30)
canvas.create_window(70, 200, window=box, anchor='nw')

btn = Button(frame, text="Go!", width=5, height=1, background='black', fg='white', command=retrieve)
canvas.create_window(170, 280, window=btn, anchor="nw")
root.mainloop()'''

"""
The windows from which the user will be able to choose an artwork or a church are identical in the format. Hence I created this class
to avoid creating twice the same file
"""

from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import os
from utils import create_or_set_root
from queries import find_names

class WindowWithCombobox():
    def __init__(self, title, bg_image_name, text, query, kb_path, x, y, answer_window, answer_window_title, answer_window_dimensions, answer_img_path, root=None):
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
        self.answer_window = answer_window
        self.a_w_title = answer_window_title
        self.a_w_dimensions = answer_window_dimensions
        self.answer_img_path = answer_img_path

    def retrieve(self):
        choose = self.box.get()
        for k in self.id_names.keys():
            if self.id_names[k] == choose:
                print(k)

    def open_answer_window(self):
        new_window = Toplevel(self.root)
        new_window = create_or_set_root(self.a_w_title, self.a_w_dimensions, False, False, new_window)
        name = self.box.get()
        for i in self.id_names:
            if self.id_names[i] == name:
                id = i
                break
        self.answer_window.open(root=new_window, id=id, kb_path=self.kb_path, img_path=self.answer_img_path)

    def create_window(self):
        frame = Frame(self.root)
        frame.pack(expand=True, fill=BOTH)

        canvas = Canvas(frame, width=400, height=500)
        canvas.pack()
        bg_image = ImageTk.PhotoImage(Image.open(os.path.join(self.bg_image_name)))
        canvas.create_image(self.x, self.y, image=bg_image)
        canvas.create_text(200, 100, text=self.text, font=('Helvetica bold', 15, 'bold'), fill='white')
        self.id_names = find_names(kb_path=self.kb_path, query=self.query)
        self.box = Combobox(frame, values=sorted(list(self.id_names.values())), width=30)
        canvas.create_window(70, 200, window=self.box, anchor='nw')

        btn = Button(frame, text="Go!", width=5, height=1, background='black', fg='white', command=self.open_answer_window)
        btn.bind("<Button>", lambda e: self.open_answer_window())
        canvas.create_window(170, 280, window=btn, anchor="nw")
        self.root.mainloop()

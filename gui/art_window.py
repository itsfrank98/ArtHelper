from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import os
from queries import find_artworks_names

def retrieve():
    choose = box.get()
    for k in artworks_id_names.keys():
        if artworks_id_names[k] == choose:
            print(k)

root = Tk()
root.geometry("400x500")
root.resizable(False, False)
root.title("Artworks")
frame = Frame(root)
frame.pack(expand=True, fill=BOTH)
canvas = Canvas(frame, width=400, height=500)
canvas.pack()
bg_image = ImageTk.PhotoImage(Image.open(os.path.join("images", "art_window_bg.png")))
canvas.create_image(350, 80, image=bg_image)
canvas.create_text(200, 100, text="Choose the artwork", font=('Helvetica bold', 15, 'bold'), fill='white')
artworks_id_names = find_artworks_names(path="../kb")
box = Combobox(frame, values=sorted(list(artworks_id_names.values())), width=30)
canvas.create_window(70, 200, window=box, anchor='nw')

btn = Button(frame, text="Go!", width=5, height=1, background='black', fg='white', command=retrieve)
canvas.create_window(170, 280, window=btn, anchor="nw")
root.mainloop()

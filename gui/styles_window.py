from tkinter import *
from PIL import ImageTk, Image
import os
from prolog.queries import find_names
from gui.answer_windows import styles_answer_window
from gui.utils import create_or_set_root

width = 15
height = 1
img_directory = "images/styles"
images = []     # Need to add images to a list otherwise they won't be displayed

def open_style_answer_window(root, style_id):
    new_window = Toplevel(root)
    new_window = create_or_set_root("Style", "500x800", False, False, new_window)
    styles_answer_window.open(new_window, style_id, kb_path="../prolog/kb")


def add_canvas(frame, button_text, img, root, style_id):
    c = Canvas(frame, width=500, height=100)
    c.pack(fill=X, expand=True)
    bg = c.create_image(80, 50, image=img)
    btn = Button(frame, text=button_text, width=width, height=height, background='black', fg="white")
    btn.bind("<Button>", lambda e: open_style_answer_window(root, style_id))
    c.create_window(130, 30, window=btn, anchor="nw")


def open(root: Toplevel):
    # Add the first frame
    first_frame = Frame(root)
    first_frame.pack(expand=True, fill=BOTH)

    # Create the main canvas inside the main frame.
    main_canvas = Canvas(first_frame, width=400, height=5000)

    # Create the scrollbar
    sbar = Scrollbar(first_frame, orient=VERTICAL, command=main_canvas.yview)
    sbar.pack(side=RIGHT, fill=Y)
    # Configure the main canvas to properly interact with the scrollbar
    main_canvas.configure(yscrollcommand=sbar.set)
    main_canvas.bind('<Configure>', lambda e:main_canvas.configure(scrollregion=main_canvas.bbox("all")))

    # Create the second frame. Very odd, but it's the only way of making the scrollbar work
    second_frame = Frame(main_canvas)
    main_canvas.create_window((0,0), window=second_frame, anchor="nw")

    styles = find_names(kb_path="../prolog/kb", query="backward(fact(style, (ID, Name, _, _, _)))")
    # Create one canvas for each style and add it to the second frame
    for k in styles.keys():
        img = ImageTk.PhotoImage(Image.open(os.path.join(img_directory, k+".png")))
        images.append(img)
        btn_text = styles[k]
        add_canvas(second_frame, btn_text, img, root, style_id=k)
    main_canvas.pack()

    root.mainloop()

from tkinter import *
from PIL import ImageTk, Image
import os
from queries import find_names
from answer_windows import artists_answer_window
from utils import create_or_set_root

width = 10
height = 1
img_directory = "images/artists"
images = []     # Need to add images to a list otherwise they won't be displayed

def open_artist_answer_window(root, artist_id):
    new_window = Toplevel(root)
    new_window = create_or_set_root("Artist", "500x800", False, False, new_window)
    artists_answer_window.open(new_window, artist_id, kb_path="../kb", img_directory=img_directory)

def add_canvas(row, column, frame, text, img, root, artist_id):
    c = Canvas(frame, width=300, height=500)
    c.grid(row=row, column=column)
    bg = c.create_image(150, 300, image=img)
    btn = Button(frame, text="Go!", width=width, height=height, background='black', fg="white")
    btn.bind("<Button>", lambda e: open_artist_answer_window(root, artist_id))
    c.create_text(150, 200, text=text, font=('Helvetica bold', 15, 'bold'), fill='white')
    ########BIND HERE
    c.create_window(100, 250, window=btn, anchor="nw")


def open(root: Toplevel):
# Initialize the root
    '''root = Tk()
    root.wm_title("Choose an artist")
    root.geometry("900x500")
    root.resizable(False, False)'''

    # Add the first frame
    first_frame = Frame(root)
    first_frame.pack(expand=True, fill=BOTH)

    # Create the main canvas inside the main frame.
    main_canvas = Canvas(first_frame, width=1000, height=500)

    # Create the scrollbar
    sbar = Scrollbar(first_frame, orient=HORIZONTAL, command=main_canvas.xview)
    sbar.pack(side=BOTTOM, fill=X)
    # Configure the main canvas to properly interact with the scrollbar
    main_canvas.configure(xscrollcommand=sbar.set)
    main_canvas.bind('<Configure>', lambda e:main_canvas.configure(scrollregion=main_canvas.bbox("all")))

    # Create the second frame. Very odd, but it's the only way of making the scrollbar work
    second_frame = Frame(main_canvas)
    main_canvas.create_window((0,0), window=second_frame, anchor="nw")

    row = 0
    column = 0
    artists = find_names(query="backward(fact(artist, (ID, Name, _, _)))", kb_path="../kb")
    # Create one canvas for each style and add it to the second frame
    for k in artists.keys():
        img = ImageTk.PhotoImage(Image.open(os.path.join(img_directory, k+".png")))
        images.append(img)
        text = k.replace("_", " ").title()    # Here I could simply use the "Name" field of the dictionary but I chose not to since some artists like have very long names, ie Caravaggio's real name is Alessandro di Mariano di Vanni Filipepi
        add_canvas(row, column, second_frame, text, img, root, k)
        column += 1
    main_canvas.pack(fill=X)

    root.mainloop()


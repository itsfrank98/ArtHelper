from tkinter import *
from PIL import ImageTk, Image
import os

width = 15
height = 1
img_directory = "images/styles"
images = []     # Need to add images to a list otherwise they won't be displayed

def add_canvas(frame, button_text, img):
    c = Canvas(frame, width=500, height=100)
    c.pack(fill=X, expand=True)
    bg = c.create_image(80, 50, image=img)
    btn = Button(frame, text=button_text, width=width, height=height, background='black', fg="white")
    ########BIND HERE
    c.create_window(130, 30, window=btn, anchor="nw")

# Initialize the root
root = Tk()
root.geometry("400x500")
root.resizable(False, False)

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

# Create one canvas for each style and add it to the second frame
for f in os.listdir(img_directory):
    img = ImageTk.PhotoImage(Image.open(os.path.join(img_directory, f)))
    images.append(img)
    btn_text = f.split(".")[0].replace("_", " ").capitalize()
    add_canvas(second_frame, btn_text, img)
main_canvas.pack()

root.mainloop()



from tkinter import *
from PIL import ImageTk, Image

width = 4
height = 1


def add_canvas(frame, img, x, y, text):
    c = Canvas(frame, width=300, height=300)
    c.pack(fill=BOTH, expand=True)
    bg = c.create_image(x, y, image=img)
    btn = Button(frame, text="Go!", width=width, height=height, background='black', fg="white")
    '''if type == "styles":
        btn.bind("<Button>", lambda e: openStylesWindow(root))
    elif type == "artists":
        btn.bind("<Button>", lambda e: openArtistsWindow(root))
    elif type == "art":
        btn.bind("<Button>", lambda e: openArtWindow(root))
    else:
        btn.bind("<Button>", lambda e: openChurchesWindow(root))'''
    c.create_text(150, 190, text=text, font=('Helvetica bold', 15), fill='white')
    c.create_window(100, 220, anchor="nw", window=btn)

# Initialize the root
root = Tk()
root.geometry("600x600")
root.wm_title("KnowYourArt")
root.resizable(False, False)

# Create the frames
f_styles = Frame(root)
f_artists = Frame(root)
f_art = Frame(root)
f_churches = Frame(root)

# Load the background images
styles_bg = ImageTk.PhotoImage(Image.open("images/styles_bg.png"))
artists_bg = ImageTk.PhotoImage(Image.open("images/artists_bg.png"))
art_bg = ImageTk.PhotoImage(Image.open("images/art_bg.png"))
churches_bg = ImageTk.PhotoImage(Image.open("images/churches_bg.png"))

# Add the canvases
add_canvas(f_styles, styles_bg, 0, 0, "Seek information about styles")
add_canvas(f_artists, artists_bg, 240, 240, "Seek information about \n artists and architects")
add_canvas(f_art, art_bg, 120, 120, "Seek information about artworks")
add_canvas(f_churches, churches_bg, 90, 150, "Seek information about churches")

f_styles.grid(row=0, column=0)
f_artists.grid(row=0, column=1)
f_art.grid(row=1, column=0)
f_churches.grid(row=1, column=1)

root.mainloop()

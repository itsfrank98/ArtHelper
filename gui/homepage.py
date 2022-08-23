from tkinter import *
from PIL import ImageTk, Image
import artists_window, styles_window
from WindowWithCombobox import WindowWithCombobox
from utils import create_or_set_root
from gui.answer_windows import artwork_answer_window, churches_answer_window

def openStylesWindow(root):
    new_window = Toplevel(root)
    new_window = create_or_set_root("Choose a style", "400x500", False, False, new_window)
    styles_window.open(new_window)
def openArtistsWindow(root):
    new_window = Toplevel(root)
    new_window = create_or_set_root("Choose an artist", "900x500", False, False, new_window)
    artists_window.open(new_window)
def openArtWindow(root):
    new_window = Toplevel(root)
    new_window = WindowWithCombobox(title="Artworks",
                                    bg_image_name="images/art_window_bg.png",
                                    text="Choose an artwork",
                                    query="backward(fact(artwork, (ID, Name, _, _, _, _)))",
                                    kb_path="../kb",
                                    x=350, y=80,
                                    answer_window=artwork_answer_window,
                                    answer_window_title="Artwork",
                                    answer_window_dimensions="500x1000",
                                    answer_img_path="images/art",
                                    root=new_window)
    new_window.create_window()
def openChurchesWindow(root):
    new_window = Toplevel(root)
    new_window = WindowWithCombobox(title="Churches",
                                    bg_image_name="images/churches_window_bg.png",
                                    text="Choose a church",
                                    query="backward(fact(church, (ID, Name, _, _, _)))",
                                    kb_path="../kb",
                                    x=150,
                                    y=200,
                                    answer_window=churches_answer_window,
                                    answer_window_title="Church",
                                    answer_window_dimensions="500x800",
                                    answer_img_path="answer_windows/churches_low_res",
                                    root=new_window)
    new_window.create_window()


def add_canvas(root, frame, img, x, y, text, type):
    c = Canvas(frame, width=300, height=300)
    c.pack(fill=BOTH, expand=True)
    bg = c.create_image(x, y, image=img)
    btn = Button(frame, text="Go!", width=4, height=1, background='black', fg="white")
    if type == "styles":
        btn.bind("<Button>", lambda e: openStylesWindow(root))
    elif type == "artists":
        btn.bind("<Button>", lambda e: openArtistsWindow(root))
    elif type == "art":
        btn.bind("<Button>", lambda e: openArtWindow(root))
    else:
        btn.bind("<Button>", lambda e: openChurchesWindow(root))
    c.create_text(150, 190, text=text, font=('Helvetica bold', 15), fill='white')
    c.create_window(100, 220, anchor="nw", window=btn)


# Initialize the root
root = create_or_set_root("ArtHelper", "600x600", False, False)

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
add_canvas(root, f_styles, styles_bg, 0, 0, "Seek information about styles", "styles")
add_canvas(root, f_artists, artists_bg, 240, 240, "Seek information about \n artists and architects", "artists")
add_canvas(root, f_art, art_bg, 120, 120, "Seek information \nabout artworks", "art")
add_canvas(root, f_churches, churches_bg, 90, 150, "Seek information \nabout churches", "churches")

f_styles.grid(row=0, column=0)
f_artists.grid(row=0, column=1)
f_art.grid(row=1, column=0)
f_churches.grid(row=1, column=1)

root.mainloop()

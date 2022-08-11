import os.path
from tkinter import *
from PIL import ImageTk, Image
from queries import find_artist_requirements
from gui.utils import create_title_label, add_frame_answer_window, print_list, convert_atoms_to_values

#TODO: implementare finestra che apre un artwork o un posto in questo file


#artist_id = "neri_fioravante"
def open(root, artist_id, kb_path, img_directory):
    #root = create_or_set_root("Artist", "500x800", False, False, root)
    frame = Frame(root)
    frame.pack()
    info, related_artists, related_styles, artworks, places = find_artist_requirements(artist_id, kb_path=kb_path)

    info = info['query_results'][0]
    related_artists = related_artists['query_results']
    artworks = artworks['query_results']
    places = places['query_results']
    works = artworks + places

    name = info['Name']
    lbl = create_title_label(frame, text=name, fontsize=15)
    lbl.pack()

    img = ImageTk.PhotoImage(Image.open(os.path.join(img_directory, "{}.png".format(artist_id))))
    c = Canvas(frame, width=450, height=400)
    c.pack()
    bg = c.create_image(200, 300, image=img)

    yb = info['Yb']
    yd = info['Yd']

    general_info = "Name: {} \n" \
                   "Birth year: {}\n" \
                   "Death year: {}".format(name, yb, yd)

    if related_artists:
        general_info += print_list("\nThis artist was influenced by: ", convert_atoms_to_values(related_artists[0]['Artists']))

    if related_styles:
        general_info += print_list("\nStyle(s) followed: ", related_styles)


    info_label = Label(frame, text=general_info)
    info_label.pack()

    if works:
        add_frame_answer_window(frame,
                                "Operas by this artist",
                                second_label_text="(Select an option and then click on the 'Go!' button to see the opera)",
                                dict_list=works,
                                button_text="Go!",
                                key="Opera",
                                lb_height=6)

    root.mainloop()

from tkinter import *
from queries import find_artwork_requirements
from PIL import ImageTk, Image
import os
from gui.utils import create_title_label, convert_atoms_to_values, print_list, add_frame_answer_window, format_id
from gui.answer_windows import explanation_window

#art_id = "adam_creation"
def open(root, id, kb_path, img_path):
    #root = create_or_set_root("Artwork", "500x1000", False, False)
    frame = Frame(root)
    frame.pack()
    info, other, same_subject, same_place = find_artwork_requirements(id, kb_path=kb_path)
    info = info['query_results'][0]
    related_artworks = other['query_results'] + same_subject['query_results'] + same_place['query_results']
    related_artworks_explanations = other['explanations'] + same_subject['explanations'] + same_place['explanations']
    title = info['Title']
    lbl = create_title_label(frame, text=title, fontsize=15)
    lbl.pack()

    img = ImageTk.PhotoImage(Image.open(os.path.join(img_path, "{}.png".format(id))))
    c = Canvas(frame, width=450, height=400)
    c.pack()
    bg = c.create_image(200, 300, image=img)

    type = info['Type'].title()
    city = info['City_name']
    year = info['Year']
    desc = info['Desc']
    author = format_id(info['ArtistName'])
    style = info['StyleNames']  # List of atoms
    museum = info['MuseumName']
    main_subject = info['MainSubjectsNames']    # List of atoms
    secondary_subject = info['SecondarySubjectsNames']  # List of atoms

    style = convert_atoms_to_values(style)
    main_subject = convert_atoms_to_values(main_subject)
    secondary_subject = convert_atoms_to_values(secondary_subject)

    general_info = "{} realized in {} in the year {}. \n" \
                   "{}\n\n" \
                   "Author: {} \n" \
                   "Placed in: {}\n".format(type, city, year, desc, author, museum)
    general_info += print_list("Style(s) followed: ", style)

    if main_subject:
        general_info += print_list("Main subject(s): ", main_subject)

    if secondary_subject:
        general_info += print_list("Secondary subject(s): ", secondary_subject)

    info_label = Label(frame, text=general_info)
    info_label.pack()

    if related_artworks:
        add_frame_answer_window(frame, label_text="\nOther artworks related to this",
                                second_label_text="(Select an option and then click on the 'Why?' button to get an explanation)",
                                dict_list=related_artworks,
                                button_text="Why?",
                                key="Artworks",
                                img_path="images/art",
                                expl=related_artworks_explanations,
                                open_window_file=explanation_window,
                                current_item_name=title)

    root.mainloop()

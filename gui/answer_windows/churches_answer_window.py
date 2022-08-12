import os.path
from tkinter import *
from PIL import ImageTk, Image
from queries import find_church_requirements
from gui.utils import create_title_label, add_frame_answer_window, print_list, convert_atoms_to_values
from gui.answer_windows import artwork_answer_window

#church_id = "st_stephen"
def open(id, root, kb_path, img_path):
    #root = create_or_set_root("Church", "500x800", False, False)
    frame = Frame(root)
    frame.pack()
    info, related_churches, artworks = find_church_requirements(id, kb_path=kb_path)

    info = info['query_results'][0]
    related_churches = related_churches['query_results']
    artworks = artworks['query_results']

    name = info['CName']
    lbl = create_title_label(frame, text=name, fontsize=15)
    lbl.pack()

    img = ImageTk.PhotoImage(Image.open(os.path.join(img_path, "{}.png".format(id))))
    c = Canvas(frame, width=450, height=300)
    c.pack()
    bg = c.create_image(150, 180, image=img)

    city = info['CityName']
    yb = info['Yb']
    ye = info['Ye']
    styles = info['StylesNames']
    styles_values = convert_atoms_to_values(styles)
    if info['ArchitectsNames']:
        architects = info['ArchitectsNames']

    general_info = "Name: {} \n" \
                   "Construction began in: {}\n" \
                   "Construction ended in: {}\n".format(name, yb, ye)

    general_info += print_list("Style(s) followed: ", styles_values)

    if info['ArchitectsNames']:
        names = convert_atoms_to_values(info['ArchitectsNames'])
        general_info += print_list("Architect(s): ", names)

    info_label = Label(frame, text=general_info)
    info_label.pack()

    if related_churches:
        add_frame_answer_window(frame, label_text="\nOther churches related to this",
                                second_label_text="(Select an option and then click on the 'Why?' button to get an explanation)",
                                dict_list=related_churches,
                                button_text="Why?",
                                lb_height=5,
                                key="Churches")
    if artworks:
        add_frame_answer_window(frame, label_text="\nArtworks held in this church",
                                second_label_text="(Select an option and then click on the 'Go!' button to see the artwork)",
                                dict_list=artworks,
                                button_text="Go!",
                                lb_height=4,
                                key="Artworks",
                                img_path="images/art",
                                open_window_file=artwork_answer_window,
                                expl=False,
                                answer_win_title="Artwork",
                                answer_win_dimensions="500x1000",
                                kb_path="../kb"
                                )




    root.mainloop()

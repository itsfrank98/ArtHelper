from tkinter import *
from queries import find_style_requirements
from gui.utils import create_or_set_root, create_title_label, add_frame_answer_window


def add_frame(root, label_text, dict_list, key):
    frame = Frame(root)
    frame.pack()
    lbl = Label(frame, text=label_text, font=('Helvetica', 12, 'bold'))
    lbl.pack()
    lbl2 = Label(frame, text="(Select an option and then click on the 'Why?' button to get an explanation)", font=('Helvetica', 10))
    lbl2.pack()
    lb = Listbox(frame, width=25, height=9)
    l = []
    i = 0
    for d in dict_list:
        item = d[key]
        if item not in l:
            lb.insert(i, item.split(".")[0].replace("_", " ").title())
            l.append(item)
            i += 1
    lb.pack()

    def selected_item():
        for i in lb.curselection():
            print(lb.get(i))

    btn = Button(frame, text="Why?", command=selected_item)
    btn.pack()
    return frame


style_id = 'romanic'
#def open(root, style_id):
root = create_or_set_root("Style", "500x800", False, True)
frame = Frame(root)
frame.pack()
info, related_styles, related_artists = find_style_requirements(style_id, '../kb')

info = info['query_results'][0]
styles = related_styles['query_results']
artists = related_artists['query_results']

style_name = info['Name']
title_label = create_title_label(frame, text=style_name, fontsize=15)
title_label.pack()
general_info = "Started in {}, ended in {}. \nField (architecture or art or both): {}".format(info['Yb'], info['Ye'], info['Field'])
info_label = Label(frame, text=general_info)
info_label.pack()

### STYLES
if styles:
    styles_frame = add_frame_answer_window(root,
                             label_text="\n\nStyles related to {}".format(style_name),
                             dict_list=styles,
                             key="Styles")
if artists:
    artists_frame = add_frame_answer_window(root,
                              label_text="\n\nArtists exponent of this style",
                              dict_list=artists,
                              key="Artist")

root.mainloop()

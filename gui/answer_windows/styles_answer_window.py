from tkinter import *
from prolog.queries import find_style_requirements
from gui.utils import create_title_label, add_frame_answer_window, format_id
from gui.answer_windows import explanation_window


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
            lb.insert(i, format_id(item.split(".")[0]))
            l.append(item)
            i += 1
    lb.pack()

    def selected_item():
        for i in lb.curselection():
            print(lb.get(i))

    btn = Button(frame, text="Why?", command=selected_item)
    btn.pack()
    return frame


#style_id = 'romanic'
def open(root, style_id, kb_path):
    #root = create_or_set_root("Style", "500x800", False, True, root)
    frame = Frame(root)
    frame.pack()
    info, coexisting_styles, same_current, same_art, related_artists = find_style_requirements(style_id, kb_path=kb_path)

    info = info['query_results'][0]
    related_styles = coexisting_styles['query_results'] + same_current['query_results'] + same_art['query_results']
    related_styles_explanations = coexisting_styles['explanations'] + same_current['explanations'] + same_art['explanations']
    artists = related_artists['query_results']

    style_name = info['Name']
    title_label = create_title_label(frame, text=style_name, fontsize=15)
    title_label.pack()
    general_info = "Started in {}, ended in {}. \nField (architecture or art or both): {}".format(info['Yb'], info['Ye'], info['Field'])
    info_label = Label(frame, text=general_info)
    info_label.pack()

    ### STYLES
    if related_styles:
        add_frame_answer_window(root,
                                label_text="\n\nStyles pre-required for {}".format(style_name),
                                second_label_text="(Select an option and then click on the 'Why?' button to get an explanation)",
                                dict_list=related_styles,
                                button_text="Why?",
                                key="Styles",
                                expl=related_styles_explanations,
                                open_window_file=explanation_window,
                                current_item_name=style_name
                                )
    if artists:
        add_frame_answer_window(root,
                                label_text="\n\nArtists exponent of this style",
                                second_label_text="(Select an option and then click on the 'Why?' button to get an explanation)",
                                dict_list=artists,
                                button_text="Why?",
                                key="Artist",
                                expl=related_artists['explanations'],
                                open_window_file=explanation_window,
                                current_item_name=style_name)

    root.mainloop()

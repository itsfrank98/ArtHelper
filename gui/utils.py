from tkinter import *

def create_or_set_root(title: str, geometry: str, resizable_1: bool, resizable_2: bool, root: Toplevel = None):
    if not root:
        root = Tk()
    root.geometry(geometry)
    root.resizable(resizable_1, resizable_2)
    root.title(title)
    return root

def create_title_label(frame, text, fontsize):
    return Label(frame, text=text, font=('Helvetica', fontsize, 'bold'))

def convert_atoms_to_values(l: list):
    for i in range(len(l)):
        l[i] = l[i].value.replace("_", " ").title()
    return l

def print_list(text, l):
    final_string = text
    used = []
    for i in range(len(l)):
        if l[i] not in used:
            final_string += "{}".format(l[i])
            used.append(l[i])
            if i+1 < len(l):
                final_string += ", "
            if i!=0 and i%3 == 0:
                final_string +="\n"
    return final_string+"\n"


def go_answer_window(root, title, dimensions, id, window, kb_path, img_path):
    new_window = Toplevel(root)
    new_window = create_or_set_root(title, dimensions, False, False, new_window)
    window.open(id, new_window, kb_path, img_path)



def add_frame_answer_window(root, label_text, second_label_text, dict_list, key, button_text, img_path=None, open_window_file=None,
                            lb_width=25, lb_height=9, expl=True, answer_win_title="Explanation",
                            answer_win_dimensions="300x300", kb_path="../kb"):
    """

    :param root: Root of the window from which the frame is opened
    :param label_text: Text of the first label to display
    :param second_label_text: Text of the second label to display
    :param dict_list: List of dictionaries returned by a query
    :param key: Key that the item we are interested in has in the dictionary
    :param button_text: Text of the button that will be displayed in the frame to display in the
    :param img_path: If there is an other window that will be opened from the current window, this is the path of the images the window will need.
    If the window doesn't need images, we can leave this param to be none
    :param open_window_file: If there is an other window that will be opened from the current window, this is the name of the file
    in which that window is coded. The open() method will be called from that file
    :param lb_width: Width of the listbox
    :param lb_height: Height of the listbox
    :param expl: Set this to true if the window that will be opened from the current window is for explanation
    :param answer_win_title: Title of the window that will be opened from the current one
    :param answer_win_dimensions: Dimension of the window that will be opened from the current one
    :param kb_path: If the window that will be opened from the current one will need to query the knowledge base, put the path to it
    :return:
    """
    frame = Frame(root)
    frame.pack()
    lbl = Label(frame, text=label_text, font=('Helvetica', 12, 'bold'))
    lbl.pack()
    lbl2 = Label(frame, text=second_label_text, font=('Helvetica', 10))
    lbl2.pack()
    lb = Listbox(frame, width=lb_width, height=lb_height)
    l = []
    i = 0
    for d in dict_list:
        item = d[key]
        if item not in l:
            if type(item) == list:  # Some rules, such as other_elements_composition (in rules_artworks.pl file) can return a list of functors
                for elem in item:
                    lb.insert(i, elem.value.split(".")[0].replace("_", " ").title())
            else:
                lb.insert(i, item.split(".")[0].replace("_", " ").title())
            l.append(item)
            i += 1
    lb.pack()
    id="monna_lisa"
    def selected_item():
        for j in lb.curselection():
            id = lb.get(j)
            id = id.replace(" ", "_").lower()
            if not expl:
                go_answer_window(root=root, title=answer_win_title, dimensions=answer_win_dimensions, id=id,
                                 window=open_window_file, kb_path=kb_path, img_path=img_path)

    btn = Button(frame, text=button_text, command=selected_item)

    btn.pack()
    return frame

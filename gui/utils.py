from tkinter import *

def format_id(id):
    return id.replace("_", " ").title()

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
        l[i] = format_id(l[i].value)
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
    window.open(new_window, id, kb_path, img_path)

def explain_answer_window(root, title, dimensions, current_item_name, id, name, window, explanations):
    """
    Open a window containing the explanation that lead the system to say that an item is related to the current one.
    :param root: Root
    :param title: Title of the window
    :param dimensions: Dimensions of the window
    :param id: Id of the item to which the current item is related
    :param name: Name of the item to which the current item is related
    :param window: Name of the file containing the method that will open the explanation window
    :param explanations: Dictionary containing the explanations to format
    :return:
    """
    new_window = Toplevel(root)
    new_window = create_or_set_root(title, dimensions, False, False, new_window)
    window.open(new_window, current_item_name, id, name, explanations)


def add_frame_answer_window(root, label_text, second_label_text, dict_list, key, button_text, img_path=None, open_window_file=None,
                            lb_width=25, lb_height=9, expl=None, answer_win_title="Explanation",
                            answer_win_dimensions="300x300", kb_path="../kb", current_item_name=None):
    """
    Add, in the window, a frame containing a listbox with some items. The listbox can be used to select and visualize the item itself, or
    to get an explanation on why the item was put in the listbox
    :param root: Root of the window from which the frame is opened
    :param label_text: Text of the first label to display
    :param second_label_text: Text of the second label to display
    :param dict_list: List of dictionaries returned by a query
    :param key: Key that the item we are interested in has in the dictionary
    :param button_text: Text of the button that will be displayed in the frame to display in the
    :param img_path: If there is another window that will be opened from the current window, this is the path of the
    images the window will need. If the window doesn't need images, we can leave this param to be none
    :param open_window_file: If there is another window that will be opened from the current window, this is the name of
    the file in which that window is coded. The open() method will be called from that file
    :param lb_width: Width of the listbox
    :param lb_height: Height of the listbox
    :param expl: if the window that will be opened from the current window is for explanation, this parameter will contain NON LO SOOOOOOOOO, otherwise leave it to None
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
                    lb.insert(i, format_id(elem.value.split(".")[0]))
            else:
                lb.insert(i, format_id(item.split(".")[0]))
            l.append(item)
            i += 1
    lb.pack()

    def selected_item():
        for j in lb.curselection():
            name = lb.get(j)
            id = name.replace(" ", "_").lower()
            if not expl:
                go_answer_window(root=root, title=answer_win_title, dimensions=answer_win_dimensions, id=id,
                                 window=open_window_file, kb_path=kb_path, img_path=img_path)
            else:
                selected_item_explanations = [] # Expl is a list of dicts, one for each explanation. We want to retrieve only the ones concerning the item selected by the user and put them into a list
                for d in expl:
                    if d['X'][0].value.__contains__(id):    #The dictionary contains the list of rules used. It is like a stack, so the last used rule is the first in the list. So in order to know if the rule concerns the item of interest we just have to check the first element ans see if it contains the id
                        selected_item_explanations.append(d)
                explain_answer_window(root=root, title="Explanation", dimensions="700x200", id=id, name=name,
                                      window=open_window_file, explanations=selected_item_explanations, current_item_name=current_item_name)

    btn = Button(frame, text=button_text, command=selected_item)

    btn.pack()
    return frame

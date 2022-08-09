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
        l[i] = l[i].value

    return l

def print_list(text, l):
    final_string = text
    for i in range(len(l)):
        final_string += "{}".format(l[i])
        if i+1 < len(l):
            final_string += ", "
        if i!=0 and i%3 == 0:
            final_string +="\n"
    return final_string+"\n"


def add_frame_answer_window(root, label_text, dict_list, key):
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
            if type(item) == list:  # Some rules, such as other_elements_composition (in rules_artworks.pl file) can return a list of functors
                for elem in item:
                    lb.insert(i, elem.value.split(".")[0].replace("_", " ").title())
            else:
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

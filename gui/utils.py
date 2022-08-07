from tkinter import *


def create_or_set_root(title: str, geometry: str, resizable_1: bool, resizable_2: bool, root: Toplevel = None):
    if not root:
        root = Tk()
    root.geometry(geometry)
    root.resizable(resizable_1, resizable_2)
    root.title(title)
    return root



from tkinter import *

def open(root, id, name, explanations):
    frame = Frame(root)
    frame.pack()
    punctuation = ["(", ")", ","]
    x = explanations[0]['X'][0].value
    for i in punctuation:
        x = x.replace(i, "")
    x = x.split(" ")

    rule_name = x[0]
    current_church_name = x[1].replace("_", " ").title()
    text = "{} is related to {} because:".format(current_church_name, name)

    print(text)


from tkinter import *
from gui.utils import format_id

def open(root, current_item_name, id, name, explanations):
    frame = Frame(root)
    frame.pack()
    punctuation = ["(", ")", ","]
    text = "Relationships between {} and {}:".format(current_item_name, name)
    used_rules = []     # For some reason there are rules that appear twice, with this list we avoid printing twice the same explanation
    for exp in explanations:
        x = exp['X'][0].value
        for i in punctuation:
            x = x.replace(i, "")
        x = x.split(" ")
        rule_name = x[0]
        if rule_name not in used_rules:
            if rule_name == "is_exponent":
                text += "\nThe following operas by {} follow {}".format(name, current_item_name)
                for exp1 in explanations:
                    for e in exp1['X']:
                        e = e.value
                        if e.__contains__("follows"):
                            for i in punctuation:
                                e = e.replace(i, "")
                            e = e.split(" ")[1]
                            text += "\n•{}".format(format_id(e))
                used_rules.append(rule_name)
            elif x[2] == id:
                if rule_name == "churches_same_construction_years":
                    text += "\n• They were built in the same city ({}) at the same time.".format(format_id(x[3]))
                elif rule_name == "churches_same_style_and_city":
                    text += "\n• They were built in the same city ({}) and follow some styles in common.".format(format_id(x[3]))
                elif rule_name == "fresco_same_place":
                    text += "\n• They are both frescos made by {} in the same place ({})".format(format_id(x[4]), format_id(x[3]))
                elif rule_name == "artwork_same_subject":
                    text += "\n• They potray the same subjects and follow the same style"
                elif rule_name == "co_existing_styles":
                    text += "\n• The two styles cover similar fields and they co-existed for some time"
                elif rule_name == "influenced_same_current":
                    text += "\n• The two styles belong to the same main current"
                elif rule_name == "influenced_same_art":
                    text += "\n• The opera {} follows both the styles".format(format_id(x[3]))
                elif rule_name == "other_elements_composition":
                        text += "\n• They are part of the same composition"
                used_rules.append(rule_name)

    l = Label(frame, text=text, width=80)
    l.pack()


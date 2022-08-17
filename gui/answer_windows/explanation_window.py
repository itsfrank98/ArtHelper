from tkinter import *

def open(root, id, name, explanations):
    frame = Frame(root)
    frame.pack()
    punctuation = ["(", ")", ","]
    current_church_name = id.replace("_", " ").title()
    text = "{} and {} may be related because:".format(current_church_name, name)
    used_rules = []     # For some reason there are rules that appear twice, with this list we avoid printing twize the same explanation
    for exp in explanations:
        x = exp['X'][0].value
        for i in punctuation:
            x = x.replace(i, "")
        x = x.split(" ")
        print(x)
        rule_name = x[0]
        if x[]
        if rule_name not in used_rules:
            if rule_name == "churches_same_construction_years":
                text += "\n• They were built in the same city ({}) at the same time.".format(x[3])
            elif rule_name == "churches_same_style_and_city":
                text += "\n• They were built in the same city ({}) and follow some styles in common.".format(x[3])
            elif rule_name == "fresco_same_place":
                text += "\n• They are both frescos made by {} in the same place ({})".format(x[4], x[3])
            elif rule_name == "other_elements_composition":
                text += "\n• They are part of the same composition"
            elif rule_name == "artwork_same_subject":
                text += "\n• They potray the same subjects and follow the same style"
            elif rule_name == "is_exponent":
                text += "\n• These operas made by this artist follow {}:".format(x[1])
            elif rule_name == "co_existing_styles":
                text += "\n• The two styles cover similar fields and they co-existed for some time"
            elif rule_name == "influenced_same_current":
                text += "\n• The two styles belong to the same main current"
            elif rule_name == "influenced_same_art":
                text += "\n• The opera {} follows both the styles".format(x[2])
            used_rules.append(rule_name)
    l=Label(frame, text=text)
    l.pack()
    #print(text)


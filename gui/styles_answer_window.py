from tkinter import *
from queries import find_style_requirements
style_id = 'early_renaissance'
#def open(root, style_id):
root = Tk()
root.geometry("500x300")
frame = Frame(root)
frame.pack(expand=True, fill=BOTH)
info, related_styles, related_artists = find_style_requirements('../kb', style_id)

info = info['query_results'][0]
styles = related_styles['query_results']
artists = related_artists['query_results']

style_name = info['Name']
title_label = Label(frame, text=style_name, font=('Helvetica', 15, 'bold'))
title_label.pack()
general_info = "Started in {}, ended in {}. \nField (architecture or art or both): {}".format(info['Yb'], info['Ye'], info['Field'])
info_label = Label(frame, text=general_info)
info_label.pack()

### STYLES
if styles:
    second_frame = Frame(root)
    related_styles_label = Label(second_frame,
                                 text="These styles are someway related to {}, so you should know them to better understand it".format(style_name),
                                 font=('Helvetica', 10, 'bold'))
    LB = Listbox(second_frame)


### ARTISTS
if artists:
    second_frame = Frame(root)
    related_styles_label = Label(second_frame,
                                 text="These artists were exponent of this style. Click on the buttons to show their artworks related to {}".format(style_name),
                                 font=('Helvetica', 15, 'bold'))
root.mainloop()

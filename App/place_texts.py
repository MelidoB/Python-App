def set_text(canvas,texts,pos_x=0,pos_y=0, text="empty", color="black", insert=False):
    if (not insert == False):
        texts.append(canvas.create_text(pos_x, pos_y, text=text, fill=color, font=('Helvetica 15 bold')))
    else:
        canvas.create_text(pos_x, pos_y, text=text, fill=color, font=('Helvetica 15 bold'))
def place_title(canvas, title,texts):
    set_text(canvas,texts, title[0], title[1],title[2])

def place_text(canvas, text_array, texts, insert):
    for text in text_array:
        set_text(canvas,texts, text[0], text[1],text[2],insert=insert)
from tkinter import Button
from functools import partial

def modify_text(canvas,texts,scrollbar):
    txt = canvas.itemcget(texts, 'text')
    txt = int(txt) + 1
    canvas.itemconfig(texts, text=str(txt))
    scrollbar.set(0.603, 1.0)
    canvas.config(xscrollcommand=scrollbar.set)
    

def create_buttons(tk,btn,canvas,texts, lenth, img_pos,scrollbar):

    y = 450
    x = 150
    #information for the buttons
    buttons_info = []


    for i in range(lenth):
        #lambda assigns the last i (in this case 3). Making a button modify just the last content
        #buttons_info.append(["Click me!", lambda: modify_text(canvas, texts[i]), img_pos[i][0] + 100, img_pos[i][1] + 200])

        #using partial functions solve this problem
        buttons_info.append(["click here", partial(modify_text,canvas,texts[i],scrollbar), img_pos[i][0]+100, img_pos[i][1]+200])


    #Creating buttons and assigning the information
    for i in range(len(buttons_info)):
        btn.append(Button(canvas, text = buttons_info[i][0], command = buttons_info[i][1]))
        canvas.create_window((buttons_info[i][2],buttons_info[i][3]), window=btn[i])

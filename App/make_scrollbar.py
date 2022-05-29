from tkinter import BOTH,X,Frame,Scrollbar,HORIZONTAL,BOTTOM

def create_frame(tk):
    frame = Frame(tk, width=500, height=400)
    frame.pack(expand=True, fill=BOTH)
    return frame

def create_scrollbar(frame, canvas):
    horibar=Scrollbar(frame,orient=HORIZONTAL)
    horibar.pack(side=BOTTOM,fill=X)
    horibar.config(command=canvas.xview)

    canvas.config(width=800,height=600)
    canvas.config(xscrollcommand=horibar.set)


    return horibar
from tkinter import Canvas, BOTH, NW, X,Frame,Scrollbar,HORIZONTAL,BOTTOM
from PIL import Image,ImageTk

from create_texts import create_texts
from create_images import create_images
from create_buttons import create_buttons
from make_scrollbar import create_frame, create_scrollbar

def making_space(tk, canvas, texts, imgs, button):
    frame = create_frame(tk)
    
    img_pos = []

    

    canvas = Canvas(frame,width=500, height=400,highlightthickness=3,bg="#FFFF00")
    scrollbar = create_scrollbar(frame, canvas)
    canvas.pack()
    
    
    #I need to return x, y for texts
    create_texts(canvas, texts) #all the text
    
    

    images_len = create_images(canvas, imgs,img_pos) #all the images
    create_buttons(tk,button,canvas,texts,images_len,img_pos,scrollbar) #all the buttons

    '''
    The canvas can't scroll items added with pack, place, or grid. 
    It will only scroll widgets added with the create_window method.
    '''
    
    x1,y1,x2,y2 = canvas.bbox("all")
    canvas.configure(scrollregion = (x1,y1,x2+50,y2))
    
    return canvas
   
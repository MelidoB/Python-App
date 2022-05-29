from tkinter import NW, Y
from PIL import ImageTk, Image


def create_images(canvas, imgs,imgs_pos):
    #if I add more images I need to add more texts in create_texts.py animes_info array
    #also, expand canvas scrollregion in making_space.py
    images_names= ["Ao Ashi.png",
                   "Heroine Tarumono!.jpg",
                   "Gaikotsu Kishi-sama.jpg",
                   "Birdie-Wing.jpg",
                   "Birdie-Wing.jpg",
                   "Gaikotsu Kishi-sama.jpg",
                   "Birdie-Wing.jpg",
                   "Birdie-Wing.jpg",
                   ]
    x = 125
    y = 140

    images_info = []

    for i in images_names:
        images_info.append([x, y,i])
        x+=250
     
    for i in images_info:
        imgs_pos.append([i[0],i[1]])
    '''
    #Just playing
    x = 10
    y = 10

    images_info =[]
    for i in range(10):
        images_info.append([x, y,"img.png"])
        x+=100
        y+=100
    '''
    for img_information in images_info:
        #saving the images so the garbabe collector doesn't remove it
        imgs.append([img_information[0],img_information[1],ImageTk.PhotoImage(Image.open(img_information[2]))]) 
    
    for img in imgs:
        canvas.create_image(img[0],img[1],anchor=NW,image=img[2])
    
    return len(images_info)
    
from place_texts import place_title, place_text

def create_texts(canvas, texts):

    title = [500, 20, "Anime"]
    # if I add new animes I need to add more images in create_images.py images_names array
    # also, expand canvas scrollregion in making_space.py
    animes_info = ["Ao Ashi","Heroine Tarumono!","Gaikotsu Kishi-sama","Birdie Wing","Birdie Wing","Gaikotsu Kishi-sama","Birdie Wing","Birdie Wing"]
    x_coor = 225
    y_coor = 100
    #to add a new anime just make a new list
    #[x-coordinate, y-coordinate, "anime-name"]

    animes = []

    for i in animes_info:
        animes.append([x_coor,y_coor,i])
        x_coor += 250


    y_coor = 380

    amount_of_animes = []
    for i in animes:
        amount_of_animes.append([i[0],y_coor,"0"])


    
    place_title(canvas, title,texts) #setting up tittle
    
    place_text(canvas, animes,texts,False) #setting up animes
    place_text(canvas, amount_of_animes,texts,True) #setting up amount of animes

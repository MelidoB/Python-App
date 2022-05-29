from tkinter import Tk
from aspect_properties import aspect_properties
from making_space import making_space

class Interface:
    def __init__(self):
        self.tk = Tk()
        self.canvas = None

        #storing data here to be able to modify it later
        self.texts = [] #The texts
        self.imgs =  [] #The images
        self.buttons = [] #The buttons

    
    def aspect_config(self):
        aspect_properties(self.tk) #modifying all properties from my window
        self.canvas = making_space(self.tk,self.canvas,self.texts, self.imgs,self.buttons) #Adding text, images,buttons to the window
        
    
           
       
        
        

    
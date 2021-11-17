import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter
import glob
from tkinter import *
from PIL import ImageTk, Image
import os
import sys
import time
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font
from tkinter.scrolledtext import ScrolledText




class color_button(ttk.Combobox):
    def __init__(self, var, master=None):

        self.r=100
        self.g=100
        self.b=100
        self.color="Red"
        li = ['Red', 'Blue', 'Yellow','Green', 'Black', 'White',
              'Gray', 'ivory', 'pink','violet', 'lawngreen', 'gold',     
              'cyan', 'lightgray','brown']     
        super().__init__(master, values=li) 
        
        self.filenames ="WS000232.JPG"
        

        button3= Button(root, text=u'ファイル選択', font=24,command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=950, y=70) 
        
    
        
        
        
        self.var = var                      
        self.bind(                          
            '<<ComboboxSelected>>',
            self.show_selected
            )


    def button3_clicked(self):  

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("JPEG", ".jpg")], initialdir=iDir)

        if(self.filenames != ""):
            button4= Button(root, text=u'表示', font=24,command=self.button4_clicked,bg='#f0e68c')  
            button4.grid(row=0, column=1)  
            button4.place(x=950, y=100) 


    def button4_clicked(self):  
        self.setnumber()


    def show_selected(self, event):
        self.color = self.get()        
    def setnumber(self):
        for file in self.filenames:
            img2 = Image.open(file)
        image2 = img2.convert('RGB')
        width, height = image2.size

        column_step=int(width/40)        
        row_step=int(height/42)
        print(width, height)
        print(column_step,row_step)
                
        column = -1
        row = 0
        for i in range(1121):
            
            if i > 0:
                if i%40 == 1:
                    row += 1 
                    column = -1
                column += 1


                self.r, self.g, self.b = image2.getpixel((column*column_step, row*row_step))

                text=f'{i}'
                btn = tk.Button(root, text="    ")
                btn.grid(column=column, row=row)
                #print(self.from_rgb_to_colorcode((self.r, self.g, self.b)))
                btn.config(command=self.collback(btn),bg=self.from_rgb_to_colorcode((self.r, self.g, self.b)))

    def collback(self,btn):
        def nothing():
            global color
            btn.config(bg=self.color)
        return nothing

    def from_rgb_to_colorcode(self,rgb):
        return "#%02x%02x%02x" % rgb
    def rgb2html(self,R, G, B):
        color_code = '#{}{}{}'.format(hex(R), hex(G), hex(B))
        return color_code.replace('0x', '')
    
    
root = tk.Tk()
root.geometry('1100x750')
root.title("button color test")

var = tk.StringVar(master=root)
l = tk.Label(textvariable=var,font=48)
l.place(x=700,y=750)
c=color_button(master=root, var=var)
c.place(x=950,y=0)
root.mainloop()



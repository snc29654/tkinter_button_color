import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image




class color_button(ttk.Combobox):
    def __init__(self, var, master=None):

        self.r=100
        self.g=100
        self.b=100
        self.color="Red"
        li = ['Red', 'Blue', 'Yellow','Green', 'Black', 'White',
              'Gray', 'ivory', 'pink','violet', 'lawngreen', 'gold',     
              'cyan', 'lightgray']     
        super().__init__(master, values=li) 
        self.var = var                      
        self.bind(                          
            '<<ComboboxSelected>>',
            self.show_selected
            )
    def show_selected(self, event):
        self.color = self.get()        
    def setnumber(self):

        img2 = Image.open("choki3.jpg")
        image2 = img2.convert('RGB')

        column = -1
        row = 0
        for i in range(1001):
            
            if i > 0:
                if i%40 == 1:
                    row += 1 
                    column = -1
                column += 1


                self.r, self.g, self.b = image2.getpixel((column*9, row*15))

                text=f'{i}'
                btn = tk.Button(root, text="    ")
                btn.grid(column=column, row=row)
                btn.config(command=self.collback(btn),bg=self.rgb2html(self.r, self.g, self.b))
        root.mainloop()

    def collback(self,btn):
        def nothing():
            global color
            btn.config(bg=self.color)
        return nothing

    def rgb2html(self,R, G, B):
        color_code = '#{}{}{}'.format(hex(R), hex(G), hex(B))
        return color_code.replace('0x', '')
    
    
root = tk.Tk()
root.geometry('1100x700')
root.title("button color test")

var = tk.StringVar(master=root)
l = tk.Label(textvariable=var,font=48)
l.place(x=700,y=750)
c=color_button(master=root, var=var)
c.place(x=950,y=0)
c.setnumber()



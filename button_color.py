import tkinter as tk
from tkinter import ttk
class color_button(ttk.Combobox):
    def __init__(self, var, master=None):
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
        column = -1
        row = 0
        for i in range(1001):
            if i > 0:
                if i%40 == 1:
                    row += 1 
                    column = -1
                column += 1
                text=f'{i}'
                btn = tk.Button(root, text="    ")
                btn.grid(column=column, row=row)
                btn.config(command=self.collback(btn))
        root.mainloop()

    def collback(self,btn):
        def nothing():
            global color
            btn.config(bg=self.color)
        return nothing
    
    
root = tk.Tk()
root.geometry('1100x700')
root.title("button color test")

var = tk.StringVar(master=root)
l = tk.Label(textvariable=var,font=48)
l.place(x=700,y=750)
c=color_button(master=root, var=var)
c.place(x=950,y=0)
c.setnumber()



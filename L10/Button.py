from tkinter import *
from tkinter import messagebox

def masbox():        
    messagebox.showerror("Message!", "Do not touch this button!")
        
master = Tk()
master.title('MessageBox')
Label(master, text = 'Push the button', font =('Verdana', 15)).pack(side = TOP, pady = 10) 
photo = PhotoImage(file = r"C:\Users\AShoom\Desktop\ShoomPython\CutCalcul_byPy\L10\image.png")
Button(master, text= 'clik mi', fg= 'black', font= 'Arial 14', width= 167,bg='yellow',
       image = photo, compound = LEFT, command=lambda : masbox()).pack(side = TOP)
Button(master, text='XAXAXO', width= 15, bg='red', fg='white',font='Arial 14',
       command=lambda: masbox()).pack(side = TOP, pady = 10)

mainloop()

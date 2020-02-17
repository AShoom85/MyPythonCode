from tkinter import *
from tkinter import messagebox

def masbox():        
    messagebox.showerror("Message!", "Don't touch this button!")
        
master = Tk()
master.title('MessageBox')
Label(master, text = 'PUSH THE BUTTON', font =('Verdana', 15), fg= 'red').pack(side = TOP, pady = 10) 
photo = PhotoImage(file = r"C:\Users\AShoom\Desktop\ShoomPython\CutCalcul_byPy\L10\image.png")
Button(master, text= 'click on me', fg= 'black', font= 'Arial 14', width= 211,bg='yellow',
       image = photo, compound = LEFT, command=lambda : masbox()).pack(side = TOP)
Button(master, text='XAXAXO', width= 19, bg='red', fg='white',font='Arial 14',
       command=lambda: masbox()).pack(side = TOP, pady = 10)

mainloop()

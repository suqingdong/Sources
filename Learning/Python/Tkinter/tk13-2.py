from tkinter import *

root = Tk()

Label(root, text='red', bg='red', fg='white').pack(fill=X) #side=LEFT 横向填充
Label(root, text='green', bg='green', fg='black').pack(fill=X)
Label(root, text='blue', bg='blue', fg='white').pack(fill=X)


mainloop()
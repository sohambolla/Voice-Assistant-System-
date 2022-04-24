from tkinter import *
import newone as new
import click
from PIL import ImageTk,Image

root = Tk()

root.title('APSIT')
root.geometry('520x320')

img = ImageTk.PhotoImage(Image.open('A1.png'))
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')

userText = StringVar()

userText.set('Your Virtual Assistant ')
userFrame = LabelFrame(root, text='APSIT',font=('Railways',24,'bold'))
userFrame.pack(fill='both', expand='yes')

top = Message(userFrame, textvariable=userText, bg='black', fg='white')
top.config(font=("Century Gothic",15, 'bold'))
top.pack(side='top',fill='both', expand='yes')

def chnagePage():
    new.takecommand()
btn1 = Button(root, text='Run', font=('railways', 10, 'bold'),bg='red', fg='white', command=chnagePage()).pack(fill='x', expand='no')

btn2 = Button(root, text='close', font=('railways', 10, 'bold'),bg='#f5bc42', fg='black', command=root.destroy).pack(fill='x',expand='no')




root.mainloop()

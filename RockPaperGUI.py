from tkinter import *
import tkinter.messagebox
from random import randint
#from PIL import Image

root = Tk()
#intialize
class myGame():
    cwin=0
    pwin=0
    rand = randint(0,2)
    l = ['Rock','Paper','Scissor'] 
    computer = l[rand]

    def Rock(self):

        if(self.computer=='Paper'):
            Label(root,bg='skyblue',text='Computer Win Paper wraps Rock').grid(row=6,column=1)
            self.cwin+=1
            Label(root,text=self.cwin).grid(row=9,column=2)
        else:
            Label(root,bg='skyblue',text='Player Win Rock smashes Paper').grid(row=6,column=1)
            self.pwin+=1
            Label(root,text=self.pwin).grid(row=8,column=2)
    def Paper(self):
        if(self.computer=='Scissor'):
            Label(root,bg='skyblue',text='Computer Win Paper wraps Rock').grid(row=6,column=1)
            self.cwin+=1
            Label(root,text=self.cwin).grid(row=9,column=2)
        else:
            Label(root,bg='skyblue',text='Player Win Rock smashes Paper').grid(row=6,column=1)
            self.pwin+=1
            Label(root,text=self.pwin).grid(row=8,column=2)
    def Scissor(self):
        if(self.computer=='Rock'):
            Label(root,bg='skyblue',text='Computer Win Paper wraps Rock').grid(row=6,column=1)
            self.cwin+=1
            Label(root,text=self.cwin).grid(row=9,column=2)
        else:
            Label(root,bg='skyblue',text='Player Win Rock smashes Paper').grid(row=6,column=1)
            self.pwin+=1
            Label(root,text=self.pwin).grid(row=8,column=2)

    def declarWinner(self):
        if(self.pwin==10 and self.cwin<10):
            tkinter.messagebox.showinfo("Player Win The match")
            root.destroy
        elif(self.cwin==10 and self.pwin<10):
            tkinter.messagebox.showinfo("Player Win The match")
            root.destroy
    

m = myGame() 
Label(root,text='Choose to play').grid(row=1,column=1)
Button(root,text='Rock',bg='blue',width=30,command=m.Rock).grid(row=3,column=20)
Button(root,text='Paper',bg='Green',width=30,command=m.Paper).grid(row=4,column=22)
Button(root,text='Scisor',bg='Blue',width=30,comman=m.Scissor).grid(row=5,column=24)
m.declarWinner()



Label(root,text="Player Win:").grid(row=8,column=1)
Label(root,text="Computer Win:").grid(row=9,column=1)


mainloop()

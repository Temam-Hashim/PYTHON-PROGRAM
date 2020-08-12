from tkinter import *
import tkinter.messagebox
import random  as r
onclick = True
computer = ''


root = Tk()
root.title("TICK TACK TOE")
root.geometry("1600x800") 
def reset():
    b1['text']=''
    b2['text']=''
    b3['text']=''
    b4['text']=''
    b5['text']=''
    b6['text']=''
    b7['text']=''
    b8['text']=''
    b9['text']=''
m = Menu(root)
root.config(menu=m)
gameMenu = Menu(m)
m.add_cascade(label='Game Sitting',font=('Times 17 bold'),menu=gameMenu)
gameMenu.add_command(label='Play With Friend',font=('Times 10 bold'),command='')
gameMenu.add_command(label='Play with computer',font=('Times 10 bold'),command='')
gameMenu.add_command(label='Start New Game',font=('Times 10 bold'),command=reset)
gameMenu.add_command(label='Exit',font=('Times 10 bold'),command=root.destroy)
#function
class Play():
  xwin = 0
  ywin = 0

  def game(self,buttons):
    global onclick
  
    # rand = r.randint(0,8)
    # l = [b1,b2,b3,b4,b5,b6,b7,b8,b9] 

    # if(buttons['text']=='' and onclick==True):
    #   buttons['text'] = 'X'
    #   onclick=False
    # elif(buttons['text']=='' and computer=='' and onclick==False):
    #     computer = l[rand]
    #     computer = 'Y'
    #     onclick=True

    if(buttons['text']=='' and onclick==True):
      buttons['text']='X'
      onclick = False
    elif(buttons['text']=='' and onclick==False ):
      buttons['text']='Y'
      onclick = True

      #first 3 is Horiz, 2nd 3 is Vert last 2 is diagonal
    if( b1['text']=='X' and b2['text']=='X' and b3['text']=='X' or
        b4['text']=='X' and b5['text']=='X' and b6['text']=='X' or
        b7['text']=='X' and b8['text']=='X' and b9['text']=='X' or
        b1['text']=='X' and b4['text']=='X' and b7['text']=='X' or
        b2['text']=='X' and b5['text']=='X' and b8['text']=='X' or
        b3['text']=='X' and b6['text']=='X' and b9['text']=='X' or
        b1['text']=='X' and b5['text']=='X' and b9['text']=='X' or
        b3['text']=='X' and b5['text']=='X' and b7['text']=='X' ):
      self.xwin+=1
      tkinter.messagebox.showinfo("Declare The Winner","Player X win!!")
      Label(root,text = self.xwin,font = ('Times 20 bold')).grid(row=1,column=2)
      reset()
    elif( b1['text']=='Y' and b2['text']=='Y' and b3['text']=='Y' or
        b4['text']=='Y' and b5['text']=='Y' and b6['text']=='Y' or
        b7['text']=='Y' and b8['text']=='Y' and b9['text']=='Y' or
        b1['text']=='Y' and b4['text']=='Y' and b7['text']=='Y' or
        b2['text']=='Y' and b5['text']=='Y' and b8['text']=='Y' or
        b3['text']=='Y' and b6['text']=='Y' and b9['text']=='Y' or
        b1['text']=='Y' and b5['text']=='Y' and b9['text']=='Y' or
        b3['text']=='Y' and b5['text']=='Y' and b7['text']=='Y' ):
      self.ywin+=1
      tkinter.messagebox.showinfo("Declare the Winner","Player Y win!!")
      Label(root,text = self.ywin,font = ('Times 20 bold')).grid(row=2,column=2)
      reset()
    # else:
    #   tkinter.messagebox.showinfo("Game Draw","No Winner Game TIE")

  


#play command
cmd=Label(root,text='Click The Button until you form similar letter  Line',fg='blue', font=('Times 20 bold'))
cmd.grid(row=0,column=1)
#result desplay
x = Label(root,text="Player X Win:",font = ('Times 20 bold'))
x.grid(row = 1,column=1)
y = Label(root,text="Player Y Win:",font = ('Times 20 bold'))
y.grid(row = 2,column=1)



#set buttons to string variable
buttons = StringVar()
#call class
p = Play()
#row 1
b1 = Button(root,bd=4, cursor='hand2',font =('Times 25 bold'), bg='skyblue',width=10,command=lambda:p.game(b1))
b1.grid(row=3,column=2)
b2 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b2))
b2.grid(row=3,column=3)
b3 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b3))
b3.grid(row=3,column=4)
# row  2
b4 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b4))
b4.grid(row=4,column=2)
b5 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b5))
b5.grid(row=4,column=3)
b6 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b6))
b6.grid(row=4,column=4)
# row 3
b7 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b7))
b7.grid(row=5,column=2)
b8 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b8))
b8.grid(row=5,column=3)
b9 = Button(root,bd=4,cursor='hand2',font =('Times 25 bold'),bg='skyblue',width=10,command=lambda:p.game(b9))
b9.grid(row=5,column=4)

resetbutton = Button(root,bd=4,cursor='hand2',text='Reset To Play Again',font =('Times 13 bold'),bg='blue',width=20,command=reset)
resetbutton.grid(row=7,column=3)


root.mainloop()

#buttonList = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
# def Play():
#   global onclick
#   if(b1['text']=='' and onclick==True):
#     b1['text']='X'
#     onclick = False
#   elif(b1['text']=='' and onclick==False):
#     b1['text']='Y'
#     onclick = True
#   if(b2['text']=='' and onclick==True):
#     b2['text']='X'
#     onclick = False
#   elif(b1['text']=='' and onclick==False):
#     b1['text']='Y'
#     onclick = True
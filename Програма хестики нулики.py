from tkinter.messagebox import showinfo
from contextlib import closing
from idlelib.pyshell import restart_line
from tkinter import *
app=Tk()

ww=0
w=[0,0,0,0,0,0,0,0,0]
icon = PhotoImage(file="Хр ну.png")
app.iconphoto(True, icon)
app.title('Хрестики нулики')
app.geometry('622x750+640+133')
app['bg']='#696969'
app.resizable(False,False)
color='red'
def click(button,namber):
    global color,ww,w
    button.config(bg=color)
    w[namber] = color
    print(w)
    if color=='red':
        color='blue'
    else:
        color='red'
    button.config(state='disabled')
    if w[0]==w[1]==w[2]!=0:
        ww=w[0]
        print("win!!!")
    if w[0]==w[4]==w[8]!=0:
        ww=w[0]
        print("win!!!")
    if w[3]==w[4]==w[5]!=0:
        ww = w[3]
        print("win!!!")
    if w[6]==w[7]==w[8]!=0:
        ww = w[6]
        print("win!!!")
    if w[0] == w[3] == w[6] != 0:
        ww = w[3]
        print("win!!!")
    if w[1]==w[4]==w[7]!=0:
        ww = w[1]
        print("win!!!")
    if w[2]==w[5]==w[8]!=0:
        ww = w[2]
        print("win!!!")
    if w[0]==w[4]==w[8]!=0:
        ww = w[4]
        print("win!!!")
    if w[2]==w[4]==w[6]!=0:
        ww = w[6]
        print("win!!!")
    if 0 not in w:
        showinfo('результат', 'нічия')
        print('нічия')
        button1.config(bg='white')
        button2.config(bg='white')
        button3.config(bg='white')
        button4.config(bg='white')
        button5.config(bg='white')
        button6.config(bg='white')
        button7.config(bg='white')
        button8.config(bg='white')
        button9.config(bg='white')
        button1.config(state='normal')
        button2.config(state='normal')
        button3.config(state='normal')
        button4.config(state='normal')
        button5.config(state='normal')
        button6.config(state='normal')
        button7.config(state='normal')
        button8.config(state='normal')
        button9.config(state='normal')
        w = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ww = 0
    if ww!=0:
        if ww=='red':
            showinfo('результат', 'перемога червоних')
        else:
            showinfo('результат', 'перемога синіх')
        button1.config(bg='white')
        button2.config(bg='white')
        button3.config(bg='white')
        button4.config(bg='white')
        button5.config(bg='white')
        button6.config(bg='white')
        button7.config(bg='white')
        button8.config(bg='white')
        button9.config(bg='white')
        button1.config(state='normal')
        button2.config(state='normal')
        button3.config(state='normal')
        button4.config(state='normal')
        button5.config(state='normal')
        button6.config(state='normal')
        button7.config(state='normal')
        button8.config(state='normal')
        button9.config(state='normal')
        w=[0,0,0,0,0,0,0,0,0]
        ww=0
button1 = Button(text=1, width=20, height=10)
button1.config(command=lambda :click(button1,0))
button1.place(x=15,y=15)
button2=Button(text=2,width=20,height=10)
button2.config(command=lambda :click(button2,1))
button2.place(x=200,y=15)
button3=Button(text=3,width=20,height=10)
button3.config(command=lambda :click(button3,2))
button3.place(x=385,y=15)
button4=Button(text=4,width=20,height=10)
button4.config(command=lambda :click(button4,3))
button4.place(x=15,y=230)
button5=Button(text=5,width=20,height=10)
button5.config(command=lambda :click(button5,4))
button5.place(x=200,y=230)
button6=Button(text=6,width=20,height=10)
button6.config(command=lambda :click(button6,5))
button6.place(x=385,y=230)
button7=Button(text=7,width=20,height=10)
button7.config(command=lambda :click(button7,6))
button7.place(x=15,y=445)
button8=Button(text=8,width=20,height=10)
button8.config(command=lambda :click(button8,7))
button8.place(x=200,y=445)
button9=Button(text=9,width=20,height=10)
button9.config(command=lambda :click(button9,8))
button9.place(x=385,y=445)
app.bind('1',lambda e:click(button1,0))
app.bind('2',lambda e:click(button2,1))
app.bind('3',lambda e:click(button3,2))
app.bind('4',lambda e:click(button4,3))
app.bind('5',lambda e:click(button5,4))
app.bind('6',lambda e:click(button6,5))
app.bind('7',lambda e:click(button7,6))
app.bind('8',lambda e:click(button8,7))
app.bind('9',lambda e:click(button9,8))
app.mainloop()
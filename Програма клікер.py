from contextlib import closing
from tkinter import *
app=Tk()

app1=None
icon = PhotoImage(file="icon.png")
app.iconphoto(True, icon)
s=['#FF2900','#00FF15','#00FFFF','#0000FF','#F700FF']
s2=0
app.title('Клікер')
app.geometry('1000x500+270+100')
app['bg']='#00CDFF'
def on_closing():
    global app1
    app1.destroy()
    app1=None
app.resizable(False,False)
b=0
d=1
def click():
    global b,s2,nix,d,app1
    if b==19:
        def click2():
            global app1,buy_button
            if app1==None:
                app1 = Toplevel(app)
                app1['bg'] = 'yellow'
                app1.geometry('265x185+600+200')
                app1.title('buy')
                app1.resizable(False,False)
                nix2 = Label(app1,text='Do you buy *5 click for 500 clicks?')
                nix2.place(x=15, y=15)
                def click4():
                    app1.destroy()
                    b += 5
                def click3():
                    click5=Button(app,text='click*5', width=20,height=10,font=('Arial',20,'bold'),command=click4)
                    click5.place(x=320,y=85)
                buy_button=Button(app1,text='buy', width=13,height=5,font=('Arial',10,'bold'),command=click3)
                buy_button.place(x=76,y=55)
                app1.protocol("WM_DELETE_WINDOW", on_closing)
    if b > 99 and d == 1:
        b -= 100
        b += 1
        button2 = Button(text='Click*2', width=20, height=10, font=('Arial', 20, 'bold'), command=click)
        button2.place(x=320, y=85)
        d=2
    if b==19:
        global nix2
        button3 =Button(text='Click*5',width=6,height=2, font=('Arial', 20, 'bold'), command=click2)
        button3.place(x=5, y=60)
    b += d
    print(b)
    nix['text'] = b
    if b%10==0:
        s2+=1
        if s2==len(s):
            s2=0
        app['bg'] =s[s2]
button = Button(text='Click Me', width=20,height=10,font=('Arial',20,'bold'),command=click)
button.place(x=320,y=85)
nix=Label (text='Score')
nix.place(x=20,y=20)


app.mainloop()
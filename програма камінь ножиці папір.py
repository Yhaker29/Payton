from tkinter.messagebox import showinfo
from contextlib import closing
from idlelib.pyshell import restart_line
import random
from tkinter import *
app=Tk()
icon = PhotoImage(file="кам нож пап.png")
app.iconphoto(True, icon)
app.title('Камінь ножиці папір')
app.geometry('900x622+640+133')
app['bg']='#696969'
# app.resizable(False,False)

def computer_choice():
    a=random.randint(1, 3)
    if a == 1:
        return ':камінь'
    if a==2:
        return ':ножиці'
    if a==3:
        return ':папір'
def click(yzer_choise,button):
    камінь ['bg']='white'
    nogiti ['bg']='white'
    paper ['bg']='white'
    computer=computer_choice()
    wibir['text']='вибір компюнтера'+computer
    print(yzer_choise)
    if computer==':папір':
        if yzer_choise=='ножиці':
            print('ви перемогли!')
            resultat['text'] = 'результат:' +'ви перемогли!'
            app['bg'] = '#00FF08'
        elif yzer_choise=="папір":
            print('нічія!')
            resultat['text'] = 'результат:' +'нічія!'
            app['bg'] = 'yellow'
        elif yzer_choise=="камінь":
            print('ви програли!')
            resultat['text'] = 'результат:' +'ви перемогли!'
            app['bg'] = '#00FF00'
    if computer==':ножиці':
        if yzer_choise=='папір':
            print('ви програли!')
            resultat['text'] = 'результат:' +'ви програли!'
            app['bg'] = 'red'
        elif yzer_choise=='ножиці':
            print('нічія!')
            resultat['text'] = 'результат:' +'нічія!'
            app['bg'] = 'yellow'
        elif yzer_choise=='камінь':
            print('ви програли!')
            resultat['text'] = 'результат:' +'ви програли!'
            app['bg'] = 'red'
    if computer==':камінь':
        if yzer_choise=='папір':
            print('ви перемогли!')
            resultat['text'] = 'результат:' +'ви перемогли!'
            app['bg']='#00FF08'
        elif yzer_choise=='камінь':
            print('нічія!')
            resultat['text'] = 'результат:' + 'нічія!'
            app['bg'] = 'yellow'
        elif yzer_choise=='ножиці':
            print('ви програли!')
            resultat['text'] = 'результат:' +'ви програли!'
            app['bg'] = 'red'
    button['bg']='blue'
камінь=Button(text='камінь',width=20,height=4,font=('Arial',10,'bold'),command=lambda:click(камінь['text'],камінь))
камінь.place(x=60,y=490)
nogiti=Button(text='ножиці',width=20,height=4,font=('Arial',10,'bold'),command=lambda:click(nogiti['text'],nogiti))
nogiti.place(x=340,y=490)
paper=Button(text='папір',width=20,height=4,font=('Arial',10,'bold'),command=lambda:click(paper['text'],paper))
paper.place(x=619,y=490)
wibir=Label(text='вибір компюнтера',width=30,height=4)
wibir.place(x=290,y=5)
resultat=Label(text='результат',width=20,height=4)
resultat.place(x=340,y=300)


app.mainloop()
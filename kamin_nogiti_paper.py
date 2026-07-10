from tkinter.messagebox import showinfo
from contextlib import closing
from tkinter import *
import random
from tkinter import *
app=Tk()
icon = PhotoImage(file="image.png")
app.iconphoto(True, icon)
app.title('Камінь ножиці папір')
app.geometry('900x622+640+133')
app['bg']='#696969'
app.resizable(False,False)

showinfo('Життя', 'У вас є 3 життя')
heart=3
wins_record=0
wins=0
def computer_choice():
    a=random.randint(1, 3)
    if a == 1:
        return ':камінь'
    if a==2:
        return ':ножиці'
    if a==3:
        return ':папір'
def click(yzer_choise,button):
    global wins,wins_record,heart
    камінь ['bg']='white'
    nogiti ['bg']='white'
    paper ['bg']='white'
    computer=computer_choice()
    wibir['text']='вибір компюнтера'+computer
    wins_label['text'] = 'перемог:' + str (wins)
    wins_record_label['text'] = 'рекорд:' + str(wins_record)
    print(yzer_choise)
    print(wins)
    print(heart)
    if computer==':папір':
        if yzer_choise=='ножиці':
            print('ви перемогли!')
            wins += 1
            resultat['text'] = 'результат:' +'ви перемогли!'
            app['bg'] = '#00FF08'
        elif yzer_choise=="папір":
            print('нічія!')
            resultat['text'] = 'результат:' +'нічія!'
            app['bg'] = 'yellow'
        elif yzer_choise=="камінь":
            print('ви програли!')
            heart-=1
            if heart == 0:
                showinfo('Життя', 'Ви програли!')
            if wins>wins_record:
                wins_record=wins
                wins_record_label['text'] = 'рекорд:' + str(wins_record)
            resultat['text'] = 'результат:' +'ви програли!'
            app['bg'] = 'red'
    if computer==':ножиці':
        if yzer_choise=='папір':
            print('ви програли!')
            heart -= 1
            if heart == 0:
                showinfo('Життя', 'Ви програли!')
            if wins>wins_record:
                wins_record=wins
                wins_record_label['text'] = 'рекорд:' + str(wins_record)
            resultat['text'] = 'результат:' +'ви програли!'
            app['bg'] = 'red'
        elif yzer_choise=='ножиці':
            print('нічія!')
            resultat['text'] = 'результат:' +'нічія!'
            app['bg'] = 'yellow'
        elif yzer_choise=='камінь':
            print('ви перемогли!')
            wins += 1
            resultat['text'] = 'результат:' +'ви перемогли!'
            app['bg'] = '#00FF08'
    if computer==':камінь':
        if yzer_choise=='папір':
            print('ви перемогли!')
            wins+=1
            resultat['text'] = 'результат:' +'ви перемогли!'
            app['bg']='#00FF08'
        elif yzer_choise=='камінь':
            print('нічія!')
            resultat['text'] = 'результат:' + 'нічія!'
            app['bg'] = 'yellow'
        elif yzer_choise=='ножиці':
            print('ви програли!')
            heart -= 1
            if heart == 0:
                showinfo('Життя', 'Ви програли!')
            if wins>wins_record:
                wins_record=wins
                wins_record_label['text'] = 'рекорд:' + str(wins_record)
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
wins_label=Label(text='перемог 0',width=20,height=4)
wins_label.place(x=10,y=5)
wins_record_label=Label(text='рекорд',width=20,height=4)
wins_record_label.place(x=720,y=5)

app.mainloop()
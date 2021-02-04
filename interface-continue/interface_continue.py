from random import shuffle
from tkinter import *
from tkinter import ttk
import random
from tkinter.filedialog import *
from tkinter import scrolledtext
import sys
from tkinter.messagebox import *
import sys, fileinput

mas4=[0]
a=input('Ввидите имя ')

fail = open("voprosi.txt", "r", encoding='UTF-8')
mas1 = []
mas2 = []
for line in fail:
    n = line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(str(line[n+1:len(line)].strip()))
fail.close()

del mas1[1::2]
del mas2[1::2]


shuffle(mas1)                  #Перемешивает список
del mas1[6:16]                 #Удаляет всё с 6 по 15 позицию

root=Tk()
root.geometry("700x600")
root.title('Опросник')
tabs=ttk.Notebook(root)
tabs_list=[]

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=0)
M.add_cascade(label='Вопросы',menu=m1)

l1 = Label(text=mas1[0], font="Arial 11")
l1.config(bd=30)
l1.pack()

l1 = Label(text=mas1[1], font="Arial 11")
l1.config(bd=30)
l1.pack()

l1 = Label(text=mas1[2], font="Arial 11")
l1.config(bd=30)
l1.pack()

l1 = Label(text=mas1[3], font="Arial 11")
l1.config(bd=30)
l1.pack()

l1 = Label(text=mas1[4], font="Arial 11")
l1.config(bd=30)
l1.pack()


def activated():                            #добавляет 1 правильный ответ
    mas4[0]+=1
    print(mas4,'gg')


def save_():
    file=asksaveasfile(mode='w',defaultextension=(('.txt')),filetypes=(('Notepad','.txt')))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()


#txt_box=scrolledtext.ScrolledText(width=40,height=5)     #Штука куда можно вводить имя
#txt_box.pack
#btn_save=Button(text='Save',command=save_)
#btn_save.pack


tab1 = Frame(tabs)
tab2 = Frame(tabs)
tab3 = Frame(tabs)
tab4 = Frame(tabs)
tab5 = Frame(tabs)


tabs.add(tab1, text='первый')                #Вкладки с кнопочками
tabs.add(tab2, text='второй')
tabs.add(tab3, text='третий')
tabs.add(tab4, text='четвёртый')
tabs.add(tab5, text='пятый')


lbl1 = Label(tab1)
lbl1.grid(column=0, row=0)
btn = Button(tab1, text="да",command=activated)
btn.grid(column=1, row=0)
btn1 = Button(tab1, text="нет")
btn1.grid(column=2, row=0)

lbl1 = Label(tab2)
lbl1.grid(column=0, row=0)
btn = Button(tab2, text="да",command=activated)
btn.grid(column=1, row=0)
btn1 = Button(tab2, text="нет")
btn1.grid(column=2, row=0)

lbl1 = Label(tab3)
lbl1.grid(column=0, row=0)
btn = Button(tab3, text="да",command=activated)
btn.grid(column=1, row=0)
btn1 = Button(tab3, text="нет")
btn1.grid(column=2, row=0)

lbl1 = Label(tab4)
lbl1.grid(column=0, row=0)
btn = Button(tab4, text="да",command=activated)
btn.grid(column=1, row=0)
btn1 = Button(tab4, text="нет")
btn1.grid(column=2, row=0)

lbl1 = Label(tab5)
lbl1.grid(column=0, row=0)
btn = Button(tab5, text="да",command=activated)
btn.grid(column=1, row=0)
btn1 = Button(tab5, text="нет")
btn1.grid(column=2, row=0)
tabs.pack(fill='both')
root.mainloop()


if mas4[0] >= int('3'):
    fail = open("oiged.txt", "a", encoding='UTF-8')
    fail.write (a)
    fail.write('Прошёл')
    fail.close()
    print('dobavlen')
else:
    fail = open("valed.txt", "a", encoding='UTF-8')
    fail.write(a)
    fail.write('не Прошёл')
    fail.close()
    print('ne dobavlen')

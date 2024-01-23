#Задание 2
    print ("Hello world") #Команда принт

#Задание 3
    a = 3
    print(type(a)) #int – целочисленный тип
    a = 3.5
    print(type(a)) #float – вещественный
    a = 'qwerty'
    print(type(a)) #str – строчный
    a = True
    print(type(a)) #bool – логический
    a = '123'
    print(type(a)) #str – строчный
#Мы не можем складывать строчный и целочисленный тип

#Задание 4
    a = 5.7
    print(int(a)) #первая задача
    a = -5.7
    print(int(a)) #вторая задача
    a = 3**39 - int(float(3**39))
    print(a) #третья задача (11)

#Задание 5
    a = input('Как ваше имя? ')
    print('Добро пожаловать домой,',a,'!') #инпут

#Задание 6
    x = int(input('Количество часов до частной клиники: '))
    y = int(input('Количество минут до поликлиники: '))
    m = sum(x * 60 + y for m in range(2)) #Выражение - генератор
    print ('Итого минут: ',m)

#Задача 7
    a = False
    b = True
    c = False
    print (not a or b and c) #задание 1 (выходит True)
    print (not (a or b) and c) #задание 2 (выходит False)

#Задача 8
    a = int(input('Введите год рождения: '))
    if a < 1900 or a > 3000:  # Выборка
        print('Год не подходит в выборку.')
    elif a % 4 != 0 or a % 100 == 0:  # Исключаем невисокосные года
        print('Обычный год :(')
    else:
        print('С днём рождения!:)')

#Задача 9
    a = 1
    while a <= 20:
        if a % 2 == 0: #Остаток от деления на 2
            print(a, end=' ') #Ставим в конец через пробел
    a += 1
    #Только когда написал,заметил, что код похожий :)

#Задача 10
    a=1
    b=0
    while a !=0: #цикл, пока а не равно нулю
        a = int(input('Введите число: '))
        b=b+a
    print(b)

#Задача 11
    x = int(input('Количество коллег в клинике: '))
    y = int(input('Количество коллег в поликлинике: '))
    a = 2
    while a % y != 0 or a % x != 0:  # Цикл для нахождения НОК
        a += 1
    print('Нужно кусков: ',a)

#Задача 12
    a=0
    for a in range(1,20+1): #цикл for
        if a%2 == 0: #проверка на четность
            print(a, end=' ')
    a +=1

#Задача 13
    a = int(input('Введите значение: '))
    b = int(input('Введите значение: '))
    c = int(input('Введите значение: '))
    d = int(input('Введите значение: '))
    print('', end='\t')  # Первый отступ, пустой
    for j in range(c, d + 1):  # Первый ряд чисел
        print(j, end='\t')
    print()  # Переход на следующий ряд
    for i in range(a, b + 1):  # Для данного ряда чисел
        print(i, end='\t')
        for j in range(c, d + 1):
            print(i * j, end='\t')  # Умножаем 2 числа
    print()

#Задача 14
    n = int(input('Введите значение матрицы: '))
    a = [[0] * n for i in range(n)]
    count = 0
    for i in range(n):   # заполнение 1 строки
        count += 1
        a[0][i] = count
    j = 0
    i = n-1
    n -= 1  # устанавливаем размер 1 блока 1 витка
    while len(a)**2 != count:  #условие выхода из цикла
        for k in range(n):  #движение вниз
            j += 1
            count += 1
            a[j][i] = count
        for k in range(n):  #движение влево
            i -= 1
            count += 1
            a[j][i] = count
        for k in range(n-1):  #движение вверх
            j -= 1
            count += 1
            a[j][i] = count
        for k in range(n-1): #движение вправо
            i += 1
            count += 1
            a[j][i] = count
        n -= 2    # обеспечиваем переход на внутренний виток
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

#Задача 15
    import time
    from tkinter import messagebox

    while True: #Цикл для бесконечности
        time.sleep(10) #Каждые 10 секунд
        if __name__ == '__main__':
            messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')

#Задача 16
import time
from tkinter import *

def main_window(): #функция созданий главного окна, здесь лежит весь код окна: кнопки, текст и т.д.
    global window
    window= Tk() #создание окна
    window.title('Будильник') #заголовок окна
    window.geometry('400x200') #размеры окна
    lbl = Label(window, text='Вы долго смотрели в монитор,\n теперь посмотрите в окно.', font=('Arial Bold', 14))
    lbl.grid(column=0, row=0)

    btn1 = Button(window, text='Перезапустить', command=clicked1)
    btn2 = Button(window, text='Выход', command=clicked2)

    btn1.grid(column=0, row=1)
    btn2.grid(column=1, row=1)
    window.mainloop()  # бесконечный цикл окна, окно ждёт нажатий

def clicked1(): #функция убивает главное окно, затем снова вызывает его и оно вновь появляется
    window.destroy()
    time.sleep(10)
    main_window()

def clicked2():
    quit()

if __name__ == '__main__': #первично вызываем главное окно при включении программы
    main_window()
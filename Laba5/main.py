#Задание 1
b = input('Введите строку: ')
b = b.lower() #Делаем нижний регистр
b = b.replace(' ','') #Убираем лишние пробелы
if b == b[::-1]:
    print('Да')
else:
    print('Нет')

#Задание 2
m = []
s = ['end'] #ключ стопер
while True:
    n = input().split() #аутпут сплит
    if n == s:
        break
    else:
        k = min(n, key=int) #поиск минимального
        m.append(k)
for i in m: #вывод
    print(i)


#Задание 3
m = [] #список
d = {} #словарь
n = str(input())
m.append([str(s.lower()) for s in n.split()])
li, lj = len(m), len(m[0])
for i in range(li):
    for j in range(lj):
        p = m[i][j]
        if p in d:
            d[p]+=1
        else:
            d[p] = 1
for key,value in d.items():
   print(key,value)

#Задание 4
import pymysql

connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='pass',
    database='my_db'
)

cur = connect.cursor()
year= int(input('Введите год: '))
s = year
cur.execute(' select first_name,last_name,date_of_birth from user where year(date_of_birth) = %s',s)
for rec in cur:
    print(rec[0],rec[1],rec[2])
from django.shortcuts import render
from django.http import HttpResponseRedirect
from manage import cursor
from .forms import NameForm
from .models import SearchingUsers

# Create your views here.
# создание формы ввода
def get_name(request):
    # если это запрос POST, нам нужно обработать данные формы
    print('Получен метод запроса: ', request.method)
    if request.method == 'POST':
        # создать экземпляр формы и заполнить данным из web-запроса
        form = NameForm(request.POST)
        print('Сырые данные: ', request.POST)

        if form.is_valid():
            print('Введенное значение: ', form.cleaned_data['user_name'])
            # сохраним значение из формы в модель данных django
            SearchingUsers.ByName = form.cleaned_data['user_name']
            # перенаправляем по адресу search
            return HttpResponseRedirect('user/search')
        else:
            print('Form is not valid')

    # Если GET (или любой другой метод), мы создадим пустую форму
    else:
        form = NameForm()

    return render(request, 'users/index.html', {'form': form})

# запрос данных из БД
def user_by_name(request):
    print('Получили: ', SearchingUsers.ByName)
    # получим значение из модели и обрамляем в % так как будем искать вхождение подстроки
    substring = '%' + SearchingUsers.ByName + '%'
    # формирование запроса
    sql = "select first_name, last_name, date_of_birth from user where first_name like %s order by first_name"
    # выполнение запроса к БД
    cursor.execute(sql, substring)
    # объявление пустого списка
    user_info = list()

    # формируем список из подсписков,
    # где один подсписок - имя, фамилия, дата рождения.
    for r in cursor:
        #print(r[0], r[1], '\t', r[2])
        #user_info = str(r[0]) + str(r[1]) + str(r[2])
        sublist = [[r[0], r[1], str(r[2])]]
        user_info += sublist

    # открываем страницу с результатами
    return render(request, 'users/results.html',
                  {'user': user_info, 'substring': substring})
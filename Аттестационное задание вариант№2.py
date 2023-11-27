﻿#Программа оперирует списком(массивом) объектов класса Checks.
#Класс Checks имеет следующие свойства: флаг отмены чека, дата время создания чека,  список товаров в чеке. А также имеет один метод add_Tovar: добавление очередного товара в чек.
#При добавлении товара в чек класс разделяет строку на два элемента: наименование и цена.
#from datetime import datetime


class Checks:
    def __init__(self, Otkat: bool):
        self.Otkat=Otkat #флаг отмены чека 1=отменен
        #self.Data=datetime.now() #дата время создания чека
        self.spisok: spisok=[] #список товаров в чеке

    def add_Tovar(self, Tovar: str): #добавление очередного товара в чек
        if Tovar.find("-")<=0: #Проверка на корректность ввода Товар-цена
            print("Введенное строка не соответсвует шаблону Товар-цена. Введите еще раз")
        else:
            strTovar=Tovar[:Tovar.find("-")]
        try:
            cenaTovara=float(Tovar[Tovar.find("-")+1:])
            self.spisok.append([strTovar,cenaTovara]) # список товаров состоит из двух элементов Наименование, Цена
        except ValueError:
            print("Введенная цена не является числом. Введите еще раз")



deisvie=0

List_Checs=[] #Список чеков
while deisvie!=4:
    print("1-Новый чек; 2-Просмотр статистики; 3-Отмена операции (отмена последнего чека); 4-Выход")
    
    try:
        deisvie=int(input())                                                                                 
    except ValueError: #Обработка ошибки,если мы ввели что-то не то...
        deisvie=0
        print("Введите число от 1 до 4. Введите еще раз")
            
    if deisvie==1:#Новый чек
        Check=Checks(0)
        print("Введите Товар-цена, например Хлеб-50. В конце <ENTER>")
        Tovar=str(input()) 
        while len(Tovar)>0: #Пока строка товар-цена непустая.
            Check.add_Tovar(Tovar) #Наполняем чек.
            Tovar=str(input())
        List_Checs.append(Check) #По окончании добавили чек в список.
        
    if deisvie==2: #Просмотр Статистики
        CountTovar=0 #Количество проданных товаров всего
        CountOtkat=0 #Количество отменённых чеков
        SummVyruchka=0 #Общая выручка
        List_Tovar=[] #Список проданных товаров по наименованию
        List_CountTovar=[] #Колличество проданных товаров по наименованию
        List_SummTovar=[] #Стоимость проданных товаров по наименованию
        for i in range(len(List_Checs)):
            if not(List_Checs[i].Otkat):
                CountTovar=CountTovar+len(List_Checs[i].spisok) #Подсчитываем количество проданных товаров всего.
                for j in range(len(List_Checs[i].spisok)):
                    Tovar=List_Checs[i].spisok[j][0]
                    ind = List_Tovar.index(Tovar) if Tovar in List_Tovar else -1 #Формируем список проданных товаров по наименованию.
                    if ind<0:
                        List_Tovar.append(Tovar)
                        List_CountTovar.append(1)
                        List_SummTovar.append(List_Checs[i].spisok[j][1])
                        SummVyruchka=SummVyruchka+List_Checs[i].spisok[j][1]
                    else:
                        List_CountTovar[ind]=List_CountTovar[ind]+1
                        List_SummTovar[ind]=List_SummTovar[ind]+List_Checs[i].spisok[j][1]
                        SummVyruchka=SummVyruchka+List_Checs[i].spisok[j][1]
            else:
                CountOtkat=CountOtkat+1
        print(f"Товаров продано всего:{CountTovar}")
        for i in range(len(List_Tovar)):
            print(List_Tovar[i],"-", List_CountTovar[i], " шт. на сумму ", List_SummTovar[i])
        print(f"Общая выручка составила:{SummVyruchka}")
        print(f"Количество отменённых чеков:{CountOtkat}")

        
    if deisvie==3:#Отмена чека
        if len(List_Checs)>0: #Есть ли чеки в списке
            i=len(List_Checs)-1
            while i>=0 and List_Checs[i].Otkat: #Ищем последний не отмененный чек
                i=i-1
            if i==-1:
                print("Вы уже отменили все чеки")
            else:
                List_Checs[i].Otkat=1
                print(f"Чек номер {i} отменён")
                
        else:
            print("Нет чеков для отмены")

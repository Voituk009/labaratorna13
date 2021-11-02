#cd D:python/python
#134.py
#Модифицируйте программу п.3 так, чтобы Car был ADT,
#и выведите из Car классы SportsCar, Wagon, Coupe. 
#Реализуйте в классах простейшие функции.

class Transport: #клас транспорт

    def set(self, number, date, mark): #конструктор
        self._protected_member = number
        self._protected_member = date
        self._protected_member = mark


    def __init__(self, number, date, mark): 
        self.number = number
        self.date = date
        self.mark = mark

    def print(self): #Метод вывода на экран
        print("\n")
        print ("Номер:", self.number)
        print ("Год выпуска: ", self.date)
        print ("Марка: ")
        return self.mark


class Car(Transport): #класс автомобиль

    def __init__(self, speed):
        self.speed = speed

    def printcar(self):
        print("Максимальная скорость: ")
        return (str(self.speed) + " км/час")


class Bus(Transport): #класс автобус

    def __init__(self, seats):
        self.seats = seats

    def printbus(self):
        print("Число посадочных мест: ")
        return self.seats


class  Sportcar(Car):
    def __init__(self, engine):
        self.engine = engine

    def print(self):
        return (str("Двигатель: " + self.engine))


class Wagon(Car):
    def __init__(self, carrying):
        self.carrying = carrying

    def print(self):
        return (str("Грузоподьемность: ") + self.carrying + "кг")


class Coupe(Car):
    def __init__(self, convenience):
        self.convenience = convenience

    def print(self):
        return (str("Удобство: ") + self.convenience)

        
a = int(input ("Номер: "))
b = int(input ("Год выпуска: "))
c = str(input ("Марка: "))
d = int(input ("1 - если машина, 0 - если автобус, 2 - спорткар, 3 - вагон, 4 - купе: "))

Tr = Transport(a, b, c) 

if int(d) == 1: #Создание транспорта автомобил

    x = int(input ("Максимальная скорость: "))
    Cr = Car(x)
    print (Tr.print())
    print (Cr.printcar())

elif int(d) == 0: #Создание транспорта автобус

    y = int(input ("Число посадочных мест: "))
    Bs = Bus(y)
    print (Tr.print())
    print (Bs.printbus())
 
#Создание транспорта микроавтобус
elif int(d) == 2:
    eng = input("Двигатель: ")
    spcar = Sportcar(eng)
    print (Tr.print())
    print (spcar.print())

elif int(d) == 3:
    car = input("Грузоподьемность: ")
    wagon = Wagon(car)
    print (Tr.print())
    print (wagon.print())

elif int(d) == 4:
    car = input("Удобство: ")
    coupe = Coupe(car)
    print (Tr.print())
    print (coupe.print())
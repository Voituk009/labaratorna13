#cd D:python/python
#135.py
#Напишите программу обработки различных средств транспорта 
#c использование 
#массива указателей типа Transport.
#При обработке  используйте как виртуальные методы, 
#так и средства RTTI


class Transport: #клас транспорт

    def set(self, number, date, mark): #конструктор
        self._protected_member = number
        self._protected_member = date
        self._protected_member = mark
        self._protected_member = transp = []


    def __init__(self, number, date, mark): 
        self.number = number
        self.date = date
        self.mark = mark

    def print(self): #Метод вывода на экран
        return "Номер:" + str(self.number), "Год выпуска: " + str(self.date), "Марка: " + str(self.mark)

 #класс автомобиль
class Car(Transport):

    def __init__(self, speed):
        self.speed = speed

    def printcar(self):
        return "Максимальная скорость: " + str(self.speed) + " км/час"


#класс автобус
class Bus(Transport): 

    def __init__(self, seats):
        self.seats = seats

    def printbus(self):
        return "Число посадочных мест: " + str(self.seats)

#класс микроавтобус
class  Microbus(Car, Bus):
    def __init__(self, number, date, mark, speed, seats):
        super(Microbus,self).__init__(speed=speed)
        Bus.__init__(self, seats=seats)
        self.number=number
        self.date=date
        self.mark=mark

    def print(self):
        return ("Номер:" + str(self.number), "Год выпуска: " + str(self.date), "Год выпуска: " + str(self.date), 
            "Марка: " + str(self.mark), "Максимальная скорость: " + str(self.speed) + " км/час", "Число посадочных мест: " 
            + str(self.seats))
        

class  Sportcar(Car):
    def __init__(self, engine):
        self.engine = engine

    def print(self):
        return (str("Двигатель: " + self.engine))


class Wagon(Car):
    def __init__(self, carrying):
        self.carrying = carrying

    def print(self):
        return (str("Грузоподьемность: ") + self.carrying + " кг")


class Coupe(Car):
    def __init__(self, convenience):
        self.convenience = convenience

    def print(self):
        return (str("Удобство: ") + self.convenience)


transport = ""

h = int(input("Введите к-ство транcпортов: "))
i = 1

for i in range(h):

    print("Транспорт №",i+1)
    d = int(input ("1 - если машина, 0 - если автобус, 2 - спорткар, 3 - вагон, 4 - купе, 5 - микроавтобус: "))
    a = int(input ("Номер: "))
    b = int(input ("Год выпуска: "))
    c = str(input ("Марка: "))
    



    #Создание транспорта автомобил
    Tr = Transport(a, b, c)
    tr = Tr.print() 

    if int(d) == 1: 
        x = int(input ("Максимальная скорость: "))
        Cr = Car(x)

        list = []
        list.extend(Tr.print())
        list.append(Cr.printcar())

        transport = transport + str(list) + "\n" 
        

    #Создание транспорта автобус
    elif int(d) == 0: 
        y = int(input ("Число посадочных мест: "))
        Bs = Bus(y)
        bs = Bs.printbus()

        list = []
        list.extend(tr)
        list.append(bs)

        transport = transport + str(list) + "\n" 


    elif int(d) == 2:
        eng = input("Двигатель: ")
        Spcr = Sportcar(eng)
        spcr = Spcr.print()

        list = []
        list.extend(tr)
        list.append(spcr)

        transport = transport + str(list) + "\n" 


    elif int(d) == 3:
        car = input("Грузоподьемность: ")
        Wg = Wagon(car)
        wg = Wg.print()

        list = []
        list.extend(tr)
        list.append(wg)

        transport = transport + str(list) + "\n" 

    elif int(d) == 4:
        car = input("Удобство: ")
        Cp = Coupe(car)
        cp = Cp.print()

        list = []
        list.extend(tr)
        list.append(cp)

        transport = transport + str(list) + "\n" 

    elif int(d) == 5:
        f = int(input ("Максимальная скорость: "))
        g = int(input ("Число посадочных мест: "))
        McBs = Microbus(a,b,c,f,g)
        mcbs = McBs.print()

        list = []
        list.extend(mcbs)
        transport = transport + str(list) + "\n" 
        
    i += 1

print (transport)
#cd D:python/python
#132.py
#4Напишите объявление для B747, который является производным от класса JetPlane?

class Rocket:

    def __init__(self, fuil, metal):
        self.fuil = fuil
        self.metal=metal

    def print1(self):
        print ("Топливо: ")
        return (str(self.fuil + " л"))

class Airplane:

    def __init__(self, speed):
        self.speed = speed

    def print2(self):
        print ("Скорость: ")
        return (str(self.speed) +  " км/час")

class JetPlane(Rocket, Airplane):
    def __init__(self, fuil, speed, metal, country):
        super(JetPlane,self).__init__(fuil=fuil, metal=metal)
        Airplane.__init__(self, speed=speed)
        self.country = country

    def print(self):
        print("\n")
        print("Создан с: " + self.metal)
        print("Топливо: " + self.fuil + " л")
        print("Скорость: " + self.speed + " км/час")
        return (str("Страна: " + self.country))

class B747(JetPlane):

    def __init__(self, carrying):
        self.carrying = carrying

    def print(self):
        return (str("Грузоподьемность: ") + self.carrying + "кг")


m = input("С какго метала сделан: ")
f = input("Топливо: ")
s = input("Скорость: ")
c = input("Страна: ")
car = input("Грузоподьемность: ")

jetplane = JetPlane(f,s,m,c)
b747 = B747(car)
print(jetplane.print())
print(b747.print())

x = input()
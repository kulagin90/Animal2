from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, type, name, sex, age, weight):
        pass

    @abstractmethod
    def eat(self):
        pass


class dog(Animal):
    def __init__(self, type, name='шарик', sex='мужской', age=0, weight=0):
        super().__init__(type, name, sex, age, weight)
        self.type = type
        self.weight = 2
        self.age = 1
        self.name = input('назовите питомаца:')
        self.sex = input('введите пол:')
        self.mode = False

    def auto(self):
        c = 0
        while c <= 24:
            c += 1
            if c >= 9 and c <= 12 or c >= 15 and c <= 17 or c >= 20 and c <= 21:
                self.walk()
            elif c >= 7 and c <= 8 or c >= 13 and c <= 14 or c >= 18 and c <= 19:
                self.eat()
            elif c >= 0 and c <= 6 or c >= 22 and c <= 24:
                self.dream()

    def man(self):
        a = int(input('введите время:'))
        if a >= 9 and a < 12 or a >= 15 and a <= 17 or a >= 20 and a <= 21:
            self.walk()
        elif a >= 7 and a <= 8 or a >= 13 and a <= 14 or a >= 18 and a <= 19:
            self.eat()
        elif a >= 0 and a <= 6 or a >= 22 and a <= 24:
            self.dream()

    def menu(self):

        print('''выберите режим:
            1.авто
            2.ручной''')
        b = int(input('введите цифру:'))

        if b == 1:
            self.auto()

        elif b == 2:
            self.man()

    def walk(self):
        print('''погулять с питомцем?:
        1.да
        2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            print('ваш питомец на прогулке')
            self.age += 0.01
            self.weight += 0.1
            self.info()
        elif a == 2:
            print('ваш питомец растроен')
            self.age -= 0.01
            self.weight -= 0.1
            self.info()

    def sex(self):
        self.info()

    def eat(self):
        print('''ваш питомец хочет кушать:
        покормить? 1.да 2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            print('''выберите чем покормить:
            мясо,кость,вода,овощи,фрукты''')
            b = input('введите название еды:')
            if b == 'мясо' or 'кость' or 'вода':
                self.weight += 0.2
                self.age += 0.02
                self.info()
            elif b == "овощи" or "фрукты":
                self.weight -= 0.2
                self.age -= 0.02
                self.info()
        elif a == 2:
            print('ваш питомец хочет кушать')
            self.weight -= 0.3
            self.age -= 0.03
            self.info()

    def dream(self):
        print('''ваш питомец хочет спать:
        уложить? 1.да 2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            self.weight += 0.2
            self.age += 0.02
            self.info()
        elif a == 2:
            self.weight -= 0.2
            self.age -= 0.01
            self.info()

    def deaht(self):
        if self.weight <= 0.8:
            print('ваш питомец умер')
            self.mode = True

    def info(self):
        print(f'имя:{self.name}')
        print(f'пол:{self.sex}')
        print(f'возраст:{self.age}')
        print(f'вес:{self.weight}')


class cat(Animal):

    def __init__(self, type, name, sex, age, weight):
        self.type = type
        self.weight = 2
        self.age = 1
        self.name = input('назовите питомаца:')
        self.sex = input('введите пол:')
        self.mode = False

    def __game(self):
        print('ваш питомец либит бегать и прыгать')
        self.info()

    def auto(self):
        c = 0
        while c <= 24:
            c += 1
            if c >= 9 and c <= 12 or c >= 15 and c <= 17 or c >= 20 and c <= 21:
                self.walk()
            elif c >= 7 and c <= 8 or c >= 13 and c <= 14 or c >= 18 and c <= 19:
                self.eat()
            elif c >= 0 and c <= 6 or c >= 22 and c <= 24:
                self.dream()

    def man(self):
        a = int(input('введите время:'))
        if a >= 9 and a < 12 or a >= 15 and a <= 17 or a >= 20 and a <= 21:
            self.walk()
        elif a >= 7 and a <= 8 or a >= 13 and a <= 14 or a >= 18 and a <= 19:
            self.eat()
        elif a >= 0 and a <= 6 or a >= 22 and a <= 24:
            self.dream()

    def menu(self):

        print('''выберите режим:
            1.авто
            2.ручной''')
        b = int(input('введите цифру:'))
        if b == 1:
            self.auto()
        elif b == 2:
            self.man()

    def walk(self):
        print('''погулять с питомцем?:
        1.да
        2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            print('ваш питомец на прогулке')
            self.age += 0.01
            self.weight += 0.1
            self.info()
        elif a == 2:
            print('ваш питомец растроен')
            self.age -= 0.01
            self.weight -= 0.1
            self.info()

    def sex(self):
        self.info()

    def eat(self):
        print('''ваш питомец хочет кушать:
        покормить? 1.да 2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            print('''выберите чем покормить:
            рыба,паштет,кости,молоко,овощи,фрукты''')
            b = input('введите название еды:')
            if b == 'рыба' or 'кости' or 'паштет' or 'молоко':
                self.weight += 0.2
                self.age += 0.02
                self.info()
            elif b == 'овощи' or 'фрукты':
                self.weight -= 0.2
                self.age -= 0.02
                self.info()
        elif a == 2:
            print('ваш питомец хочет кушать')
            self.weight -= 0.3
            self.age -= 0.03
            self.info()

    def dream(self):
        print('''ваш питомец хочет спать:
        уложить? 1.да 2.нет''')
        a = int(input('введите цифру:'))
        if a == 1:
            self.weight += 0.2
            self.age += 0.02
            self.info()
        elif a == 2:
            self.weight -= 0.2
            self.age -= 0.01
            self.info()

    def deaht(self):
        if self.weight <= 0.8:
            print('ваш питомец умер')
            self.mode = True

    def info(self):
        print(f'{self.__game}')
        print(f'имя:{self.name}')
        print(f'пол:{self.sex}')
        print(f'возраст:{self.age}')
        print(f'вес:{self.weight}')


while True:
    print('''выберите класс животного:
    1.собака
    2.кот''')
    a = int(input('введите цифру:'))
    if a == 1:
        print('вы выбрали собаку')
        cls1 = dog(type='', name='', sex='', age='', weight='')
        while True:
            cls1.menu()
            cls1.info()
            cls1.deaht()
            if cls1.mode == True:
                break
    elif a == 2:
        print('вы выбрали кота')
        cls2 = cat(type='', name='', sex='', age='', weight='')
        while True:
            cls2.menu()
            cls2.info()
            cls2.deaht()
            if cls2.mode == True:
                break

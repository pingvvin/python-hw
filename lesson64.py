# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f"{self.name.title()} moved")

    def stop(self):
        print(f"{self.name.title()} stopped")

    def turn(self, direction):
            self.direction = str(direction)
            if self.direction.lower() == 'left' or self.direction.lower() == 'right':
                print(f'{self.name.title()} turned {self.direction.lower()}')
            else:
                print('Wrong input')

    def show_spd(self):
        print(f'The speed of {self.color} {self.name.title()} is {self.speed} km/h')

class TownCar(Car):
    def show_spd(self):
        print(f'The speed of {self.color} {self.name.title()} is {self.speed} km/h')
        if self.speed > 60:
            print('Oi mate. You are to fast slow down.')

class WorkCar(Car):
    def show_spd(self):
        print(f'The speed of {self.color} {self.name.title()} is {self.speed} km/h')
        if self.speed > 40:
            print('Oi mate. You are to fast slow down.')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def signal(self):
        print('Viu viu viu')


c = Car(60, 'red', 'Zaporozhets', False)
c.go()
c.turn('left')
c.turn(12)
c.show_spd()
c.speed = 70
c.show_spd()
c.stop()

p = PoliceCar(100,'black','ford')

p.signal()
p.go()
print(p.is_police)
p.show_spd()

w = WorkCar(35,'yellow','maz')
w.go()
w.turn('right')
w.stop()
w.speed = 50
w.show_spd()
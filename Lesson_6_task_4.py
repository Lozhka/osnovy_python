""""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} едет!'.format(self.name))

    def stop(self):
        print('{} останавливается!'.format(self.name))

    def turn(self, direction):
        print('{} поворачивается {}!'.format(self.name, direction))

    def show_speed(self):
        print('Текущая скорость: ', self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Осторожно! Высокая скорость!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Текущая: ', self.speed)
        if self.speed > 40:
            return('Осторожно! Высокая скорость!')

class PoliceCar(Car):
    pass

sport_car = SportCar(240, 'Красная', 'Спортивная машина', False)
town_car = TownCar(140, 'Белая', 'Городская машина', False)
work_car = WorkCar(90, 'Фиолетовая', 'Рабочая машина', False)
police_car = PoliceCar(210, 'Синяя', 'Полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('НАЛЕВО')
# -*- coding: utf-8 -*-


class Animals:
    ready_for_action = False
    type_of_action = 'some action'
    result_of_action = 'some good'
    kind_of = 'some kind of...'
    sound = 'make a sound'
    mass = 0  # Kg
    name = 'some name'

    def __init__(self, name):
        self.name = name

    def feed(self):
        self.ready_for_action = True
        print('Soon you`ll can get {}!'.format(self.result_of_action))

    def time_interval(self):
        self.ready_for_action = False
        print('It`s been a long time. I`m hungry...')

    def perform_an_action(self):
        if self.ready_for_action:
            print('Ready! You can {}.'.format(self.type_of_action))
            self.ready_for_action = False
        else:
            print('You try to {}, but i`m hungry... Try to feed me...'.format(self.type_of_action))

    def make_a_sound(self):
        print('\nI`m {} {} and i can {}.'.format(self.kind_of, self.name, self.sound))


class Birds(Animals):
    type_of_action = 'get egg'
    result_of_action = 'egg'


class Goose(Birds):
    kind_of = 'goose'
    mass = 4  # Kg
    sound = 'hiss'


class Chicken(Birds):
    kind_of = 'chicken'
    mass = 2  # Kg
    sound = 'cluck'


class Duck(Birds):
    kind_of = 'duck'
    mass = 3  # Kg
    sound = 'quack'


class DairyAnimal(Animals):
    type_of_action = 'milk'
    result_of_action = 'milk'


class Cow(DairyAnimal):
    kind_of = 'cow'
    mass = 500  # Kg
    sound = 'low'


class Goat(DairyAnimal):
    kind_of = 'goat'
    mass = 50  # Kg
    sound = 'shout'


class Sheep(Animals):
    kind_of = 'sheep'
    type_of_action = 'shear'
    result_of_action = 'wool'
    mass = 70  # Kg
    sound = 'bleat'


data = {
    'Серый': ['Goose', 'gray'],
    'Белый': ['Goose', 'white'],
    'Манька': ['Cow', 'manka'],
    'Барашек': ['Sheep', 'lamb'],
    'Кудрявый': ['Sheep', 'curly'],
    'Ко-Ко': ['Chicken', 'ko_ko'],
    'Кукареку': ['Chicken', 'cock_a_doodle_doo'],
    'Рога': ['Goat', 'horns'],
    'Копыта': ['Goat', 'hoof'],
    'Кряква': ['Duck', 'mallard'],
}

max_mass = 0
max_mass_name = ''
sum_mass = 0

for key, value in data.items():
    globals()[value[1]] = globals()[value[0]](key)
    if globals()[value[1]].mass > max_mass:
        max_mass = globals()[value[1]].mass
        max_mass_name = globals()[value[1]].name
    sum_mass += globals()[value[1]].mass

    globals()[value[1]].make_a_sound()
    globals()[value[1]].perform_an_action()
    globals()[value[1]].feed()
    globals()[value[1]].perform_an_action()
    globals()[value[1]].time_interval()
    globals()[value[1]].perform_an_action()
    globals()[value[1]].feed()
    globals()[value[1]].perform_an_action()

print('\nОбщая масса всех животных - {} кг. '
      'Самое тяжелое животное - {} - {} кг.'.format(sum_mass, max_mass_name, max_mass))

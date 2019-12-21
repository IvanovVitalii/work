class Human:
    def __init__(self, sex=None, weight=None, height=None, age=None):
        self._sex = sex
        self._weight = weight
        self._height = height
        self._age = age

    def calculation_calories(self, sex, weight, height, age):
        if sex == 'м':
            bmr = 88.36 + 13.4 * weight + 4.8 * height - 5.7 * age
            return bmr
        elif sex == 'ж':
            bmr = 447.6 + 9.2 * weight + 3.1 * height - 4.3 * age
            return bmr

    def set_sex(self, value):
        if value == 'м' or value == 'ж':
            self._sex = value
            return self._sex
        else:
            self._sex = None
            print('Неверно указан пол. Повторите.')
            return self._sex

    def set_weight(self, value):
        try:
            value = float(value)
            self._weight = value
            return self._weight
        except ValueError:
            print('Ошибка ввода. Повторите.')
            self._weight = None
            return self._weight

    def set_height(self, value):
        try:
            value = float(value)

            if value <= 250 and value >= 50:
                self._height = value
            else:
                print('Рост не в допустимых приделах (50-250 см).')
                self._height = None
            return self._height
        except ValueError:
            print('Ошибка ввода. Повторите.')
            self._height = None
            return self._height

    def set_age(self, value):
        try:
            value = float(value)

            if value <= 100 and value >= 0:
                self._age = value
            else:
                print('Возраст не в допустимых приделах (0-100 лет).')
                self._age = None
            return self._age
        except ValueError:
            print('Ошибка ввода. Повторите.')
            self._age = None
            return self._age


while True:
    user = Human()

    try:
        com1 = int(input('Посчитать калории - 1 \n'
                     'Выйти - 0 \n'))
        if com1 == 1:

            while user._sex == None:
                sex = input('Введите пол, м/ж: ')
                user.set_sex(sex)

            while user._weight == None:
                weight = input('Введите вес, кг: ')
                user.set_weight(weight)

            while user._height == None:
                height = input('Введите рост, см: ')
                user.set_height(height)

            while user._age == None:
                age = input('Введите возраст, полных лет: ')
                user.set_age(age)

            while True:
                print('')
                list_activity = [1.2, 1.375, 1.55, 1.725, 1.9]
                try:
                    choice_activity = int(input('Введите уровень активности:\n'
                                                'Минимальный уровень активности — 0\n'
                                                'Низкий уровень активности — 1\n'
                                                'Средний уровень активности — 2\n'
                                                'Высокий уровень — 3\n'
                                                'Очень высокий —  4\n'))
                    if choice_activity in range(5):
                        activity = list_activity[choice_activity]
                        print('')
                        break
                    else:
                        print('Неверный выбор. Повторите.')
                except ValueError:
                    print('Неверный выбор. Повторите.')





            calories = activity * (user.calculation_calories(user._sex, user._weight, user._height, user._age)) // 1
            print(f'Норма калорий: {int(calories)}')
            print('')


        elif com1 == 0:
            break
        else:
            print('Неверный ввод. Повторите выбор.')
    except ValueError as e:
        print('Неверный ввод. Повторите выбор.')

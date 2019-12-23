def decorator(func):
    def wrapper(*args):
        print('')
        print('----------')
        func(*args)
        print('----------')
        print('')
    return wrapper


class Human:

    def __init__(self, gender=None, weight=None, height=None, age=None, activity=None):
        self._gender = gender
        self._weight = weight
        self._height = height
        self._age = age
        self._activity = activity

    # указываем пол
    def set_sex(self, value):
        if value == 'м' or value == 'ж':
            self._gender = value
            return self._gender
        else:
            self._gender = None
            print('Неверно указан пол. Повторите.')
            return self._gender

    # указываем вес
    def set_weight(self, value):
        try:
            value = float(value)
            self._weight = value
            return self._weight
        except ValueError:
            print('Ошибка ввода. Повторите.')
            self._weight = None
            return self._weight

    # указываем рост
    def set_height(self, value):
        try:
            value = float(value)

            if 250 > value > 50:
                self._height = value
            else:
                print('Рост не в допустимых приделах (50-250 см).')
                self._height = None
            return self._height
        except ValueError:
            print('Ошибка ввода. Повторите.')
            self._height = None
            return self._height

    # указываем возраст
    def set_age(self, value):
        try:
            value = float(value)

            if 100 > value >= 0:
                self._age = value
            else:
                print('Возраст не в допустимых приделах (1-100 лет).')
                self._age = None
            return self._age
        except ValueError:
            print('Ошибка ввода. Повторите.')
            self._age = None
            return self._age

    # указываем уровень активности
    def set_activity(self, value):

        LIST_ACTIVITY = [1.2, 1.375, 1.55, 1.725, 1.9]

        try:
            value = int(value)
            value -= 1
            if value in range(5):
                self._activity = LIST_ACTIVITY[value]
                print('')
                return self._activity
            else:
                print('Неверный выбор. Повторите.')
                self._activity = None
                return self._activity

        except ValueError:
            print('Неверный выбор. Повторите.')
            self._activity = None
            return self._activity

    # считаем калории
    @decorator
    def calculation_calories(self, gender, weight, height, age, activity):
        if gender == 'м':
            bmr = (activity * (88.36 + 13.4 * weight + 4.8 * height - 5.7 * age)) // 1
            return print(f'Норма калорий: {int(bmr)}')
        elif gender == 'ж':
            bmr = (activity * (447.6 + 9.2 * weight + 3.1 * height - 4.3 * age)) // 1
            return print(f'Норма калорий: {int(bmr)}')

    @property
    def activity(self):
        return self._activity

    @property
    def age(self):
        return self._age

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @property
    def gender(self):
        return self._gender


# интерфейс программы
while True:
    user = Human()

    try:
        com1 = int(input('Посчитать калории - 1 \n'
                         'Выйти - 0 \n'))
        if com1 == 1:

            while user.gender is None:
                sex = input('Введите пол, м/ж: ')
                user.set_sex(sex)

            while user.weight is None:
                weight = input('Введите вес, кг: ')
                user.set_weight(weight)

            while user.height is None:
                height = input('Введите рост, см: ')
                user.set_height(height)

            while user.age is None:
                age = input('Введите возраст, полных лет: ')
                user.set_age(age)

            while user.activity is None:
                print('')
                choice_activity = input('Введите уровень активности:\n'
                                        'Минимальный уровень активности — 1\n'
                                        'Низкий уровень активности — 2\n'
                                        'Средний уровень активности — 3\n'
                                        'Высокий уровень — 4\n'
                                        'Очень высокий —  5\n')
                user.set_activity(choice_activity)

            # считаем и выводим калории
            calories = user.calculation_calories(user.gender,
                                                 user.weight,
                                                 user.height,
                                                 user.age,
                                                 user.activity)

        elif com1 == 0:
            break
        else:
            print('Неверный ввод. Повторите выбор.')
    except ValueError:
        print('Неверный ввод. Повторите выбор.')

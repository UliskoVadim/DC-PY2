import doctest


class AntColony:
    """Класс описывает колонию красных муравьев"""
    def __init__(self, size_in_thousands: float, breeding_rate_thousands_per_month: float,
                 relative_strength: int, life_temperature: float, temperature: float):
        """
        Создание и подготовка к работе объекта колония красных муравьев
        :param size_in_thousands: размер колонии в тысячах
        :param breeding_rate_thousands_per_month: скорость разможения в тысячах за месяц
        :param relative_strength: относительная сила
        :param life_temperature: температура в Кельвинах при которой возможно существование
        :param temperature: температура среды в Кельвинах

        Примеры:
        >>> red_ant_colony_1 = AntColony(3 , 5 , 5, 290, 300)  # инициализация экземпляра класса
        >>> black_ant_colony_1 = AntColony(3 , 5 , 5, 1, 1)  # инициализация экземпляра класса
        """
        if not isinstance(size_in_thousands, (int, float)):
            raise TypeError("Численность колонии указывается в тысячах и должно быть int или float")
        if size_in_thousands <= 0:
            raise ValueError("Численность колонии указывается в тысячах и не должно быть положительным числом")
        self.size_in_thousands = size_in_thousands

        if not isinstance(breeding_rate_thousands_per_month, (int, float)):
            raise TypeError("Скорость размножения указывается в тысячах за месяц и должно быть int или float")
        self.breeding_rate_thousands_per_month = breeding_rate_thousands_per_month

        if not isinstance(relative_strength, int):
            raise TypeError("Относительная сила указывается в int")
        if relative_strength <= 0 or relative_strength >= 10:
            raise ValueError("Относительная сила задается в диапазоне от 0 до 10")
        self.relative_strength = relative_strength

        if not isinstance(life_temperature, (int, float)):
            raise TypeError("Температура указывается в Кельвинах и должно быть int или float")
        if life_temperature <= 0:
            raise ValueError("Температура в Кельвинах можеть быть только положительным числом")
        self.life_temperature = life_temperature

        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура указывается в Кельвинах и должно быть int или float")
        if temperature <= 0:
            raise ValueError("Температура в Кельвинах можеть быть только положительным числом")
        self.temperature = temperature

    def kill_colony(self):
        """
        Метод убивает колонию

        :return: убить колонию

        Пример:
        >>> red_ant_colony_1 = AntColony(3 , 5 , 5, 290, 280)
        >>> red_ant_colony_1.kill_colony()
        """
        self.size_in_thousands = 0
        self.breeding_rate_thousands_per_month = 0
        self.relative_strength = 0

    def kill_queen(self):
        """
        Метод убивает муравьиную матку
        :return: убить матку

        Пример:
        >>> red_ant_colony_1 = AntColony(3 , 5 , 5, 290, 300)
        >>> red_ant_colony_1.kill_queen()
        """
        self.breeding_rate_thousands_per_month = 0

    def colonization(self):
        """
        Метод распространения колонии
        :return: судьба в зависимости от теммпературы

        >>> red_ant_colony_1 = AntColony(3 , 5 , 5, 290, 280)
        >>> red_ant_colony_1.colonization()
        """
        if self.temperature <= self.life_temperature:  # если температура средыы меньше, чем температура существования
            self.kill_colony()
        if self.temperature >= self.life_temperature:
            self.size_in_thousands += self.breeding_rate_thousands_per_month  # если температура больше
            return self.size_in_thousands


class Environment:
    """Класс описывает окружающую среду"""
    def __init__(self, lifetime_in_months: float, temperature: float):
        """
        Создание и подготовка к работе объекта окружающая среда
        :param lifetime_in_months: время существования среды в месяцах
        :param temperature: температура среды в Кельвинах

        Пример:
        >>> environment = Environment(12, 300)  # инициализация экземпляра класса
        """
        if not isinstance(lifetime_in_months, (int, float)):
            raise TypeError("Время существования среды указывается в месяцах должно быть int или float")
        if lifetime_in_months <= 0:
            raise ValueError("Время существования среды указывается в месяцах должно быть положительным числом")
        self.lifetime_in_months = lifetime_in_months

        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура указывается в Кельвинах и должно быть int или float")
        if temperature <= 0:
            raise ValueError("Температура в Кельвинах можеть быть только положительным числом")
        self.temperature = temperature

    def increase_temperature(self, increase_to: float):
        """Метод увеличивает температуру среды
        :return: увеличить температуру

        Пример:
        >>> environment = Environment(12, 300)
        >>> environment.increase_temperature(10) # увеличили температуру на 10 градусов
        """
        if not isinstance(increase_to, (int, float)):
            raise TypeError("Температура указывается в Кельвинах и должно быть int или float")
        if increase_to <= 0:
            raise ValueError("Температура в Кельвинах можеть быть только положительным числом")
        self.temperature += increase_to

    def decrease_temperature(self, decrease_to: float):
        """Метод уменьшает температуру среды
        :return: увеличить температуру

        Пример:
        >>> environment = Environment(12, 300)
        >>> environment.decrease_temperature(10) #  уменьшили температуру на 10 градусов
        """
        if not isinstance(decrease_to, (int, float)):
            raise TypeError("Температура указывается в Кельвинах и должно быть int или float")
        if decrease_to <= 0:
            raise ValueError("Температура в Кельвинах можеть быть только положительным числом")
        self.temperature -= decrease_to


class Anteater:
    """Класс описывает муравьеда"""
    def __init__(self, age: int, lifetime: int, ant_eating_speed: float, ants_eaten_today: int):
        """
        Создание и подготовка к работе объекта муравьед
         :param age: возраст муравьеда в месяцах
         :param lifetime: допустимый возраст жизни в месяцах
         :param ant_eating_speed: скорость поедания муравьев (тысячи муравьев/день)
         :param ants_eaten_today: съедено муравьев сегодня

        Пример:
        >>> anteater_1 = Anteater(10 , 150, 30, 290)  # инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Возраст муравьеда указывается в месяцах и должен быть int")
        if age <= 0 and age <= 168:
            raise ValueError("Возраст муравьеда  должен быть положительным числом")
        self.age = age

        if not isinstance(lifetime, int):
            raise TypeError("Допустимое время жизни муравьеда указывается в месяцах и должен быть int")
        if lifetime <= 0 or lifetime >= 168:
            raise ValueError("Допустимое время жизни муравьеда указывается в месяцах, не превышает 168 (14 лет) и должно быть положительным числом")
        self.lifetime = lifetime

        if not isinstance(ant_eating_speed, int):
            raise TypeError("Скорость поедания муравьев указывается в тысячах в день и должно быть int или float")
        if ant_eating_speed <= 0:
            raise ValueError("Скорость поедания муравьев не может быть отрицательным числом")
        self.ant_eating_speed = ant_eating_speed

        if not isinstance(ants_eaten_today, int):
            raise TypeError("Количество съеденных муравьев за сегодня указывается в int")
        if ants_eaten_today <= 0:
            raise ValueError("Количество съеденных муравьев за сегодня не может быть отрицательным числом")
        self.ants_eaten_today = ants_eaten_today

    def death(self):
        """
        Метод убивает муравьеда

        :return: убить муравьеда

        Пример:
        >>> anteater_1 = Anteater(10 , 150, 30, 290)
        >>> anteater_1.death()
        """
        self.ant_eating_speed = None
        self.age = None

    def death_from_oldness(self):
        """
        Смерть от старости

        :return: смерть от старости

        Пример:
        >>> anteater_1 = Anteater(10 , 150, 30, 290)
        >>> anteater_1.death_from_oldness()
        """
        if self.age >= self.lifetime:
            self.death()

    def death_from_eaten(self):
        """
        Смерть от количества съеденных муравьев

        :return: смерть недоедания/переедания

        Пример:
        >>> anteater_1 = Anteater(10 , 150, 30, 290)
        >>> anteater_1.death_from_eaten()
        """
        if self.ant_eating_speed <= self.ants_eaten_today or self.ants_eaten_today == 0:
            self.death()

    def aging_for_month(self):
        """
        Старение за месяц

        :return: Прибавить месяц к возрасту муравьеда

        Пример:
        >>> anteater_1 = Anteater(10 , 150, 30, 290)
        >>> anteater_1.aging_for_month()
        """
        self.age += 1
        self.ant_eating_speed += 1


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

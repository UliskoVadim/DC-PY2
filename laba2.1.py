import doctest

class RedAntColony:
    """Класс описывает колонию красных муравьев"""
    def __init__(self, size_in_thousands: float, breeding_rate_thousands_per_month: float, relative_strength: int, life_temperature: float, temperature):
        """
        Создание и подготовка к работе объекта колония красных муравьев
        :param size_in_thousands: размер колонии в тысячах
        :param breeding_rate_thousands_per_month: скорость разможения в тысячах за месяц
        :param relative_strength: относительная сила
        :param life_temperature: температура в Кельвинах при которой возможно существование
        :param temperature: температура среды в Кельвинах

        Пример:
        >>> red_ant_colony_1 = RedAntColony(3 , 5 , 5, 290)  # инициализация экземпляра класса
        """
        if not isinstance(size_in_thousands, (int, float)):
            raise TypeError("Численность колонии указывается в тысячах и должно быть int или float")
        if size_in_thousands <= 0:
            raise ValueError("Численность колонии указывается в тысячах и не должно быть положительным числом")
        self.size_in_thousands = size_in_thousands

        if not isinstance(breeding_rate_thousands_per_month, (int, float)):
            raise TypeError("Скорость размножения указывается в тысячах за месяц и должно быть int или float")
        self.breeding_rate_thousands_per_month = breeding_rate_thousands_per_month

        if not isinstance(relative_strength, (int)):
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
        >>> red_ant_colony_1 = RedAntColony(3 , 5 , 5, 290)
        >>> red_ant_colony_1.kill_colony()
        """
        self.size_in_thousands = 0
        self.breeding_rate_thousands_per_month = 0
        self.relative_strength = 0
        return (self)

    def kill_queen(self):
        """
        Метод убивает муравьиную матку
        :return: убить матку

        Пример:
        >>> red_ant_colony_1 = RedAntColony(3 , 5 , 5, 290)
        >>> red_ant_colony_1.kill_queen()
        """
        self.breeding_rate_thousands_per_month = 0
        return(self.breeding_rate_thousands_per_month)

    def colonization(self, temperature):
        """
        Метод распространения колонии
        :return: судьба в зависимости от теммпературы

        >>> red_ant_colony_1 = RedAntColony(3 , 5 , 5, 290)
        >>> red_ant_colony_1.colonization()
        """
        if temperature <= self.life_temperature: #если температура средыы меньше, чем температура существования
            self.kill_colony()
        if temperature >= self.life_temperature:
            self.size_in_thousands += self.breeding_rate_thousands_per_month #если температура больше температуры существования
            return (self.size_in_thousands)

class BlackAntColony:
    """Класс описывает колонию красных муравьев"""
    def __init__(self, size_in_thousands: float, breeding_rate_thousands_per_month: float, relative_strength: int):
        """Класс описывает колонию красных муравьев
         Создание и подготовка к работе объекта колония черных муравьев
        :param size_in_thousands: размер колонии в тысячах
        :param breeding_rate_thousands_per_month: скорость разможения в тысячах за месяц
        :param relative_strength: относительная сила
        Пример:
        >>> black_ant_colony_1= BlackAntColony(1 , 2 , 9)  # инициализация экземпляра класса
        """
        if not isinstance(size_in_thousands, (int, float)):
            raise TypeError("Численность колонии указывается в тысячах и должно быть int или float")
        if size_in_thousands <= 0:
            raise ValueError("Численность колонии указывается в тысячах и не должно быть положительным числом")
        self.size_in_thousands = size_in_thousands

        if not isinstance(breeding_rate_thousands_per_month, (int, float)):
            raise TypeError("Скорость размножения указывается в тысячах за месяц и должно быть int или float")
        self.breeding_rate_thousands_per_month = breeding_rate_thousands_per_month

        if not isinstance(relative_strength, (int)):
            raise TypeError("Относительная сила указывается в int")
        if relative_strength <= 0 or relative_strength >= 10:
            raise ValueError("Относительная сила задается в диапазоне от 0 до 10")
        self.relative_strength = relative_strength

    def kill_colony(self):
        """
        Метод убивает колонию

        :return: убить колонию

        Пример:
        >>> black_ant_colony_1 = BlackAntColony(1 , 2 , 9)
        >>> black_ant_colony_1.kill_colony()
        """
        self.size_in_thousands = 0
        self.breeding_rate_thousands_per_month = 0
        self.relative_strength = 0
        return (self)

    def kill_queen(self):
        """
        Метод убивает муравьиную матку
        :return: убить матку

        Пример:
        >>> black_ant_colony_1 = BlackAntColony(1 , 2 , 9)
        >>> black_ant_colony_1.kill_queen()
        """
        self.breeding_rate_thousands_per_month = 0
        return(self)


class Environment:
    """Класс Документация на класс.
        Класс описывает окружающую среду"""
    def __init__(self, lifetime_in_months: float, temperature: float):
        """
        Создание и подготовка к работе объекта колония красных муравьев
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

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


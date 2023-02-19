import doctest


class TypesOfPasta:
    def __init__(self, cook_time: int, material: str, size: float):
        """
        Создание базового класса длинных макаронных изделий
        :param cook_time: Время варки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        """
        self.cook_time = cook_time
        self.material = material
        self.size = size

    def __str__(self) -> str:
        """
        :return: Главная информация о макаронных изделяих
        """
        return f"Время варки {self.cook_time}. Сделаны из {self.material} теста"

    def __repr__(self) -> str:
        """
        :return: вывод всей информации об изделяих
        """
        return f"{self.__class__.__name__}(cook_time={self.cook_time!r}, material={self.material!r}, size={self.size!r})"

    def configuration(self, cook_time: int, material: str, size: float) -> None:
        """
        Конфигурация изделий с учетом параметров
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        :return: тип изделий по заданным параметрам
        """
        ...

    def cook_pasta(self) -> None:
        """
        Варить макаронные изделия
        :return: Сваренные макаронные изделия
        """
        ...


class ShortPasta(TypesOfPasta):
    def __init__(self, cook_time: int, material: str, size: float, shape: str):
        """
        Создание коротких макаронных изделий
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        :param shape: Форма изделий.
        """
        super().__init__(cook_time, material, size)
        self.shape = shape

    # Метод __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры

    def __repr__(self) -> str:
        """
        Перегрузка нужна для добавления в информацию параметра формы
        :return: вывод всей информации об изделиях
        """
        return f"{self.__class__.__name__}(cook_time={self.cook_time!r}, material={self.material!r}, size={self.size!r}, shape={self.shape!r})"

    def configuration(self, cook_time: int, material: str, size: float) -> None:
        """
        Конфигурация изделий с учетом параметров
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        :return: тип изделий по сконфигурированным параметрам
        Перегрузка нужна, чтобы учесть форму
        """
        super().configuration(cook_time, material, size)
        ...


class LongPasta(TypesOfPasta):
    def __init__(self, cook_time: int, material: str, size: float, thickness: int):
        """
        Создание класса длинных макаронных изделий
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        :param thickness: Толщина в миллиметрах
        """
        super().__init__(cook_time, material, size)
        self.thickness = thickness

    # Методы __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры

    def __repr__(self):
        """
        Перегрузка нужна для добавления параметра толщины в модель макаронных изделий
        :return: вывод всей информации об изделиях
        """
        return f"{self.__class__.__name__}(cook_time={self.cook_time!r}, frame={self.material!r}, size={self.size!r}, thickness={self.thickness!r})"

    def configuration(self, cook_time: int, material: str, size: float) -> None:
        """
        Создание класса длинных макаронных изделий
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        Перегрузка нужна, чтобы учесть толщину изделий
        """
        super().configuration(cook_time, material, size)
        ...


if __name__ == "__main__":
    doctest.testmod()    # тестирование примеров, которые находятся в документации

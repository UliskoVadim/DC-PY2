import doctest


class TypesOfPasta:
    def __init__(self, cook_time: int, material: str, size: float):
        """
        Создание базового класса длинных макаронных изделий
        :param cook_time: Время варки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах

        Примеры:
        >>> vermicelli = TypesOfPasta(10, "wheat", 200)
        """
        self.cook_time = cook_time
        self.material = material
        self.size = size

    def __str__(self) -> str:
        """
        :return: Главная информация о макаронных изделяих

        Примеры:
        >>> vermicelli = TypesOfPasta(10, "wheat", 200)
        >>> vermicelli.__str__()
        """
        return f"Время варки {self.cook_time}. Сделаны из {self.material} теста"

    def __repr__(self) -> str:
        """
        :return: вывод всей информации об изделяих

        Примеры:
        >>> vermicelli = TypesOfPasta(10, "wheat", 200)
        >>> vermicelli.__repr__()
        """
        return f"{self.__class__.__name__}(cook_time={self.cook_time!r}, material={self.material!r}, size={self.size!r})"

    def find_recipes(self, cook_time: int, material: str, size: float) -> None:
        """
        Найти рецепты
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        :return: Список рецептов

        Примеры:
        >>> vermicelli = TypesOfPasta(10, "wheat", 200)
        >>> vermicelli.find_recipes()
        """
        ...

    def cook_pasta(self) -> None:
        """
        Варить макаронные изделия
        :return: Сваренные макаронные изделия

        Примеры:
        >>> vermicelli = TypesOfPasta(10, "wheat", 200)
        >>> vermicelli.cook_pasta()
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

        Примеры:
        >>> fusilli = ShortPasta(8, "wheat", 50, "spirals")
        >>> penne = ShortPasta(9, "rice", 90, "cylinder")
        """
        super().__init__(cook_time, material, size)
        self.shape = shape

    """
    Методы __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры
    
    Примеры:
    >>> penne = ShortPasta(9, "rice", 90, "cylinder")
    >>> penne.cook_pasta()  #Методы __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры
    >>> penne.__str__()  #Методы __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры
    """

    def __repr__(self) -> str:
        """
        Перегрузка нужна для добавления в информацию параметра формы
        :return: вывод всей информации об изделиях

        Примеры:
        >>> penne = ShortPasta(8, "wheat", 50, "spirals")
        >>> penne.__repr__()

        """
        return f"{self.__class__.__name__}(cook_time={self.cook_time!r}, material={self.material!r}, size={self.size!r}, shape={self.shape!r})"

    def find_recipes(self, cook_time: int, material: str, size: float) -> None:
        """
        Найти рецепты
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        :return: Список рецептов
        Перегрузка нужна, чтобы учесть форму

        Примеры:
        >>> penne = ShortPasta(9, "rice", 90, "cylinder")
        >>> penne.find_recipes()
        """
        super().find_recipes(cook_time, material, size)
        ...


class LongPasta(TypesOfPasta):
    def __init__(self, cook_time: int, material: str, size: float, thickness: int):
        """
        Создание класса длинных макаронных изделий
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        :param thickness: Толщина в миллиметрах

        Примеры:
        >>> capellini = LongPasta(11, "wheat", 200, 1)
        >>> pappardelle = LongPasta(8, "wheat", 150, 12)
        """
        super().__init__(cook_time, material, size)
        self.thickness = thickness

    def __repr__(self):
        """
        Перегрузка нужна для добавления параметра толщины в модель макаронных изделий
        :return: вывод всей информации об изделиях

        Примеры:
        >>> capellini = LongPasta(11, "wheat", 200, 1)
        >>> capellini.__repr__()
        """
        return f"{self.__class__.__name__}(cook_time={self.cook_time!r}, frame={self.material!r}, size={self.size!r}, thickness={self.thickness!r})"

    """
    Методы __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры
    
    Примеры:
    >>> capellini = LongPasta(11, "wheat", 200, 1)
    >>> capellini.cook_pasta()
    >>> capellini.__str__()  # Методы __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры
    """

    def find_recipes(self, cook_time: int, material: str, size: float) -> None:
        """
        Найти рецепты
        :param cook_time: время готовки в минутах
        :param material: Материал, из которого сделаны
        :param size: длина в миллиметрах
        Перегрузка нужна, чтобы учесть толщину изделий

        Примеры:
        >>> capellini = LongPasta(11, "wheat", 200, 1)
        >>> capellini.find_recipes()
        >>> capellini.cook_pasta()  #Методы __str__ и cook_pasta могут быть унаследованы из родительского класса, так как в них не используются новые параметры
        """
        super().find_recipes(cook_time, material, size)
        ...


if __name__ == "__main__":
    doctest.testmod()    # тестирование примеров, которые находятся в документации

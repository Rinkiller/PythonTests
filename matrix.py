# Урок 11. ООП. Особенности Python
# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:
    """Class Matrix"""
    matriza:list[list[int]]

    def __init__(self , matriza:list[list[int]]) -> None:
        """INIT function
        >>> a = Matrix(None)
        Traceback (most recent call last):
        ...
        ValueError
        """
        if matriza:
            self.matriza = matriza
        else:
            raise ValueError

    def __str__(self) -> str:
        """ String output matrix
        >>> print(Matrix([[1,2],[3,4]]))
        [1, 2]
        [3, 4]
        """
        rezult_str = ''
        for line in self.matriza:
            rezult_str = rezult_str + str(line) + '\n'
        return rezult_str[:-1]
    def mapsum(self) -> float:
        """ Sqrt matrix elements
        >>> print(Matrix([[1,1],[1,1]]).mapsum())
        1.0
        """
        el = len(self.matriza) * len(self.matriza[0])
        result = sum(sum([*line]) for line in self.matriza)
        return result / el
    def __eq__(self, other: object) -> bool:
        """ equels matrixs
        >>> print(Matrix([[1,2],[3,4]]) == Matrix([[3,4],[1,2]]))
        True
        """
        return self.mapsum() == other.mapsum()
    def __gt__(self, other: object) -> bool:
        """
        >>> print(Matrix([[1,2],[3,4]]) > Matrix([[1,1],[1,2]]))
        True
        """
        return self.mapsum() > other.mapsum()
    
    def __add__(self, other: object) -> object:
        """
        >>> print(Matrix([[1,2],[3,4]]) + Matrix([[0,1],[2,5]]))
        [1, 3]
        [5, 9]
        """
        if len(self.matriza) != len(other.matriza):
            raise ValueError 
        else:
            for index in range(len(self.matriza)):
                if len(self.matriza[index]) != len(other.matriza[index]):
                    raise ValueError
        new_matrix = []
        for index in range(len(self.matriza)):
            line = []
            for ind_el in range(len(self.matriza[index])):
                line.append(self.matriza[index][ind_el] + other.matriza[index][ind_el])
            new_matrix.append(line)
        return Matrix(new_matrix)

    def __mul__(self, other: object) -> object: 
        """
        >>> print(Matrix([[1,2],[3,4]]) * Matrix([[5,6],[7,8]]))
        [19, 22]
        [43, 50]
        >>> print(Matrix([[1,2],[2,3],[4,5],[1,2]]) * Matrix([[1,3,4],[4,5,6]]))
        [9, 13, 16]
        [14, 21, 26]
        [24, 37, 46]
        [9, 13, 16]
        >>> print(Matrix([[1,2],[1,1]]) * Matrix([[5,6],[7,8],[2,3]]))
        Traceback (most recent call last):
        ...
        ValueError
        """
        for index in range(len(self.matriza)):
            if len(other.matriza) != len(self.matriza[index]):
                raise ValueError
        return Matrix(list(map(lambda x: list(map(lambda y: sum(i * j for i , j in zip(x , y)) , zip(*other.matriza))), self.matriza)))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


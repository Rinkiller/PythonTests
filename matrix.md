Документация к модулю матиц обеспечивающему работу с прямоугольными целочисленными матрицами
===

Модуль содержит внутренний класс Matrix
обеспечивающий хранение и арифметические операции с прямоугольными целочисленными матрицами
---
Для хранения прямоугольных целочисленных матриц используйте класс Matrix 
Импортируйте его в свой код.

    >>> from matrix import Matrix

Теперь можно использовать его для работы. Сохранение матриц для их последующей обработки производится следующим образом:

    >>> matrix = Matrix([[1, 1], [1, 1]])

Можно сравнивать матрицы друг с другом
    >>> Matrix([[1, 1], [1, 1]]) == Matrix([[1, 1], [1, 1]])
    True

    >>> Matrix([[1, 1], [1, 1]]) > Matrix([[0, 1], [1, 0]])
    True

Можно проводить арифметические операции:
    сложение матриц:

    >>> print(Matrix([[1, 1], [1, 1]]) + Matrix([[1, 1], [1, 1]]))
    [2, 2]
    [2, 2]

    или умножение матриц друг на друга:

    >>> print(Matrix([[1,2],[3,4]]) * Matrix([[5,6],[7,8]]))
    [19, 22]
    [43, 50]

 Важно помнить, что данный класс поддерживает только целочисленные матрицы
 При попытке ввести некорректные данные код будет приостановлен

    >>> a = Matrix(None)
    Traceback (most recent call last):
    ...
    ValueError
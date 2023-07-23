"""Test module of Matrix class object"""
from matrix import Matrix
import pytest


def test_init():
    with pytest.raises(ValueError):
        Matrix(None)

def test_add():
    assert Matrix([[1, 2], [3, 4]]) + Matrix([[0, 1], [2, 5]]) == Matrix([[1, 3],[5, 9]]) , 'Код дал сбой'

def test_mull():
    assert Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]]) == Matrix([[19, 22],[43, 50]]) , 'Код дал сбой'

def test_eq():
    assert Matrix([[1, 2], [3, 4]]) == Matrix([[3, 4], [1, 2]]) , 'Код дал сбой'

# def test_str_out(capfd):   #dfhfgjh
#     print(Matrix([[1, 1], [1, 1]]))
#     captured = capfd.readouterr()
#     assert captured.out == '[1, 1]\n[1, 1]', 'Код дал сбой'

if __name__ == '__main__':
    pytest.main(['-v'])
    print(Matrix([[1, 1], [1, 1]]))
import unittest
from unittest.mock import MagicMock, Mock


class Car:
    pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        car = Car()
        car.brand = MagicMock(return_value=3)
        car.brand(3, 4, 5, key='value')


mock = Mock(side_effect=KeyError('foo'))
values = {'a': 1, 'b': 2, 'c': 3}


def side_effect_1(arg):
    return values[arg]

mock.side_effect = side_effect_1

mock=Mock()

mock.side_effect = [5, 4, 3, 2, 1]
if __name__ == '__main__':
    # unittest.main()
    # print(mock('a'), mock('b'), mock('c'))
    # mock()
    mock(), mock(), mock()
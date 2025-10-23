from src.task_10_2 import divide, calculate_logarithm
import pytest

def test_divide():
    assert divide(2, 1) == 2


def test_zero_divide():

    assert divide(2, 0) == 0


def test_calc_log():
    assert calculate_logarithm(8, 2) == 3.0
    assert calculate_logarithm(8, 4) == 1.5

    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)
        calculate_logarithm(8, 0)

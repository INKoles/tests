def add_numbers(a, b):
    return a + b


def is_even(a):
    return a % 2 == 0


def find_max(my_list):
    return max(my_list)


def divide(a, b):
    if b > 0:
        return a / b
    return 0


if __name__ == "10_2_task":
    assert add_numbers(2, 2) == 4, "add success"

    assert is_even(2) == True

    assert find_max([1, 2, 3, 4, 5]) == 5

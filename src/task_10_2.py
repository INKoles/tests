import math

# if __name__ == "10_2_task":
#     assert add_numbers(2, 2) == 4, "add success"
#
#     assert is_even(2) == True
#
#     assert find_max([1, 2, 3, 4, 5]) == 5


def divide(a, b):
    if b > 0:
        return a / b
    return 0


def calculate_logarithm(x, base):
    return math.log(x, base)


def reverse_string(my_string):
    return my_string[::-1]
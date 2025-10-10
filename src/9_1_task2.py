"""
Написать функцию, которая получает на вход список чисел и
возвращает новый список, содержащий только числа,
которые являются палиндромами.
Пример ввода: [121, 123, 131, 34543]
Пример вывода:
[121, 131, 34543]
"""


def get_palindromes(num_list: list[int]) -> list[int]:

    palindrome_list = []
    for i in num_list:
        if str(i) == str(i)[::-1]:
            palindrome_list.append(i)

    return palindrome_list


print(get_palindromes([121, 123, 131, 34543]))

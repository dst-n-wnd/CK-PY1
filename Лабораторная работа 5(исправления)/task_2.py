from random import randint


def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
    lst = []
    while len(lst) < size:
        value = randint(start, stop)
        if value not in lst:
            lst.append(value)
    return lst


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

from random import randint


def get_unique_list_numbers() -> list[int]:
    set_size = 15
    set_ = set()
    while len(set_) < set_size:
        set_.add(randint(-10, 10))
    return list(set_)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

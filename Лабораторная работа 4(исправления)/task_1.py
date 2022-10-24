def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for ch in str_:
        if ch.isalpha():
            if ch in dict_:
                dict_[ch] += 1
            else:
                dict_[ch] = 1

    return dict_


def percentages(dict_):
    sum_of_values = sum(dict_.values())
    for key in dict_.keys():
        dict_[key] = (dict_[key] * 100) // sum_of_values

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(percentages(get_count_char(main_str)))

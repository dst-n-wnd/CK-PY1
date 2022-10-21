def get_count_char(str_):
    keys = []
    count = []
    new_str = sorted(''.join(str_.split()).lower())
    for i in new_str:
        if i.isalpha():
            keys.append(i)
            count.append(new_str.count(i))
    dict_ = {k: v for k, v in zip(keys, count)}

    return dict_


def percentages(dict_):
    values = []
    sum_of_values = sum(dict_.values())

    for value in dict_.values():
        value = (value * 100) / sum_of_values
        values.append(round(value, 1))

    new_dict = {k: v for k, v in zip(dict_.keys(), values)}

    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(percentages(get_count_char(main_str)))

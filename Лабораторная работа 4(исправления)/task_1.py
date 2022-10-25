def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for ch in str_:
        if ch.isalpha():
            dict_[ch] = dict_.get(ch, 0) + 1

    return dict_


def percentages(dict_):
    new_dict = {}
    sum_of_values = sum(dict_.values())
    for key in dict_.keys():
        new_dict[key] = round(dict_[key] * 100 / sum_of_values, 1)

    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

counts = get_count_char(main_str)
percents = percentages(counts)
print(counts)
print(percents)

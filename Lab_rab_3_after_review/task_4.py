def func(salary=5000, spend=6000):
    months = 10
    increase = 0.03
    need_money = 0

    need_money += spend - salary
    for i in range(2, months+1):
        spend += spend * increase
        need_money += spend - salary

    return round(need_money)


print(func())

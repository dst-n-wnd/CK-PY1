def func(salary=5000, spend=6000):
    months = 10
    increase = 0.03
    need_money = 0

    for i in range(1, months+1):
        if i >= 2:
            spend += spend * increase
        need_money += spend - salary

    print(round(need_money))


func()

def func(money_capital=10000, salary=5000, spend=6000):
    increase = 0.05
    month = 0

    while True:
        spend += spend * increase
        money_capital += (salary - spend)
        if money_capital <= 0:
            break
        else:
            month += 1

    print(month)


func()


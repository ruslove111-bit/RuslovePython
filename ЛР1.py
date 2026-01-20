money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_alive = 0
while money_capital + salary > spend:
    if salary < spend:
        money_capital -= (spend - salary)
    if money_capital <= 0:
        break
    months_alive += 1
    spend = spend + (spend * increase)




# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months_alive)

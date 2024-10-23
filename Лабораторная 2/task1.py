money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

total_money = money_capital + salary

month = 0

while total_money > spend:
    total_money = total_money - spend
    total_money += salary
    spend = (1 + increase) * spend
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

begin_month_money = money_capital + salary

month = 0

while begin_month_money >= spend:
    begin_month_money = begin_month_money - spend
    begin_month_money += salary
    spend = (1+increase) * spend
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)

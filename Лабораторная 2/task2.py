salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

debt = 0

for i in range(months):
    total_spend = salary - spend
    spend = (1+increase) * spend
    debt += total_spend

money_capital = -debt

if money_capital % 1 == 0:
    money_capital = money_capital
else:
    money_capital += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))

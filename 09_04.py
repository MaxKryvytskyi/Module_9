'''
Повернемося до завдання розрахунку ціни з урахуванням дисконту та розберемо підхід із позиції карування. 
Створіть функцію discount_price(discount), яка визначатиме в собі та повертатиме функцію розрахунку реальної ціни з урахуванням знижки.

Виклик функції discount_price(discount) поверне функцію, яка розраховує ціну на товар зі знижкою, що дорівнює discount .

Наприклад:

cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
Повинен вивести:

85.0
90.0
95.0
'''

price = 100
def cost_25_func(price):
    return price * (1 - 0.25)
def cost_15_func(price):
    return price * (1 - 0.15)
def cost_10_func(price):
    return price * (1 - 0.10)
def cost_05_func(price):
    return price * (1 - 0.05)

def cost_00_func(price):
    return price 

def discount_price(discount):
    return OPERATIONS[str(discount)]

OPERATIONS = {
    '0.25': cost_25_func,
    '0.15': cost_15_func,
    '0.1': cost_10_func,
    '0.05': cost_05_func,
    '0' : cost_00_func
}

cost_25 = discount_price(0.25)
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)
cost_00 = discount_price(0)

print(cost_25(price))
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
print(cost_00(price))
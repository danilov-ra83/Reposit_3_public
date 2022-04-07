ticket = int(input("Введите необходимое количество билетов: "))
price = 0
for i in range(ticket):
    age = int(input("Введите возраст участника: "))
    i += 1
    if age < 18:
        print("Бесплатно!")
    elif 18 <= age <= 25:
        price += 990
        print('Стоимость билета 990 рублей')
    else:
        price += 1390
        print("Стоимость билета 1390 рублей")
if ticket > 3:
    price = price*0.9
    print("Стоимость билетов с 10% скидкой для 3+ человек: ", price)
else:
    print("Общая сумма к оплате", price)




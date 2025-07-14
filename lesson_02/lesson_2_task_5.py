num_of_month = int(input("Введите номер месяца: "))

def month_to_season(n):
    if 0 < n <= 2 or n == 12:
        print("Зима")
    elif 3 <= n <= 5:
        print("Весна")
    elif 6 <= n <= 8:
        print("Лето")
    elif 9 <= n <= 11:
        print("Осень")
    else:
        print("Неправильный номер месяца. Попробуйте снова!")

result = month_to_season(num_of_month)

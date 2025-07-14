num = int(input("Введите номер года: "))

def is_year_leap(year):
    return True if year % 4 == 0 else False

result = is_year_leap(num)

print (f"Год: {input}: {result}")

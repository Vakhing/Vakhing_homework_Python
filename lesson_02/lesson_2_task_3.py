import math 

def square(side):
    return side * side

Sq = float(input("Введите длину стороны квадрата: "))

result = square(Sq)
math.ceil(result)

rounded_result = math.ceil(result)
print(f"Площадь квадрата равна: {rounded_result}")


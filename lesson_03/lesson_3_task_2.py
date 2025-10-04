from Vakhing_homework_Python.lesson_03.smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "X30", "+79634567890"),
    Smartphone("iPhone", "11Pro", "+78321292276"),
    Smartphone("Samsung", "Galaxy", "+78329097534"),
    Smartphone("Xiaomi", "RedmiNote 14", "+73295460117"),
    Smartphone("Honor", "X9b", "+72980336451")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")


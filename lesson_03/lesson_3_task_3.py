from address_file import Address
from mailing_file import Mailing

from_address = Address("321501", "Санкт-Петербург", "улица Тверская", "дом 15A", "кв.4")
to_address = Address("305491", "Москва", "улица Арбат", "дом 37B", "кв.6")

mail = Mailing(from_address, to_address, 155, "TRK123456789")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.town}, {mail.from_address.street},"
      f"{mail.from_address.house} - {mail.from_address.room} в {mail.to_address.index}, {mail.to_address.town},"
      f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.room}. Стоимость {mail.cost} рублей.")


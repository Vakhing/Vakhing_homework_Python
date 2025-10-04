from address_file import Address
class Mailing:

 def __init__(self, to_address: Address, from_address: Address, cost: int, track: str):
     self.to_address = to_address
     self.from_address = from_address
     self.cost = cost
     self.track = track

# еще вместо типа данных int можно поставить float, если стоимость будет не круглая, например 155.75 рублей
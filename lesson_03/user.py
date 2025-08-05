class User:

 def __init__(self, first_name, last_name):
     self.first_name = first_name
     self.last_name = last_name

 def get_name(self):
     return self.first_name

 def get_surname(self):
     return self.last_name

 def full_name(self):
     return f"Имя: {self.first_name}, Фамилия: {self.last_name}"

 def __str__(self):
     return self.full_name()


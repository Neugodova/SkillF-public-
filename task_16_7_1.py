class Cat:
# создаем констуктор класса
    def __int__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

# объявляем метод get c нужными ключами
    def init_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.gender = cat_dict.get("gender")
        self.age = cat_dict.get("age")

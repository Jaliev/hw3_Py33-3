class Bank:
    def __init__(self, name, age, money, password):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__passw = password
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        self.__money = money
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

# Для удаления:
#     @password.deleter
#     def password(self):
#         del self.__password

beka = Bank('бека', 20, 0, '12345678987543')
# del beka.password
beka.name = 'name: Bond'
print(beka.name)
beka.age = f'age: {35}'
print(beka.age)
beka.money = f'money: {5678} {"$"}'
print(beka.money)
beka.password = f'password: {963852741}'
print(beka.password)

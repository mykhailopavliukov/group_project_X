class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def change_balance(self, change):
        self.__balance -= change

    def __str__(self):
        return f"Client name: {self.__name}, client balance: {self.__balance}"

















class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_name(self, name):
        return self.__name

    def get_balance(self, name):
        return self.__balance

    def change_balance(self, change):
        self.__balance -= change

















class Client:
    def __init__(self, name: str, balance: float):
        self.__name = name
        self.__balance = balance
    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def change_balance(self, change: float):
            self.__balance -= change

            if self.__balance < 0:
                raise ValueError("Balance cannot be negative")
    def __str__(self):
        return f"Client name: {self.__name}, client balance: {round(self.__balance, 2)} uah"

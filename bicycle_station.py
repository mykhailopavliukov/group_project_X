#Клас зберігає та повертає інформацію про кількість велосипедів.
import datetime
import client

class Station:

    def __init__(self, id: int, bicycles: list[Bicycle]):
        self.id = id
        self.bicycles = bicycles

    def get_count_of_bicycles(self):
        return len(self.bicycles)

    def remove_bicycle(self, bicycle: Bicycle):
        self.bicycles.remove(bicycle)

    def get_bicycle(self, bicycle: Bicycle):
        self.bicycles.append(bicycle)

#Клас зберігає інформацію про велосипед(його тип, номер),
#також для кожної поїздки буде зберігати та повертати час та ім'я клієнта.
class Bicycle:
    def __init__(self, number: int, type: str):
        self.number = number
        self.type = type
        self.time = None
        self.client = None

    def start_ride(self, client: client.Client):
        self.client = client
        self.time = datetime.datetime.now()

    def end_ride(self):
        end_time = datetime.datetime.now()
        difference = int(datetime.timedelta(end_time - self.time).total_seconds()) / 60
        if type == "NORMAL":
            self.client.change_balance(difference * 2)
        else:
            self.client.change_balance(difference * 5)

        self.client = None
        self.time = None
        return None

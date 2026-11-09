#Клас зберігає та повертає інформацію про кількість велосипедів.
import datetime

class Station:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def give_info(self):
        print(self.name)
        print(self.capacity)

#Клас зберігає інформацію про велосипед(його тип, номер),
#також для кожної поїздки буде зберігати та повертати час та ім'я клієнта.
class Bicycle:
    def __init__(self, number, type):
        self.number = number
        self.type = type
        self.time = None
        self.client = None

    def start_ride(self, client):
        self.client = client
        self.time = datetime.datetime.now()

    def end_ride(self):
        end_time = datetime.datetime.now()
        difference = int(datetime.timedelta(end_time - self.time).total_seconds()) / 60
        if type == "NORMAL":
            return difference * 2
        else:
            return difference * 5

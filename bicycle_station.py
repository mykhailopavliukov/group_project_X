#Клас зберігає та повертає інформацію про кількість велосипедів.
import datetime
from logging import setLogRecordFactory

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
        self.__number = number
        self.__type = type
        self.__time = None
        self.__client = None

    def start_ride(self, client: client.Client):
        self.__client = client
        self.__time = datetime.datetime.now()

    def end_ride(self):
        end_time = datetime.datetime.now()
        difference = int(datetime.timedelta(end_time - self.__time).total_seconds()) / 60


        if type == "NORMAL":
            result = (self.__client, difference * 2)
        else:
            result = (self.__client, difference * 5)

        self.__client = None
        self.__time = None
        return result

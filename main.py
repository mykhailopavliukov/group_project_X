import random
import time

from system import System
from client import Client
from bicycle_station import Bicycle
from bicycle_station import Station

def create_test_data():
    data = {}
    bicycles = []
    for i in range(5):
        bicycles.append(Bicycle(i, "NORMAL" if i % 2 == 0 else "ELECTRIC"))
        data["bicycles"] = bicycles

    stations = []
    stations.append(Station(1, [bicycles[0], bicycles[1], bicycles[4]]))
    stations.append(Station(2, [bicycles[3], bicycles[2]]))

    data["stations"] = stations

    users = [Client("Artem", 200), Client("Lola", 100)]
    data["users"] = users

    data["system"] = System()

    return data

def start_simulation(data, rides_min):
    rides_completed = 0
    system = data["system"]
    rides_to_complete = random.randint(rides_min, rides_min*5)
    while rides_completed <= rides_to_complete:
        took_bicycle = system.take_bicycle(random.choice(data["users"]), random.choice(data["stations"]))
        if took_bicycle:
            pass
        else:
            print("Sorry, there is no bicycle")
            continue
        time.sleep(1)
        try:
            system.return_bicycle(took_bicycle, random.choice(data["stations"]))
        except ValueError:
            print("Sorry, you dont have enough money")
        rides_completed += 1

    print("Rides completed: ", rides_completed)
    for user in data["users"]:
        print(user)

    for station in data["stations"]:
        print("Count of bicycles on station: ", station.get_count_of_bicycles())
    print("Total earnings: ", system.get_total_earn())

def test_station_with_no_bicycle():
    station = Station(1, [])
    client = Client("Artem", 200)
    system = System()
    if system.take_bicycle(client, station):
        print("Took bicycle")
    else:
        print("Sorry, there is no bicycle on station")


def main():
    test_data = create_test_data()
    start_simulation(test_data, 3)
    print("---"*50)
    print("test")
    test_station_with_no_bicycle()


main()
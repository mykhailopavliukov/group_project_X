class System:
    def __init__(self):
        self.__total_earn = 0

    def take_bicycle(self, client, station):
        try:
            bicycle = station.get_bicycle()
            bicycle.start_ride(client)
            return bicycle
        except IndexError:
            return False

    def get_total_earn(self):
        return self.__total_earn


    def balance_manipulation(self, client, pay):
        try:
            client.change_balance(pay)
            self.__total_earn += pay
        except ValueError:
            return False
        else:
            return True

    def return_bicycle(self, bicycle, station):
        client, pay = bicycle.end_ride()
        station.return_bicycle(bicycle)
        self.balance_manipulation(client, pay)




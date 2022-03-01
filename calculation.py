import datetime as dt

class Departure:
    def departure_time(self,to_home,to_work):

        # getting the time from api list
        departure_to_home = to_home[0]["when"]
        departure_to_work = to_work[0]["when"]

        # changing the time to isoformat
        iosformat_to_home = dt.datetime.fromisoformat(departure_to_home)
        iosformat_to_work = dt.datetime.fromisoformat(departure_to_work)

        # getting the departure time
        time_to_home = iosformat_to_home.time()
        time_to_work = iosformat_to_work.time()

        print ("departure from Tierpark to Alexanderplatz: {}\nand departure from Alexanderplatz to Tierpark: {}".format(time_to_work,time_to_home))

        # calculating 30 minutes before the departure time
        def time_change(departure,time_in_minutes=30):
            change = dt.timedelta(minutes=time_in_minutes)
            reminder_before_departure = departure - change
            reminder_before_departure_in_str = reminder_before_departure.strftime("%H:%M:%S")
            return reminder_before_departure_in_str

        departure_time_list = [time_change(iosformat_to_home),time_change(iosformat_to_work)]
        return departure_time_list

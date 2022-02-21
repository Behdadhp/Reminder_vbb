import API
import calculation
import schedule
import datetime as dt
import time as module_time
from plyer import notification

req = API.RequestAPI()
dep = calculation.Departure()

api_to_home = "https://v5.bvg.transport.rest/stops/900000100003/departures?direction=900000161002&duration=11&when=today+time"
api_to_work = "https://v5.bvg.transport.rest/stops/900000161002/departures?direction=900000100003&duration=11&when=today+time"

to_work_time   = str(input("When do you want to leave the home? wrtie in this format: hh:mm(am/pm): "))
to_home_time   = str(input("When do you want to leave the office? wrtie in this format: hh:mm(am/pm): "))

new_to_home_time_api = api_to_home.replace("time",to_home_time)
new_to_work_time_api = api_to_work.replace("time",to_work_time)

api_to_home_output = req.url(new_to_home_time_api )
api_to_work_output = req.url(new_to_work_time_api)



result = dep.departure_time(
          api_to_home_output,
          api_to_work_output
          )

print (result)

def notif():
    notification.notify(
        title ="Departure",
        message ="Your train is leaving in 30 minutes",
        timeout = 10
    )

if dt.datetime.today().strftime('%a') == 'Sat' or dt.datetime.today().strftime('%a') == 'Sun' :
    print ('You can sleep today!')
else:
    for i in result:
        schedule.every().day.at(i).do(notif)
    while True:
        schedule.run_pending()
        module_time.sleep(1)

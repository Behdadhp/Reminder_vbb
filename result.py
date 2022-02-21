from API import RequestAPI
import time as module_time

req = RequestAPI()


api = "https://v5.bvg.transport.rest/stops/900000100003/departures?direction=900000161002&duration=11&when=today+time"
to_office_time = str(input("When do you want to leave the home? wrtie in this format: hh:mm(am/pm): "))
to_home_time   = str(input("When do you want to leave the office? wrtie in this format: hh:mm(am/pm): "))

new_to_home_time_api   = api.replace("time",to_home_time)
new_to_office_time_api = api.replace("time",to_office_time)

api_to_home_output = req.url(new_to_home_time_api )
api_to_work_output = req.url(new_to_office_time_api)

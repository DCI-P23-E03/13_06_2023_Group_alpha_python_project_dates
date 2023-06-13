import datetime

def current_time():
    Now=datetime.datetime.now()
    print(f"The current time is: {Now.strftime('%H:%M:%S)')}")
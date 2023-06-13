import datetime, pytz

TZ=input("""Show time where?\n
    1. Tokyo, Japan\n
    2. Dublin / Ireland\n
    3. San Francisco / USA\n
    4. Johannesburg / South Africa\n
    5. Berlin / Germany\n
    Input a number (1 - 5) or anything else to abort: """)

#print(pytz.all_timezones)

flag=0
if TZ=="1":
   Time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
   Place="Tokyo, Japan"
elif TZ=="2":
   Time=datetime.datetime.now(pytz.timezone('Europe/Dublin'))
   Place="Dublin / Ireland"
elif TZ=="3":
    Time=datetime.datetime.now(pytz.timezone('US/Pacific'))
    Place="San Francisco / USA"
elif TZ=="4":
    Time=datetime.datetime.now(pytz.timezone('Africa/Johannesburg'))
    Place="Johannesburg / South Africa"
elif TZ=="5":
    Time=datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Place="Berlin / Germany"
else:
    print("Whatever")
    flag=1

if flag==0:
    print(f"The time in {Place} is {Time.strftime('%H:%M:%S %Z)')}")


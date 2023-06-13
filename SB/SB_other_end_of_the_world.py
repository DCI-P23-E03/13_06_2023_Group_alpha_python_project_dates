import datetime, pytz

print("The other end of the world is New Zealand. Not up for discussion.")

Time_NZ=datetime.datetime.now(pytz.timezone('Pacific/Auckland'))
Time_here=datetime.datetime.now()
Naive_Time_NZ=datetime.datetime(Time_NZ.year,Time_NZ.month,Time_NZ.day,Time_NZ.hour,Time_NZ.minute,Time_NZ.second)
Time_Delta=Naive_Time_NZ-Time_here

print(f"The time in Auckland, NZ is {Time_NZ.strftime('%H:%M:%S')}.\nThe time in Germany is {Time_here.strftime('%H:%M:%S')}.\nThe time difference is {round(Time_Delta/datetime.timedelta(hours=1),2)} hours.")


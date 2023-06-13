import SB_calendar,SB_convert,SB_display_current_time,SB_display_unix_time,SB_jokes,SB_leap,SB_other_end_of_the_world,SB_timedelta,SB_timezones
#import datetime,calendar,time, pyjokes,pytz

menu = input("""We're all about time today. What to you want to do?
[1] What time is it?)
[2] What UNIX time is it?
[3] What is your favorite date?
[4] Leapyear time?
[5] How much time has passed?
[6] Calendar
[7] What time is it in...?
[8] What time is it on the other side of the planet
[9] Tell me a joke
[10] Surprise: """)
             

if menu=="1":
    SB_display_current_time.current_time()
elif menu=="2":
    SB_display_unix_time.unix_time()
elif menu=="3":
    SB_convert.convert()
elif menu=="4":
    SB_leap.take_and_check_leap()
elif menu=="5":
    SB_timedelta.find_timedelta()
elif menu=="6":
    SB_calendar.print_calender()
elif menu=="7":
    SB_timezones.print_local_time()
elif menu=="8":
    SB_other_end_of_the_world.other_end()
elif menu=="9":
    SB_jokes.random_joke()
from datetime import datetime
import pytz

# Get the timezone object for New York
tz_NY = pytz.timezone('America/New_York') 

# Get the current time in New York
datetime_NY = datetime.now(tz_NY)

# Format the time as a string and print it
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

# Get the timezone object for London
tz_London = pytz.timezone('Europe/London')

# Get the current time in London
datetime_London = datetime.now(tz_London)

# Format the time as a string and print it
print("London time:", datetime_London.strftime("%H:%M:%S"))

# Get the timezone object for London
tz_India = pytz.timezone('Etc/GMT+9')

# Get the current time in India
datetime_India = datetime.now(tz_India)

# Format the time as a string and print it
print("Indian time:", datetime_India.strftime("%H:%M:%S"))

'''
print('Timezones')
for timeZone in pytz.all_timezones:
    print(timeZone)
'''
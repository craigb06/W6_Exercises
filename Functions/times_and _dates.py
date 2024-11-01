# Import datetime module
import datetime

# Question # 2
# Define known values
today = datetime.datetime.now()

# Identify pieces of information
day_name = today.strftime('%A')
month = today.strftime('%B')
day = today.strftime('%d')
year = today.strftime('%Y')

# Display the results
print(f'Today is {day_name}, {month} {day}, {year}')


# Question # 3
# Define known values
bday = datetime.date(1999,4,18)


# Display the results
print(f'My birthday is {bday.strftime('%m/%d/%Y')}')


# Question # 4
# Define known values
ninety_d = today + datetime.timedelta(days=90)

# Identify pieces of information
month = ninety_d.strftime('%B')
day = ninety_d.strftime('%d')
year =ninety_d.strftime('%Y')

# Display the results
print(f'90 days from today is {month} {day}, {year}')


# Question # 5
# Define known values
dinner_time = datetime.time()

# Display the results
print(f'Let\'s meet for dinner at {dinner_time.strftime('%I:%M %p')}')
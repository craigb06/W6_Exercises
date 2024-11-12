# Open pi million digits in read mode

pi = open('pi_million_digits.txt', 'r')
# print(pi.readline())
# pi.close()

# Create variable pi_lines

pi_lines = pi.readlines()
# pi_lines = pi.readlines(500)
# print(pi_lines)

# Create variable user birthday

user_birthday = input(f'Enter your birthday in the format MMDDYY: ')

# Create loop for i in pi lines

birthday_found = None

for i in pi_lines:
    if user_birthday in i:
        print(f'Your birthday is in the first million digits of pi')
        birthday_found = 1
        break

# if birthday_found != 1:
#     print('Sorry, your birthday was not found')
# else:
#     print(f'Your birthday begins at decimal place {birthday_position}')

# Print first two lines items of pi_lines

# print(pi_lines[0])
# print(pi_lines[1])
# print(len(pi_lines[0]))
# print(len(pi_lines[1]))

# Find position of birthday within pi

pi_string = ''

for i in pi_lines:
    pi_string += i.strip()

birthday_position = pi_string.index(user_birthday) - 1


if birthday_found != 1:
    print('Sorry, your birthday was not found')
else:
    print(f'Your birthday begins at decimal place {birthday_position}')
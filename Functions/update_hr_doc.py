# Define known values
hr_list = [
    ('0123', 'HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahna Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000')
]


# Updated hr list
for x, hr in enumerate(hr_list):

    if hr[2] == 'Mark Blick':
        hr_list[x] = (hr[0], hr[1], 'Mark Blick-Hawley', hr[3])

for x, hr in enumerate(hr_list):

    if hr[2] == 'Jim Smith':
        hr_list[x] = (hr[0], 'CS', hr[2], '60000')



# Display updated contents in following format 
# Employee# | DeptCode | Name | NN,NNN
for hr in hr_list:

    salary = f'{int(hr[3]):,}'

    print(f'{hr[0]} | {hr[1]} | {hr[2]} | {salary}')

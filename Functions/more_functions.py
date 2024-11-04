# Define three functions
# diplay mailing label function

def display_mailing_label(name, address, city, state, zip):
    print(f'{name}\n{address}\n{city}, {state} {zip}')

display_mailing_label('Craig Bowman', '2648 W 98th St.', 'Evergreen Park', 'Illinois', '60805')
display_mailing_label('Monkey D. Luffy', '545 Mystery St', 'Flower Capital', 'Wano', '55555')

# add numbers

def add_numbers(*args):
    return sum(args)

print(add_numbers(16))
print(add_numbers(53, 27))
print(add_numbers(1,2,3,4,5,6,7,8))

# display receipt
def display_receipt(total_due, amount_paid):
    if amount_paid < total_due:
        return f'Remaining balance to be paid: ${round(total_due - amount_paid, 2)}\n'
    else:
        return f'Total due: ${total_due}\nAmount Paid: ${amount_paid}\n\nChange Due: ${round(amount_paid - total_due, 2)}\n'

print(display_receipt(23.47, 30))

print(display_receipt(22.52, 22.52))

print(display_receipt(27.18, 23.60))
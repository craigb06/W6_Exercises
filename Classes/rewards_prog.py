# Create class RewardsProgram
# Create global cust_list

cust_list = []

class RewardsProgram:
    '''Rewards program for loyal customers'''
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f'Name:{self.cust_name}\nPhone:{self.phone}\nEmail:{self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!')

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))


# Create three instances of the class with sample data of customers

cust1 = RewardsProgram('John Doe', '420-555-5050', 'johndoe@mail.com')
cust2 = RewardsProgram('Jane Doe', '240-555-5353', 'janedoe@mail.com')
cust3 = RewardsProgram('Craig Bowman', '708-310-9807', 'cbowman@yearup.org')

# Display the results

cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()
cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()
cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()

# Print customer list

print(cust_list)
        
# create three functions
# get social security tax

def get_soc_sec_tax(gross_pay):
    soc_tax = gross_pay * .062
    return round(soc_tax, 2)

# get medicare tax

def get_medicare_tax(gross_pay):
    medi_tax = gross_pay * .0145
    return round(medi_tax, 2)

# get federal tax

def get_federal_tax(gross_pay, withhold_code):
    if withhold_code == 0:
        fed_tax = gross_pay * .23
        return round(fed_tax, 2)
    elif withhold_code == 1:
        fed_tax = gross_pay * .21
        return round(fed_tax, 2)
    elif withhold_code == 2:
        fed_tax = gross_pay * .195
        return round(fed_tax, 2)
    elif withhold_code == 3:
        fed_tax = gross_pay * .185
        return round(fed_tax, 2)
    elif withhold_code == 4:
        fed_tax = gross_pay * .18
        return round(fed_tax, 2)
    else:
        tax_rate = .18 - ((withhold_code - 4)* .005)
        fed_tax = gross_pay * tax_rate
        return round(fed_tax, 2)
    
# Display the results
# person 1

print(get_soc_sec_tax(750))
print(get_medicare_tax(750))
print(get_federal_tax(750, 0))

# person 2

print(get_soc_sec_tax(1550))
print(get_medicare_tax(1550))
print(get_federal_tax(1550, 2))

# person 3

print(get_soc_sec_tax(1100))
print(get_medicare_tax(1100))
print(get_federal_tax(1100, 5))
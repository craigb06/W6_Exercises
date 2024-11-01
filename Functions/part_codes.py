# Define known values
a = 'ACME:123-L'
b = 'DI:12345-M'
c = 'ACE:1-12'

# Find indexes to parse at
print(a.find(':'), b.find(':'), c.find(':'))
print(a.find('-'), b.find('-'), c.find('-'))

# Parse codes
supplier_code = [
    'supplied by {}'.format(a[0:4]),
    'supplied by {}'.format(b[0:2]),
    'supplied by {}'.format(c[0:3])
]

prod_num = [
    'Part #{}'.format(a[5:8]),
    'Part #{}'.format(b[3:8]),
    'Part #{}'.format(c[4:5])
]

size = [
    'size {}'.format(a[-1]),
    'size {}'.format(b[-1]),
    'size {}'.format(c[6:8])
]

# Display the results
print(f'{prod_num[0]}, {size[0].replace('L', 'large')}, {supplier_code[0]}')
print(f'{prod_num[1]}, {size[1].replace('M', 'medium')}, {supplier_code[1]}')
print(f'{prod_num[2]}, {size[2]}, {supplier_code[2]}')


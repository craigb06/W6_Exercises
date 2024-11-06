# Define known values
name = input('What is your name? ').lower()


# create trunc_name function

def trunc_name(n):
    vowels = 'a','e','i','o','u','y'
    if name[0] in vowels:
        return name
    elif name[1] in vowels:
        return name[1:]
    else:
        return name[2:]
    
# print(trunc_name(name))

# create name game function

tname = trunc_name(name)

def name_game(n):
    yield f'{name.capitalize()}, {name.capitalize()}, bo-b{tname}'
    yield f'banana fana fo-f{tname}'
    yield f'me my mo-m{tname}'
    yield f'{(name.capitalize())}'

for i in name_game(name):
    print(i)
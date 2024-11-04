# create a function that converts celsius to fahrenheit

def conv_c_to_f(curent_temp_C):
    curent_temp_F = (curent_temp_C * 9 / 5) + 32
    return round(curent_temp_F)

# Display the results

print(conv_c_to_f(100))
print(conv_c_to_f(45))
print(conv_c_to_f(19))
print(conv_c_to_f(0))
print(conv_c_to_f(-7))
print(conv_c_to_f(-40))

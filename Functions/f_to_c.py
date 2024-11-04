# create a function to convert fahrenheit to celsius

def conv_f_to_c(current_temp_F):
    current_temp_C = (current_temp_F - 32) * 5 / 9
    return round(current_temp_C)

# Display the results

print(conv_f_to_c(212))
print(conv_f_to_c(90))
print(conv_f_to_c(72))
print(conv_f_to_c(32))
print(conv_f_to_c(0))
print(conv_f_to_c(-40))

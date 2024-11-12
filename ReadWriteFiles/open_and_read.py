# Open the file about me in read mode

about_me = open('about_me.txt', 'r')
# print(about_me.read())
about_me.close()

# Change print statement to use .read(50)

about_me = open('about_me.txt', 'r')
# print(about_me.read(50))
# print(about_me.read(50))
about_me.close()

# Use .readline() method

about_me = open('about_me.txt', 'r')
# print(about_me.readline(10))
# print(about_me.readline())

# for i in range(1, 5):
#     print(about_me.readline())


# Use .readlines() method

# print(about_me.readlines(1))
# print(about_me.readlines(1))
# print(about_me.readlines(10))
# print(about_me.readlines(10))
# print(about_me.readlines(100))
# print(about_me.readlines(-1))               # .readlines(-1) reads the entire script


# Combining different types of read methods

fifty = about_me.read(50)
fourline = []
for i in range(1, 5):
    fourline.append(about_me.readline())
onehundred = about_me.readlines(100)

# Display the results

print(f'''First 50 characters: {fifty}
Next four lines, as list by line: {fourline}
Next 100 characters, as list by line, rounded up to complete lines: {onehundred}''')
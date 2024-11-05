# Define known values
doubler = lambda n: n * 2

# Display the results
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))


# tripler variable
# Define known values
tripler = lambda n: n * 3

# Display the results
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


# Create multiplier variable for numbers 4 through 10
def multiplier(n):
    return lambda m: m * n

quad = multiplier(4)
quin = multiplier(5)
sext = multiplier(6)
sept = multiplier(7)
octu = multiplier(8)
nonu = multiplier(9)
decu = multiplier(10)

# Display the results
print(quad(8))
print(quad(-4))
print(quad('banana'))
print(quin(8))
print(quin(-4))
print(quin('banana'))
print(sext(8))
print(sext(-4))
print(sext('banana'))
print(sept(8))
print(sept(-4))
print(sept('banana'))
print(octu(8))
print(octu(-4))
print(octu('banana'))
print(nonu(8))
print(nonu(-4))
print(nonu('banana'))
print(decu(8))
print(decu(-4))
print(decu('banana'))

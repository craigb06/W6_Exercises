# Import three modules
import random
import math
import statistics

# Define known values
vals1_100 = range(1, 100)
vals_sample = random.sample(vals1_100, 75)
vals_choices = random.choices(vals1_100, k = 200)
radius = random.randint(3, 10)
pi = math.pi

# Use a combination of functions from all three models
# _Exerimenting with a subset of integers 1-100:
sum75 = sum(vals_sample)
avg75 = sum(vals_sample) / len(vals_sample)
med75 = statistics.median(vals_sample)

# _Exerimenting with a superset of 200 values, integers 1-100:
avg200 = sum(vals_choices) / len(vals_choices)
med200 = statistics.median(vals_choices)
mode200 = statistics.mode(vals_choices)
stdev200 = statistics.stdev(vals_choices)
var200 = statistics.variance(vals_choices)

# _Modeling a random circle
area = math.pi * radius**2

# Display the results
print(f'_Experimenting with a subset of integers 1-100:\nSum of 75 sample values from 1 to 100: {sum75}\nAverage of 75 sample values: {avg75}\nMedian of 75 sample values: {med75}')

print(f'_Experimenting with a subset of 200 values, integers 1-100:\nAverage of 200 values: {avg200}\nMedian of 200 values: {med200}\nMode of 200 values: {mode200}\nStandard deviation of 200 values: {stdev200}\nVariance of 200 values: {var200}')

print(f'_Modeling a random circle:\nRadius = {radius}, area = {math.ceil(area)}\nRadius = {radius}, area = {math.floor(area)}')
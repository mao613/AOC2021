# import the panda module
import pandas as pd

# read csv with pandas csv reader module
df = pd.read_csv('input_day2.csv')

# convert to list using zip
df_list = list(zip(df.Direction,df.Magnitude))
#=
# Start horizonal distance and depth at 0
horizontal = 0
depth = 0

# Exercise 1 Day 2
#iterate over list to find horizontal position and depth
for a,b in df_list:
    if a == 'forward':
        horizontal += b
    if a == 'down':
        depth += b
    if a == 'up' :
        depth -= b

print(f'Horizontal distance is : {horizontal}')
print(f'Depth is : {depth}')
print(f'The multiplication of Horizontal distance times depth is equal to : {depth*horizontal}')

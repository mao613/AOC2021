# import the panda module
import pandas as pd

# read csv with pandas csv reader module
df = pd.read_csv('input_day2.csv')

# convert to list using zip
df_list = list(zip(df.Direction,df.Magnitude))
#=
# Start horizonal distance, aim, depth at 0
horizontal = 0
aim = 0
depth = 0

# Exercise 2 Day 2
#iterate over list to find horizontal position and depth
for a,b in df_list:
    if a == 'down':
        aim += b
    if a == 'up' :
        aim -= b
    if a == 'forward':
        horizontal += b
        depth += aim * b

# Print results
print(f'Horizontal distance is : {horizontal}')
print(f'Aim is : {aim}')
print(f'Depth is : {depth}')
print(f'The multiplication of Horizontal distance times depth is equal to : {depth*horizontal}')

import pandas as pd

data = pd.read_csv("AOC_Day1_Input.csv")

lists_from_csv = data['Dataset'].tolist()
count = 0
for ele in range(1, len(lists_from_csv)):
    x = lists_from_csv[ele] - lists_from_csv[ele-1]
    if x > 0:
        count +=1
print(count)

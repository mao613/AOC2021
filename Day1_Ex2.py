import pandas as pd

data = pd.read_csv("AOC_Day1_Input.csv")

lists_from_csv = data['Dataset'].tolist()
print(lists_from_csv)
sum_list = []
count = 0
for ele in range(2, len(lists_from_csv)):
    x = lists_from_csv[ele] + lists_from_csv[ele-1]  + lists_from_csv[ele-2]
    sum_list.append(x)
for elem in range(1, len(sum_list)):
    y = sum_list[elem] - sum_list[elem-1]
    if y > 0:
        count +=1
print(count)

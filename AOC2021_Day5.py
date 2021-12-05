import requests
import numpy as np

YEAR = '2021'
DAY = 5
PART = 1

AOC_COOKIE = '53616c7465645f5f4692237825686e1173f7058c564122a428e21de3b48f30e0964e285f91ab0c9e19279e63dc6db4b0'

def get_input(day):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input',
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text
def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}',
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]
def submit(day, level, answer):
    print(f'You are about to submit the follwing answer:')
    print(f'>>>>>>>>>>>>>>>>> {answer}')
    input('Press enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer',
                             headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        # You will get this if you submitted a wrong answer less than 60s ago.
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        # You will get this if you submit on a level you already solved.
        # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
        print('VERDICT : ALREADY SOLVED')
    else:
        print('VERDICT : OK !')
def Convert(string):
    li = list(string.split("\n"))
    return li
def Convertint(string):
    li = list(string.split("\n"))
    for i in range(0 , len(li)):
        li[i] = int(li[i])
    return li

input = get_input(DAY).strip() # the daily input is stored in input
input_list = Convert(input)
#input_list_num = Convertint(input)
example = get_example(DAY).strip()
example_list = Convert(example)

lines = [line.split(' -> ') for line in input_list]
print(lines)
# initialise array with zeroes,n = matrix size
n = 2000
diagram = np.zeros([n,n], dtype = int)

#iterate through lines
for line in lines:
    #start and finish coordinates on int type
    x1, y1 = map(int, line[0].split(','))
    x2, y2 = map(int, line[1].split(','))
    #Vertical Lines
    if x1 == x2:
        if y1 < y2:
            y_range = range(y1, y2+1)
        else:
            y_range = range(y2, y1+1)
        for y in y_range:
            diagram[y][x1] += 1

    elif y1 == y2:
        if x1 < x2:
            x_range = range(x1, x2+1)
        else:
            x_range = range(x2, x1+1)
        for x in x_range:
            diagram[y1][x] += 1
print(np.count_nonzero(diagram>1))

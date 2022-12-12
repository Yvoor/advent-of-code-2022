from pathlib import Path
import math
import numpy as np

def check_signal_strength(cycle):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        bandwidth_total.append(V*cycle)
        print('i = ' + str(i))
        print('bandwidth at cycle ' + str(cycle) + ' is ' + str(V*cycle))

def draw(cycle):
    # define column and row of matrix
    column = int(cycle)
    row = 0
    if cycle > 39:
        for k in range(math.floor(column/40)) :
            column = column - 40
            row += 1
            
    if column == V or column == (V-1) or column == (V+1):
        matrix[row][column] = 1
    else:
        matrix[row][column] = 0

## get data
data = open(Path("input") / "day10.txt", "r")
content = data.read().splitlines()

## part 1
bandwidth_total = []
cycle = 0
V = 1

for i in range(len(content)):
    if 'noop' in content[i]:
        cycle += 1
        check_signal_strength(cycle)
    elif 'addx' in content[i]:
        cycle += 1
        check_signal_strength(cycle)
        cycle += 1
        check_signal_strength(cycle)
        V += int(content[i].split(' ')[1])

print('total bandwidth = ' + str(sum(bandwidth_total)))

## part 2

bandwidth_total = []
cycle = 0
V = 1
matrix = np.zeros((6,40))

for i in range(len(content)):
    if 'noop' in content[i]:
        draw(cycle)
        cycle += 1
    elif 'addx' in content[i]:
        draw(cycle)
        cycle += 1
        draw(cycle)
        cycle += 1
        V += int(content[i].split(' ')[1])

print(matrix)


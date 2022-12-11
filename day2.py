from pathlib import Path

## part 1

data = open(Path("input") / "day2.txt", "r")
content = data.read().splitlines()

opponent = [i.split(' ', 1)[0] for i in content]
me = [i.split(' ',1)[1] for i in content]

score = 0

for i in range(len(opponent)):
    if (opponent[i] == 'A' and me[i] == 'X') or (opponent[i] == 'B' and me[i] == 'Y') or (opponent[i] == 'C' and me[i] == 'Z'):
        score += 3
    elif (opponent[i] == 'A' and me[i] == 'Y') or (opponent[i] == 'B' and me[i] == 'Z') or (opponent[i] == 'C' and me[i] == 'X'):
        score += 6
        
    if me[i] == 'X': score += 1
    elif me[i] == 'Y': score += 2
    else: score += 3

print(score)

## part 2

score = 0

for i in range(len(opponent)):
    # points for rock (1), paper(2), scissors(3)
     # points for result of each round, X = loose (0 points), Y = draw (3 points), Z = win (6 points)
    if opponent[i] == 'A' and me[i] == 'X':
        score += (3 + 0)
    elif opponent[i] == 'A' and me[i] == 'Y':
        score += (1 + 3)
    elif opponent[i] == 'A' and me[i] == 'Z':
        score += (2 + 6)
    elif opponent[i] == 'B' and me[i] == 'X':
        score += (1 + 0)
    elif opponent[i] == 'B' and me[i] == 'Y':
        score += (2 + 3)
    elif opponent[i] == 'B' and me[i] == 'Z':
        score += (3 + 6)
    elif opponent[i] == 'C' and me[i] == 'X':
        score += (2 + 0)
    elif opponent[i] == 'C' and me[i] == 'Y':
        score += (3 + 3)
    elif opponent[i] == 'C' and me[i] == 'Z':
        score += (1 + 6)
    
print(score)
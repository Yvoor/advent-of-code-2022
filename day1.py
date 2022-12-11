from pathlib import Path

## part 1

data = open(Path("input") / "day1.txt", "r")
content = data.read().splitlines()

callories_per_elf = []
callories = 0

for i in range (len(content)):
    if content[i] != '':
        callories += int(content[i])
    else: 
        callories_per_elf.append(callories)
        callories = 0
        
max_callories = max(callories_per_elf)   
 
print(max_callories)

## part 2

set = sorted(frozenset(callories_per_elf))
max_callories_3_elves = set[len(set)-1] + set[len(set)-2] + set[len(set)-3]

print(max_callories_3_elves)


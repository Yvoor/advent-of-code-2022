from pathlib import Path

def split_elf(elf):
    low = [i.split("-")[0] for i in elf]
    high = [i.split("-")[1] for i in elf]
    return list(map(int, low)), list(map(int, high))

# get data
data = open(Path("input") / "day4.txt", "r")
content = data.read().splitlines()

# split data 
elf1 = [i.split(',', 1)[0] for i in content]
elf2 = [i.split(',',1)[1] for i in content]

elf1_low, elf1_high = split_elf(elf1)
elf2_low, elf2_high = split_elf(elf2)

## part 1

redundant_elf = 0

for i in range(0, len(content)):
    if elf2_low[i] >= elf1_low[i] and elf2_high[i] <= elf1_high[i]:
        redundant_elf += 1
    elif elf1_low[i] >= elf2_low[i] and elf1_high[i] <= elf2_high[i]:
        redundant_elf += 1

print("redundant elfs: " + str(redundant_elf))

## part 2
overlapping_assignment = 0

for i in range(0, len(content)):
    if elf2_low[i] >= elf1_low[i] and elf2_low[i] <= elf1_high[i]:
        overlapping_assignment += 1
    elif elf1_low[i] >= elf2_low[i] and elf1_low[i] <= elf2_high[i]:
        overlapping_assignment += 1

print("overlapping assignments: " + str(overlapping_assignment))
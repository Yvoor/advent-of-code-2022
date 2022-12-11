from pathlib import Path

## part 1

data = open(Path("input") / "day6.txt", "r")
content = data.read()

## part 1

for i in range(len(content)):
    i1 = ord(content[i])
    i2 = ord(content[i+1])
    i3 = ord(content[i+2])
    i4 = ord(content[i+3])
    if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i2 != i3) and (i2 != i4) and (i3 != i4):
        i_stop = i + 4
        print(i_stop)
        break

## part 2

for i in range(len(content)):
    # create string of 14 characters, starting at i
    marker = content[i:i+14]
    # create a set
    marker_set = set(marker)
    # check length of set
    if len(marker_set) == 14:
        marker_location = i + 14 
        print(marker_location)
        break




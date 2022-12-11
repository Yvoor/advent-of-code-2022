from pathlib import Path

def value(letter):
    if str.islower(letter):
        return ord(letter) - ord('a') + 1
    elif str.isupper(letter):
        return ord(letter) - ord('A') + 27
    
# get data
data = open(Path("input") / "day3.txt", "r")
content = data.read().splitlines()

## part 1
double_items_value = 0

for i in range(len(content)):
    # devide string into 2 parts of equal length
    compartment1, compartment2 = content[i][:len(content[i])//2], content[i][len(content[i])//2:]
    
    # compare strings
    common_items = ''.join(set(compartment1).intersection(compartment2))
    
    # add value of common items value
    double_items_value += value(common_items)

print(double_items_value)

## part 2
sum_item_types = 0

for i in range (0,len(content),3):
    # find item type for group of 3 elves
    common_items_elf12 = ''.join(set(content[i]).intersection(content[i+1]))
    common_items_elf123 = ''.join(set(common_items_elf12).intersection(content[i+2]))

    # add value of common item types value
    sum_item_types += value(common_items_elf123)
    
print(sum_item_types)
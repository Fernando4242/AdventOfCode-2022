file = open("input.txt", "r")
lines = file.read().split("\n")


# part 1
count = 0
for line in lines:
    if line == '':
        break;
    
    elfs = line.split(',');
    
    elfOneSections = elfs[0].split('-')
    elfTwoSections = elfs[1].split('-')

    if(int(elfOneSections[0]) <= int(elfTwoSections[0]) and int(elfOneSections[1]) >= int(elfTwoSections[1])):
        count += 1
    elif (int(elfOneSections[0]) >= int(elfTwoSections[0]) and int(elfOneSections[1]) <= int(elfTwoSections[1])):
        count += 1
        
print(count)
file.close()
        
# part 2
file = open("input.txt", "r")
lines = file.read().split("\n")
count = 0
for line in lines:
    if line == '':
        break;
    
    elfs = line.split(',');
    
    elfOneSections = elfs[0].split('-')
    elfTwoSections = elfs[1].split('-')

    if(set(range(int(elfOneSections[0]), int(elfOneSections[1]) + 1)) & set(range(int(elfTwoSections[0]), int(elfTwoSections[1]) + 1))):
        count += 1;

print(count)
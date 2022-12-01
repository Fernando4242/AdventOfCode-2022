file = open("input.txt", "r")
lines = file.read().split('\n')

elf_snacks_total = []
current = 0

for line in lines:
    if line != "":
        current += int(line)
    else:
        elf_snacks_total.append(current)
        current = 0;
        
elf_snacks_total.sort(reverse=True)

print("Top Elf:")
print(elf_snacks_total[0])

print("\nTop 3 Elfs Total:")
print(sum(elf_snacks_total[:3]))
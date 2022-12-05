file = open("input.txt", "r")
lines = file.read().split("\n")

score = 0

for line in lines:
    frequency = {}
    letter = ""

    if line != "":
        firstPart, secondPart = line[: len(line) // 2], line[len(line) // 2 :]

        for element in range(0, len(firstPart)):
            key = firstPart[element]

            if key in frequency:
                frequency[firstPart[element]] += 1
            else:
                frequency[firstPart[element]] = 1

        for element in range(0, len(secondPart)):
            if secondPart[element] in frequency:
                letter = secondPart[element]
                break

        value = 0
        found = False

        for dec in range(97, 123, 1):
            value += 1

            if letter == chr(dec):
                score += value
                found = True
                break
        if not found:
            for dec in range(65, 91, 1):
                value += 1
                if letter == chr(dec):
                    score += value
                    found = True
                    break

print(score)
file.close()

file = open("input.txt", "r")
lines = file.read().split("\n")

# part two
score = 0
current = 0
for i in range(0, len(lines), 3):
    parts = []
    frequency = {}
    letter = ""

    if lines[i] == "":
        break

    for j in range(0, 3):
        parts.append(lines[i + j])

    # remove duplicates
    one = "".join(set(parts[0]))
    two = "".join(set(parts[1]))
    three = "".join(set(parts[2]))

    # combine back to one
    combined = one + two + three

    # count frequency
    for element in range(0, len(combined)):
        key = combined[element]

        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1

        # if three are the same
        if key in frequency and frequency[key] == 3:
            letter = key
            break

    value = 0
    found = False
    # find value based on ASCII a - z
    for dec in range(97, 123, 1):
        value += 1

        if letter == chr(dec):
            score += value
            found = True
            break

    # find value based on ASCII A - Z
    if not found:
        for dec in range(65, 91, 1):
            value += 1
            if letter == chr(dec):
                score += value
                break

print(score)

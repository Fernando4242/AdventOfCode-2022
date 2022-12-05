keys = {'X': {'Score': 1, 'Type': 'A'}, 'Y': {'Score': 2, 'Type': 'B'}, 'Z': {'Score': 3, 'Type': 'C'}};

file = open("input.txt", "r")
lines = file.read().split('\n')
score = 0

# part one
for line in lines:
    if line != "":
        choices = line.split(' ')    
        score += keys[choices[1]]['Score'];
        
        if choices[0] == keys[choices[1]]['Type']:
            score += 3;
        elif choices[0] == 'A' and keys[choices[1]]['Type'] == 'B':
            score +=  6;
        elif choices[0] == 'B' and keys[choices[1]]['Type'] == 'C':
            score +=  6;
        elif choices[0] == 'C' and keys[choices[1]]['Type'] == 'A':
            score +=  6;
print(score);

# part two
keys = {
    'X': {'A': 'C', 'B': 'A', 'C': 'B', 'Score': 0},
    'Y': {'A': 'A', 'B': 'B', 'C': 'C', 'Score': 3},
    'Z': {'A': 'B', 'B': 'C', 'C': 'A', 'Score': 6}}
scores = {'A': 1, 'B': 2, 'C': 3};

file = open("input.txt", "r")
lines = file.read().split('\n')

score = 0
for line in lines:
    if line != "":
        choices = line.split(' ')    
        score += keys[choices[1]]['Score'] + scores[keys[choices[1]][choices[0]]]
        
print(score)
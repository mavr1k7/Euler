# Parse the contents of the file. Remove quotes and use comma delimiter
contents = []
with open("names.txt", "r") as file:
    line = file.readline().replace('"', '')
    lines = line.split(',')
    for name in lines:
        contents.append(name)
# Sort list alphabetically
names = sorted(contents)

# Calculate the scores for each name. Sum of letter indexes in alphabet * index in alphabetical list
# ie. COLIN = 3 + 15 + 12 + 9 + 14 = 53 * 938 = 49714. 937th name in list (starting at 0)
total = 0
for i, name in enumerate(names):
    score = 0
    for c in name:
        val = ord(c) - 64
        score += val
    total += (score * (i + 1))
print("Solution: " + str(total))
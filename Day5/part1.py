filePointer = open('input.txt', 'r')
seed = filePointer.read()

allStrings = []
niceStrings = 0
position = 0
tempString = ""
ignore = False
check1Pass = False
check2Pass = False
check3Pass = False
totalVowels = 0

with open('input.txt') as f:
    allStrings = [x.strip('\n') for x in f.readlines()]

for item in allStrings:
    check1Pass = False
    check2Pass = False
    check3Pass = False
    totalVowels = 0
    storedChar = ''

    # Vowel Check
    for char in item:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            totalVowels = totalVowels + 1
        if totalVowels >= 3:
            check1Pass = True
            break

    # 1 Repeated Letter Check
    for char in item:
        if char == storedChar:
            check2Pass = True
            break
        storedChar = char

    # String Containment Check
    if "ab" not in item:
        if "cd" not in item:
            if "pq" not in item:
                if "xy" not in item:
                    check3Pass = True

    # Check if string is nice or not
    if check1Pass is True and check2Pass is True and check3Pass is True:
        niceStrings = niceStrings + 1

print("Total Nice Strings:", niceStrings)

filePointer = open('input.txt', 'r')
seed = filePointer.read()

pairs = []
allStrings = []
niceStrings = 0
tempString = ""
ignore = False
check1Pass = False
check2Pass = False
totalVowels = 0


def check2(item):
    first = False
    for i in range(len(item) - 3):
        sub = item[i: i + 2]
        if sub in item[i + 2:]:
            first = True
            break
    if not first:
        return False
    second = False
    for i in range(len(item) - 2):
        if item[i] == item[i + 2]:
            second = True
            break
    return second


with open('input.txt') as f:
    allStrings = [x.strip('\n') for x in f.readlines()]

for item in allStrings:
    check1Pass = False
    check2Pass = False
    storedChar = ''
    pairs = []

    # Repeating Letters Twice Check
    for char in item:
        pairs.append(storedChar + char)
        storedChar = char

    if len(pairs) != len(set(pairs)):
        check1Pass = True

    # Repeating Letter with 1 random in between check
    if check2(item):
        check2Pass = True

    # Check if string is nice or not
    if check1Pass is True and check2Pass is True:
        niceStrings = niceStrings + 1

print("Total Nice Strings:", niceStrings)

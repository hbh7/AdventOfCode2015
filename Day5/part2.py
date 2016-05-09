import re

filePointer = open('input.txt','r')
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
            print ("Check 2 Passed")
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

print (allStrings)

for item in allStrings:
    check1Pass = False
    check2Pass = False
    storedChar = ''    
    pairs = []

    print (item)
    # Repeating Letters Twice Check
    for char in item:
        pairs.append(storedChar + char)
        storedChar = char 
        
    if len(pairs) != len(set(pairs)):
        print ("Check 1 Passed")
        check1Pass = True      
        
    # Repeating Letter with 1 random in between check 
    if check2(item):
        check2Pass = True



    '''
    for char in item:
        print ("StoredChar:", storedChar, "CurrentChar:",char)
        if char == storedChar:
            print ("Check 2 Passed")
            check2Pass = True      
        storedChar = char 
   ''' 
    # Check if string is nice or not
    if check1Pass == True and check2Pass == True:
        print ("This string passes all checks! It's nice!") 
        niceStrings = niceStrings + 1


print ("Total Nice Strings:",niceStrings)



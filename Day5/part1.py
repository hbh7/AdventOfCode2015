filePointer = open('input.txt','r')
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

print (allStrings)

for item in allStrings:
    check1Pass = False
    check2Pass = False
    check3Pass = False
    totalVowels = 0
    storedChar = ''    

    print (item)
    # Vowel Check
    #if 's' and 'd' in item:
    for char in item:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            print ("Found a vowel:", char)
            totalVowels = totalVowels + 1
            print ("Total Vowels:", totalVowels)
        if totalVowels >= 3: 
            print ("Check 1 Passed")
            check1Pass = True
            
    # 1 Repeated Letter Check
    for char in item:
        print ("StoredChar:", storedChar, "CurrentChar:",char)
        if char == storedChar:
            print ("Check 2 Passed")
            check2Pass = True      
        storedChar = char 

    # String Containment Check 
    if "ab" not in item:
        if "cd" not in item:
            if "pq" not in item:
                if "xy" not in item:
                    print ("Check 3 Passed")
                    check3Pass = True
    
    # Check if string is nice or not
    if check1Pass == True and check2Pass == True and check3Pass == True:
        print ("This string passes all checks! It's nice!") 
        niceStrings = niceStrings + 1

    

print ("Total Nice Strings:",niceStrings)



filePointer = open('input_test2.txt','r')
seed = filePointer.read()

pairs = []
allStrings = []
niceStrings = 0
tempString = ""
ignore = False
check1Pass = False
check2Pass = False
totalVowels = 0

with open('input_test2.txt') as f:
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
#        print ("StoredChar:", storedChar, "CurrentChar:",char)
        pairs.append(storedChar + char)
        print (storedChar + char)
        storedChar = char 
        
    if len(pairs) != len(set(pairs)):
        print ("Check 1 Passed")
        check1Pass = True      
        

'''    
    # Repeating Letter with 1 random in between check 
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

    '''

print ("Total Nice Strings:",niceStrings)



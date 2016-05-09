filePointer = open('input.txt','r')
seed = filePointer.read()

numOfLeft = 0
numOfRight = 0
position = 0

for char in seed:
    position = position + 1
    if char == "(":
        numOfLeft = numOfLeft + 1
        
    elif char == ")":
        numOfRight = numOfRight + 1
        
    else:
        print ("Wat. Ignoring")
    
    if numOfLeft - numOfRight >= 0:
        continue
    else:
        print (position)
        break


final = numOfLeft - numOfRight
print ("numOfLeft: " + str(numOfLeft))
print ("numOfRight: " + str(numOfRight))
print ("final: " + str(final))

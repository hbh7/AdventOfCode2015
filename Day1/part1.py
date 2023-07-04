filePointer = open('input.txt', 'r')
seed = filePointer.read()

numOfLeft = 0
numOfRight = 0

for char in seed:
    if char == "(":
        numOfLeft = numOfLeft + 1
    elif char == ")":
        numOfRight = numOfRight + 1

print("Floor:", numOfLeft - numOfRight)

filePointer = open('input.txt', 'r')
seed = filePointer.read()

x = 0
y = 0
housesVisited = set()
housesVisited.add("0,0")

for char in seed:
    if char == "^":
        y = y + 1
    elif char == "v":
        y = y - 1
    elif char == ">":
        x = x + 1
    elif char == "<":
        x = x - 1

    xstr = str(x)
    ystr = str(y)
    coord = xstr + "," + ystr

    # Comment the following line for reduced output
    print("Current Pos:", coord)

    housesVisited.add(coord)

print("Number of houses visited:", len(housesVisited))


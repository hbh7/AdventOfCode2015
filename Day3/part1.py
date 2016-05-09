filePointer = open('input.txt','r')
seed = filePointer.read()

x = 0
y = 0
housesVisited = ['0,0']
housesVisitedMoreThanOnce = 0

for char in seed:
    if char == "^":
        y = y+1
    elif char == "v":
        y = y-1
    elif char == ">":
        x = x+1
    elif char == "<":
        x = x-1
    else:
        print ("Wat. Ignoring")
        continue

    xstr = str(x)
    ystr = str(y)
    coord = xstr + "," + ystr
    housesVisited.append(coord)

    print ("Current Pos:", x, y)

print (housesVisited)
new_list = list(housesVisited)

for coord in housesVisited:
    if housesVisited.count(coord) > 1: 
        print ("House was visited more than once:", coord)
        housesVisitedMoreThanOnce = housesVisitedMoreThanOnce + 1
        print (housesVisited.count(coord))
        while housesVisited.count(coord) > 0:
            housesVisited.remove(coord)
            print (housesVisited.count(coord))

print (housesVisitedMoreThanOnce)

filePointer = open('input.txt','r')
seed = filePointer.read()

s1x = 0
s1y = 0
s2x = 0
s2y = 0
housesVisited = ['0,0']
housesVisitedMoreThanOnce = 0
whichSanta = 1

for char in seed:
    if whichSanta == 1:
        if char == "^":
            s1y = s1y+1
        elif char == "v":
            s1y = s1y-1
        elif char == ">":
            s1x = s1x+1
        elif char == "<":
            s1x = s1x-1
        else:
            print ("Wat. Ignoring")
            continue
        s1xstr = str(s1x)
        s1ystr = str(s1y)
        coord = s1xstr + "," + s1ystr
        housesVisited.append(coord)
        whichSanta = 2
        continue
    if whichSanta == 2:
        if char == "^":
            s2y = s2y+1
        elif char == "v":
            s2y = s2y-1
        elif char == ">":
            s2x = s2x+1
        elif char == "<":
            s2x = s2x-1
        else:
            print ("Wat. Ignoring")
            continue
        s2xstr = str(s2x)
        s2ystr = str(s2y)
        coord = s2xstr + "," + s2ystr
        housesVisited.append(coord)
        whichSanta = 1
        continue        

    print ("Real Santa Current Pos:", s1x, s1y)
    print ("Robo Santa Current Pos:", s2x, s2y)

new_list = list(housesVisited)

#for coord in housesVisited:
#    if housesVisited.count(coord) > 0: 
#        print ("House was visited more than once:", coord)
#        housesVisitedMoreThanOnce = housesVisitedMoreThanOnce + 1
#        print (housesVisited.count(coord))
#        while housesVisited.count(coord) > 0:
#            housesVisited.remove(coord)
#            print (housesVisited.count(coord))




set1 = set(new_list)

list1 = list(set1)
print (len(list1))

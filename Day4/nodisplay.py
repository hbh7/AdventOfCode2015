import hashlib
puzzleInput = "ckczppom"

for i in range(1,1000000000):
    seed = puzzleInput + str(i)
    hash = hashlib.md5(seed.encode('utf-8')).hexdigest()
    #print(str(i) + " " + hash)    
    
    if hash.startswith("000000"):
        print ("WOAH THAT'S IT")
        print (i)
        break 


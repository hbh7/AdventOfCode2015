import hashlib
puzzleInput = "abcdef"

for i in range(609000, 610000):
    seed = puzzleInput + str(i)
    hash = hashlib.md5(seed.encode('utf-8')).hexdigest()
    print(str(i) + " " + hash)    

    if hash.startswith("00000"):
        print ("WOAH THAT'S IT")
        break 


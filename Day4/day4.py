import hashlib
puzzleInput = "ckczppom"

targetZeroes = 5
maxTargetZeroes = 6
i = 0
while True:
    seed = puzzleInput + str(i)
    hashVal = hashlib.md5(seed.encode('utf-8')).hexdigest()

    if hashVal.startswith("0" * targetZeroes):
        print("Lowest value ({} leading zeroes): {}".format(targetZeroes, i))

        if targetZeroes != maxTargetZeroes:
            targetZeroes += 1
        else:
            break

    i += 1


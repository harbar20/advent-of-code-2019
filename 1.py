#All of the following is for Problem 1
with open("modules.txt") as f:
    print("Problem 1: ", sum([int(int(i)/3) - 2 for i in f]))

#All of the following is for Problem 2
def one(mass):
    total = int(mass/3) - 2
    if total < 0:
        return 0
    total += one(total)
    return total

with open("modules.txt") as f:
    ls = [int(i) for i in f]
    
total = 0
for i in  ls:
    total += one(i)

print("Problem 2: ", total)

#Problem 1:  3347838
#Problem 2:  5018888
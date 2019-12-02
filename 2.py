#The following code is for Problem 1
with open("intcode.txt") as f:
    for i in f:
        intcode = i.split(",")
    intcode = [int(i) for i in intcode]
    intcode[1] = 12
    intcode[2] = 2
    
def two(intcode):
    i = 0
    while i < len(intcode):
        opcode = intcode[i]
        first = intcode[i+1]
        second = intcode[i+2]
        third = intcode[i+3]
        
        if opcode == 99:
            break
        elif opcode == 1:
            intcode[third] = intcode[first] + intcode[second]
        elif opcode == 2:
            intcode[third] = intcode[first] * intcode[second]
        else:
            break
        
        i += 4
    
    return intcode

Ls1 = []
for i in range(len(intcode)):
    if i == 1:
        one = 12
    elif i == 2:
        one = 2
    else:
        one = intcode[i]
    Ls1.append(one)
print("Problem 1: ", two(Ls1)[0])

#The following code is for Problem 2
works = False;
a = 0
b = 0
for i in range(100):
    for j in range(100):
        Ls2 = []
        for k in range(len(intcode)):
            if k == 1:
                one = i
            elif k == 2:
                one = j
            else:
                one = intcode[k]
            Ls2.append(one)
        
        if two(Ls2) == 19690720:
            works = True
            a = i
            b = j
            break
    if works:
        break

print("Problem 2: ", a, b)
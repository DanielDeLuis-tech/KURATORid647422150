f = open ('17.hard.txt')

M = []
F = 0
P = 0

for x in f.readlines ():
    M.append (int (x))


for i in range (2, len (M)):
    C1, C2, C3 = M [i - 2], M [i - 1], M [i]

    if C1 + C2 == C3:
        F += 1

    if C1 ** 2 + C2 ** 2 == C3 ** 2:
        P += 1

if F > P:
    print ('F',F)
else:
    print ('P',P)




f = open ('17.medium.txt')

M = []
TRUE = 0

for x in f.readlines ():
    M.append (int (x))


for i in range (3, len (M)):
    AL, AR, E, O =  M [i - 3], M [i - 2], M [i - 1], M [i]

    if AR > AL and AR > E and AR > O:

        TRUE += 1

print (TRUE)




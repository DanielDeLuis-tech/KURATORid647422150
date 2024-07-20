f = open ('17.easy.txt')

M = []
k = 0
summa = 0
year = 2000
bestyear = 0
maxpoints = -10 ** 5

for x in f.readlines ():
    M.append (int (x))

for i in range (0, len (M)):
    for p in range (0, len (M), 5):
        year += 1
        summa = sum (M [i + p:i + 5 + p])
        if summa > maxpoints:
            maxpoints = summa
            bestyear = year
        k += 1
    if k == len (M) // 5:
        break

print (bestyear, maxpoints)



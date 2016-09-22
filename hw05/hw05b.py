total = 0
a = [0, 2]
counter = 1
while total < 4000000 :
    total = a[counter-1] + a[counter]
    a.append(total)
    counter += 1

print sum(a)

list = [1,2,3,3,2,1]
badge = set(list)
print(badge)

#cant do his
# `print(badge[1])'

if 4 in badge:
    print("yes")
else:
    print("no")

badge.add(4)
badge.add(5)
badge.add(5)
print(badge)

#error|
#     v
#badge.remove(6)
badge.remove(1)
print(badge)
badge.discard(6)

#set operations
#union
a={1,2,3,4,5}
b={5,6,7,8,9}

print(a | b)

#intersection
print(a.intersection(b))

#difference
print(a.difference(b))

#symmertric_difference
 
print(a.symmetric_difference(b))
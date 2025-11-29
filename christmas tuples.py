#packing the values
reindeer = ('dasher','Prancer','Blitzen','vixen','rudolph','dancer','cupid','comet','donner')
print(reindeer)

#UN-packing the values
a2,b4,c9,d5,e1,f3,g7,h6,i8 = reindeer

print(e1,a2,f3,b4,d5,h6,g7,i8,c9)

antlers = 'gray','biege','brown','dark-brown'

print(antlers)

#nested tuple(double tuple)

elves =('Alabaster Snowball',('naughty list','nice list'), 'Bushy Evergreen',['Stuffed bears','plastic cars','Pretend doctors kit'], 'Pepper Minstix',('Village gardian','Protecter'))
print(elves)
print(elves[3][0])
print(elves[1][0])

# elves[0]= 'snowball'
# print(elves)
elves[3][1]='plastic toys'
print(elves)

CandyCanes=('red`n`white','green`n`red','green,white,red','green`n`white','pink`n`white')
print(CandyCanes[1:4])
print(CandyCanes[:])
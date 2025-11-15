#count occurence of vowels

h = input("Enter a chosen string -")
v = {"a":0,"e":0,"i":0,"o":0,"u":0}

for i in h:
  if i in v:
    v[i]+=1
print(v)

repeat = input("enter a chosen string -")
a = { }

for o in repeat:
  if o.isalpha():
    if o in a:
      a[o]+=1
    else:
      a[o]=1
print(a)

numb = (input("Enter a interger(s) of your choice -"))
n = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0,}

for p in numb:
  if p in n:
    n[p]+=1
fish = True
for j in n.values():
  if j == 0:
    fish = False
if fish:
  print("enter a number!")
else:
  print("this isnt a panagram")


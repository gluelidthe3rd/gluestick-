rain = [[1,2,3],[4,5,6],[7,8,9]]

print(rain)

#row printer
print(len(rain))
#column printer
print(len(rain[0]))
# first for row , second for column
print(rain[0][2])
print(rain[2][0])

for i in range(len(rain)):
    for ji in range(len(rain[0])):
       print(rain[i][ji],end=" ")
    print()

y = int(input("enter the number of rows you would like -"))
ki = int(input("enter the number of columns you would like"))

yi = []

for xi in range(y):
    zi = []
    for ye in range(ki):
        ie =int(input("enter your element-"))
        zi.append(ie)
    yi.append(zi)
for igh in range(y):
    for ia in range(ki):
        print(yi[igh][ia],end=" ")
    print()
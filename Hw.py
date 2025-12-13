# B= badminton , S= soccer , Interval means student

B={1,3,4,6,7,9}
S={2,4,6,8,1,5}

# 1- students who play both
print(S.intersection(B))
#2-student who either play badminton or soccer , not both
print(S.symmetric_difference(B))
#3-ones who only play badminton
print(B.difference(S))
#extra- ones who only play soccer
print(S.difference(B))
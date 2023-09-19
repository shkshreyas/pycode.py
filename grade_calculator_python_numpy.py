from numpy import *
a=array([[100,90,80,70,60,50,45],[90,80,70,60,50,40,30]])
L=["S", "A","B","C","D","E","F"]
n=int(input("Enter Marks Scored by Students: "))
for i in range(len(L)):
    if a[0][i]>n and a[1][i]<n:
        b=L[i]
print("Grade",b)

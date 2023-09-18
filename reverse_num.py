#reversing dictionary
d={"name":"shreyas","age":17}
rd={val:k for k,val in d.items()}
print(rd)
#reversing list
L=list(map(int,input().split(" ")))
print(L[::-1])
print(*L[::-1]) #reverse number
#reversing tuple
t=tuple(map(int,input().split(" ")))
print(t[::-1])
print(*t[::-1])




    
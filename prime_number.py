n=int(input("Enter Number: "))
if n==1:
    print(f"{n} is not a PRIME number")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not a PRIME number")
            break
    else:
        print(f"{n} is a PRIME number")
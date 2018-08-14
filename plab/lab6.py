def calnum():
    s1=input("enter a number")
    v2=int(s1)
    while v2!=1:
        if v2%2==0:
            v2=v2//2
            print(v2)
        elif v2%2==1:
            v2=v2*3+1
            print(v2)
        else:
            break
print(calnum())
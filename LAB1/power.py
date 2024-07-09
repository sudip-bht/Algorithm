def power(b,n):
    if(n==0):
        return 1
    elif (n<0):
        return 1/power(b,-n)
    else:
        p=power(b,int(n/2))
        if(n%2==0):
            return p*p
        else:
            return b*p*p
result=power(2,4)
result =power(2,-4)
print(result)

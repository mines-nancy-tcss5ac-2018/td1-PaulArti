def inv(n):
    s=str(n)
    L=[s[-1-i] for i in range(len(s))]
    s=''
    for e in L:
        s+=e
    return int(s)

def isPalindro(n):
    if n==inv(n):
        return True
    else:
        return False

def solve(n):
    i=0
    p=n
    while n<10**4 and i<50:
        p+=inv(p)
        i+=1
        if isPalindro(p):
            return False
    return True

assert solve(196)

res=0
for n in range(10**4):
    if solve(n):
        res+=1
print(res)
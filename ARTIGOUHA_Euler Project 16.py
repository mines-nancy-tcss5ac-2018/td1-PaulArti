def solve(n):
    x=[]
    while n>0:
        x.append(n%10)
        n=int(n/10)
    return sum(x)
    
assert solve(2**15)==26
print(solve(2**1000))

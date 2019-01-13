def fib_range(end_limit):
    a,b=1,2
    while True :
        yield a
        a,b = b,a+b
        if a>=end_limit:
            break
'''l=[]
for i in fib_range(40_000_00):
    if i %2==0:
        l.append(i)
result=sum(l)
print(result)'''

result = sum([x for x in fib_range(40_000_00) if x%2==0])
print(result)


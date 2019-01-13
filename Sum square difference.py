s=0
sqr=0
sqrs=[]
for i in range(1,101,1):
    s=s+i
    sq=i*i
    sqrs.append(sq)
sqr=sum(sqrs)
sumsqr=s*s
print(abs(sqr-sumsqr))
    
    
    
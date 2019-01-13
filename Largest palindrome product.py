
def check_palidrome(s) :
    s=str(s)
    if s[::]==s[::-1]:
        return True
final=[]
for i in range(999,100,-1):
    for j in range(999,100,-1):
        product= i*j
        if check_palidrome(product):
            final.append(product)
            print(i,j)
print(max(final))
            
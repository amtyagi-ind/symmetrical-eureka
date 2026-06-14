def factorial(j):
    i=j;
    j=1;
    while i>1:
        j=j*i
        i=i-1        
    return (j)

fact= lambda x,y,z:(x*y*z)

x=111111112140247;
for a in range(2,x+1,1):
    if x%a==0:
        print("Composite")
        break
print(a)
if a==x:
        print("Prime")    
    

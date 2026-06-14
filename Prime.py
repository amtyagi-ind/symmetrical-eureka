import time
import math
start_time = time.perf_counter()
def factorial(j):
    i=j;
    j=1;
    while i>1:
        j=j*i
        i=i-1        
    return (j)

fact= lambda x,y,z:(x*y*z)

x=3000000019 
z=int(math.sqrt(x))
for a in range(2,z+1,1):
    if x%(a)==0:
        print("Composite")
        break
print(a)
if a==int(math.sqrt(x)):
        print("Prime")    

end_time = time.perf_counter()

execution_time = end_time - start_time
print (execution_time)
    

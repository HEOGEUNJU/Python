#로또를 생성하시오(1~45 숫자 중에서 중복없이 6개 가져오기)
from random import random

a = random.randint(1,46)
b = random.randint(1,46)
c = random.randint(1,46)
d = random.randint(1,46)
e = random.randint(1,46)
f = random.randint(1,46)

arr=[a,b,c,d,e,f]

for i in range(1):
    arr[i] =random.randint(1,46)

print(arr)


    
arr6=[1,2,3,4,5,6]

for i in range(1000):
    rnd = int(random()*6)  
    
    a = arr6[0]
    b = arr6[rnd]
    arr6[0]=b
    arr6[rnd]=a

print(arr6[0],arr6[1],arr6[2])



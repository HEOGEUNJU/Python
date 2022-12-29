#로또를 생성하시오(1~45 숫자 중에서 중복없이 6개 가져오기)
from random import random

# a = random.randint(1,46)
# b = random.randint(1,46)
# c = random.randint(1,46)
# d = random.randint(1,46)
# e = random.randint(1,46)
# f = random.randint(1,46)
#
# arr=[a,b,c,d,e,f]
#
# for i in range(1):
#     arr[i] =random.randint(1,46)
#
# print(arr)
#

arr45 = list(range(1,46))    
print(arr45)
for i in range(100):
    rnd = int(random()*45)

     
    a=arr45[0]
    b=arr45[rnd]
    arr45[0]=b
    arr45[rnd]=a

print(arr45[0],arr45[1],arr45[2], arr45[3], arr45[4], arr45[5] )



#가위/바위/보를 넣으세요 가위
#나 : 가위
#컴 : 가위
#결과 : 비김
import random

me = input("가위바위보를 넣으세요")
com = random.random()
com1 = ""
result = ""


# for i in range(100):
#     rnd = int(random()*3)
#
#     a=com[0]
#     b=com[rnd]
#     com[0]=b
#     com[rnd]=a
#
# print(com[0])

# if com[0]==1:
#     com1="가위"
# elif com[0]==2:
#     com1="바위"
# else:
#     com1="보"

if com >0.66:
    com1 = "가위"
elif com >0.33:
    com1 = "바위"
else :
    com1 = "보"    
    
    
    
if me == com1:
    result="비김"
elif me=="가위" and com1=="바위" or me=="바위" and com1=="보" or me=="보"  and com1=="가위" :
    result="컴퓨터 승리"
else: 
    result="플레이어 승리"    

print("플레이어 : {}".format(me))
print("컴퓨터 : {}".format(com1))
print("결과 : {}".format(result))
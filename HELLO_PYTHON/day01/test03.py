# 홀/짝을 넣으세요 홀
# 나 : 홀
# 컴 : 짝
# 결과 : 졌음
import random

com =""
result=""

a= random.random()
b= float(0.5)
me = input("홀/짝을 넣으세요")

print("나 : {}".format(me))

if a>=b :
        com="짝"
else:
        com="홀"

print("컴 : {}".format(com))

if me == com:
    result = "플레이어 승리"
else:
    result = "컴퓨터 승리"

print("결과 : {}".format(result))


#출력할 단수를 넣으세요 4
#4*1=4
#4*2=8

# dan = int(input("출력할 단수를 넣으세요"))
arr = [9,8,7,2]
# for i in range(1,10):
#     print("{}*{}={}".format(dan,i,dan*i))
    
for j in range(4):
    print()
    for k in range(1,10):
        print("{}*{}={}".format(arr[j],k,arr[j]*k))
            
#출력할 단수를 넣으세요 4
#4*1=4
#4*2=8

# dan = int(input("출력할 단수를 넣으세요"))
arr = [0,1,2,3,4,5,6,7,8,9]
# for i in range(1,10):
#     print("{}*{}={}".format(dan,i,dan*i))
    
for j in range(1,10):
    print()
    for k in range(1,10):
        
        print("{}*{}={}".format(arr[j],k,arr[j]*k))
            
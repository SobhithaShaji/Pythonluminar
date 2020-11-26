lst = [1,2,3,4,6,7]
sum=6
for num in lst:
    for i in lst:
        total=num+i
        if(sum==total):
            print((num,i))
            break
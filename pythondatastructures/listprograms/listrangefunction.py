# lst =[2,3,4,6] 2*1=2 3**2=9 4***3=64
lst =[2,3,4,6]
cnt=1
out=[]
for num in lst:
    data = num**cnt
    out.append(data)
    cnt+=1
print(out)

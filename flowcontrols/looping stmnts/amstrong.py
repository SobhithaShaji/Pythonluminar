number = int(input("Enter the number"))
res = 0
while(number!=0):
    digit = number%10
    res = res+(digit**3)
    number = number//10
print (res)

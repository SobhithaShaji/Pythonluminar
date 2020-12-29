students=[[1001,"Ajay","mca",150],
        [1002,"Vijay","mca",150],
        [1003,"jay","bca",150]]
for student in students:
    print (student[1])

for student in students:
    if student[2]=='mca':
        print(student)

totalmc,totalbc=0
for student in students:
    if student[2]=='mca':
        totalmc+=student[3]

f=open("complete.csv")
#Date,Name of State / UT,Latitude,Longitude,Total Confirmed cases,Death,Cured/Discharged/Migrated,New cases,New deaths,New recovered
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmed_cases=data[4]
    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,v)
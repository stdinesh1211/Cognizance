#student details 
n=int(input("Enter The Number of Students : "))
l=[["Roll No","Name","Marks"]]
for i in range(n):
    roll=input("Enter The Roll No : ")
    sname=input("Enter The Student Name : ")
    marks=int(input("Enter The Marks : "))
    l.append([roll,sname,marks])
for i in range(len(l)):
    for j in range(len(l[i])):
        k=l[i][j]
        print(k,end='\t')
    print('\n')
h=int(input("Enter The Row to be Printed : "))
for i in l[h]:
    print(i,end='\t')
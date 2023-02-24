salariesFile=open("salaries.txt","w")



for i in range(0,10):
   salary=0
   while(salary<5000):
    salary=int(input("Enter salary: "))

   salariesFile.write(str(salary)+"\n")
    

salariesFile.close()
salariesFile=open("salaries.txt","r")
for i in range(0,10):
   salary=salariesFile.readline()
   if(int(salary)>10000):
    print("Salary is greater than 10000.It is:",salary)
salariesFile.close()
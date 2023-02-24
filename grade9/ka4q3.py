list=[10,36,54,74,58,41,25,39,47]
size=9
for i in range(0,size):
    for j in range(0,size-i-1):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("The sorted list is: ",list)
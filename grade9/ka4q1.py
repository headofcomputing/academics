count=0
totalSale=0
above80Count=0
betweenCount=0
lessCount=0
averageSale=0

while count<7:
    dailySale=-1
    while dailySale<0 or dailySale>100:
        dailySale=int(input("Enter daily sale: "))
    totalSale=totalSale+dailySale
    if dailySale>=80:
        above80Count=above80Count+1
    elif dailySale>=0:
        betweenCount=betweenCount+1
    else:
        lessCount=lessCount+1
    totalSale=totalSale+dailySale
    count=count+1
averageSale=totalSale/7
print("Total sale is:",totalSale)
print("Average sale is:",averageSale)
print("Number of days with sales above 80 is:",above80Count)
print("Number of days with sales between 0 and 80 is:",betweenCount)
print("Number of days with sales less than 0 is:",lessCount)

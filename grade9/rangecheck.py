accept=False
while accept==False:
    goals=int(input("How many goals did you score?"))
    if goals<0 or goals>10:
        print("Invalid number of goals, please try again")
    else:
        accept=True
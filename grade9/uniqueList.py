import random
player1List=[None]*13
player2List=[None]*13
player3List=[None]*13
player4List=[None]*13

#unique list for player 1
counter=0
while(counter<13):
    number=random.randint(1,13)
    if number not in player1List:
        player1List[counter]=number
        counter=counter+1
print(player1List)

#unique list for player 2
counter=0
while(counter<13):
    number=random.randint(1,13)
    if number not in player2List:
        player2List[counter]=number
        counter=counter+1
print(player2List)
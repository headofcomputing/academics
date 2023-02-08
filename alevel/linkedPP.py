class node:
    def __init__(self,theData,nextNodeNumber):
        self.data=theData
        self.nextNode=nextNodeNumber
    def outputNodes(linkedList,currentPointer):
        while currentPointer!=-1:
            print(linkedList[currentPointer].data)
            currentPointer=linkedList[currentPointer].nextNode
    def addNode(linkedList,currentPointer,emptyList):
        dataToAdd=int(input("Enter data to add: "))
        if emptyList<0 or emptyList>9:
            return False
        else:
            newNode=node(dataToAdd,-1)
            linkedList[emptyList]=newNode
            previousPointer=0
            while currentPointer!=-1:
                previousPointer=currentPointer
                currentPointer=linkedList[currentPointer].nextNode
            linkedList[previousPointer].nextNode=emptyList
            emptyList=linkedList[emptyList].nextNode
            return True
    def deleteNode(linkedList,currentPointer,emptyList):
        dataToDelete=int(input("Enter data to delete: "))
        previousPointer=0
        while currentPointer!=-1:
            if linkedList[currentPointer].data==dataToDelete:
                linkedList[previousPointer].nextNode=linkedList[currentPointer].nextNode
                linkedList[currentPointer].nextNode=emptyList
                emptyList=currentPointer
                return True
            previousPointer=currentPointer
            currentPointer=linkedList[currentPointer].nextNode
        return False
linkedList=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]

startPointer=0
emptyList=5
outputNodes(linkedList,startPointer)
returnValue=linkedList[0].addNode(linkedList,startPointer,emptyList)
if returnValue==True:
    print("Items added successfully")
else:
    print("Items not added, list full")
#outputNodes(linkedList,startPointer)


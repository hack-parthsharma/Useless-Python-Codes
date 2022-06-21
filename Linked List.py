class Node :
    nextNode=None
    def __init__(self, idata) :
        self.idata=idata
class LinkedList :
    head=None
    tail=None
    def addToTail(self, data) :
        newNode=Node(data)
        if LinkedList.head==None :
            LinkedList.head==newNode
            LinkedList.tail==newNode
        else :
            LinkedList.tail.nextNode=newNode
            LinkedList.tail=newNode
    def addToHead(self, data) :
        newNode=Node(data)
        if LinkedList.head==None :
            LinkedList.head==newNode
            LinkedList.tail==newNode
        else :
            LinkedList.tail.nextNode=LinkedList.head
            LinkedList.tail=newNode
    def deleteHead(self) :
        if LinkedList.head==None :
            print("List Empty")
        else :
            i=LinkedList.head.nextNode
            LinkedList.head=i
    def deleteTail(self) :
        if LinkedList.tail==None :
            print("List Empty")
        else :
            i=LinkedList.head
            while i.nextNode != LinkedList.tail :
                i=i.nextNode
                LinkedList.tail=i
                LinkedList.tail.nextNode=None
    def showList(self) :
        i=LinkedList.head
        while i!=None :
            print(i.idata)
            i=i.nextNode
linklist=LinkedList()
add=[x for x in input('Add Data :\n').split()]
for i in add :
    linklist.addToHead(i)
    linklist.addToTail(i)
    linklist.showList()
    linklist.deleteHead()
    linklist.deleteTail()
            
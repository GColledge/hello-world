import DL_List

myList = DL_List.DLList(5)
myList.append(4)
myList.append(3)

for each in range(10, 100, 13):
    myList.append(each)

myList.printList()

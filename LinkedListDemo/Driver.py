import LinkedList

linkedList = LinkedList.LinkedList()

print "Hello, welcome to the Linked List Driver"

print "Please enter data to input in the linked list, enter \"no\" to Stop"

keepGoing = True

while keepGoing is True:
    x = raw_input("")

    if x.lower() == "no":
        keepGoing = False

    else:
        linkedList.AppendToEnd(x)

print "Printing the numbers"
linkedList.PrintList()

print "The head of the list is: ", linkedList.GetHeadData().rjust(5, " ")
print "The tail of the list is: ", linkedList.GetTailData().rjust(5, " ")
print "The second node is: ", linkedList.At(1).rjust(5, " ")

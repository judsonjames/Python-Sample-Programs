import Node
"""
@author Judson James
@version 1.0
This class is used to demonstrate the uses of a Linked List, more information
can be found at:
https://en.wikipedia.org/wiki/Linked_list
"""
class LinkedList:

    """
    Valid Constructor Detail:
        - Contains one node to start with, which will become the head
        - Contains the size of the list, in case that is needed for any
            member functions or size constraints in a project.

        Instance Variables are:
            - size : int, this is used to find out how big the list is
            - head : Duck-Type, I will not make this list type specific and as
                    such, it will be generic.
    """
    def __init__(self):
        self.size_ = 0
        self.head_ = None

    """
    Accessors; Mutators are the "append" functions.
    """
    def GetHead (self):
        return self.head_

    def GetSize (self):
        return self.size_

    def GetHeadData (self):
        return self.head_.GetData()

    def GetTailData (self):
        return self.GetTail().GetData()

    """
    Iterates through the list in order by checking the next link
    to be able to find the tail. I do not keep a member variable for the tail
    because I find this to be verbose.
    """
    def GetTail (self):
        tempNode = self.head_

        while tempNode.GetNextLink() is not None:
            tempNode = tempNode.GetNextLink()

        return tempNode

    """
    Appends the Data object to the end of the list. This is normally standard
    in most implementations of a linked list.
    """
    def AppendToEnd (self, data):
        if (self.head_ is None):
            self.head_ = Node.Node(data, None)

        else:
            oldTail = self.GetTail()
            newTail = Node.Node(data, None)
            oldTail.SetNextLink(newTail)

        self.size_ = self.size_ + 1

    """
    Appends the Data object to the front of the list, this would be useful if
    a user would have to rewrite the head rather than the tail.
    A use case for this would be in a Queue.
    """
    def AppendToFront (self, data):
        if (self.head_ is None):
            self.head_ = Node.Node(data, None)

        else:
            oldHead = self.head_
            newHead = Node.Node(data, oldHead)
            self.head_ = newHead

        self.size_ = self.size_ + 1

    def At(self, index):
        localIndex = int(index)

        if self.size_ <= index:
            print "The index is out-of-bounds, returning null value"
            return "None"

        else:
            tempNode = self.head_
            for x in range(0, index):
                tempNode = tempNode.GetNextLink()

            return tempNode.GetData()
    """
    Prints out the List
    """
    def PrintList (self):
        tempNode = self.head_

        keepGoing = True
        while keepGoing is True:
            print tempNode.GetData()

            if tempNode.GetNextLink() == None:
                keepGoing = False
            else:
                tempNode = tempNode.GetNextLink()

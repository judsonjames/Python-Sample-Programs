"""
@author Judson James
@version 1.0
Everything in this class is used as an encapsulated data object.
"""
class Node:

    """
    Member Variables
        - Data_ : duck-typed
        - NextLink_ : Node
    """
    def __init__(self, data, nextLink):
        self.nextLink_ = nextLink
        self.data_ = data

    """
    Accessors and Mutators
    """
    def GetNextLink(self):
        return self.nextLink_

    def GetData(self):
        return self.data_

    def SetNextLink(self, theNextLink):
        self.nextLink_ = theNextLink

    def SetData(self, theData):
        self.data_ = theData

from functools import total_ordering
from collections import Counter as frequencies
from printBin import Node, nodeToString

DEFAULT = "$"


@total_ordering
class FrequencyNode:
    """Node for Huffman coding tree with frequency values"""
    
    def __init__(self, symb=DEFAULT, val=0, left=None, right=None):
        self.val = val
        self.symb = symb
        self.left = left
        self.right = right
    
    def __bool__(self) -> bool:
        return self.val != 0 and self.symb != " "
    
    def __repr__(self) -> str:
        return str((self.symb, self.val))
    
    def __str__(self) -> str:
        """Pretty print the tree structure using printBin"""
        if not self:
            return ""
        return nodeToString(self.toPrintNode())

    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other) -> bool:
        if type(self) == type(other): 
            return self.val == other.val and self.symb == other.symb
        return False
    
    def __add__(self, other):
        if type(self) == type(other):
            mini, maxi = sorted([self, other])
            return FrequencyNode(val=self.val + other.val, 
                                left=mini,
                                right=maxi)
        else:
            return FrequencyNode()
    
    def codes(self, binLeft=0):
        """Generate Huffman codes for all symbols in the tree"""
        res = {}
        res[self.symb] = ""
        if self.left:
            res[self.left.symb] = str(binLeft)
            left = self.left.codes(binLeft)
            for code in left:
                left[code] = str(binLeft) + left[code]
            res.update(left)
        if self.right:
            res[self.right.symb] = str(1 - binLeft)
            right = self.right.codes(binLeft)
            for code in right:
                right[code] = str(1 - binLeft) + right[code]
            res.update(right)
        return res
    
    def toPrintNode(self):
        """Converts FrequencyNode tree to printBin Node format"""
        if not self:
            return None
        leftNode = self.left.toPrintNode() if self.left else None
        rightNode = self.right.toPrintNode() if self.right else None
        return Node(val=f"({self.symb}, {self.val})", left=leftNode, right=rightNode)


def appendWithOrder(sortedList: list, el):
    """
    Appends el in sortedList keeping order (preference left).

    Args:
        sortedList: List of elements comparable to el
        el: Element to insert
    """
    l, r = 0, len(sortedList) - 1
    res = 0
    while l <= r:
        m = (l + r) // 2
        if sortedList[m] >= el:
            r = m - 1
            res = min(res, m)
        else:
            l = m + 1
    sortedList.insert(res, el)
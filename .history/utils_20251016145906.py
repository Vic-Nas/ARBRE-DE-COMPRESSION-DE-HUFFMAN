from functools import total_ordering
from collections import Counter as frequencies, deque
DEFAULT = "$"

@total_ordering
class Node:
    def __init__(self, symb = DEFAULT, val = 0, left = None, right = None):
        self.symb = symb
        self.val = val
        self.left = left
        self.right = right       

    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other) -> bool:
        if type(self) == type(other): 
            return self.val == other.val and self.symb == other.symb
        return False
    
    def __add__(self, other):
        if type(self) == type(other):
            mini, maxi = sorted([self, other])
            return Node(val = self.val + other.val, 
                        left = mini,
                        right = maxi)
        else:
            return Node()
        
    def __bool__(self) -> bool:
        return self.val != 0
    
    def codes(self):
        res = {}
        res[self.symb] = ""
        if self.left:
            res[self.left.symb] = "1"
            left = self.left.codes()
            for code in left:
                left[code] = "1" + left[code]
            res.update(left)
        if self.right:
            res[self.right.symb] = "0"
            right = self.right.codes()
            for code in right:
                right[code] = "0" + right[code]
            res.update(right)
        return res
    
    def __repr__(self) -> str:
        return str((self.symb, self.val))
    
    def __str__(self):
        f = deque([self])
        level = 1
        toPrint = []
        while f:
            el = f.popleft()
            toPrint.append(())
            
            
            
        res =  str((self.symb, self.val))
        return res
    
    def level(self, root) -> int:
        if root is None:
            return 0
        
        if root == self:
            return 1
        
        # Search in left subtree
        left_level = self.level(root.left)
        if left_level != 0:
            return 1 + left_level
        
        # Search in right subtree
        right_level = self.level(root.right)
        if right_level != 0:
            return 1 + right_level
        
        # Not found in either subtree
        return 0
    
    def maxLevel(self, root = None) -> int:
        if not root: root = self
        if self:
            res = self.level(root)
            if self.left:
                res = max(res, self.left.maxLevel(root))
            if self.right:
                res = max(res, self.right.maxLevel(root))
            return res
        return 0
    
    
def appendWithOrder(sortedList: list, el):
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

from functools import total_ordering
from collections import Counter as frequencies, deque, defaultdict

DEFAULT = "$"


class BinaryNode:
    """Base class for binary tree nodes with string representation and level methods"""
    
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def __str__(self):
        """Pretty print the tree structure"""
        if not self:
            return ""
        
        f = deque([self])
        maxLevel = self.maxLevel()
        toPrint = defaultdict(list)
        
        while f:
            el = f.popleft()
            itsLevel = el.level(self)
            itsRepr = el._nodeRepr()
            toPrint[itsLevel].append(itsRepr)
            
            if el.left:
                f.append(el.left)
            elif itsLevel < maxLevel:
                # Add placeholder for missing nodes
                f.append(self._createEmptyNode())
            
            if el.right:
                f.append(el.right)
            elif itsLevel < maxLevel:
                # Add placeholder for missing nodes
                f.append(self._createEmptyNode())
        
        res = ""
        for level in range(1, maxLevel + 1):
            res += "  ".join(toPrint[level]) + "\n"
        
        return res.rstrip()
    
    def _nodeRepr(self):
        """Override this in subclasses to customize node representation"""
        return repr(self)
    
    def _createEmptyNode(self):
        """Override this in subclasses to create appropriate empty nodes"""
        return BinaryNode()
    
    def level(self, root) -> int:
        """Find the level of this node in the tree rooted at 'root'"""
        if root is None:
            return 0
        
        if root == self:
            return 1
        
        # Search in left subtree
        leftLevel = self.level(root.left)
        if leftLevel != 0:
            return 1 + leftLevel
        
        # Search in right subtree
        rightLevel = self.level(root.right)
        if rightLevel != 0:
            return 1 + rightLevel
        
        # Not found in either subtree
        return 0
    
    def maxLevel(self, root=None) -> int:
        """Find the maximum depth of the tree"""
        if not root:
            root = self
        if self:
            res = self.level(root)
            if self.left:
                res = max(res, self.left.maxLevel(root))
            if self.right:
                res = max(res, self.right.maxLevel(root))
            return res
        return 0


@total_ordering
class FrequencyNode(BinaryNode):
    """Node for Huffman coding tree with frequency values"""
    
    def __init__(self, symb=DEFAULT, val=0, left=None, right=None):
        super().__init__(left, right)
        self.symb = symb
        self.val = val

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
        
    def __bool__(self) -> bool:
        return self.val != 0
    
    def codes(self):
        """Generate Huffman codes for all symbols in the tree"""
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
    
    def _nodeRepr(self):
        """Custom node representation for frequency nodes"""
        maxVal = self.maxVal()
        valLen = len(str(maxVal))
        return str((self.symb, str(self.val).ljust(valLen, "0")))
    
    def _createEmptyNode(self):
        """Create empty placeholder node for tree printing"""
        return FrequencyNode(" ", 0)
    
    def maxVal(self) -> int:
        """Find the maximum frequency value in the tree"""
        if self:
            res = self.val
            if self.left:
                res = max(res, self.left.maxVal())
            if self.right:
                res = max(res, self.right.maxVal())
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

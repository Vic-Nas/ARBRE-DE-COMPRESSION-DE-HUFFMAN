from functools import total_ordering
from collections import Counter as frequencies, deque, defaultdict

DEFAULT = "$"


class BinaryNode:
    """Base class for binary tree nodes with string representation and level methods"""
    
    def __init__(self, symb=DEFAULT, val=0, left=None, right=None):
        self.symb = symb
        self.val = val
        self.left = left
        self.right = right
    
    def __bool__(self) -> bool:
        return self.val != 0 and self.symb != " "
    
    def __repr__(self) -> str:
        return str((self.symb, self.val))
    
    def __str__(self):
        """Pretty print the tree structure"""
        if not self:
            return ""
        
        f = deque([(self, 1)])  # Store (node, level) tuples
        maxLevel = self.maxLevel()
        maxVal = self.maxVal()
        toPrint = defaultdict(list)
        
        while f:
            el, itsLevel = f.popleft()
            itsRepr = el._nodeRepr(maxVal)
            toPrint[itsLevel].append(itsRepr)
            
            # Add children (or empty placeholders) if not at max level
            if itsLevel < maxLevel:
                if el.left:
                    f.append((el.left, itsLevel + 1))
                else:
                    f.append((self._createEmptyNode(), itsLevel + 1))
                
                if el.right:
                    f.append((el.right, itsLevel + 1))
                else:
                    f.append((self._createEmptyNode(), itsLevel + 1))
        
        # Get node width for spacing calculations
        nodeWidth = len(toPrint[1][0])
        
        res = ""
        for level in range(1, maxLevel + 1):
            # Calculate spacing: each level has half the spacing of the level below
            # Bottom level nodes are separated by nodeWidth spacing
            # Each level up doubles the spacing between node centers
            nodesInLevel = 2 ** (level - 1)
            spacingMultiplier = 2 ** (maxLevel - level)
            spacing = " " * (nodeWidth * spacingMultiplier)
            
            row = spacing.join(toPrint[level])
            
            # Add padding to center the row
            # The total width is determined by the bottom level
            bottomWidth = len(toPrint[maxLevel][0]) * (2 ** (maxLevel - 1)) + nodeWidth * (2 ** (maxLevel - 1) - 1)
            res += row.center(bottomWidth) + "\n"
        
        return res.rstrip()
    
    def _nodeRepr(self, maxVal=None):
        """Override this in subclasses to customize node representation"""
        if not self:
            if maxVal is None:
                maxVal = 1
            valLen = len(str(maxVal))
            nodeStr = str((" ", "0".ljust(valLen, "0")))
            return " " * len(nodeStr)
        
        if maxVal is None:
            maxVal = self.maxVal()
        valLen = len(str(maxVal))
        return str((self.symb, str(self.val).ljust(valLen, "0")))
    
    def _createEmptyNode(self):
        """Override this in subclasses to create appropriate empty nodes"""
        return BinaryNode(" ", 0)
    
    def level(self, root) -> int:
        """Find the level of this node in the tree rooted at 'root'"""
        if root is None:
            return 0
        
        if root == self:
            return 1
        
        # Don't search in empty placeholder nodes
        if not root:
            return 0
        
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
    
    def maxVal(self) -> int:
        """Find the maximum value in the tree"""
        if self:
            res = self.val
            if self.left:
                res = max(res, self.left.maxVal())
            if self.right:
                res = max(res, self.right.maxVal())
            return res
        return 0


@total_ordering
class FrequencyNode(BinaryNode):
    """Node for Huffman coding tree with frequency values"""
    
    def __init__(self, symb=DEFAULT, val=0, left=None, right=None):
        super().__init__(symb, val, left, right)

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
    
    def codes(self, binLeft="0"):
        """Generate Huffman codes for all symbols in the tree"""
        binRight = str(1 - int(binLeft))
        res = {}
        res[self.symb] = ""
        if self.left:
            res[self.left.symb] = binLeft
            left = self.left.codes(binLeft)
            for code in left:
                left[code] = binLeft + left[code]
            res.update(left)
        if self.right:
            res[self.right.symb] = binRight
            right = self.right.codes(binLeft)
            for code in right:
                right[code] = "0" + right[code]
            res.update(right)
        return res
    
    def _createEmptyNode(self):
        """Create empty placeholder node for tree printing"""
        return FrequencyNode(" ", 0)

    
    
    
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

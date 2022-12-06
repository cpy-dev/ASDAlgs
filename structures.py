class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None
        self.name = None

m = 0

null = None

red = 1
black = 0

class BRTree:
    def __init__(self):
        self.null = None
        self.root = None

class BRNode:
    def __init__(self, tree: BRTree):
        self.tree = tree
        self.parent = None
        self.key = None
        self.left = None
        self.right = None
        self.name = None
        self.color = None
        self.size = None

class IntervalTree(BRTree):
    def __init__(self):
        super(IntervalTree, self).__init__()

class IntervalNode(BRNode):
    def __init__(self):
        super(IntervalNode, self).__init__()
        self.low = None
        self.high = None

inf = None
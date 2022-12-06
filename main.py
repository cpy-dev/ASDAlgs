from structures import *

def hashSerach(table, value):
    i = 0
    j = 0
    while table[j] == null or i == m:
        j = hash(value, i)
        if table[j] == value:
            return j
        i += 1
    return

def hashInsert(table, value):
    i = 0
    while i != m:
        j = hash(value, i)
        if table[j] == null:
            table[j] = value
            return j

        i += 1
    raise Exception('Hash table overflow')

def hash(value, i):
    return (baseHash(value) + i) % m

def baseHash(value):
    return value % m

############## BINARY TREES ##################

def treeInsert(tree: Tree, node: Node):
    finalParent = null
    possibleParent = tree.root

    while possibleParent != null:
        finalParent = possibleParent
        if node.key < possibleParent.key:
            possibleParent = possibleParent.left
        else:
            possibleParent = possibleParent.right

    node.parent = finalParent

    if finalParent == null:
        tree.root = node

    elif possibleParent.key < finalParent.key:
        finalParent.left = node

    else:
        finalParent.right = node

def treeSearch(baseNode: Node, value):
    if baseNode == null or baseNode.key == value:
        return baseNode

    if value < baseNode.key:
        return treeSearch(baseNode.left, value)

    return treeSearch(baseNode.right, value)

def iterativeTreeSearch(baseNode: Node, value):
    while baseNode != null and value != baseNode.key:
        if value < baseNode.key:
            baseNode = baseNode.left
        else:
            baseNode = baseNode.right
    return baseNode

def treeMinimum(node: Node):
    while node.left != null:
        node = node.left
    return node

def treeMaximum(node: Node):
    while node.right != null:
        node = node.right
    return node

def inorderTreeWalk(node):
    if node != null:
        inorderTreeWalk(node.left)
        print(node)
        inorderTreeWalk(node.right)

def preorderTreeWalk(node):
    if node != null:
        print(node)
        preorderTreeWalk(node.left)
        preorderTreeWalk(node.right)

def postorderTreeWalk(node):
    if node != null:
        postorderTreeWalk(node.left)
        postorderTreeWalk(node.right)
        print(node)

def parenthesizedPrint(node):
    if node != null:
        print(f'{node.name}(')
        parenthesizedPrint(node.left)
        print(',')
        parenthesizedPrint(node.right)
        print(')')
    else:
        print('_')

def treeSuccessor(node):
    if node.right != null:
        return treeMinimum(node.right)
    successor = node.parent

    while successor != null and node == successor.right:
        node = successor
        successor = successor.parent

    return successor

def treePredecessor(node):
    if node.left != null:
        return treeMaximum(node.left)
    predecessor = node.parent

    while predecessor != null and node == predecessor.left:
        node = predecessor
        predecessor = predecessor.parent

    return predecessor

def trasplant(tree: Tree, node1: Node, node2: Node):
    if node1.parent == null:
        tree.root = node2

    elif node1 == node1.parent.left:
        node1.parent.left = node2

    else:
        node1.parent.right = node2

    if node2 != null:
        node2.parent = node1.parent

def treeDelete(tree, node):
    if node.left == null:
        trasplant(tree, node, node.right)

    elif node.right == null:
        trasplant(tree, node, node.left)

    else:
        replacer = treeMinimum(node.right)

        if replacer.parent != node:
            trasplant(tree, replacer, replacer.right)
            replacer.right = node.right
            replacer.right.parent = replacer

        trasplant(tree, node, replacer)
        replacer.left = node.left
        replacer.left.parent = replacer

####################################################

def leftRotate(tree: BRTree, node: BRNode):
    localRoot = node.right
    node.right = localRoot.left

    if localRoot.left != tree.null:
        localRoot.left.parent = node
    localRoot.parent = node.parent

    if node.parent == tree.null:
        tree.root = localRoot

    elif node == node.parent.left:
        node.parent.left = localRoot

    else:
        node.parent.right = localRoot

    node.left = node
    node.parent = localRoot

def rightRotate(tree: BRTree, node: BRNode):
    localRoot = node.left
    node.left = localRoot.right

    if localRoot.right != tree.null:
        localRoot.right.parent = node
    localRoot.parent = node.parent

    if node.parent == tree.null:
        tree.root = localRoot

    elif node == node.parent.right:
        node.parent.right = localRoot

    else:
        node.parent.left = localRoot

    node.right = node
    node.parent = localRoot

def brInsert(tree: BRTree, node: BRNode):
    finalInsertRoot = tree.null
    possibleInsertRoot = tree.root

    while possibleInsertRoot != tree.null:
        finalInsertRoot = possibleInsertRoot
        if node.key < possibleInsertRoot.key:
            possibleInsertRoot = possibleInsertRoot.left
        else:
            possibleInsertRoot = possibleInsertRoot.right

    node.parent = finalInsertRoot

    if finalInsertRoot == tree.null:
        tree.root = node

    elif node.key < finalInsertRoot.key:
        finalInsertRoot.left = node

    else:
        finalInsertRoot.right = node

    node.left = tree.null
    node.right = tree.null

    node.color = red
    brInsertFixup(tree, node)


def brInsertFixup(tree, node):
    while node.parent.color == red:
        if node.parent == node.parent.parent.left:
            uncleNode = node.parent.parent.right

            if uncleNode.color == red:
                node.parent.color == black
                uncleNode.color = black

                node.parent.parent.color = red
                node = node.parent.parent

            else:
                if node == node.parent.right:
                    node = node.parent
                    leftRotate(tree, node)

                node.parent.color = black
                node.parent.parent.color = red
                rightRotate(tree, node.parent.parent)

        else:
            node = node.parent.parent.left

            if uncleNode.color == red:
                node.parent.color = black
                uncleNode.color = black

                node.parent.parent.color = red
                node = node.parent.parent

            else:
                if node == node.parent.left:
                    node = node.parent
                    rightRotate(tree, node)

                node.parent.color = black
                node.parent.parent.color = red
                leftRotate(tree, node.parent.parent)

    tree.root.color = black

def osSelect(node, position):
    rank = node.left.size + 1

    if position == rank:
        return node

    elif position < rank:
        return osSelect(node.left, position)

    else:
        return osSelect(node.right, position-rank)

def osRank(tree, node):
    rank = node.left.size + 1
    y = node

    while y != tree.root:
        if y == y.parent.right:
            rank += y.parent.left.size + 1
        y = y.parent

    return rank

def setSize(node: BRNode):
    if node == node.tree.null:
        node.size = 0
        return 0

    rightSize = setSize(node.right)
    leftSize = setSize(node.left)

    node.size = rightSize + leftSize + 1
    return node.size

#######################################################

def intervalSearch(tree, value):
    node = tree.root

    while node != tree.null and not (value.low >= node.low and value.high <= node.high):
        if node.left != tree.null and node.left.high >= value.low:
            node = node.left

        else:
            node = node.right

    return node

######################################################

def cutRod(priceTable, lenght):
    if lenght == 0:
        return 0

    cutQuote = - inf
    i = 1

    while i < lenght:
        cutQuote = max(cutQuote, priceTable[i]+cutRod(priceTable, lenght-i))
        i += 1

    return cutQuote

def memorizedCutRod(priceTable, lenght):
    results = []

    for i in range(lenght):
        results.append(-inf)

    return memorizedCutRodAux(priceTable, lenght, results)

def memorizedCutRodAux(priceTable, lenght, results):
    if results[lenght] >= 0:
        return results[lenght]

    if lenght == 0:
        cutQuote = 0

    else:
        cutQuote = - inf

        for i in range(lenght):
            cutQuote = max(cutQuote, priceTable[i]+memorizedCutRodAux(priceTable, lenght-i, results))

        results[lenght] = cutQuote
        return cutQuote

def bottomUpCutRod(priceTable, lenght):
    results = []

    for i in range(lenght):
        results.append(0)

    j = 1
    while j < lenght:
        cutQuote = -inf

        i = 1
        while i < j:
            cutQuote = max(cutQuote, priceTable[i]+results[j-i])
            i += 1

        results[j] = cutQuote
        j += 1

    return results[lenght]

def extendedBottomUpCutRod(priceTable, lenght):
    results = []
    slices = []

    for i in range(lenght):
        results.append(0)
        slices.append(0)

    j = 1
    while j < lenght:
        cutQuote = - inf

        i = 1
        while i < j:
            if cutQuote < priceTable[i] + results[j-1]:
                cutQuote = priceTable[i] + results[j-1]
                slices[j] = i

            i += 1

        results[j] = cutQuote
        j += 1
    return results, slices

def printCutRodSolution(priceTable, lenght):
    results, slices = extendedBottomUpCutRod(priceTable, lenght)

    while lenght > 0:
        print(slices[lenght])
        lenght -= slices[lenght]

##########################################################


def lcsLenght(sequence1, sequence2):
    sequence1Lenght = len(sequence1)
    sequence2Lenght = len(sequence2)

    costs = [[]]

    
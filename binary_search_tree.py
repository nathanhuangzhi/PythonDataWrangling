class Node(object):
    def __init__(self,k,val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None

import collections

def levelorderprint(tree):

    nodes = [tree]
    currentCount = 1
    nextCount = 0

    while len(nodes) != 0:

        currentNode = nodes.pop()
        currentCount -= 1

        print(currentNode.key)

        if currentNode.left:
            nodes.insert(0, currentNode.left)
            nextCount += 1

        if currentNode.right:
            nodes.insert(0,currentNode.right)
            nextCount += 1



        if currentCount ==0:
            print('\n')
            currentCount,nextCount = nextCount,currentCount




root = Node(10,'Hello')
root.left = Node(5,'Five')
root.right = Node(30,'Thirty')
root.left.right = Node(15,'Fifteen')

# print(levelorderprint(root))





def trimBST(tree,minVal, maxVal):

    if not tree:
        return

    tree.left  = trimBST(tree.left,minVal,maxVal)
    tree.right = trimBST(tree.right,minVal,maxVal)


    if minVal<=tree.key<=maxVal:
        return tree

    if tree.key<minVal:
        return tree.right

    if tree.key>maxVal:
        return tree.left

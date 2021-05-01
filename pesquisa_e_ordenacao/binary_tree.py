# Binary Search Tree (BST)
from random import randint, shuffle

def createTree(value):
  treeDict = {"value": value, "left": None, "right": None}
  return treeDict

def insertTree(tree, value):
  branch = "left" if value < tree["value"] else "right"
  if tree[branch] is None:
    tree[branch] = createTree(value)
  else:
    insertTree(tree[branch], value)
  
def searchTree(tree, value):
  if value == tree["value"]:
    return True
  branch = "left" if value < tree["value"] else "right"
  if tree[branch] is None:
    return False
  else:
    return searchTree(tree[branch], value)

def findTree(tree, value):
  if searchTree(tree, value):
    print(f"{value} is part of the tree")
  else:
    print(f"{value} is not part of the tree")

# In order
def printTree(tree, firstCall = True):
  if tree is not None:
    print(tree["value"], end="")
    print("(", end="")
    printTree(tree["left"], False)
    printTree(tree["right"], False)
    print(")", end="")
  # New line after printing the tree
  if firstCall:
    print("\n")

def indentPrintTree(tree, count = 0, symbol = None, firstCall = True):
  if firstCall:
    print("<tree>")
  if tree is not None:
    for i in range(count - 1):
      print("    ", end="")
    if count >= 1:
      print(f"{symbol}---", end="")
    print(tree["value"])
    count = count + 1
    indentPrintTree(tree["left"], count, "L", False)
    indentPrintTree(tree["right"], count, "R", False)
  if firstCall:
    print("</tree>\n")

def removeTree(tree, value):
  if value == tree["value"]:
    tree = None
  while True:
    branch = "left" if value < tree["value"] else "right"
    parent = tree
    tree = tree[branch]
    if tree is None:
      return
    if value == tree["value"]:
      isLeftNone = tree["left"] is None
      isRightNone = tree["right"] is None
      # No children
      if isLeftNone and isRightNone:
        parent[branch] = None
      # One child
      elif isLeftNone or isRightNone:
        parent[branch] = tree["left" if isRightNone else "right"]
      # Two children
      else:
        successor = tree["right"]
        if successor["left"] is None:
          successor["left"] = tree["left"]
          parent[branch] = successor
          return
        successorParent = tree
        while successor["left"] is not None:
          successorParent = successor
          successor = successor["left"]
        parent[branch]["value"] = successor["value"]
        successorParent["left"] = successor["right"]
      return

def listTree(tree, list = [], firstCall = True):
  if tree is not None:
    list.append(tree["value"])
    listTree(tree["left"], list)
    listTree(tree["right"], list)
  if firstCall:
    return list

tree = createTree(randint(0, 100))
for i in range(10):
  insertTree(tree, randint(0, 100))
indentPrintTree(tree)
treeList = listTree(tree)
shuffle(treeList)
print(f"Remove {treeList[:3]}\n")
for i in range(3):
  removeTree(tree, treeList[i])
indentPrintTree(tree)

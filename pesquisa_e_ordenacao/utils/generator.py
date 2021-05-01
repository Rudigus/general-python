import random

def getRandomList(elementCount):
  intList = [element for element in range(elementCount)]
  random.shuffle(intList)
  return intList

def getRandomRepeatingList(elementCount):
  intList = [random.randint(0, elementCount - 1) for _ in range(elementCount)]
  return intList

def getRandomRepeatingListWithRange(elementCount, elementRange):
  intList = [random.randint(0, elementRange - 1) for _ in range(elementCount)]
  return intList

def getDecrescentList(elementCount):
  list = [element for element in range(elementCount)]
  list.reverse()
  return list

import random
from .element import Element

def getRandomRepeatingListWithRange(elementCount, elementRange):
  intList = [Element(random.randint(0, elementRange - 1), i) for i in range(elementCount)]
  return intList

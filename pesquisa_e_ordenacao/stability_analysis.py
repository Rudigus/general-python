from generator import getRandomRepeatingListWithRange
from sorter import bubbleSort, insertionSort, selectionSort, quickSort

def printElements(elements):
  for i in range(len(elements)):
    print(f"({elements[i].value}, {elements[i].id})", end = "")
    if(i < len(elements) - 1):
      print(", ", end="")
    else:
      print()

def testStability(sortFunction, sortName, stable):
  print(f"{sortName} - Before Ordering\n")
  elements = getRandomRepeatingListWithRange(10, 4)
  printElements(elements)
  print(f"\n{sortName} - After Ordering\n")
  sortFunction(elements)
  printElements(elements)
  if stable:
    print(f"\n{sortName} is stable because the order of repeated elements does not change after the sorting, which is shown when you compare elements with the same value: their ID always increases as you move from left to right.\n")
  else:
    print(f"\n{sortName} is unstable because the order of repeated elements may change after the sorting, so if you compare elements with the same value, you can have an element to the right of another one but with a smaller ID.\n")

print("Format: (value, id)\n")
testStability(bubbleSort, "Bubble Sort", True)
testStability(insertionSort, "Insertion Sort", True)
testStability(selectionSort, "Selection Sort", False)
testStability(quickSort, "Quick Sort", False)

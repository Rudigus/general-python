# Bubble Sort
def bubbleSort(list):
  endIndex = len(list) - 1
  while True:
    shouldContinue = False
    for i in range(endIndex):
      if list[i].value > list[i + 1].value:
        temp = list[i + 1]
        list[i + 1] = list[i]
        list[i] = temp
        shouldContinue = True
    if not shouldContinue:
      break
    endIndex -= 1

# Insertion Sort
def insertionSort(list):
  for i in range(len(list) - 1):
    sortedEndIndex = i
    indexToInsert = i + 1
    elementToInsert = list[sortedEndIndex + 1]
    for j in range(sortedEndIndex, -1, -1):
      if not elementToInsert.value < list[j].value:
        break
      list[j + 1] = list[j]
      indexToInsert -= 1
    list[indexToInsert] = elementToInsert

# Selection Sort
def selectionSort(list):
  for i in range(len(list) - 1):
    lowestNumberIndex = i
    for j in range(i + 1, len(list)):
      if list[j].value < list[lowestNumberIndex].value:
        lowestNumberIndex = j
    if lowestNumberIndex != i:
      temp = list[i]
      list[i] = list[lowestNumberIndex]
      list[lowestNumberIndex] = temp

# Quick Sort
def quickSort(list, startIndex = 0, endIndex = None):
  if endIndex == None:
    endIndex = len(list) - 1
  if startIndex < endIndex:
    pivot = partition(list, startIndex, endIndex)
    quickSort(list, startIndex, pivot - 1)
    quickSort(list, pivot + 1, endIndex)

def partition(list, startIndex, endIndex):
  pivot = list[endIndex].value
  lowerDivider = startIndex
  for higherDivider in range(startIndex, endIndex):
    if list[higherDivider].value <= pivot:
      list[lowerDivider], list[higherDivider] = list[higherDivider], list[lowerDivider]
      lowerDivider += 1
  list[lowerDivider], list[endIndex] = list[endIndex], list[lowerDivider]
  return lowerDivider

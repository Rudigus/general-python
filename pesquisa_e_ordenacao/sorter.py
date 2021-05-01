# Bubble Sort
def bubbleSort(list):
  endIndex = len(list) - 1
  while True:
    shouldContinue = False
    for i in range(endIndex):
      if list[i] > list[i + 1]:
        temp = list[i + 1]
        list[i + 1] = list[i]
        list[i] = temp
        shouldContinue = True
    if not shouldContinue:
      break
    endIndex -= 1
  print("Finished bubble sorting list of {} elements.".format(len(list)))

# Selection Sort
def selectionSort(list):
  for i in range(len(list) - 1):
    lowestNumberIndex = i
    for j in range(i + 1, len(list)):
      if list[j] < list[lowestNumberIndex]:
        lowestNumberIndex = j
    if lowestNumberIndex != i:
      temp = list[i]
      list[i] = list[lowestNumberIndex]
      list[lowestNumberIndex] = temp
  print("Finished selection sorting list of {} elements.".format(len(list)))

# Insertion Sort
def insertionSort(list):
  for i in range(len(list) - 1):
    sortedEndIndex = i
    indexToInsert = i + 1
    elementToInsert = list[sortedEndIndex + 1]
    for j in range(sortedEndIndex, -1, -1):
      if not elementToInsert < list[j]:
        break
      list[j + 1] = list[j]
      indexToInsert -= 1
    list[indexToInsert] = elementToInsert
  print("Finished insertion sorting list of {} elements.".format(len(list)))

# Quick Sort
def quickSort(list, startIndex = 0, endIndex = None):
  if endIndex == None:
    endIndex = len(list) - 1
  if startIndex < endIndex:
    pivot = partition(list, startIndex, endIndex)
    quickSort(list, startIndex, pivot - 1)
    quickSort(list, pivot + 1, endIndex)
  if startIndex == 0 and endIndex == len(list) - 1:
    print("Finished quick sorting list of {} elements.".format(len(list)))

def partition(list, startIndex, endIndex):
  pivot = list[endIndex]
  lowerDivider = startIndex
  for higherDivider in range(startIndex, endIndex):
    if list[higherDivider] <= pivot:
      list[lowerDivider], list[higherDivider] = list[higherDivider], list[lowerDivider]
      lowerDivider += 1
  list[lowerDivider], list[endIndex] = list[endIndex], list[lowerDivider]
  return lowerDivider

# Merge Sort
def mergeSort(list, startIndex = 0, endIndex = None):
  if endIndex == None:
    endIndex = len(list) - 1
  if startIndex < endIndex:
    middleIndex = (startIndex + endIndex) // 2
    mergeSort(list, startIndex, middleIndex)
    mergeSort(list, middleIndex + 1, endIndex)
    merge(list, startIndex, middleIndex, endIndex)
  if startIndex == 0 and endIndex == len(list) - 1:
    print("Finished merge sorting list of {} elements.".format(len(list)))

def merge(list, startIndex, middleIndex, endIndex):
  left = list[startIndex:middleIndex + 1]
  right = list[middleIndex + 1:endIndex + 1]
  topLeft, topRight = 0, 0
  for k in range(startIndex, endIndex + 1):
    if topLeft >= len(left):
      list[k] = right[topRight]
      topRight += 1
    elif topRight >= len(right):
      list[k] = left[topLeft]
      topLeft += 1
    elif left[topLeft] < right[topRight]:
      list[k] = left[topLeft]
      topLeft += 1
    else:
      list[k] = right[topRight]
      topRight += 1

# Shell Sort
def shellSort(list):
  gap = 1
  listLength = len(list)
  while gap < listLength / 3:
    gap = gap * 3 + 1
  while gap > 0:
    for i in range(gap, listLength):
      elementToInsert = list[i]
      indexToInsert = i
      for j in range(i, 0, -gap):
        if not elementToInsert < list[j - gap]:
          break
        list[j] = list[j - gap]
        indexToInsert -= gap
      list[indexToInsert] = elementToInsert
    gap = (gap - 1) // 3 
  print(f"Finished shell sorting list of {len(list)} elements.")

# Counting Sort
def countingSort(list):
  elementRange = range(len(list))
  countArray = [0 for _ in elementRange]
  for element in list:
    countArray[element] += 1
  for i in range(1, len(list)):
    countArray[i] += countArray[i-1]
  outputArray = [0 for _ in elementRange]
  for i in range(len(list)-1, -1, -1):
    elementPosition = countArray[list[i]] - 1
    outputArray[elementPosition] = list[i]
    countArray[list[i]] -= 1
  list[:] = outputArray[:]
  print(f"Finished counting sorting list of {len(list)} elements.")

# Bucket Sort
def bucketSort(intList, bucketNumber = None, isFirstCall = True):
  buckets = []
  listLength = len(intList)
  if bucketNumber == None or not isFirstCall:
    bucketNumber = listLength
  bucketSize = (max(intList) - min(intList)) / bucketNumber
  if bucketSize == 0:
    return
  [buckets.append([]) for _ in range(bucketNumber)]
  minValue = min(intList)
  for i in range(listLength):
   targetIndex = int((intList[i] - minValue) / bucketSize)
   if targetIndex == bucketNumber:
     buckets[targetIndex - 1].append(intList[i])
   else:
     buckets[targetIndex].append(intList[i])
  # print(f"Buckets: {buckets}. Bucket Number = {bucketNumber}, Bucket Size = {bucketSize:.2f}")
  for bucket in buckets:
    if len(bucket) > 1:
      bucketSort(bucket, isFirstCall = False)
  intList.clear()
  for bucket in buckets:
    intList += bucket
  if isFirstCall:
    print(f"Finished bucket sorting list of {listLength} elements. Bucket Number: {bucketNumber}, Bucket Size: {bucketSize:.2f}")

# Radix Sort
def radixSort(list):
  maxItem = max(list)
  exp = 1
  while maxItem // exp > 0:
    radixCountingSort(list, exp)
    exp *= 10
  print(f"Finished radix sorting list of {len(list)} elements.")

def radixCountingSort(list, exp):
  symbolNumber = 10
  elementRange = range(len(list))
  countArray = [0 for _ in range(symbolNumber)]
  for element in list:
    countArray[(element // exp) % 10] += 1
  for i in range(1, symbolNumber):
    countArray[i] += countArray[i-1]
  outputArray = [0 for _ in elementRange]
  for i in range(len(list)-1, -1, -1):
    elementPosition = countArray[(list[i] // exp) % 10] - 1
    outputArray[elementPosition] = list[i]
    countArray[(list[i] // exp) % 10] -= 1
  list[:] = outputArray[:]

from utils.plotter import plot
from utils.generator import getRandomList, getRandomRepeatingList, getRandomRepeatingListWithRange
from timeit import timeit
from utils.line import Line
from utils.sorter import radixSort

# Little test to check if algorithm is working
#intList = getRandomRepeatingListWithRange(15, 100)
#print(f"Initial: {intList}")
#radixSort(intList)
#print(f"Final: {intList}")

# Change this value to switch from and to test mode
testMode = False
testDivisor = 100

counts = [10000,20000,40000,70000,100000,500000]

if testMode:
  counts = [int(n / testDivisor) for n in counts]

numberOfTests = 1

randomLists = [getRandomList(count) for count in counts]

elapsedTimes = [timeit(lambda: radixSort(list), number = numberOfTests) for list in randomLists]

lines = [Line((counts, elapsedTimes), "Caso aleatório", 'b')]
plot(lines, figname = "products/radix_sort_graph.png")

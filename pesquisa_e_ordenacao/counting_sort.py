from utils.plotter import plot
from utils.generator import getRandomList
from timeit import timeit
from utils.line import Line
from utils.sorter import countingSort

# Little test to check if algorithm is working
#list = getRandomList(25)
#print(list)
#countingSort(list)
#print(list)

# Change this value to switch from and to test mode
testMode = False
testDivisor = 100

counts = [10000,20000,40000,70000,100000,500000]

if testMode:
  counts = [int(n / testDivisor) for n in counts]

randomLists = [getRandomList(count) for count in counts]

elapsedTimes = [timeit(lambda: countingSort(list), number = 1) for list in randomLists]

lines = [Line((counts, elapsedTimes), "Caso aleatório", 'b')]
plot(lines, figname = "products/counting_sort_graph.png")

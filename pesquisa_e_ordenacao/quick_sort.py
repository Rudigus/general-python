from utils.plotter import plot
from utils.generator import getRandomList
from timeit import timeit
from utils.line import Line
from utils.sorter import quickSort

# Change this value to switch from and to test mode
testMode = False
testDivisor = 100

counts = [100000, 200000, 400000, 700000, 1000000, 5000000]

if testMode:
  counts = [int(n / testDivisor) for n in counts]

randomLists = [getRandomList(count) for count in counts]

elapsedTimes = [timeit(lambda: quickSort(list), number = 1) for list in randomLists]

lines = [Line((counts, elapsedTimes), "Caso aleatório", 'b')]
plot(lines, figname = "products/quick_sort_graph.png")

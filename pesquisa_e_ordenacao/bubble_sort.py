from utils.plotter import plot
from utils.generator import getRandomList, getDecrescentList
from timeit import timeit
from utils.line import Line
from utils.sorter import bubbleSort

counts = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]

randomLists = [getRandomList(count) for count in counts]
worstLists = [getDecrescentList(count) for count in counts]

elapsedTimes = [timeit(lambda: bubbleSort(list), number = 1) for list in randomLists]
worstElapsedTimes = [timeit(lambda: bubbleSort(list), number = 1) for list in worstLists]

lines = [Line((counts, elapsedTimes), "Caso aleatório", 'b'), Line((counts, worstElapsedTimes), "Pior caso", 'k')]
plot(lines, figname = "products/bubble_sort_graph.png")

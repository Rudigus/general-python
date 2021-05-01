from utils.plotter import plot
from utils.generator import getRandomList, getRandomRepeatingList, getRandomRepeatingListWithRange
from timeit import timeit
from utils.line import Line
from utils.sorter import bucketSort

# Little test to check if algorithm is working
#intList = getRandomRepeatingListWithRange(15, 100)
#print(f"Initial: {intList}")
#bucketSort(intList)
#print(f"Final: {intList}")

# Change this value to switch from and to test mode
testMode = False
testDivisor = 100

counts = [10000,20000,40000,70000,100000,500000]

if testMode:
  counts = [int(n / testDivisor) for n in counts]

numberOfTests = 1

randomLists = [getRandomList(count) for count in counts]

elapsedTimes = [timeit(lambda: bucketSort(list), number = numberOfTests) for list in randomLists]

lines = [Line((counts, elapsedTimes), "Caso aleatório", 'b')]
plot(lines, "products/bucket_sort_graph.png")

bucketNumbers = [1, 10, 100, 1000, 10000, 100000]
bucketNumberTimes = [timeit(lambda: bucketSort(getRandomList(100000), bucketNumber), number = numberOfTests) for bucketNumber in bucketNumbers]

lines = [Line((bucketNumbers, bucketNumberTimes), "Lista com 100000 elementos", 'b')]
plot(lines, 'products/bucket_number_graph.png', 'Número de buckets')
print("De acordo com as informações obtidas ao analisar o gráfico, sugiro uma quantidade de buckets igual ao tamanho da entrada, ou uma quantidade de buckets igual a 1% do tamanho da entrada.")

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')

def plot(lines, figname = 'graph.png', xLabel = 'Tamanho das listas'):
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)
  for line in lines:
    xList = [point for point in line.points[0]]
    yList = [point for point in line.points[1]]
    plt.plot(xList, yList, '{}o-'.format(line.color), label=line.label)
  plt.ylabel('Tempo de execução')
  plt.xlabel(xLabel)
  plt.legend()
  fig.savefig(figname)

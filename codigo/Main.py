import pandas as pd
import time
import re
from Grafo import Graph
from Metodos import *


inicio = time.time()

# Se utilizo el codigo del algoritmo de Dijkstras, la clase grafo
# y la funcion print_result de la siguiente ref:
# https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
# El codigo para graficar el mapa junto con los datos del Json pertenecen a Viktor Daniel


Archivo = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
Archivo2= pd.read_csv('data_csv.csv', sep=';', on_bad_lines='skip')

df = pd.DataFrame(Archivo)
df2 = pd.DataFrame(Archivo2)

df1 = pd.DataFrame()
df3 = pd.DataFrame()

listaO = []
listaD = []
listaL = []
listaA = []
listaP = []

df1['origen'] = df['origin']
df1['destino'] = df['destination']
df1['distancia'] = df['length']
df1['acoso'] = df['harassmentRisk']

df3['nodo'] = df2['node']

nodes = df3['nodo'].to_numpy().tolist()

for i in range(len(nodes)):
    nodes[i] = re.sub("\'","",nodes[i])
    nodes[i] = nodes[i].replace('[', '(')
    nodes[i] = nodes[i].replace(']', ')')

init_graph = {}
for node in nodes:
    init_graph[node] = {}


for (content) in df1['origen'].items():
    listaO.append(content[1])

for (content) in df1['destino'].items():
    listaD.append(content[1])

for (content) in df1['distancia'].items():
    listaL.append(content[1])

for (content) in df1['acoso'].items():
    listaA.append(content[1])

for i in range(len(listaL)):
    promedio = (listaL[i] * listaA[i]) / 6000
    listaP.append(promedio)


elementosFaltantes(init_graph)

asignacion(listaO, listaD, listaP, init_graph)

graph = Graph(nodes, init_graph)

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="(-75.5832559, 6.2601878)")
print_result(previous_nodes, shortest_path, start_node="(-75.5832559, 6.2601878)", target_node="(-75.5778046, 6.2029412)")


fin = time.time()

print(fin-inicio)
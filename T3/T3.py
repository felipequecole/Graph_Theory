# -*- coding: utf-8 -*-

import networkx as nx
from heapq import heappop, heappush
import numpy as np
import matplotlib.pyplot as plt


def prim (G, root = '1'): 
    push = heappush
    pop = heappop
    
    aux = G.copy()
    nodes = aux.nodes()
    
    for n in nodes:
        # iniciar todos os vertices com lambda = infinito e sem predecessor
        aux.node[n]['lambda'] = np.Infinity
        aux.node[n]['pi'] = None
    
    aux.node[root]['lambda'] = 0
    # colocar o lambda do vertice inicial como 0
    
    Q = [] # fila de prioridades
    visited = []
    
    for n in nodes: 
        push(Q, (aux.node[n]['lambda'], n))
    
    while Q: 
        u = pop(Q)
        u = u[1]
        visited.append(u)
        for v in aux.neighbors(u):
            if v not in visited and aux.node[u]['lambda'] > aux[u][v]['weight']: 
                # tiro atual da fila 
                Q.remove((aux.node[v]['lambda'], v))
                aux.node[v]['lambda'] = aux[u][v]['weight'] # atualiza peso
                aux.node[v]['pi'] = u   # atualiza predecessor
                push(Q, (aux.node[v]['lambda'], v)) # atualiza valores na fila
    mst = nx.Graph()
    for v in aux.nodes():
        mst.add_node(v)
        if aux.node[v]['pi'] is not None: 
            u = aux.node[v]['pi']
            mst.add_edge(v, u)
            mst[v][u]['weight'] = aux[v][u]['weight']
    return mst 
    
def calcular_peso(T): 
    peso = 0
    for v in T.edges():
        peso += v['weight']
    return peso
        
        

def main ():
    G = nx.read_weighted_edgelist('facebook.edgelist')
    prim_G = prim(G)
    peso = calcular_peso(prim_G)
    print("Peso:",peso)
    nx.draw(prim_G)
   
  
    
if __name__ == '__main__': 
    main()
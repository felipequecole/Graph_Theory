import numpy as np # importa a biblioteca NumPy

markov_tabuleiro = np.genfromtxt('sal.csv', delimiter=',') #importa o diagrama de estados de um arquivo csv

'''
Função: power_method
Parâmetros: uma matriz da biblioteca NumPy (que representa a cadeia de Markov), 
            número de iterações do Power Method
'''

def power_method (markov_tabuleiro,n_iteracoes) :
    p_atual = np.genfromtxt('p_atual.csv', delimiter=',') # carrega o vetor de probabilidades inicial de um arquivo csv
    
    for i in range (0, n_iteracoes): # aplica o power method pelo número de vezes passado como parâmetro
        p_atual = np.matmul(p_atual,markov_tabuleiro) # realiza o produto da matriz de probabilidade atual com a da Cadeia de Markov e guarda o resultado em p_atual
        
    return p_atual # retorna a distribuição estacionária da Cadeia de Markov

dist_estacionaria = power_method(markov_tabuleiro,1000) # aplica o Power Method 100 vezes
dist_estacionaria.tofile("dist_estacionaria.csv",sep=",",format = '%.20f') # escreve o resultado em um arquivo csv


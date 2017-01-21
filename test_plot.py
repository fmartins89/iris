#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import pylab
import dateutil

# Diretorio atual
path = os.path.dirname(os.path.realpath(__file__))
# Arquivo com dados
arquivo = path + '/data/iris.data'
# Arquivo de imagem com grafico
figname = path + '/data/iris.png'

# Ler arquivo e gravar dados em variavel
labels = pylab.loadtxt(arquivo, delimiter=',',dtype='str', usecols=[4])
values = pylab.loadtxt(arquivo, delimiter=',', usecols=[0,1,2,3])
 
# Plotar 3 series de dados em funcao da data (cores definidas automaticamente)
pylab.plot(values[0:49,0],values[0:49,1],'ro',label=labels[0])
pylab.plot(values[50:99,0],values[50:99,1],'gx',label=labels[50])
pylab.plot(values[100:149,0],values[100:149,1],'bs',label=labels[100])
# Definir label, titulo e quadro com legenda
#plt.ylabel("Variavel")
#plt.title(estacao,fontsize=30)
pylab.legend()
# Abre janela com grafico para visualizacao
pylab.show()
# Salva figura em arquivo
pylab.savefig(figname)
 
## Opcao para eixo com strings ##
# Criar vetor com mesmo tamanho do vetor de nomes
#x = range(0,total)
# Vetor de nomes
#my_xticks = dados.estacao
#ax=plt.gca()
# Ligar grid horizontal e vertical
#ax.yaxis.grid(True)
#ax.xaxis.grid(True)
# Plotar duas series de dados em funcao de sequencia numerica (cores definidas no codigo)
#plt.xticks(x, dados.estacao, rotation=30, fontsize=8)
#plt.plot(x, dados.obs, 'bo-', label="observao")
#plt.plot(x, dados.prev, 'go-', label="previsto")
#plt.plot(x, dados.cor, 'ro-', label="corrigido")

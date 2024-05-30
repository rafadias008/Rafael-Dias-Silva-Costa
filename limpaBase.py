import pandas as pd
import csv

df = pd.read_csv('Ecommerce_DBS.csv')

df.dropna()

with open('Ecommerce_DBS.csv') as arquivo:
    leitor_cvs = csv.reader(arquivo)
    
    linhas = list(leitor_cvs)
    
    colunasParaUso = [0,1,2,3,4,6,7,8,9,10]
    
    novas_linhas = [[linha[i] for i in colunasParaUso] for linha in linhas]
    
    with open ('NovaBase.csv', 'w', newline='') as novo_arquivo:
        escritor_csv = csv.writer(novo_arquivo)
        escritor_csv.writerows(novas_linhas)
        



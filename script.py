import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_financeiro_treino.csv')

df_impostos = df[df['categoria'] == 'Impostos'] #adicionando o filtro#

metodo = df_impostos.groupby('cliente')['valor'].sum().sort_values() 
print(metodo)

# Criar o gráfico
metodo.plot(kind='bar', title='impostos por clientes');
plt.xlabel('cliente')
plt.ylabel('total impostos')
plt.show()


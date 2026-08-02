import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_financeiro_treino.csv')

#adicionando filtro#
divida = df[df['status'] == 'Atrasado']

total_atrasado = divida.groupby('cliente') ['valor'].sum().sort_values()

total_atrasado.plot(kind='bar', title='total atrasado por cliente');
plt.xlabel('cliente')
plt.ylabel('valor em atraso')
plt.show()

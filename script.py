import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_financeiro_treino.csv')

# Filtrar só as linhas de imposto
df_impostos = df[df['categoria'] == 'Impostos']

# Somar o valor gasto em impostos, por cliente
gastos_impostos = df_impostos.groupby('cliente')['valor'].sum().sort_values()
print(gastos_impostos)

gastos_impostos.plot(kind= 'bar', title= "total impostos por cliente")
plt.xlabel('clientes')
plt.ylabel('valor')
plt.show()

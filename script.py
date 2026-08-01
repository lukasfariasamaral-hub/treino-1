import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_financeiro_treino.csv')

maiores_clientes = df.groupby('cliente')['valor'].sum().sort_values(ascending=False)
print(maiores_clientes)

# Criar o gráfico
maiores_clientes.plot(kind='bar', color='steelblue')
plt.title('Total de Valor por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Valor Total (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
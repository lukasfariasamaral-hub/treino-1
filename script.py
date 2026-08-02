import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset_financeiro_treino.csv')

print(df['status'].unique())
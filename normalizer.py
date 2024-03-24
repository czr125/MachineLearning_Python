import pandas as pd
import matplotlib.pyplot as plt

arquivo = 'imdb_movies.csv'

df = pd.read_csv(arquivo)

top_10_notas = df.nlargest(10, 'score')

plt.plot(df['names'], df['score'])  # Substitua 'coluna_x' e 'coluna_y' pelos nomes das colunas que você deseja plotar
plt.xlabel('Nomes')  # Substitua 'Rótulo do Eixo X' pelo rótulo adequado para o eixo x
plt.ylabel('Notas')  # Substitua 'Rótulo do Eixo Y' pelo rótulo adequado para o eixo y
plt.title('Gráfico de filmes com maiores notas')  # Substitua 'Gráfico de Linha' pelo título do gráfico
plt.grid(True)  # Adiciona grade ao gráfico (opcional)
plt.show()  # Mostra o gráfico
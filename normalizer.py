import pandas as pd
import matplotlib.pyplot as plt
# Carrega o arquivo csv cru
arquivo = 'imdb_movies.csv'

# Define a variável do arquivo
conteudo = pd.read_csv(arquivo)

# Refina o dataframe
df = pd.DataFrame(conteudo)
df = df.drop('overview', axis=1)
df = df.drop('revenue', axis=1)
df = df.drop('status', axis=1)
df = df.drop('orig_title', axis=1)
df = df.drop('crew', axis=1)

# Variaveis para análise dos dados
filme_maior_orçamento_ind = df['budget_x'].idxmax()
filme_mais_votado_ind = df['score'].idxmax()
filme_mais_votado= df.loc[filme_mais_votado_ind, 'names']
nome_filme_maior_orcamento = df.loc[filme_maior_orçamento_ind, 'names']
orcamento_filme_maior_orcamento = df.loc[filme_maior_orçamento_ind, 'budget_x']

# Cria outro arquivo csv sendo ele refinado
df.to_csv('movies_refined.csv', index=False)


print(df)
print('O filme mais votado é:', filme_mais_votado)
print("O filme com o maior orçamento é:", nome_filme_maior_orcamento)
print("Valor do orçamento:", orcamento_filme_maior_orcamento)

top_10 = df.sort_values(by='budget_x', ascending=False).head(10)

plt.bar(top_10['names'], top_10['budget_x'])

plt.title('Top 10 Orçamento dos Filmes')
plt.xlabel('Filme')
plt.ylabel('Orçamento')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
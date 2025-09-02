
import pandas as pd
from IPython.display import display

vendas_df = pd.read_excel("Vendas.xlsx")
display(vendas_df)
display(vendas_df.head(10)) # Mostra as 10 primeiras linhas da tabela
print(vendas_df.shape) # Demonstra a quantidade de linhas e colunas
display(vendas_df.describe()) # Exibe informações relevantes dos dados da tabela

produtos = vendas_df[['Produto', 'ID Loja']] # Seleciona a coluna(serie) Produto
display(produtos)

display(vendas_df.loc[1]) # Seleciona a linha
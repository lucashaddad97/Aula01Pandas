import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
df = pd.read_csv(url,)
df = pd.read_csv(url, sep =';')
dados = pd.read_csv(url, sep =';')
 # VALOR MÉDIO DE ALUGUEL DOS IMOVEIS, AULA DE COMO REALIZAR
## Algumas perguntas que podemos fazer nesse momento:
#Quais os valores médios de aluguel por tipo de imóvel?
#Qual o percentual de cada tipo de imóvel na nossa base de dados?

#print(dados.groupby('Tipo').mean(numeric_only=True))
#print(dados.groupby('Tipo')['Valor'].mean())
df_preco_tipo = dados.groupby('Tipo')['Valor'].mean()
df_preco_tipo.plot(kind='barh', figsize = (14,10), color = 'red')
#print(df_preco_tipo)
#plt.show()
imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']


#print(dados.nunique())
#print(dados['Tipo'].unique())

# print(dados.query('@imoveis_comerciais in Tipo'))
#print(dados.query('@imoveis_comerciais not in Tipo'))
df1 = dados.query('@imoveis_comerciais not in Tipo')
#print(df1)
# print(df1['Tipo'].unique())

df_preco_tipo = df1.groupby('Tipo')['Valor'].mean()
df_preco_tipo.plot(kind='barh', figsize = (14,10), color = 'red')
#print(df_preco_tipo)
# plt.show()

#print(imoveis_comerciais)

# print(dados.query('@imoveis_comerciais not in Tipo'))
df2 = dados.query('@imoveis_comerciais not in Tipo')
#print(df2.nunique())

df_preco_tipo = df2.groupby('Tipo')['Valor'].mean()
df_preco_tipo.plot(kind='barh', figsize = (7,5), color = 'red')
#print(df_preco_tipo)
#plt.show()

# QUAL PERCENTUAL DE CADA TIPO DE IMOVEL NA NOSSA BASE DE DADOS

# print(df2.Tipo.unique())
#print(df2.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo'))
#df_percentual_tipo = df2.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')
#df_percentual_tipo.plot(kind='barh', figsize = (7,5), color = 'red',xlabel = 'Tipos', ylabel = 'Percentual')
#print(df_percentual_tipo)
#plt.show()

# Selecionando apenas imoveis do tipo apartaemnto
# print(df2.Tipo.unique())
#print(df2.query('Tipo == "Apartamento"'))
df_apt = df2.query('Tipo == "Apartamento"')
print(df_apt)






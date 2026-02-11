import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
df = pd.read_csv(url, sep =';')
dados1 = pd.read_csv(url, sep =';')

#tratar valores nulos

# print(df.isnull())
# print(df.isnull().sum())
# print(df.fillna(0))
df1 = df.fillna(0)
# print(df1.isnull().sum())
# df1.query('Valor == 0 | Condominio ==0')
# print(df1.query('Valor == 0 | Condominio ==0'))
# MOSTRANDO OS INDEX DE CADA LINHA
# print(df1.query('Valor == 0 | Condominio ==0').index)
registros_remover = df1.query('Valor == 0 | Condominio ==0').index

df1.drop(registros_remover, axis = 0, inplace = True)
# print(df1.Tipo.unique())

# filtro1 APARTEMTNO Q POSSUI 1 QUARTO E ALUGUEL MENOR 1200
# print(df['Quartos'] ==1)
selecao1 = df['Quartos'] ==1
# print(df[selecao1])
selecao2 = df['Valor'] <1200
# print(df[selecao2])
selecaofinal = (selecao1 & selecao2)
# print(df1[selecaofinal])

dffim =df1[selecaofinal]
# print(dffim)

# APARTAEMNTO QUE POSSUEM 2 QUARTOS E ALUGUEL MENOR Q 3000 E AREA MAIOR Q 70
selecao = (df['Quartos'] >2) & (df['Valor'] <3000) & (df ['Area'] > 70)
# print(df[selecao])

#SALVAR EM CSV OS AQR
df =df.to_csv('dados_apartamentos.csv', index = False, )
df2 = pd.read_csv('dados_apartamentos.csv',sep=';')
apto = pd.read_csv('dados_apartamentos.csv')
print(apto)

# CRIANDO COLUNAS NUMERICAS




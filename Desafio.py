import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url, sep =',')
# print(df)
dados['Pontos_extras'] = dados['Notas'] * 0.4
# print(dados)

dados['Notas_finais'] = dados['Notas'] + dados['Pontos_extras']
# print(dados)

dados['Aprovados_apos_ponto_extras'] = dados['Notas_finais'] .apply(lambda x: "Aprovado" if x>=6 else"Reprovado")
print(dados)

dados ['Aprovados_depois'] = (dados['Notas'] < 6) & (dados['Notas_finais'] >6)
print(dados)

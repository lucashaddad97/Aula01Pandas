import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
df = pd.read_csv(url, sep =';')
dados = pd.read_csv(url, sep =';')

dados['Valor_por_mes ']= dados['Valor'] + dados['Condominio']
#print(dados)

dados['Valor_por_ano'] = (dados['Valor'] + dados['Condominio']) * 12 +(dados['IPTU'])
# print(dados)

#CRIANDO COLUNAS
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'


# print(dados)

#criando colunas binarias
dados['Possui_suite']= dados ['Suites'].apply(lambda x :  "Sim" if x > 0 else "Nao")
print(dados)

dados.to_csv('dados_completo_dev.csv', index = False, sep=';')


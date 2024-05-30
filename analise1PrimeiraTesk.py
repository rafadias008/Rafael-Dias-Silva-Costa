import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("NovaBase.csv")

#Remove os missing values
dataFrame = dataFrame.dropna()

#Realiza a soma de todos os itens vendidos por produto , assim podendo gerar uma analise,
#de qual produto teve maior numero de vendas e menor numero de vendas

#Agrupa os dados da caluna product category e soma a quantidade de produtos vendidos por categoria
contador = dataFrame.groupby('Product Category')['Quantity'].sum()

print("########################################################################")
print("\nTotal de venda por categoria de produto: \n")
print(contador)
print("\n")
print("########################################################################")

#Realiza a soma dos itens vendidos por canal e categoria , então me gera a soma para cada tipo de canal e categoria,
#Assim podendo realizar uma analise mais detalhada de qual canal ideal para cada produto

#Agrupa os dados da coluna Source e Product Category e soma as quantidades de itens vendidos por categoria para cada canal
contador2 = dataFrame.groupby(['Source', 'Product Category'])['Quantity'].sum()
    
print("\nTotal de vendas de produtos por categoria e canal: \n")
print(contador2)
print("\n")

#Agrupa por categoria e somas as quantidades
contagem_categoria_produto = dataFrame.groupby('Product Category')['Quantity'].sum()
print("\n")
def soma_vendas_ultimos_3_anos(dataFrame):
    #Converte os dados da coluna para dados de data, assumindo que o dia vem primeiro
    dataFrame['Purchase Date'] = pd.to_datetime(dataFrame['Purchase Date'], dayfirst=True)
    
    #Filtra os dados para os últimos 3 anos
    data_limite = dataFrame['Purchase Date'].max() - pd.DateOffset(years=3)
    ultimos_3_anos = dataFrame[dataFrame['Purchase Date'] >= data_limite]
    
    #Agrupa os dados por Source e Product Category e soma as quantidades
    contador2 = ultimos_3_anos.groupby(['Source', 'Product Category'])['Quantity'].sum()
    
    print("\nTotal de vendas de produtos por categoria e canal nos últimos 3 anos: \n")
    print(contador2)
    print("\n")
    
    return contador2
print("########################################################################")

contador2 = soma_vendas_ultimos_3_anos(dataFrame)
print("########################################################################")


#Realiza a soma de produtos vendidos por categoria num filtro de idades, onde o intervalo das idades
#é determinado com a lista abaixo e os rotulos

#Define os intervalos de idade para gerar as somas
intervalo = [18, 32,45, 58, 71]  # 18-27, 28-55, 56-70 anos

#Define os rótulos para os intervalos
rotulos = ['18-31', '32-44','45-57', '58-70']

#Adiciona uma nova coluna chamada 'Faixa Etaria' a base com base nos intervalos de idade
dataFrame['Faixa Etaria'] = pd.cut(dataFrame['Customer Age'], bins=intervalo, labels=rotulos, right=False)


print("Maior publico de compra por produto: \n")
#Define a função analyze_data atualizada
def analise_data(data):
    
    #Agrupa os dados por product category, faixa etaria e sexo e realiza a soma dos numeros de ocorrencias
    grouped_data = data.groupby(['Product Category', 'Faixa Etaria', 'Gender']).size().reset_index(name='Contagem')

    #Ordena os dados dentro de cada grupo por 'contagem' em ordem decrescente
    grouped_data = grouped_data.sort_values(by=['Product Category', 'Contagem'], ascending=[True, False])

    #Obtem as duas principais ocorrências para cada categoria de produto, considerando ambos os sexos
    maiorAudiencia = grouped_data.groupby('Product Category').head()

    return maiorAudiencia

#Chama a função analise_data com o DataFrame atualizado
maiorAudiencia = analise_data(dataFrame)

print(maiorAudiencia)
print("########################################################################")


#Função para consultar as vendas dos ultimos 3 anos e devolver qual foi a maior venda
def maior_venda_3_ultimos_anos(dataframe):
    
     #Converte os dados da coluna para dados de data, assumindo que o dia vem primeiro
    dataframe['Purchase Date'] = pd.to_datetime(dataframe['Purchase Date'], dayfirst=True)
    
    #Filtra os dados para os últimos 3 anos
    ultimos_3_anos = dataframe[dataframe['Purchase Date'] >= dataframe['Purchase Date'].max() - pd.DateOffset(years=3)]
    
    #Agrupa os produtos por categoria e soma as quantidades vendidas
    vendas_produto = ultimos_3_anos.groupby('Product Category')['Quantity'].sum()
    
    #Ordenas os produtos por quantidade vendida e pegando os mais vendidos
    produtos_mais_vendidos = vendas_produto.sort_values(ascending=False).head()
    
    return produtos_mais_vendidos


print(maior_venda_3_ultimos_anos(dataFrame))
print("\n")
#############################################################################################################################
#Função para encontrar os produtos mais caros e mais barato
def produto_mais_caro_e_mais_barato(dataframe):
    #Encontra o produto mais caro
    produto_mais_caro = dataframe.loc[dataframe['Product Price'].idxmax()]
    
    #Encontra o produto mais barato
    produto_mais_barato = dataframe.loc[dataframe['Product Price'].idxmin()]
    
    return produto_mais_caro, produto_mais_barato
    
produto_mais_caro, produto_mais_barato = produto_mais_caro_e_mais_barato(dataFrame)
print("######################################################################")
print("\nProduto mais caro:")
print(produto_mais_caro)
print("######################################################################")
print("\nProduto mais barato:")
print(produto_mais_barato)
print("\n")

###############################################################################################################################
def categoria_mais_e_menos_cara(dataframe):
    #Calcula o preço médio de todos os produtos em cada categoria
    preco_medio_por_categoria = dataframe.groupby('Product Category')['Product Price'].mean()
    
    print("######################################################################")
    print("\nPreço médio por categoria:\n")
    for categoria, preco_medio in preco_medio_por_categoria.items():
        print(f"{categoria}: {preco_medio:.2f}")
    
    #Encontra a categoria mais cara
    categoria_mais_cara = preco_medio_por_categoria.idxmax()
    
    #Encontra a categoria com menor valor
    categoria_menos_cara = preco_medio_por_categoria.idxmin()
    
    return categoria_mais_cara, categoria_menos_cara
    
    
categoria_mais_cara, categoria_menos_cara = categoria_mais_e_menos_cara(dataFrame)

def categoria_mais_e_menos_cara(dataframe):
    #Converte os dados da coluna para dados de data, assumindo que o dia vem primeiro
    dataframe['Purchase Date'] = pd.to_datetime(dataframe['Purchase Date'], dayfirst=True)
    
    #Filtra os dados para os últimos 3 anos
    ultimos_3_anos = dataframe[dataframe['Purchase Date'] >= dataframe['Purchase Date'].max() - pd.DateOffset(years=3)]
    
    #Calcula o preço médio de todos os produtos em cada categoria nos últimos 3 anos
    preco_medio_por_categoria = ultimos_3_anos.groupby('Product Category')['Product Price'].mean()
    
    print("######################################################################")
    print("\nPreço médio por categoria nos últimos 3 anos:\n")
    for categoria, preco_medio in preco_medio_por_categoria.items():
        print(f"{categoria}: {preco_medio:.2f}")
    
    #Encontra a categoria mais cara
    categoria_mais_cara = preco_medio_por_categoria.idxmax()
    
    #Encontra a categoria menos cara
    categoria_menos_cara = preco_medio_por_categoria.idxmin()
    
    return categoria_mais_cara, categoria_menos_cara


categoria_mais_cara, categoria_menos_cara = categoria_mais_e_menos_cara(dataFrame)
print("######################################################################")
print("\nCategoria mais cara:", categoria_mais_cara)
print("\nCategoria menos cara:", categoria_menos_cara)
print("######################################################################")

######################################################################################################################
def calcular_nps_medio_por_categoria(dataframe):
    #Calcula o NPS médio por categoria
    nps_medio_por_categoria = dataframe.groupby('Product Category')['NPS'].mean()
    
    print("\nNPS médio por categoria:\n")
    for categoria, nps_medio in nps_medio_por_categoria.items():
        print(f"{categoria}: {nps_medio:.2f}")
    
    return nps_medio_por_categoria


nps_medio_por_categoria = calcular_nps_medio_por_categoria(dataFrame)
print("######################################################################")
def calcular_nps_medio_por_categoria(dataframe):
     #Converte os dados da coluna para dados de data, assumindo que o dia vem primeiro
    dataframe['Purchase Date'] = pd.to_datetime(dataframe['Purchase Date'], dayfirst=True)
    
    #Filtra os dados para os últimos 3 anos
    ultimos_3_anos = dataframe[dataframe['Purchase Date'] >= dataframe['Purchase Date'].max() - pd.DateOffset(years=3)]
    
    #Calcula o NPS médio por categoria nos últimos 3 anos
    nps_medio_por_categoria = ultimos_3_anos.groupby('Product Category')['NPS'].mean()
    
    print("\nNPS médio por categoria nos últimos 3 anos:\n")
    for categoria, nps_medio in nps_medio_por_categoria.items():
        print(f"{categoria}: {nps_medio:.2f}")
    
    return nps_medio_por_categoria

#Chama a função e imprimindo a média do NPS por categoria
nps_medio_por_categoria = calcular_nps_medio_por_categoria(dataFrame)

#GRAFICOS
#######################################################################################################################################
#Gera um gráfico de barras para categoria de produtos
plt.figure(figsize=(10, 6))
contagem_categoria_produto.plot(kind='bar', color='skyblue')
plt.title('Quantidade Total Vendida por Categoria de Produto')
plt.xlabel('Categoria de Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Agrupa por idade e conta a quantidade de pessoar por idade
contagem_idade = dataFrame['Customer Age'].value_counts().sort_index()

#Gera um gráfico de barras para quantidade de pessoas por idade
plt.figure(figsize=(10, 6))
contagem_idade.plot(kind='bar', color='orange')
plt.title('Número de Pessoas por Idade')
plt.xlabel('Idade')
plt.ylabel('Número de Pessoas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Agrupa os dados da coluna product category e idade , em seguida soma as quantidades de itens vendidos por idade
contagem_produto_por_idade = dataFrame.groupby(['Product Category', 'Customer Age'])['Quantity'].sum()

#Reseta o indice
contagem_produto_por_idade = contagem_produto_por_idade.reset_index()

#Obtem os tipos unicos de produtos
tipos_de_produto = dataFrame['Product Category'].unique()

###########################################################################################

# Definir o número de linhas e colunas para os subplots
num_linhas = len(tipos_de_produto) // 2 + len(tipos_de_produto) % 2
num_colunas = 2

# Criar subplots
fig, axs = plt.subplots(num_linhas, num_colunas, figsize=(15, 10))

############################################################################################

#Intera sobre os tipos de produto e gera os gráficos de barras 
for i, categoria in enumerate(tipos_de_produto):
    linha = i // num_colunas
    coluna = i % num_colunas

    #Filtra os dados para a categoria de produto atual
    dados_categoria = contagem_produto_por_idade[contagem_produto_por_idade['Product Category'] == categoria]

    #Gera gráfico de barras para a categoria de produto atual
    axs[linha, coluna].bar(dados_categoria['Customer Age'], dados_categoria['Quantity'])
    axs[linha, coluna].set_title(categoria)
    axs[linha, coluna].set_xlabel('Idade')
    axs[linha, coluna].set_ylabel('Quantidade Vendida')
    axs[linha, coluna].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
#########################################################################################################################

plt.figure(figsize=(8, 8))
plt.pie(contador, labels=contador.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Quantidade por Categoria de Produto')
plt.show()
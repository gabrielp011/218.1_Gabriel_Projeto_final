import pandas as pd
import matplotlib.pyplot as plt

# Leitura do dataset
df = pd.read_csv('C:\\Users\\Youth_Space_38\\OneDrive\\Desktop\\projeto final - datascience 218.1\\parte1_tratado.csv', sep=';')

# Padronizando nomes das colunas
df.columns = df.columns.str.lower()


#1 Proporção de pedidos com problema vs normais
# plt.figure()
# df['problema_entrega'].value_counts().plot(kind='bar')
# plt.title('Proporção de pedidos com e sem problema')
# plt.xlabel('Problema (0 = Não, 1 = Sim)')
# plt.ylabel('Quantidade')
# plt.show()

#2 Distribuição do valor dos pedidos
# plt.figure()
# plt.hist(df['price'], bins=30)
# plt.title('Distribuição do valor dos pedidos')
# plt.xlabel('Valor do pedido')
# plt.ylabel('Frequência')
# plt.show()

#3 Distribuição do tempo de entrega (atraso)
# plt.figure()
# plt.hist(df['atraso_entrega'], bins=30)
# plt.title('Distribuição do tempo de entrega')
# plt.xlabel('Atraso (0 = no prazo, 1 = atraso)')
# plt.ylabel('Frequência')
# plt.show()

#4 Categorias de produtos mais vendidas
# plt.figure()
# df['product_category_name'].value_counts().head(10).plot(kind='bar')
# plt.title('Categorias de produtos mais vendidas')
# plt.xlabel('Categoria')
# plt.ylabel('Quantidade')
# plt.show()

#5 Estados com maior número de pedidos
# plt.figure()
# df['customer_state'].value_counts().head(10).plot(kind='bar')
# plt.title('Estados com maior número de pedidos')
# plt.xlabel('Estado')
# plt.ylabel('Quantidade de Pedidos')
# plt.show()

#6 Formas de pagamento mais utilizadas
# plt.figure()
# df['payment_type'].value_counts().plot(kind='bar')
# plt.title('Formas de pagamento mais utilizadas')
# plt.xlabel('Forma de Pagamento')
# plt.ylabel('Quantidade')
# plt.show()

#PARTE2 - ANÁLISES AVANÇADAS
#1 Pedidos com problema por estado
# plt.figure()
# df.groupby(['customer_state', 'problema_entrega']).size().unstack(fill_value=0).plot(kind='bar')
# plt.title('Pedidos com problema por estado')
# plt.xlabel('Estado')
# plt.ylabel('Quantidade de Pedidos')
# plt.legend(['Sem Problema', 'Com Problema'])
# plt.show()

#2 O valor do frete influencia a chance de problema?
plt.figure()
df.boxplot(column='freight_value', by='problema_entrega')
plt.title('Valor do frete por tipo de pedido')
plt.suptitle('')
plt.xlabel('Problema de Entrega (0 = Não, 1 = Sim)')
plt.ylabel('Valor do Frete')
plt.show()


#3 O número de parcelas influencia a chance de atraso?
# plt.figure()
# df.boxplot(column='payment_installments', by='atraso_entrega')
# plt.title('Número de parcelas vs atraso')
# plt.suptitle('')
# plt.xlabel('Atraso (0 = Não, 1 = Sim)')
# plt.ylabel('Número de parcelas')
# plt.show()

#4 Relação entre valor do pedido e avaliação
# plt.figure()
# plt.scatter(df['price'], df['review_score'])
# plt.title('Valor do pedido vs avaliação do cliente')
# plt.xlabel('Valor do pedido')
# plt.ylabel('Avaliação')
# plt.show()

#5 Gasto médio por estado
# plt.figure()
# df.groupby('customer_state')['price'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
# plt.title('Gasto médio por estado')
# plt.xlabel('Estado')
# plt.ylabel('Valor médio do pedido')
# plt.show()

#6 Valor médio por categoria de produto
# plt.figure()
# df.groupby('product_category_name')['price'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
# plt.title('Valor médio do pedido por categoria')
# plt.xlabel('Categoria')
# plt.ylabel('Valor médio')
# plt.show()

#7 Correlação com o valor do pedido
# plt.figure()
# corr_price = df.select_dtypes('number').corr()['price']
# plt.imshow(corr_price.values.reshape(-1, 1))
# plt.yticks(range(len(corr_price.index)), corr_price.index)
# plt.xticks([0], ['price'])
# plt.title('Correlação com valor do pedido')
# plt.colorbar()
# plt.show()

#8 Correlação com "PROBLEMA"
# plt.figure()
# corr_problem = df.select_dtypes('number').corr()['problema_entrega']
# plt.imshow(corr_problem.values.reshape(-1, 1))
# plt.yticks(range(len(corr_problem.index)), corr_problem.index)
# plt.xticks([0], ['problema_entrega'])
# plt.title('Correlação com problema de entrega')
# plt.colorbar()
# plt.show()
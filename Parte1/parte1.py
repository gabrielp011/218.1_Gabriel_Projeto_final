import numpy as np
import pandas as pd

#Importando o dataset
data_vendas = pd.read_csv('C:\\Users\\Youth_Space_38\\OneDrive\\Desktop\\projeto final - datascience 218.1\\olist_df_unificado.csv', sep=';', encoding='latin-1',low_memory=False)

print(data_vendas.columns)

# Criação do dataset contendo, cidade, estado, categoria do produto, valor, frete, datas, tipo de pagamento, numero de parcelas e avaliação do cliente

data_vendas_selecionado = data_vendas[['customer_city', 'customer_state', 'product_category_name', 'payment_type', 'payment_installments', 'order_status', 'order_delivered_customer_date', 'order_estimated_delivery_date', 'price', 'freight_value', 'review_score']]

print(data_vendas_selecionado.head())

# Criar variavel problema baseado no atraso da entrega e a nota menor < 2


#Verificar se a data de entrega ao cliente é maior que a data estimada de entrega
data_vendas_selecionado['atraso_entrega'] = np.where(data_vendas_selecionado['order_delivered_customer_date'] > data_vendas_selecionado['order_estimated_delivery_date'], 1, 0)

print(data_vendas_selecionado[['order_delivered_customer_date', 'order_estimated_delivery_date', 'atraso_entrega']].head())

data_vendas_selecionado['problema_entrega'] = np.where((data_vendas_selecionado['atraso_entrega'] == 1) | (data_vendas_selecionado['review_score'] <= 2), 1, 0)

print(data_vendas_selecionado[['problema_entrega', 'atraso_entrega', 'review_score']].head(15))

#Verificar dados faltantes
print(data_vendas_selecionado.isnull().sum())

#Exportar o dataset tratado para um novo arquivo CSV
data_vendas_selecionado.to_csv('C:\\Users\\Youth_Space_38\\OneDrive\\Desktop\\projeto final - datascience 218.1\\parte1_tratado.csv', sep=';', index=False, encoding='latin-1')
📌 Sobre o Projeto

Este projeto tem como objetivo aplicar um pipeline completo de Ciência de Dados utilizando dados reais do e-commerce brasileiro disponibilizados pela Olist.

O trabalho envolve:

🔹 Engenharia e integração de dados

🔹 Análise Exploratória (EDA)

🔹 Construção de Dashboard no Power BI

🔹 Modelagem de Machine Learning (Classificação e Regressão)

📂 Dataset

Base pública disponível no Kaggle:

🔗 https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

O dataset contém informações sobre:

Clientes

Pedidos

Produtos

Vendedores

Pagamentos

Avaliações

🧹 1️⃣ Pré-processamento e Engenharia de Dados
🔗 Integração das Tabelas

As tabelas foram integradas utilizando:

Chave	Descrição
order_id	Pedidos + Pagamentos + Reviews + Itens
customer_id	Dados dos clientes
product_id	Dados dos produtos
seller_id	Dados dos vendedores
🏗 Tabela Fato Final

A base consolidada contém:

👤 Cidade e estado do cliente

📦 Categoria do produto

💰 Valor do pedido e frete

💳 Tipo de pagamento e parcelas

⭐ Avaliação do cliente

⏳ Tempo de entrega

⚠ Criação da Variável Target – PROBLEMA
PROBLEMA = 1  # Se houve atraso OU review_score <= 2
PROBLEMA = 0  # Pedido entregue no prazo e review_score > 2
🧽 Tratamentos Aplicados

Tratamento de valores ausentes (remoção ou imputação justificada)

Codificação de variáveis categóricas:

LabelEncoder (variáveis ordinais)

OneHotEncoder (variáveis nominais)

Normalização com MinMaxScaler

Criação de duas bases finais:

df_classificacao  # Prever PROBLEMA
df_regressao      # Prever VALOR_DO_PEDIDO (somente pedidos normais)
📊 2️⃣ Análise Exploratória de Dados (EDA)

A EDA foi estruturada em formato de perguntas e respostas.

Cada análise contém:

✔ Gráfico

✔ Interpretação objetiva

📈 Parte 1 – Distribuições Básicas

Proporção de pedidos com problema

Distribuição do valor dos pedidos

Distribuição do tempo de entrega

Categorias mais vendidas

Estados com maior número de pedidos

Formas de pagamento mais utilizadas

📊 Parte 2 – Análises Avançadas

Problemas por estado

Frete × chance de problema

Parcelas × atraso

Valor do pedido × avaliação

Gasto médio por estado

Valor médio por categoria

Heatmap – Correlação com valor do pedido

Heatmap – Correlação com PROBLEMA

📄 Entregável: Relatório em Word com gráficos e interpretações.

📊 3️⃣ Power BI – Modelo Estrela e Dashboard

Dashboard desenvolvido no Microsoft Power BI

⭐ Modelo Estrela
Dimensões

dim_cliente

dim_produto

dim_vendedor

dim_tempo

dim_pagamento

Fato

fact_pedidos

📊 Estrutura do Dashboard
📌 Página 1 – Visão Geral

Faturamento Total

Ticket Médio

% Pedidos com Problema

Pedidos por mês

📌 Página 2 – Perfil de Consumo

Categoria × Faturamento

Forma de pagamento × Valor Médio

Parcelas × Problemas

📌 Página 3 – Mapa Geográfico

Faturamento por Estado

% Problemas por Estado

📁 Arquivo entregue: .pbix

🤖 4️⃣ Modelagem de Machine Learning
🔵 Classificação – Previsão de PROBLEMA
Algoritmos utilizados:

MLP (Rede Neural)

SVM

Random Forest

Métricas avaliadas:

Matriz de Confusão

Acurácia

F1-Score

AUC-ROC

⚠ Inclui discussão sobre desbalanceamento das classes.

🟢 Regressão – Previsão de VALOR_DO_PEDIDO

(Apenas pedidos normais)

Algoritmos utilizados:

MLP Regressor

SVR

Regressão Linear / Random Forest Regressor

Métricas avaliadas:

RMSE

MAE

R²

🛠 Tecnologias Utilizadas
Python
Pandas
NumPy
Scikit-Learn
Matplotlib
Seaborn
Power BI
📁 Estrutura do Projeto
📦 projeto-olist-data-science
 ┣ 📂 data
 ┣ 📂 notebooks
 ┣ 📂 src
 ┣ 📄 eda_relatorio.docx
 ┣ 📄 dashboard.pbix
 ┗ 📄 README.md
📈 Resultados Esperados

✔ Identificação de padrões de compra
✔ Identificação de fatores associados a atraso
✔ Modelo preditivo de problemas
✔ Modelo de previsão de valor de pedido
✔ Dashboard executivo para tomada de decisão

👨‍💻 Autor

Gabriel Mayã
Projeto Acadêmico – Ciência de Dados

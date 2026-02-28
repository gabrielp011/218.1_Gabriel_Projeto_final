# =========================================================
# PROJETO FINAL - MODELAGEM DE MACHINE LEARNING
# Gabriel Mayã
# =========================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix, accuracy_score, f1_score,
    roc_auc_score, mean_squared_error,
    mean_absolute_error, r2_score
)

from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# =========================================================
# 1️⃣ CARREGAR DADOS
# =========================================================

df = pd.read_csv('C:\\Users\\PC\\Desktop\\repositorio\\218.1_Gabriel_Projeto_final\\parte1_tratado.csv', sep=';', encoding='latin-1')

# # =========================================================
# # 2️⃣ TRATAMENTO DOS DADOS
# # =========================================================

# # Converter datas
df['order_delivered_customer_date'] = pd.to_datetime(
    df['order_delivered_customer_date'], dayfirst=True, errors='coerce'
)
df['order_estimated_delivery_date'] = pd.to_datetime(
    df['order_estimated_delivery_date'], dayfirst=True, errors='coerce'
)

# # Criar diferença em dias
df['dias_diferenca'] = (
    df['order_delivered_customer_date'] -
    df['order_estimated_delivery_date']
).dt.days

# # Remover colunas problemáticas
df = df.drop(columns=[
    'order_delivered_customer_date',
    'order_estimated_delivery_date',
    'customer_city'
])

# # Preencher nulos
df = df.fillna(0)

# # =========================================================
# # =========================================================
# # 🔥 PARTE 1 - CLASSIFICAÇÃO
# # =========================================================
# # =========================================================

print("\n================ CLASSIFICAÇÃO ================\n")

X = df.drop(columns=['problema_entrega'])
y = df['problema_entrega']

# # OneHot Encoding apenas em colunas categóricas seguras
X = pd.get_dummies(
    X,
    columns=['customer_state', 'product_category_name',
             'payment_type', 'order_status'],
    drop_first=True
)

# # Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# # Escalonamento
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# # ---------------------------------------------------------
# # 🔹 MODELO 1 - MLP
# # ---------------------------------------------------------

mlp = MLPClassifier(hidden_layer_sizes=(100,50),
                    max_iter=300,
                    random_state=42)

mlp.fit(X_train, y_train)
y_pred_mlp = mlp.predict(X_test)
y_prob_mlp = mlp.predict_proba(X_test)[:,1]

print("MLP Classifier")
print("Acurácia:", accuracy_score(y_test, y_pred_mlp))
print("F1-Score:", f1_score(y_test, y_pred_mlp))
print("AUC:", roc_auc_score(y_test, y_prob_mlp))
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred_mlp))
print("-"*50)

# # ---------------------------------------------------------
# # 🔹 MODELO 2 - SVM
# # ---------------------------------------------------------

svm = SVC(kernel='rbf',
          probability=True,
          class_weight='balanced',
          random_state=42)

svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
y_prob_svm = svm.predict_proba(X_test)[:,1]

print("SVM")
print("Acurácia:", accuracy_score(y_test, y_pred_svm))
print("F1-Score:", f1_score(y_test, y_pred_svm))
print("AUC:", roc_auc_score(y_test, y_prob_svm))
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred_svm))
print("-"*50)

# # ---------------------------------------------------------
# # 🔹 MODELO 3 - Random Forest
# # ---------------------------------------------------------

rf = RandomForestClassifier(n_estimators=150,
                            class_weight='balanced',
                            random_state=42)

rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
y_prob_rf = rf.predict_proba(X_test)[:,1]

print("Random Forest")
print("Acurácia:", accuracy_score(y_test, y_pred_rf))
print("F1-Score:", f1_score(y_test, y_pred_rf))
print("AUC:", roc_auc_score(y_test, y_prob_rf))
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred_rf))
print("-"*50)

# # =========================================================
# # =========================================================
# # 🔥 PARTE 2 - REGRESSÃO
# # =========================================================
# # =========================================================

print("\n================ REGRESSÃO ================\n")

# Apenas pedidos normais
df_reg = df[df['problema_entrega'] == 0]

X_reg = df_reg.drop(columns=['price', 'problema_entrega'])
y_reg = df_reg['price']

X_reg = pd.get_dummies(
    X_reg,
    columns=['customer_state', 'product_category_name',
             'payment_type', 'order_status'],
    drop_first=True
)

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg,
    test_size=0.3,
    random_state=42
)

scaler_r = StandardScaler()
X_train_r = scaler_r.fit_transform(X_train_r)
X_test_r = scaler_r.transform(X_test_r)

# # ---------------------------------------------------------
# # Função de Avaliação
# # ---------------------------------------------------------

def avaliar_regressao(nome, y_test, y_pred):
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(nome)
    print("RMSE:", rmse)
    print("MAE:", mae)
    print("R²:", r2)
    print("-"*50)

# # ---------------------------------------------------------
# # 🔹 MODELO 1 - MLP Regressor
# # ---------------------------------------------------------

mlp_reg = MLPRegressor(hidden_layer_sizes=(100,50),
                       max_iter=300,
                       random_state=42)

mlp_reg.fit(X_train_r, y_train_r)
y_pred_mlp_r = mlp_reg.predict(X_test_r)

avaliar_regressao("MLP Regressor", y_test_r, y_pred_mlp_r)

# # ---------------------------------------------------------
# # 🔹 MODELO 2 - SVR
# # ---------------------------------------------------------

svr = SVR(kernel='rbf')

svr.fit(X_train_r, y_train_r)
y_pred_svr = svr.predict(X_test_r)

avaliar_regressao("SVR", y_test_r, y_pred_svr)

# # ---------------------------------------------------------
# # 🔹 MODELO 3 - Random Forest Regressor
# # ---------------------------------------------------------

rf_reg = RandomForestRegressor(n_estimators=150,
                               random_state=42)

rf_reg.fit(X_train_r, y_train_r)
y_pred_rf_r = rf_reg.predict(X_test_r)

avaliar_regressao("Random Forest Regressor", y_test_r, y_pred_rf_r)

print("\n✅ PROCESSO FINALIZADO COM SUCESSO")




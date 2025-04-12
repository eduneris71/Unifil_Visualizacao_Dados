import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo
import os


try:
    # Tenta buscar os dados do site UCI
    from ucimlrepo import fetch_ucirepo
    student_data = fetch_ucirepo(id=320)
    df = student_data.data.original
    print(" Dados carregados com sucesso do UCI.")
except Exception as e:
    # Se houver erro (ex: falta de conexão), usa o arquivo local
    print(" Falha ao conectar ao UCI. Carregando dados locais...")

    # Caminho local (nome do arquivo deve estar correto e na mesma pasta)
    local_file = "student-por.csv"
    
    if os.path.exists(local_file):
        df = pd.read_csv(local_file, sep=";")
        print("Dados carregados com sucesso do arquivo local.")
    else:
        raise FileNotFoundError(f" Arquivo '{local_file}' não encontrado na pasta atual.")


# ====== LIMPEZA E PREPARAÇÃO DOS DADOS ======

# Converter colunas numéricas
df["G1"] = pd.to_numeric(df["G1"])
df["G2"] = pd.to_numeric(df["G2"])
df["G3"] = pd.to_numeric(df["G3"])

# Substituir valores "yes"/"no" por 1/0
df_bin = df.replace({"yes": 1, "no": 0})

# One-hot encoding para colunas categóricas
df_encoded = pd.get_dummies(df_bin, drop_first=False)

# Converter booleanos em inteiros (caso existam)
df_encoded = df_encoded.astype({col: int for col in df_encoded.select_dtypes("bool").columns})


# Padronização dos dados para cálculo de correlação
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_encoded)
df_scaled = pd.DataFrame(X_scaled, columns=df_encoded.columns)

# Matriz de correlação
corr = df_scaled.corr()

# ====== TÍTULO E INTRODUÇÃO ======
st.title("Dashboard Interativo – Desempenho Escolar de Estudantes Portugueses")
st.markdown(
    """
    Este painel interativo apresenta a análise exploratória dos dados de desempenho de alunos de duas escolas de Portugal.
    É possível explorar diferentes atributos e visualizar as correlações, distribuições e médias das notas com base em variáveis sociais, escolares e familiares.
    """
)

# ====== BARRA LATERAL INTERATIVA ======
st.sidebar.header("Filtros Interativos")
tipo_grafico = st.sidebar.radio("Escolha o tipo de visualização", ["Histograma", "Barras Agrupadas", "Gráfico de Dispersão"])

# ====== GRÁFICO 1: HISTOGRAMA INTERATIVO ======
if tipo_grafico == "Histograma":
    st.header(" Distribuição das Notas por Sexo e Escola")
    sexo = st.sidebar.selectbox("Filtrar por sexo:", df["sex"].unique())
    nota_escolhida = st.sidebar.selectbox("Escolha a nota:", ["G1", "G2", "G3"])
    df_filtrado = df[df["sex"] == sexo]

    fig_hist = px.histogram(df_filtrado, x=nota_escolhida, color="school", nbins=15,
                            title=f"Distribuição da {nota_escolhida} para sexo {sexo}", barmode="overlay",color_discrete_sequence=["#636EFA", "#EF553B"])
    st.plotly_chart(fig_hist, use_container_width=True)

# ====== GRÁFICO 2: BARRAS AGRUPADAS ======
elif tipo_grafico == "Barras Agrupadas":
    st.header("Médias das Notas por Atributo")

    coluna_cat = st.sidebar.selectbox("Escolha o atributo categórico:", df.select_dtypes("object").columns)
    df_grouped = df.groupby(coluna_cat)[["G1", "G2", "G3"]].mean().reset_index()
    df_melted = pd.melt(df_grouped, id_vars=[coluna_cat], value_vars=["G1", "G2", "G3"],
                        var_name="Nota", value_name="Média")

    fig_barras = px.bar(df_melted, x=coluna_cat, y="Média", color="Nota", barmode="group",
                        title=f"Média das Notas por Categoria de {coluna_cat}")
    st.plotly_chart(fig_barras, use_container_width=True)

# ====== GRÁFICO 3: DISPERSÃO INTERATIVA ======
elif tipo_grafico == "Gráfico de Dispersão":
    st.header("Gráfico de Dispersão entre Variáveis")

    colunas_numericas = df.select_dtypes(include="number").columns.tolist()
    eixo_x = st.sidebar.selectbox("Escolha o eixo X:", colunas_numericas, index=colunas_numericas.index("studytime"))
    eixo_y = st.sidebar.selectbox("Escolha o eixo Y:", colunas_numericas, index=colunas_numericas.index("G3"))
    cor = st.sidebar.selectbox("Colorir por:", df.select_dtypes(include="object").columns, index=0)
    tamanho = st.sidebar.selectbox("Tamanho dos pontos por:", ["Nenhum"] + colunas_numericas, index=0)

    fig_disp = px.scatter(
        df,
        x=eixo_x,
        y=eixo_y,
        color=cor,
        size=tamanho if tamanho != "Nenhum" else None,
        title=f"Dispersão entre {eixo_x} e {eixo_y}",
        opacity=0.7,
        hover_data=["sex", "school", "G1", "G2", "G3"],
        color_discrete_sequence=["#636EFA", "#EF553B"] 
    )

    st.plotly_chart(fig_disp, use_container_width=True)

# ====== FOOTER ======
st.markdown("---")
st.caption("Fonte dos dados: UCI Machine Learning Repository - Student Performance Dataset")

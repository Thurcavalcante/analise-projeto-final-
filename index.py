# Importação de Bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(layout="wide", page_title="Insuficiência Cardíaca")

# Leitura e Preprocessamento dos Dados
arquivo = 'heart.csv'
dados = pd.read_csv(arquivo)

# Título
st.title('Insuficiências Cardíacas')
st.write('---')
    
# Descrição sobre o tema
if st.checkbox('Sobre o tema'):
    st.write("As doenças cardiovasculares (DCV) são a causa número 1 de morte em todo o mundo, ceifando cerca de 17,9 milhões de vidas a cada ano, o que representa 31% de todas as mortes em todo o mundo. Quatro em cada cinco mortes por DCV são devidas a ataques cardíacos e acidentes vasculares cerebrais, e um terço destas mortes ocorre prematuramente em pessoas com menos de 70 anos de idade.")
    st.write("Quatro em cada cinco mortes por DCV são devidas a ataques cardíacos e acidentes vasculares cerebrais, e um terço destas mortes ocorre prematuramente em pessoas com menos de 70 anos de idade. A insuficiência cardíaca é um evento comum causado por DCV e este conjunto de dados contém 11 características que podem ser usadas para prever uma possível doença cardíaca.")
    st.write("Pessoas com doenças cardiovasculares ou que apresentam alto risco cardiovascular (devido à presença de um ou mais fatores de risco, como hipertensão, diabetes, hiperlipidemia ou doença já estabelecida) necessitam de detecção e gestão precoces, onde um modelo de aprendizagem automática pode ser de grande ajuda.")

# Mostrar conjunto de dados
if st.checkbox("Mostrar Dados"):
    st.write(dados)

# Sidebar
st.sidebar.image("dataset-cover.png", caption="Insuficiência Cardíaca", use_column_width=True)
# Adiciona controles deslizantes para a faixa etária
age_range = st.sidebar.slider("Faixa Etária", int(dados["Age"].min()), int(dados["Age"].max()), (int(dados["Age"].min()), int(dados["Age"].max())))

# Adiciona condições para idade e sexo
dados_filtered = dados[(dados["Age"].between(age_range[0], age_range[1]))]

# Layout da Interface separado por colunas
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, col9 = st.columns(3)

# Gráfico de contagem para mostrar a distribuição por gênero
fig_sex = px.bar(dados_filtered, x="Sex", y="HeartDisease", color="Sex", title="Distribuição por Gênero")
col1.plotly_chart(fig_sex, use_container_width=True)

# Gráfico de Barras para Distribuição de Idade
fig_age = px.bar(dados_filtered, x="HeartDisease", y="Age", color="Age", title="Distribuição de Idade") 
col2.plotly_chart(fig_age, use_container_width=True)

# Gráfico de pizza para distribuição de tipos de dor
fig_chest_pain = px.pie(dados_filtered, names="ChestPainType", title="Distribuição de Tipo de Dor")
col3.plotly_chart(fig_chest_pain, use_container_width=True)

# Gráfico de Barras para Idade e Frequência Cardíaca Máxima (BPM)
fig_date = px.bar(dados_filtered, x="Age", y="MaxHR", color="HeartDisease", title="Dispensação entre Idade e BPM)")
col4.plotly_chart(fig_date, use_container_width=True)

# Gráfico de Barras para Influência de Idade por Gênero
fig_Idade_Influencia_genero = px.bar(dados_filtered, x="Age", y="HeartDisease", color="Sex", title="Dispensação de Idade de influencia por gêneros")
col5.plotly_chart(fig_Idade_Influencia_genero, use_container_width=True)

# Gráfico de Barras para Contagem por Gênero e Insuficiência Cardíaca
fig_prod = px.bar(dados_filtered, x="Sex", y="HeartDisease", color="HeartDisease", title="Contagem por Gênero e DCV")
col6.plotly_chart(fig_prod, use_container_width=True)

# Gráfico de Barras Empilhadas para Distribuição de Idade por Sexo
fig_age_sex = px.histogram(dados_filtered, x="Age", color="Sex", title="Distribuição de Idade por Sexo")
col7.plotly_chart(fig_age_sex, use_container_width=True)

# Gráfico de Dispersão para Pressão e Colesterol
fig_bp_cholesterol = px.scatter(dados_filtered, x="RestingBP", y="Cholesterol", color="HeartDisease", title="Relação entre Pressão e Colesterol")
col8.plotly_chart(fig_bp_cholesterol, use_container_width=True)

# Boxplot para Distribuição da Frequência Cardíaca Máxima
fig_bpm_boxplot = px.box(dados_filtered, y="MaxHR", title="Distribuição da Frequência Cardíaca Máxima")
col9.plotly_chart(fig_bpm_boxplot, use_container_width=True)
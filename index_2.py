# Importação de Bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(layout="wide", page_title="Insuficiência Cardíaca")

# Leitura e Preprocessamento dos Dados
arquivo = 'heart.csv'
dados = pd.read_csv(arquivo)

# Mostrar conjunto de dados (opcional)
if st.checkbox("Mostrar Dados"):
    st.write(dados)

# Adiciona controles deslizantes para a faixa etária
age_range = st.sidebar.slider("Faixa Etária", int(dados["Age"].min()), int(dados["Age"].max()), (int(dados["Age"].min()), int(dados["Age"].max())))

# Adiciona um seletor de rádio para o sexo
#sex = st.sidebar.radio("Sexo", dados["Sex"].unique())

# Filtragem dos Dados com Base nos Filtros Selecionados
# Adiciona condições para idade e sexo
dados_filtered = dados[(dados["Age"].between(age_range[0], age_range[1]))]

# Criação de Gráficos e Layout da Interface
col1, col2 = st.columns(2) 
col3, col4, col5 = st.columns(3) 

# Gráfico de barras para mostrar a distribuição da idade
fig_age = px.bar(dados_filtered, x="Sex", y="Age", color="Sex", title="Distribuição de Idade") 
col1.plotly_chart(fig_age, use_container_width=True)

# Gráfico de contagem para mostrar a distribuição do sexo
fig_sex = px.bar(dados_filtered, x="Age", y="Sex", color="Age", title="Distribuição de Sexo",  orientation="h")
col2.plotly_chart(fig_sex, use_container_width=True)

# Gráfico de barras para mostrar o faturamento por dia
fig_date = px.bar(dados_filtered, x="Sex", y="Age", color="ChestPainType", title="Faturamento por dia")
col3.plotly_chart(fig_date, use_container_width=True)

# Gráfico de barras para mostrar o faturamento por dia
fig_prod = px.bar(dados_filtered, x="Sex", y="Age", color="ChestPainType", title="Faturamento por dia", orientation="h")
col4.plotly_chart(fig_prod, use_container_width=True)

# Gráfico de barras para mostrar o faturamento por filial
city_total = dados_filtered.groupby("Sex")[["Age"]].sum().reset_index()
fig_city = px.bar(city_total, x="Sex", y="Age", color="Sex", title="Faturamento por filial")
col5.plotly_chart(fig_city, use_container_width=True)




# -----------------------------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import seaborn as sns
# from matplotlib import style
# import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec
# import plotly.express as px

# # Definir paleta de cores
# cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # Carregar dados
# arquivo = 'heart.csv'
# dados = pd.read_csv(arquivo)

# # Dicionário de tradução de nomes de colunas
# traducao_colunas = {
#     'Idade': 'Age',
#     'Sexo': 'Sex',
#     'Tipo de dor': 'ChestPainType',
#     'Pressão': 'RestingBP',
#     'Colesterol': 'Cholesterol',
#     'Glicemia': 'FastingBS',
#     'Eletro': 'RestingECG',
#     'BPM': 'MaxHR',
#     'Dor por exec.': 'ExerciseAngina',
#     'Incl. ST': 'ST_Slope',
#     'DCV': 'HeartDisease'
# }

# # Aplicar a tradução aos nomes das colunas
# dados = dados.rename(columns=traducao_colunas)

# # Função adaptada para Streamlit usando Plotly Express
# def streamlit_grafico_pizza(data_frame, coluna, cores, explode, titulo, fonte):
#     df = data_frame[coluna].value_counts()
#     fig = px.pie(df, names=df.index, values=df.values,
#                  title=titulo, hole=0.3,
#                  color_discrete_sequence=cores)
#     fig.update_layout(
#         font=dict(size=fonte),
#         annotations=[dict(text=titulo, x=0.5, y=0.5, font_size=30, showarrow=False)]
#     )
#     st.plotly_chart(fig, use_container_width=True)

# def streamlit_grafico_distribuicao(data_frame, coluna, titulo):
#     dados = data_frame[coluna]
#     fig = plt.figure(figsize=(17, 7))
#     grade = GridSpec(nrows=2, ncols=1, figure=fig)
#     cor = np.random.choice(cores, 1)[0]
#     st.write(f'Assimetria de {titulo}: {np.round(dados.skew(), 3)}')
#     ax0 = fig.add_subplot(grade[0, :])
#     ax0.set_title(f'Histograma e BoxPlot de {titulo}', y=1.05)
#     sns.histplot(data=dados, ax=ax0, color=cor)
#     ax1 = fig.add_subplot(grade[1, :])
#     plt.axis('off')
#     sns.boxplot(x=dados, ax=ax1, color=cor)
#     st.pyplot(fig)

# def streamlit_grafico_influencia(data_frame, coluna, bins, labels, com_bins=True):
#     influencia = data_frame.loc[:, [coluna, 'HeartDisease']]
#     if com_bins:
#         influencia[coluna] = pd.cut(influencia[coluna],
#                                    bins=bins,
#                                    labels=labels)
#     cor = np.random.choice(cores, 1)[0]
#     plt.figure(figsize=(15, 5))
#     grafico = sns.pointplot(x=coluna, y='HeartDisease', data=influencia, color=cor)
#     grafico.set_title(f'{coluna} influência', fontsize=25)
#     st.pyplot()

# # Adaptação para Streamlit usando o gráfico de barras do Plotly Express
# def streamlit_grafico_barra(data_frame, x, y, color, titulo):
#     fig = px.bar(data_frame, x=x, y=y, color=color, title=titulo)
#     st.plotly_chart(fig, use_container_width=True)

# # Adaptação para Streamlit usando o gráfico de barra horizontal do Plotly Express
# def streamlit_grafico_barra_horizontal(data_frame, x, y, color, titulo):
#     fig = px.bar(data_frame, x=x, y=y, color=color, title=titulo, orientation="h")
#     st.plotly_chart(fig, use_container_width=True)

# # Adaptação para Streamlit usando o gráfico de pizza do Plotly Express
# def streamlit_grafico_pizza_plotly(data_frame, values, names, titulo):
#     fig = px.pie(data_frame, values=values, names=names, title=titulo)
#     st.plotly_chart(fig, use_container_width=True)
    
# # Função para criar heatmap
# def streamlit_grafico_heatmap(data_frame, titulo):
#     plt.figure(figsize=(15, 10))
#     data_frame_numeric = data_frame.select_dtypes(include=[np.number])
#     mascara = np.triu(data_frame_numeric.corr())
#     sns.heatmap(data=data_frame_numeric.corr(), cmap='Blues', mask=mascara, annot=True)
#     st.pyplot()
#     # 

# # Adaptação para Streamlit usando o gráfico de dispersão do seaborn
# def streamlit_grafico_dispersao(data_frame, x, y, hue, titulo):
#     plt.figure(figsize=(12, 8))
#     sns.scatterplot(data=data_frame, x=x, y=y, hue=hue)
#     plt.title(titulo)
#     st.pyplot()

# # Adaptação para Streamlit usando o gráfico de caixa do seaborn
# def streamlit_grafico_caixa(data_frame, x, y, titulo):
#     plt.figure(figsize=(12, 8))
#     sns.boxplot(data=data_frame, x=x, y=y)
#     plt.title(titulo)
#     st.pyplot()

# # Adaptação para Streamlit usando o gráfico de violino do seaborn
# def streamlit_grafico_violino(data_frame, x, y, titulo):
#     plt.figure(figsize=(12, 8))
#     sns.violinplot(data=data_frame, x=x, y=y)
#     plt.title(titulo)
#     st.pyplot()

# # Adaptação para Streamlit usando o gráfico de contagem do seaborn
# def streamlit_grafico_contagem(data_frame, x, hue, titulo):
#     plt.figure(figsize=(12, 8))
#     sns.countplot(data=data_frame, x=x, hue=hue)
#     plt.title(titulo)
#     st.pyplot()
    
# # =============
# # Função para criar gráfico de dispersão
# def streamlit_grafico_dispersao(data_frame, eixo_x, eixo_y, hue, titulo):
#     st.subheader(titulo)
#     scatter_plot = px.scatter(data_frame, x=eixo_x, y=eixo_y, color=hue)
#     st.plotly_chart(scatter_plot)

# # Função para criar gráfico de caixa (boxplot)
# def streamlit_grafico_caixa(data_frame, eixo_x, eixo_y, titulo):
#     st.subheader(titulo)
#     box_plot = px.box(data_frame, x=eixo_x, y=eixo_y)
#     st.plotly_chart(box_plot)

# # Função para criar gráfico de violino
# def streamlit_grafico_violino(data_frame, eixo_x, eixo_y, titulo):
#     st.subheader(titulo)
#     violin_plot = px.violin(data_frame, x=eixo_x, y=eixo_y)
#     st.plotly_chart(violin_plot)

# # Função para criar gráfico de contagem
# def streamlit_grafico_contagem(data_frame, eixo_x, eixo_y, titulo):
#     st.subheader(titulo)
#     count_plot = sns.countplot(x=eixo_x, hue=eixo_y, data=data_frame, palette=cores)
#     st.pyplot()
# # =========

# # Chamar as funções no Streamlit
# st.title("Análise de Doenças Cardiovasculares")

# # Mostrar conjunto de dados (opcional)
# if st.checkbox("Mostrar Dados"):
#     st.write(dados)

# # Exemplos de gráficos
# streamlit_grafico_pizza(dados, 'HeartDisease', ['#140E36', '#091AAB'], (0.05, 0.05), 'Doença Cardiovascular', 25)
# streamlit_grafico_distribuicao(dados, 'Age', 'Idade')
# streamlit_grafico_influencia(dados, 'Age', [0, 30, 40, 50, 60, 70, 100], ['<30', '30-40', '40-50', '50-60', '60-70', '70+'])
# streamlit_grafico_barra(dados, 'Sex', 'HeartDisease', 'Sex', 'Distribuição por Gênero')
# streamlit_grafico_barra_horizontal(dados, 'HeartDisease', 'Sex', 'Sex', 'Distribuição por Gênero (Horizontal)')
# streamlit_grafico_pizza_plotly(dados, 'HeartDisease', 'Sex', 'Distribuição por Gênero (Plotly)')
# streamlit_grafico_heatmap(dados, 'Matriz de Correlação')
# streamlit_grafico_dispersao(dados, 'Age', 'MaxHR', 'HeartDisease', 'Dispersão entre Idade e BPM')
# streamlit_grafico_caixa(dados, 'HeartDisease', 'Age', 'Boxplot de Idade por DCV')
# streamlit_grafico_violino(dados, 'HeartDisease', 'Age', 'Violinplot de Idade por DCV')
# streamlit_grafico_contagem(dados, 'Sex', 'HeartDisease', 'Contagem por Gênero e DCV')

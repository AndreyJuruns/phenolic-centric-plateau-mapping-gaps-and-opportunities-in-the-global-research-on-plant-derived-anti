import pandas as pd
import streamlit as st

# Define layout como wide
st.set_page_config(
    layout="wide", page_title="Frequência de Compostos Bioativos"
)

# Carrega os dados
df_contagem = pd.read_csv('contagem_termos.csv')

# Agrupamento manual de termos semelhantes
agrupamento = {
    # variações de phenolics
    "phenolic": "phenolics",
    "phenolics": "phenolics",
    "phenols": "phenolics",
    # variações de flavonoids
    "flavonoid": "flavonoids",
    "flavonoids": "flavonoids",
    # variações de essential oils
    "essential oil": "essential oils",
    # variações de terpenoids
    "terpenoids": "terpenoids",
    "terpenes": "terpenoids",
    "terpenoid": "terpenoids",
    # variações de alkaloids
    "alkaloids": "alkaloids",
    "alkaloid": "alkaloids",
    # variações de ruidos
    "examine": "noise",
    "examined": "noise",
    "flavor": "noise",
    # adicione outros agrupamentos se necessário
}

# Cria nova coluna com os termos padronizados
df_contagem["Termo Agrupado"] = ''
df_contagem["Termo Agrupado"] = df_contagem["Termo"].replace(agrupamento)

# Agrupa e soma as frequências
df_contagem = (
    df_contagem.groupby("Termo Agrupado", as_index=False)["Frequência"]
    .sum()
    .sort_values(by="Frequência", ascending=False)
)


logo_path = 'Lap.jpeg'
# ----- SIDEBAR -----
st.sidebar.image(logo_path, width=1000)
st.sidebar.title("Análise de Compostos Bioativos")
st.sidebar.markdown("---")  # linha divisória
st.sidebar.title("Configurações")

# Seleção de quantidade de termos a mostrar
top_n = st.sidebar.slider("Quantidade de compostos (Top N):", 5, 100, 20)

# Seleção de tipo de gráfico principal
grafico_principal = st.sidebar.radio(
    "Tipo de gráfico principal:",
    ("Área", "Linha", "Barra")
)

# ----- CONTEÚDO PRINCIPAL -----
with st.container():

    st.title("📊 Frequência de Compostos Bioativos")

    # Exibe a tabela
    st.dataframe(df_contagem)
    # Botão de download
    st.download_button(
        label="⬇️ Baixar planilha CSV",
        data=df_contagem.to_csv(index=False).encode('utf-8'),
        file_name='contagem_termos.csv',
        mime='text/csv',
    )


# Filtra os dados
top_n_data = df_contagem.head(top_n).set_index('Termo Agrupado')

# Container: gráfico principal
with st.container():
    st.subheader(f"Gráfico Principal")

    if grafico_principal == "Área":
        st.area_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Linha":
        st.line_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Barra":
        st.bar_chart(top_n_data, use_container_width=True)

# Container: comparação
with st.container():
    st.subheader("📊 Comparação Lado a Lado")
    col1, col2 = st.columns(2)

    with col1:
        st.write("🔵 Gráfico de Barras")
        st.bar_chart(top_n_data, use_container_width=True)

    with col2:
        st.write("🔴 Gráfico de Linhas")
        st.line_chart(top_n_data, use_container_width=True)

# %%

df_contagem_02 = pd.read_csv('contagem_termos_bacte.csv')
                            

# Seleção de tipo de gráfico principal
grafico_principal = st.sidebar.radio(
    "Tipo de gráfico principal 02:",
    ("Área", "Linha", "Barra")
)

# ----- CONTEÚDO PRINCIPAL -----
with st.container():

    st.title("📊 Frequência de Bactérias")

    # Exibe a tabela
    st.dataframe(df_contagem_02)
    # Botão de download
    st.download_button(
        label="⬇️ Baixar planilha CSV",
        data=df_contagem_02.to_csv(index=False).encode('utf-8'),
        file_name='contagem_termos_02.csv',
        mime='text/csv',
    )


# Filtra os dados
top_n_data = df_contagem_02.head(top_n).set_index('Termo')

# Container: gráfico principal
with st.container():
    st.subheader(f"Gráfico Principal")

    if grafico_principal == "Área":
        st.area_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Linha":
        st.line_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Barra":
        st.bar_chart(top_n_data, use_container_width=True)

# Container: comparação
with st.container():
    st.subheader("📊 Comparação Lado a Lado")
    col1, col2 = st.columns(2)

    with col1:
        st.write("🔵 Gráfico de Barras")
        st.bar_chart(top_n_data, use_container_width=True)

    with col2:
        st.write("🔴 Gráfico de Linhas")
        st.line_chart(top_n_data, use_container_width=True)


# cd "C:\Users\Andrey\Desktop\Artigo_Maio\Códigos"
# streamlit run Streamlit.py

# %%

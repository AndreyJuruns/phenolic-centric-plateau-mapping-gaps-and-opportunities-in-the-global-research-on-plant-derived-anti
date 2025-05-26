import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import streamlit.components.v1 as components
# Define layout como wide


# ✅ Deve ser o primeiro comando Streamlit!
st.set_page_config(
    layout="wide",
    page_title="Frequência de Compostos Bioativos"
)

# Dicionário com usuários e senhas (em produção, use hashing!)
USERS = {
    "Carlos": "Carollo Alexandre",
    "": ""
}

# Verifica se o usuário já está logado
# if 'logged_in' not in st.session_state:
# st.session_state.logged_in = True

# Desativa o login (força como logado)
st.session_state.logged_in = True
st.session_state.username = "DevUser"

# Tela de loginS
if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login bem-sucedido!")
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
else:
    st.success(f"Bem-vindo, {st.session_state.username}!")

    # Aqui entra o conteúdo principal da sua aplicação
    st.write("🎉 Este é o conteúdo da aplicação após login.")

    # Carrega os dados
    df_banco = pd.read_csv('Banco_Dados_Filtrado01.csv')
    df_contagem = pd.read_csv('contagem_termos.csv')
    df_countsN = pd.read_csv('contagemN.csv')
    df_countsP = pd.read_csv('contagemP.csv')

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
        ("Barra", "Área", "Linha")
    )

    with st.container():

        st.title("🌿 Phylogenetic Tree 📈")
        st.header("Árvore Filogenética dos Compostos Bioativos")

        image_file = "arvore_com_per.svg"

        # Opção do usuário
        expand = st.checkbox("🔍 Expand to full width")

        # Exibição da imagem com largura condicional
        if expand:
            st.image(image_file, width=2000,
                     caption="Árvore Filogenética dos Compostos Bioativos")
        else:
            st.image(image_file, width=1000,
                     caption="Árvore Filogenética dos Compostos Bioativos")
        # ___________________________________________________________________________
        st.header("Árvore Filogenética dos Compostos Bioativos 01")

        image_file = "arvore_completa.svg"

        # Opção do usuário
        expand01 = st.checkbox("🔍 Expand to full width a")

        # Exibição da imagem com largura condicional
        if expand01:
            st.image(image_file, width=2000,
                     caption="Árvore Filogenética dos Compostos Bioativos 01")
        else:
            st.image(image_file, width=1000,
                     caption="Árvore Filogenética dos Compostos Bioativos 01")

        # ___________________________________________________________________________
        st.header("Árvore Filogenética dos Compostos Bioativos")
        image_file = "arvore_com_per.svg"

        # Opção do usuário
        expand = st.checkbox("🔍 Expand to full width b")

        # Exibição da imagem com largura condicional
        if expand:
            st.image(image_file, width=2000,
                     caption="Árvore Filogenética dos Compostos Bioativos")
        else:
            st.image(image_file, width=1000,
                     caption="Árvore Filogenética dos Compostos Bioativos")

    # ----- CONTEÚDO PRINCIPAL -----
    with st.container():

        st.title("📊 TABELA GERAL")

        # Exibe a tabela
        st.dataframe(df_banco)
        # Botão de download
        st.download_button(
            label="⬇️ Baixar planilha CSV",
            data=df_banco.to_csv(index=False).encode('utf-8'),
            file_name='bancod_de_dados.csv',
            mime='text/csv',
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
            file_name='contagem_compostos_bioativos.csv',
            mime='text/csv',
        )

    # Filtra os dados
    top_n_data = df_contagem.head(top_n).set_index('Termo')

    # Container: gráfico principal
    with st.container():
        st.subheader(f"Gráfico Principal")

        if grafico_principal == "Área":
            st.area_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Linha":
            st.line_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Barra":
            st.bar_chart(top_n_data, use_container_width=True)

# ____________________________________________________________________________________

    df_contagem_02 = pd.read_csv('contagem_termos_bacte.csv')

    # ----- CONTEÚDO PRINCIPAL BACTERIAS -----
    with st.container():

        st.title("📊 Frequência de Bactérias")

        # Exibe a tabela
        st.dataframe(df_contagem_02)
        # Botão de download
        st.download_button(
            label="⬇️ Baixar planilha CSV",
            data=df_contagem_02.to_csv(index=False).encode('utf-8'),
            file_name='frequência_bactérias_02.csv',
            mime='text/csv',
        )

    # Filtra os dados
    top_n_data = df_contagem_02.head(top_n).set_index('Termo')

    # Container: gráfico principal de Bactérias
    with st.container():
        st.subheader(f"Gráfico Bactérias")

        if grafico_principal == "Área":
            st.area_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Linha":
            st.line_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Barra":
            st.bar_chart(top_n_data, use_container_width=True)
# ____________________________________________________________________________________
# ____________________________________________________________________________________
    import pandas as pd
    df_contagem_03 = pd.read_csv('contagem_termos_fung.csv')

    # ----- CONTEÚDO PRINCIPAL FUNGOS -----
    with st.container():

        st.title("📊 Frequência de Fungos")

        # Exibe a tabela
        st.dataframe(df_contagem_03)
        # Botão de download
        st.download_button(
            label="⬇️ Baixar planilha CSV",
            data=df_contagem_03.to_csv(index=False).encode('utf-8'),
            file_name='frequência_Fungos.csv',
            mime='text/csv',
        )

    # Filtra os dados
    top_n_data = df_contagem_03.head(top_n).set_index('Termo')

    # Container: gráfico principal de Fungos
    with st.container():
        st.subheader(f"Gráfico Fungos")

        if grafico_principal == "Área":
            st.area_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Linha":
            st.line_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Barra":
            st.bar_chart(top_n_data, use_container_width=True)
# ____________________________________________________________________________________
# ____________________________________________________________________________________
    df_countsN = df_countsN.head(top_n).set_index('bioactives_grouped')
    df_countsP = df_countsP.head(top_n).set_index('bioactives_grouped')

    with st.container():
        st.subheader("📊 Comparação Lado a Lado")
        col1, col2 = st.columns(2)
        with col1:
            st.write("🔴 Frequência Gram Negative")

            # Exibe a tabela
            st.dataframe(df_countsN)
            # Botão de download
            st.download_button(
                label="⬇️ Baixar planilha CSV",
                data=df_countsN.to_csv(index=False).encode('utf-8'),
                file_name='frequência_bactérias_neg.csv',
                mime='text/csv',
            )
        with col2:
            st.write("🔵 Frequência Gram Positive")

            # Exibe a tabela
            st.dataframe(df_countsP)
        # Botão de download
            st.download_button(
                label="⬇️ Baixar planilha CSV",
                data=df_countsP.to_csv(index=False).encode('utf-8'),
                file_name='frequência_bactérias_pos.csv',
                mime='text/csv',
            )

    with st.container():
        st.subheader("📊 Comparação Lado a Lado")
        col1, col2 = st.columns(2)
        with col1:
            st.write("🔴Gráfico de Negative")

            if grafico_principal == "Área":
                st.area_chart(df_countsN, use_container_width=True)
            elif grafico_principal == "Linha":
                st.line_chart(df_countsN, use_container_width=True)
            elif grafico_principal == "Barra":
                st.bar_chart(df_countsN, use_container_width=True)
        with col2:
            st.write("🔵 Gráfico de Positive")

            if grafico_principal == "Área":
                st.area_chart(df_countsP, use_container_width=True)
            elif grafico_principal == "Linha":
                st.line_chart(df_countsP, use_container_width=True)
            elif grafico_principal == "Barra":
                st.bar_chart(df_countsP, use_container_width=True)

    # Suponha que df_countsN e df_countsP já estejam definidos

    df_countsN.columns = df_countsN.columns.str.strip()
    df_countsP.columns = df_countsP.columns.str.strip()

    df_countsN = df_countsN.reset_index()
    df_countsP = df_countsP.reset_index()
    # Renomeia colunas para facilitar o merge
    dfN = df_countsN.rename(
        columns={'bioactives_grouped': 'termo', 'count': 'negativo'})
    dfP = df_countsP.rename(
        columns={'bioactives_grouped': 'termo', 'count': 'positivo'})

    # Junta os dois por "termo", preenchendo ausências com 0
    df_merged = pd.merge(dfN, dfP, on='termo', how='outer').fillna(0)

    # Ordena pelo total para melhor visualização (opcional)
    df_merged['total'] = df_merged['negativo'] + df_merged['positivo']
    df_merged = df_merged.sort_values(by='total', ascending=False)

    # Gráfico de barras lado a lado com Plotly
    fig = go.Figure(data=[
        go.Bar(name='Gram Negative',
               x=df_merged['termo'], y=df_merged['negativo']),
        go.Bar(name='Gram Positive',
               x=df_merged['termo'], y=df_merged['positivo'])
    ])

    fig.update_layout(
        title='📊 Frequência por Termo (Gram + / -)',
        xaxis_title='Termo',
        yaxis_title='Frequência',
        barmode='group',
        xaxis_tickangle=-45,
        height=500
    )

    # Exibe no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Ajustes
    import pandas as pd
    df_cont_bacte = pd.read_csv('contagem_fam_bio_bacte_gram.csv')
    df_cont_fam01 = pd.read_csv('contagem_fam_bio_ModelosU.csv')
    df_cont_fung = pd.read_csv('contagem_fam_bio_fung_bios.csv')

    df_cont_fam01 = df_cont_fam01[df_cont_fam01['family'].notna()]

    # Somar somente as colunas numéricas (os compostos)
    df_cont_fam01['total_compostos'] = df_cont_fam01.select_dtypes(
        include='number').sum(axis=1)

    df_cont_bacte['total_compostos'] = df_cont_bacte.select_dtypes(
        include='number').sum(axis=1)
    df_cont_fung['total_compostos'] = df_cont_fung.select_dtypes(
        include='number').sum(axis=1)

    # Remover a coluna 'noise' se existir
    df_cont_fam01 = df_cont_fam01.drop(columns=['noise'])
    df_cont_bacte = df_cont_bacte.drop(columns=['noise'])
    df_cont_fung = df_cont_fung.drop(columns=['noise'])

    df_cont_fam01 = df_cont_fam01.sort_values(
        by='total_compostos', ascending=False)
    df_cont_bacte = df_cont_bacte.sort_values(
        by='total_compostos', ascending=False)
    df_cont_fung = df_cont_fung.sort_values(
        by='total_compostos', ascending=False)
    # _______________________________________________________________________________________
    # Supondo que você já tenha o DataFrame df_cont_fam01
    df_heat = df_cont_fam01.set_index('family')
    df_heat = df_heat.select_dtypes(include='number')  # Apenas dados numéricos

    # Seleção interativa de quantidade de compostos

    # Seleciona as top_n colunas (compostos) com base na soma total
    top_columns = df_heat.sum().sort_values(ascending=False).head(top_n).index
    df_filtered = df_heat[top_columns]

    zmin = df_filtered.values.min()
    zmax = np.percentile(df_filtered.values, 95)

    # Criação do heatmap com Plotly fam_01
    fig = go.Figure(data=go.Heatmap(
        z=df_filtered.values,
        x=df_filtered.columns,
        y=df_filtered.index,
        colorscale=[
            [0.0, 'rgba(255,255,255,0)'],  # zmin: totalmente transparente
            [0.05, 'rgb(237,248,233)'],
            [0.25, 'rgb(186,228,179)'],
            [0.5, 'rgb(116,196,118)'],
            [0.75, 'rgb(49,163,84)'],
            [1.0, 'rgb(0,109,44)']
        ],
        zmin=zmin,
        zmax=zmax
    ))

    fig.update_layout(
        title='Heatmap Interativo dos Compostos Model Unidos',
        xaxis_nticks=top_n,
        yaxis_nticks=top_n,
        height=1000

    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.title("📊 Compostos Bioativos e familias")

        # Exibe a tabela
        st.dataframe(df_cont_fam01)
        # Botão de download
        st.download_button(
            label="⬇️ Baixar planilha CSV",
            data=df_cont_fam01.to_csv(index=False).encode('utf-8'),
            file_name='compostos_bioativos_familiasNER_Model.csv',
            mime='text/csv',
        )

    # _______________________________________________________________________________________
    # Supondo que você já tenha o DataFrame df_cont_fam01
    df_heat = df_cont_bacte.set_index(['bacteria', 'gram'])
    df_heat = df_heat.select_dtypes(include='number')  # Apenas dados numéricos

    # Seleção interativa de quantidade de compostos

    # Seleciona as top_n colunas (compostos) com base na soma total
    top_columns = df_heat.sum().sort_values(ascending=False).head(top_n).index
    df_filtered_bac = df_heat[top_columns]
    # Criação do heatmap com Plotly fam_02
    zmin = df_filtered_bac.values.min()
    zmax = np.percentile(df_filtered_bac.values, 95)

    sort_option = st.selectbox(
        "Ordenar bactérias por:",
        options=["Total de compostos Bacterias",
                 "Gram positivo primeiro", "Gram negativo primeiro"]
    )

    # Lógica para ordenar
    if sort_option == "Total de compostos":
        df_filtered_bac = df_filtered_bac.loc[df_filtered_bac.sum(
            axis=1).sort_values(ascending=False).index]
    elif sort_option == "Gram positivo primeiro":
        df_filtered_bac = df_filtered_bac.sort_index(
            level='gram', ascending=False)
    elif sort_option == "Gram negativo primeiro":
        df_filtered_bac = df_filtered_bac.sort_index(
            level='gram', ascending=True)

    # Criação do heatmap com Plotly fam01
    fig = go.Figure(data=go.Heatmap(
        z=df_filtered_bac.values,
        x=df_filtered_bac.columns,
        y=[f'{idx[0]} ({idx[1]})' for idx in df_filtered_bac.index],
        colorscale=[
            [0.0, 'rgba(255,255,255,0)'],  # zmin: totalmente transparente
            [0.05, 'rgb(237,248,233)'],
            [0.25, 'rgb(186,228,179)'],
            [0.5, 'rgb(116,196,118)'],
            [0.75, 'rgb(49,163,84)'],
            [1.0, 'rgb(0,109,44)']
        ],
        zmin=zmin,
        zmax=zmax
    ))

    fig.update_layout(
        title='Heatmap Interativo dos Compostos',
        xaxis_nticks=top_n,
        yaxis_nticks=top_n,
        height=1000

    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.title("📊 Compostos Bioativos e familias")

        # Exibe a tabela
        st.dataframe(df_cont_bacte)
        # Botão de download
        st.download_button(
            label="⬇️ Baixar planilha CSV",
            data=df_cont_bacte.to_csv(index=False).encode('utf-8'),
            file_name='compostos_bioativos_familias_batecerias.csv',
            mime='text/csv',
        )

 # _______________________________________________________________________________________
    # Supondo que você já tenha o DataFrame df_cont_fam01
    df_heat = df_cont_fung.set_index('FUNG')
    df_heat = df_heat.select_dtypes(include='number')  # Apenas dados numéricos

    # Seleção interativa de quantidade de compostos

    # Seleciona as top_n colunas (compostos) com base na soma total
    top_columns = df_heat.sum().sort_values(ascending=False).head(top_n).index
    df_filtered = df_heat[top_columns]

    zmin = df_filtered.values.min()
    zmax = np.percentile(df_filtered.values, 95)

    # Criação do heatmap com Plotly fam_01
    fig = go.Figure(data=go.Heatmap(
        z=df_filtered.values,
        x=df_filtered.columns,
        y=df_filtered.index,
        colorscale=[
            [0.0, 'rgba(255,255,255,0)'],  # zmin: totalmente transparente
            [0.05, 'rgb(237,248,233)'],
            [0.25, 'rgb(186,228,179)'],
            [0.5, 'rgb(116,196,118)'],
            [0.75, 'rgb(49,163,84)'],
            [1.0, 'rgb(0,109,44)']
        ],
        zmin=zmin,
        zmax=zmax
    ))

    fig.update_layout(
        title='Heatmap Interativo dos Compostos Model Unidos Fungos',
        xaxis_nticks=top_n,
        yaxis_nticks=top_n,
        height=1000

    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.title("📊 Compostos Bioativos e familias Fungos")

        # Exibe a tabela
        st.dataframe(df_cont_fung)
        # Botão de download
        st.download_button(
            label="⬇️ Baixar planilha CSV",
            data=df_cont_fung.to_csv(index=False).encode('utf-8'),
            file_name='compostos_bioativos_familias_fungos.csv',
            mime='text/csv',
        )

    # cd "C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit"
    # streamlit run Streamlit.py

    # %%

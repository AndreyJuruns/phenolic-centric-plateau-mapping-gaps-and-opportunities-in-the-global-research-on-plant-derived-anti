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
    st.success(f"Welcome, {st.session_state.username}!")

    # Carrega os dados
    df_banco = pd.read_csv('Banco_Dados_Filtrado02.csv')
    df_contagem = pd.read_csv('contagem_termos.csv')
    df_contagem = df_contagem[(~df_contagem['Termo'].str.contains("noise", regex=False, na=False, case=False)) & (
        ~df_contagem['Termo'].str.contains("isolated compounds", regex=False, na=False, case=False))]

    df_countsN = pd.read_csv('contagemN.csv')
    df_countsN = df_countsN[(~df_countsN['bioactives_grouped'].str.contains("noise", regex=False, na=False, case=False)) & (
        ~df_countsN['bioactives_grouped'].str.contains("isolated compounds", regex=False, na=False, case=False))]

    df_countsP = pd.read_csv('contagemP.csv')
    df_countsP = df_countsP[(~df_countsP['bioactives_grouped'].str.contains("noise", regex=False, na=False, case=False)) & (
        ~df_countsP['bioactives_grouped'].str.contains("isolated compounds", regex=False, na=False, case=False))]
    

    logo_path = 'Lap.png'

    # ----- SIDEBAR -----
    st.sidebar.image(logo_path, width=1000)
    st.sidebar.markdown(
        "👨‍🔬👩‍🔬 **Researchers:**  \nAndrey Gaspar Sorrilha Rodrigues  \nAline Regina Hellmann Carollo  \nCarlos Alexandre Carollo")
    st.sidebar.title("🔬 Bioactive Compounds Analysis")
    st.sidebar.markdown("---")  # Line divisória
    st.sidebar.title("⚙️ Settings")

    # Seleção de quantidade de termos a mostrar
    top_n = st.sidebar.slider("Number of Compounds (Top N):", 5, 100, 20)

    # Seleção de tipo de gráfico principal
    grafico_principal = st.sidebar.radio(
        "Main Chart Type:",
        ("Bar", "Area", "Line")
    )

    with st.container():

        st.title(
            "🌿 Phylogenetic Tree of Tree Species Identified Through Bibliometric Filtering 📈")
        st.header("🧬 Evolutionary Relationships Among Tree Families")

        image_file = "Tree_all_species.tiff"

        # Opção do usuário
        expand = st.checkbox("🔍 Expand to full width")

        # Exibição da imagem com largura condicional
        if expand:
            st.image(image_file, width=2000,
                     caption="Evolutionary Relationships Among Tree Families")
        else:
            st.image(image_file, width=1000,
                     caption="Evolutionary Relationships Among Tree Families")
        # ___________________________________________________________________________
        st.header("🧬 Botanical Families Associated with Bioactive Compounds")

        image_file = "family_compounds_end.tiff"

        # Opção do usuário
        expand01 = st.checkbox("🔍 Expand to full width a")

        # Exibição da imagem com largura condicional
        if expand01:
            st.image(image_file, width=2000,
                     caption="Distribution of Compounds by Plant Family with Pharmacological Potential")
        else:
            st.image(image_file, width=1000,
                     caption="Distribution of Compounds by Plant Family with Pharmacological Potential")

        # ___________________________________________________________________________
        st.header(
            "🧬 Taxonomic Distribution of Microorganisms and Associated Compounds")
        image_file = "classes.tiff"

        # Opção do usuário
        expand02 = st.checkbox("🔍 Expand to full width c")

        # Exibição da imagem com largura condicional
        if expand02:
            st.image(image_file, width=2000,
                     caption="Classification of Microorganisms and Relative Frequency of Bioactive Compounds")
        else:
            st.image(image_file, width=1000,
                     caption="Classification of Microorganisms and Relative Frequency of Bioactive Compounds")

        # ___________________________________________________________________________

        st.header(
            "🧬 Taxonomic Distribution of Microorganisms and Associated Compounds")
        image_file = "bacteria_compounds.tiff"

        # Opção do usuário
        expand03 = st.checkbox("🔍 Expand to full width d")

        # Exibição da imagem com largura condicional
        if expand03:
            st.image(image_file, width=2000,
                     caption="Profile of Natural Origin Compounds Active Against Selected Bacteria")
        else:
            st.image(image_file, width=1000,
                     caption="Profile of Natural Origin Compounds Active Against Selected Bacteria")

        # ___________________________________________________________________________
        st.header(
            "🧬Taxonomic Distribution of Microorganisms and Associated Compounds")
        image_file = "compounds_fung.tiff"

        # Opção do usuário
        expand04 = st.checkbox("🔍 Expand to full width e")

        # Exibição da imagem com largura condicional
        if expand04:
            st.image(image_file, width=2000,
                     caption="Diversity of Compounds in Pathogenic and Environmental Fungi")
        else:
            st.image(image_file, width=1000,
                     caption="Diversity of Compounds in Pathogenic and Environmental Fungi")

        # ___________________________________________________________________________

    # ----- CONTEÚDO PRINCIPAL -----
    with st.container():

        st.title(
            "📊 Integrated Table of Bioactive Compounds and Associated Organisms from Web of Science Data")

        # Exibe a tabela
        st.dataframe(df_banco)
        # Botão de download
        st.download_button(
            label="⬇️ Download CSV Spreadsheet",
            data=df_banco.to_csv(index=False).encode('utf-8'),
            file_name='bancod_de_dados.csv',
            mime='text/csv',
        )

    # ----- CONTEÚDO PRINCIPAL -----

    with st.container():

        st.title("📊 Frequency Distribution of Bioactive Compounds")
        st.header(
            "Bioactive Compounds identified in the analyzed bibliometric dataset.")
        # Exibe a tabela
        st.dataframe(df_contagem.rename(columns={
            "Termo": "🧪 Term",
            "Frequência": "🔢 Frequency"
        }))
        # Botão de download
        st.download_button(
            label="⬇️ Download CSV Spreadsheet",
            data=df_contagem.to_csv(index=False).encode('utf-8'),
            file_name='contagem_compostos_bioativos.csv',
            mime='text/csv',
        )

    # Filtra os dados
    top_n_data = df_contagem.head(top_n).set_index('Termo')

    # Container: gráfico principal
    with st.container():
        st.subheader(f"🔬 Bioactive Compounds: Frequency Overview")

        if grafico_principal == "Area":
            st.area_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Line":
            st.line_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Bar":
            st.bar_chart(top_n_data, use_container_width=True)

# ____________________________________________________________________________________

    df_contagem_02 = pd.read_csv('contagem_termos_bacte.csv')

    # ----- CONTEÚDO PRINCIPAL BACTERIAS -----
    with st.container():

        st.title("📊 Frequency Distribution of Bacteria")
        st.header(
            "Bacteria species identified in the analyzed bibliometric dataset.")
        # Exibe a tabela
        st.dataframe(df_contagem_02.rename(columns={
            "Termo": "🧪 Term",
            "Frequência": "🔢 Frequency"
        }))
        # Botão de download
        st.download_button(
            label="⬇️ Download CSV Spreadsheet",
            data=df_contagem_02.to_csv(index=False).encode('utf-8'),
            file_name='frequência_bactérias_02.csv',
            mime='text/csv',
        )

    # Filtra os dados
    top_n_data = df_contagem_02.head(top_n).set_index('Termo')

    # Container: gráfico principal de Bactérias
    with st.container():
        st.subheader("🦠 Bacteria: Frequency Overview")

        if grafico_principal == "Area":
            st.area_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Line":
            st.line_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Bar":
            st.bar_chart(top_n_data, use_container_width=True)
# ____________________________________________________________________________________
# ____________________________________________________________________________________
    import pandas as pd
    df_contagem_03 = pd.read_csv('contagem_termos_fung.csv')

    # ----- CONTEÚDO PRINCIPAL FUNGOS -----
    with st.container():

        st.title("📊 Frequency Distribution of Fungi")
        st.header("Fungal species identified in the analyzed bibliometric dataset.")
        # Exibe a tabela
        st.dataframe(df_contagem_03.rename(columns={
            "Termo": "🧪 Term",
            "Frequência": "🔢 Frequency"
        }))
        # Botão de download
        st.download_button(
            label="⬇️ Download CSV Spreadsheet",
            data=df_contagem_03.to_csv(index=False).encode('utf-8'),
            file_name='frequência_Fungos.csv',
            mime='text/csv',
        )

    # Filtra os dados
    top_n_data = df_contagem_03.head(top_n).set_index('Termo')

    # Container: gráfico principal de Fungos
    with st.container():
        st.subheader("🍄 **Fungi: Frequency Overview**")

        if grafico_principal == "Area":
            st.area_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Line":
            st.line_chart(top_n_data, use_container_width=True)
        elif grafico_principal == "Bar":
            st.bar_chart(top_n_data, use_container_width=True)
# ____________________________________________________________________________________
# ____________________________________________________________________________________
    df_countsN = df_countsN.head(top_n).set_index('bioactives_grouped')
    df_countsP = df_countsP.head(top_n).set_index('bioactives_grouped')

    with st.container():
        st.title(
            "📊 Side-by-Side Comparison of Bioactive Compound Frequencies")
        st.header(
            "Based on Gram-negative and Gram-positive bacterial targets identified in the bibliometric dataset.")
        col1, col2 = st.columns(2)
        with col1:
            st.write("🔴 Gram-Negative Frequency")

            # Exibe a tabela
            st.dataframe(df_countsN)
            # Botão de download
            st.download_button(
                label="⬇️ Download CSV Spreadsheet",
                data=df_countsN.to_csv(index=False).encode('utf-8'),
                file_name='frequência_bactérias_neg.csv',
                mime='text/csv',
            )
        with col2:
            st.write("🔵 Gram-Positive Frequency")

            # Exibe a tabela
            st.dataframe(df_countsP)
        # Botão de download
            st.download_button(
                label="⬇️ Download CSV Spreadsheet",
                data=df_countsP.to_csv(index=False).encode('utf-8'),
                file_name='frequência_bactérias_pos.csv',
                mime='text/csv',
            )

    with st.container():
        st.header("📊 Side-by-Side Frequency Overview")
        col1, col2 = st.columns(2)
        with col1:
            st.write("🔴 Gram-Negative Overview")

            if grafico_principal == "Area":
                st.area_chart(df_countsN, use_container_width=True)
            elif grafico_principal == "Line":
                st.line_chart(df_countsN, use_container_width=True)
            elif grafico_principal == "Bar":
                st.bar_chart(df_countsN, use_container_width=True)
        with col2:
            st.write("🔵 Gram-Positive Overview")

            if grafico_principal == "Area":
                st.area_chart(df_countsP, use_container_width=True)
            elif grafico_principal == "Line":
                st.line_chart(df_countsP, use_container_width=True)
            elif grafico_principal == "Bar":
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

    # Gráfico de Bars lado a lado com Plotly
    fig = go.Figure(data=[
        go.Bar(name='Gram-Negative',
               x=df_merged['termo'], y=df_merged['negativo']),
        go.Bar(name='Gram-Positive',
               x=df_merged['termo'], y=df_merged['positivo'])
    ])

    fig.update_layout(

        xaxis_title='Termo',
        yaxis_title='Frequência',
        barmode='group',
        xaxis_tickangle=-45,
        height=500
    )

    # Exibe no Streamlit
    st.title('📊 Frequency by Term (Gram + / -)')
    st.plotly_chart(fig, use_container_width=True)

    # Ajustes
   
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
    df_cont_fam01 = df_cont_fam01.drop(columns=['noise','isolated compounds'])
    df_cont_bacte = df_cont_bacte.drop(columns=['noise','isolated compounds'])
    df_cont_fung = df_cont_fung.drop(columns=['noise','isolated compounds'])

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

        xaxis_nticks=top_n,
        yaxis_nticks=top_n,
        height=1000

    )

    # Exibe o gráfico no Streamlit
    st.title('🟩 **Interactive Heatmap of Compounds by Family**')
    st.subheader(
        'Taxonomic families vs. bioactive compounds based on bibliometric analysis.')
    st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.title("📊 **Bioactive Compounds by Plant Family**")

        # Exibe a tabela
        st.dataframe(df_cont_fam01)
        # Botão de download
        st.download_button(
            label="⬇️ Download CSV Spreadsheet",
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
    st.title('🟩 **Interactive Heatmap of Bioactive Compounds by Bacterial Species**')
    st.subheader(
        'Compounds associated with Gram-positive and Gram-negative bacteria based on bibliometric data.')
    sort_option = st.selectbox(
        "Sort bacteria by:",
        options=[
            "Total number of compounds",
            "Gram-positive first",
            "Gram-negative first"
        ]
    )

    # Lógica para ordenar
    if sort_option == "Total number of compounds":
        df_filtered_bac = df_filtered_bac.loc[df_filtered_bac.sum(
            axis=1).sort_values(ascending=False).index]
    elif sort_option == "Gram-negative first":
        df_filtered_bac = df_filtered_bac.sort_index(
            level='gram', ascending=False)
    elif sort_option == "Gram-positive first":
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

        xaxis_nticks=top_n,
        yaxis_nticks=top_n,
        height=1000

    )

    # Exibe o gráfico no Streamlit

    st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.title("📊 Bioactive Compounds by Bacterial Species")

        # Exibe a tabela
        st.dataframe(df_cont_bacte)
        # Botão de download
        st.download_button(
            label="⬇️ Download CSV Spreadsheet",
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

        xaxis_nticks=top_n,
        yaxis_nticks=top_n,
        height=1000

    )

    # Exibe o gráfico no Streamlit
    st.title('🟩 **Interactive Heatmap of Bioactive Compounds by Fungal Species**')
    st.subheader(
        'Fungal species and their associated bioactive compounds identified through bibliometric analysis.')
    st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.title("📊 Bioactive Compounds by Bacterial Species")

        # Exibe a tabela
        st.dataframe(df_cont_fung)
        # Botão de download
        st.download_button(
            label="⬇️ Download CSV Spreadsheet",
            data=df_cont_fung.to_csv(index=False).encode('utf-8'),
            file_name='compostos_bioativos_familias_fungos.csv',
            mime='text/csv',
        )

    # cd "C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit"
    # streamlit run Streamlit.py

    # %%

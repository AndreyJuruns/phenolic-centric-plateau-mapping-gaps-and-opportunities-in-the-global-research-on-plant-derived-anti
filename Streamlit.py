import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import altair as alt
import streamlit as st

# Define layout como wide

agrupamento = {
    "cartone": 'carotenoids'
}


def substituir_bioativos(texto):
    if pd.isna(texto):
        return texto
    compostos = [x.strip() for x in texto.split(',')]
    compostos_substituidos = [agrupamento.get(x, x) for x in compostos]
    return ', '.join(compostos_substituidos)


# ✅ Deve ser o primeiro comando Streamlit!
st.set_page_config(
    layout="wide",
    page_title="🌿 Phenolic-Centric Plateau? Mapping Gaps and Opportunities in the Global Research on Plant-Derived Antimicrobials 🌿"
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

    import pandas as pd
    # Carrega os dados
    df_banco = pd.read_csv('Banco_Dados_Filtrado04.csv')
    df_contagem = pd.read_csv('contagem_termos.csv')
    df_contagem = df_contagem[(~df_contagem['Termo'].str.contains("noise", regex=False, na=False, case=False)) & (
        ~df_contagem['Termo'].str.contains("isolated compounds", regex=False, na=False, case=False))]

    df_countsN = pd.read_csv('contagemN.csv')
    df_countsN = df_countsN[(~df_countsN['bioactives_grouped'].str.contains("noise", regex=False, na=False, case=False)) & (
        ~df_countsN['bioactives_grouped'].str.contains("isolated compounds", regex=False, na=False, case=False))]

    df_countsP = pd.read_csv('contagemP.csv')
    df_countsP = df_countsP[(~df_countsP['bioactives_grouped'].str.contains("noise", regex=False, na=False, case=False)) & (
        ~df_countsP['bioactives_grouped'].str.contains("isolated compounds", regex=False, na=False, case=False))]

    # Logo do Lab no canto
    logo_path = 'Lap.png'

    # ----- SIDEBAR -----
    st.sidebar.image(logo_path, width=1000)
    st.sidebar.markdown(
        "👨‍🔬 **Researchers:**  \nAndrey Gaspar Sorrilha Rodrigues  \nProfº Dra. Aline Regina Hellmann Carollo  \nProfº Dra. Denise Brentan da Silva  \nProfº Dr. Carlos Alexandre Carollo")
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

    st.title("Phenolic-Centric Plateau? Mapping Gaps and Opportunities in the Global Research on Plant-Derived Antimicrobials")

    tab1, tab2 = st.tabs(
        ["Graphical and Tabular Data Visualization", "Cartographic Representation"])
    with tab1:
        with st.container():

            st.header(
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

# __    __________________________________________________________________________________

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
# __    __________________________________________________________________________________
# __    __________________________________________________________________________________
        import pandas as pd
        df_contagem_03 = pd.read_csv('contagem_termos_fung.csv')

        # ----- CONTEÚDO PRINCIPAL FUNGOS -----
        with st.container():

            st.title("📊 Frequency Distribution of Fungi")
            st.header(
                "Fungal species identified in the analyzed bibliometric dataset.")
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
# __    __________________________________________________________________________________
# __    __________________________________________________________________________________
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

            xaxis_title='Types of Phytochemicals',
            yaxis_title='Frequency of Occurrence',
            barmode='group',
            xaxis_tickangle=-45,
            height=500
        )

        # Exibe no Streamlit
        st.title('📊 Frequency by Term (Gram + / -)')
        st.plotly_chart(fig, use_container_width=True)

        # Ajustes
        import pandas as pd
        df_cont_bacte = pd.read_csv('contagem_fam_bio_bacte_gram.csv')
        df_cont_bacte = df_cont_bacte.drop(
            columns=['noise', 'isolated compounds'])
        df_cont_bacte = df_cont_bacte.drop([50, 48, 91, 92, 93])
        
        df_cont_fam01 = pd.read_csv('contagem_fam_bio_ModelosU.csv')
        df_cont_fam01 = df_cont_fam01.drop(
            columns=['noise', 'isolated compounds'])
        df_cont_fam01 = df_cont_fam01.drop([86, 80, 133, 117, 168, 175])
        
        df_cont_fung = pd.read_csv('contagem_fam_bio_fung_bios.csv')
        df_cont_fung = df_cont_fung.drop(
            columns=['noise', 'isolated compounds'])
        df_cont_fung = df_cont_fung.drop([47, 62, 61])
        
        df_cont_fam01 = df_cont_fam01[df_cont_fam01['family'].notna()]

        # Somar somente as colunas numéricas (os compostos)
        df_cont_fam01['Total compound count'] = df_cont_fam01.select_dtypes(
            include='number').sum(axis=1)
        df_cont_bacte['Total compound count'] = df_cont_bacte.select_dtypes(
            include='number').sum(axis=1)
        df_cont_fung['Total compound count'] = df_cont_fung.select_dtypes(
            include='number').sum(axis=1)

        df_cont_fam01 = df_cont_fam01.sort_values(
            by='Total compound count', ascending=False)
        df_cont_bacte = df_cont_bacte.sort_values(
            by='Total compound count', ascending=False)
        df_cont_fung = df_cont_fung.sort_values(
            by='Total compound count', ascending=False)
        # _______________________________________________________________________________________
        # Supondo que você já tenha o DataFrame df_cont_fam01
        df_heat = df_cont_fam01.set_index('family')
        df_heat = df_heat.select_dtypes(
            include='number')  # Apenas dados numéricos

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
        df_heat = df_heat.select_dtypes(
            include='number')  # Apenas dados numéricos

        # Seleção interativa de quantidade de compostos

        # Seleciona as top_n colunas (compostos) com base na soma total
        top_columns = df_heat.sum().sort_values(ascending=False).head(top_n).index
        df_filtered_bac = df_heat[top_columns]
        # Criação do heatmap com Plotly fam_02
        zmin = df_filtered_bac.values.min()
        zmax = np.percentile(df_filtered_bac.values, 95)
        st.title(
            '🟩 **Interactive Heatmap of Bioactive Compounds by Bacterial Species**')
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

 # _    ______________________________________________________________________________________
        # Supondo que você já tenha o DataFrame df_cont_fam01
        df_heat = df_cont_fung.set_index('fungi')
        df_heat = df_heat.select_dtypes(
            include='number')  # Apenas dados numéricos

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

            st.title("📊 Bioactive Compounds by Fungal Species")

            # Exibe a tabela
            st.dataframe(df_cont_fung)
            # Botão de download
            st.download_button(
                label="⬇️ Download CSV Spreadsheet",
                data=df_cont_fung.to_csv(index=False).encode('utf-8'),
                file_name='compostos_bioativos_familias_fungos.csv',
                mime='text/csv',
            )

    with tab2:
        st.title("Cartography")

        df_pais = pd.read_csv(r'contagemPaís.csv')
        df_pais['Termo'] = df_pais['Termo'].str.capitalize()
        df_pais = df_pais.head(20)

        lista_la = [20.5937, -14.2350, 30.3753, 35.8617,
                    38.9637, 33.8869, 26.8206, 28.0339, 31.7917, 23.6345,
                    32.4279, 51.9194, 44.0165, 41.8719, 39.3999, 15.8700, 45.9432, 4.2105, 23.8859, 9.0820]
        lista_lo = [78.9629, -51.9253, 69.3451, 104.1954,
                    35.2433, 9.5375, 30.8025, 1.6596, -7.0926, -102.5528,
                    53.6880, 19.1451, 21.0059, 12.5674, -8.2245, 100.9925, 24.9668, 101.9758, 45.0792, 8.6753]

        df_pais['Latitude'] = lista_la
        df_pais['Longitude'] = lista_lo
        df_pais['Frequência'] = df_pais['Frequência']*5000

        # Gera RGB aleatório
        rgb = np.random.rand(len(df_pais), 3)
        # Cria alpha fixo 1
        alpha = np.full((len(df_pais), 1), 0.7)
        # Concatena RGB + alpha
        rgba = np.hstack([rgb, alpha])
        # Atribui ao DataFrame como lista
        df_pais['color'] = rgba.tolist()

        st.map(df_pais, latitude='Latitude',
               longitude='Longitude', size="Frequência", color="color")

        # ______________________________________________________________

        # Bottom panel is a bar chart of weather type

        st.title("Geospatial Data Interactive Dashboard")
        df_pais = pd.read_csv(r'contagemPaís.csv')
        df_pais['Termo'] = df_pais['Termo'].str.capitalize()
        df_pais = df_pais.head(20)
        lista_la = [20.5937, -14.2350, 30.3753, 35.8617,
                    38.9637, 33.8869, 26.8206, 28.0339, 31.7917, 23.6345,
                    32.4279, 51.9194, 44.0165, 41.8719, 39.3999, 15.8700, 45.9432, 4.2105, 23.8859, 9.0820]
        lista_lo = [78.9629, -51.9253, 69.3451, 104.1954,
                    35.2433, 9.5375, 30.8025, 1.6596, -7.0926, -102.5528,
                    53.6880, 19.1451, 21.0059, 12.5674, -8.2245, 100.9925, 24.9668, 101.9758, 45.0792, 8.6753]
        df_pais['Latitude'] = lista_la
        df_pais['Longitude'] = lista_lo
        scale = alt.Scale(
            domain=['India', 'Brazil', 'Pakistan', 'China', 'Turkey', 'Tunisia', 'Egypt', 'Algeria', 'Morocco', 'Mexico',
                    'Iran', 'Poland', 'Serbia', 'Italy', 'Portugal', 'Thailand', 'Romania', 'Malaysia', 'Saudi arabia', 'Nigeria'],
            range=['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                   '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']
        )
        color = alt.Color("Termo:N", scale=scale)
        # brush = alt.selection_interval(encodings=["y"])
        click = alt.selection_multi(encodings=["color"])
        bars = (
            alt.Chart(df_pais)
            .mark_bar()
            .encode(
                x=alt.X("Frequência", axis=alt.Axis(
                    title="Number of Articles")),
                y=alt.Y("Termo:N", sort='-x',
                        axis=alt.Axis(title="Countries")),
                color=alt.condition(click, color, alt.value("lightgray")),
            )
            # .transform_filter(brush)
            .properties(width=550)
            .add_selection(click)
        )

        # URL de GeoJSON do mundo (fronteiras dos países)
        geojson_url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"

        # Mapa base com países

        mapa_base = alt.Chart(alt.Data(url=geojson_url, format=alt.DataFormat(property='features', type='json'))) \
            .mark_geoshape(
            fill='#222222',     # cor de preenchimento escura
            stroke='#444444',   # cor da borda dos países, também escura para contraste
            strokeWidth=0.5
        ) \
            .project(
            'naturalEarth1')\
            .properties(
            width=800, height=700)
        # Pontos sobre o mapa
        pontos = alt.Chart(df_pais).mark_circle().encode(
            longitude='Longitude:Q',
            latitude='Latitude:Q',
            size=alt.Size(
                'Frequência:Q',
                scale=alt.Scale(range=[200, 2000]),
                legend=alt.Legend(orient='top', title='Sample article')
            ),
            color=alt.condition(click, alt.Color(
                'Termo:N', scale=scale, legend=None), alt.value("lightgray")),
            tooltip=['Termo', 'Frequência']
        ).add_selection(
            click
        ).transform_filter(click)
        # Sobrepõe os dois
        mapa_com_pontos = mapa_base + pontos
        final_chart = bars & mapa_com_pontos
        st.altair_chart(final_chart, use_container_width=True)


# cd "C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit"
# streamlit run Streamlit.py

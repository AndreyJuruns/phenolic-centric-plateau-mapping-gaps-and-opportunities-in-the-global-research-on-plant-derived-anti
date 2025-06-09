# %% importando bibliotecas
import ast
import plotly.express as px
import pandas as pd
import os
import re
# %%
df_Biosafety = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\Lista_fungos.csv')
df_fung = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02_FUNG.csv')

# %%
if 'Biosafety' not in df_fung.columns:
    df_fung['Biosafety'] = ''

mask_fung = df_fung[df_fung['FUNG'] != '[]']
mask_Biosafety = df_Biosafety[['Pathogen name', 'Biosafety level']
                              ][df_Biosafety['Biosafety level'].notna()]


for index, row in mask_fung.iterrows():
    print(row)
    lista_fung = []

    entidades = [f.strip().lower() for f in row['FUNG'].replace(
        "'", '').strip()[1:-1].split(',')]

    for entidade in entidades:
        # Filtra as linhas de mask_fung onde 'Pathogen name' contém a entidade
        mask_filtered = mask_Biosafety[mask_Biosafety['Pathogen name'].str.contains(
            re.escape(entidade), case=False, na=False)]

        for _, row_fung in mask_filtered.iterrows():
            clima = row_fung['Biosafety level']

            lista_fung.append(clima)

    # Preenche as colunas no df_Biosafety

    df_fung.loc[index, 'Biosafety'] = ', '.join(lista_fung)

df_fung.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02_FUNG_Biosafety.csv', index=False, sep=",", encoding="utf-8")

# %%


df_bacte = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02_FUNG_Biosafety.csv')

# %%
df_bacte['FUNG'] = df_bacte['FUNG'].apply(ast.literal_eval)
df_bacte['FUNG'] = df_bacte['FUNG'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)

df_bacte.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02_FUNG_Biosafety01.csv', index=False
)
# %%

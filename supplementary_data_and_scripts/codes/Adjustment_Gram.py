# %% importando bibliotecas
import ast
import plotly.express as px
import pandas as pd
import os
import re

# %% Leitura dos arquivos
df_gram = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\Lista_bacteria.csv')
df_bacte = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_Bio_bac.csv')

# %%


pasta_diretorio = r'C:\Users\Andrey\Desktop\Artigo_Maio\Bacteria\\'


arquivos = os.listdir(pasta_diretorio)

dfs = []

for arquivo in arquivos:
    if arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(pasta_diretorio, arquivo)
        dfs.append(pd.read_excel(caminho_arquivo))

dfs

concat = pd.concat(dfs, ignore_index=True)
# %% Dicionário de agrupamento
agrupamento = {'-': 'negative', '+': 'positive'}
concat['gram_stain'] = concat['gram_stain'].replace(agrupamento)
concat.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\Lista_bacteria.csv', index=False)


# %%
if 'gram' not in df_bacte.columns:
    df_bacte['gram'] = ''

mask_bacte = df_bacte[df_bacte['Bacteria'] != '[]']
mask_gram = df_gram[['Pathogen name', 'gram_stain']
                    ][df_gram['gram_stain'].notna()]


for index, row in mask_bacte.iterrows():
    print(row)
    lista_gram = []

    entidades = [f.strip().lower() for f in row['Bacteria'].replace(
        "'", '').strip()[1:-1].split(',')]

    for entidade in entidades:
        # Filtra as linhas de mask_gram onde 'Pathogen name' contém a entidade
        mask_filtered = mask_gram[mask_gram['Pathogen name'].str.contains(
            re.escape(entidade), case=False, na=False)]

        for _, row_gram in mask_filtered.iterrows():
            clima = row_gram['gram_stain']

            lista_gram.append(clima)

    # Preenche as colunas no df_bacte

    df_bacte.loc[index, 'gram'] = ', '.join(lista_gram)

df_bacte.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram.csv', index=False)


# %%
df_bacte = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram.csv')

df_bacte[['bioactives']]


# %% contagem simples

df_count = df_bacte['gram'].value_counts()

contador_positivo = 0
contador_negativo = 0

for valores in df_bacte['gram']:
    if 'positive' in valores:
        contador_positivo += 1
    if 'negative' in valores:
        contador_negativo += 1


# %%


df_bacte['bioactives'] = df_bacte['bioactives'].apply(ast.literal_eval)
df_bacte['bioactives'] = df_bacte['bioactives'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)

df_bacte['Bacteria'] = df_bacte['Bacteria'].apply(ast.literal_eval)
df_bacte['Bacteria'] = df_bacte['Bacteria'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)
df_bacte.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01.csv', index=False
)

import pandas as pd

df_bacte = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\FIltros_Tree\Banco_Dados_Filtrado01.csv')

df_negative = df_bacte[['bioactives_grouped', 'gram']][df_bacte['gram'].notna(
) & ~df_bacte['gram'].str.contains('positive', na=False)]

df_negative['bioactives_grouped'] = df_negative['bioactives_grouped'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)

df_negative = df_negative[df_negative['bioactives_grouped'] != '']

contagemN = df_negative['bioactives_grouped'].str.split(', ').explode().value_counts()

pd.DataFrame(contagemN, columns=['bioactives_grouped', 'count'])
contagemN.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\contagemN.csv', index=True, header=['count'])
# %%
df_positive = df_bacte[['bioactives_grouped', 'gram']][df_bacte['gram'].notna(
) & ~df_bacte['gram'].str.contains('negative', na=False)]

df_positive['bioactives_grouped'] = df_positive['bioactives_grouped'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)

df_positive = df_positive[df_positive['bioactives_grouped'] != '']

df_positive['bioactives_grouped'].str.split(', ').explode().value_counts()

contagemP = df_positive['bioactives_grouped'].str.split(', ').explode().value_counts()

contagemP.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\contagemP.csv', index=True, header=['count'])
# %%

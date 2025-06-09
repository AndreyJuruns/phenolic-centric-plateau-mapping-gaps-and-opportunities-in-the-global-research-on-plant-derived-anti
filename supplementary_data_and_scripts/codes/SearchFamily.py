# %% import libraries
import pandas as pd
import json
import re
# %%
df_taxon = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Metabolites\Geral\wcvp_taxon.csv', delimiter='|')
df_species = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01.csv')
df_species = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit\contagemSpecies.csv')
# %%

df_taxon['lifeform'] = df_taxon['dynamicproperties'].apply(
    lambda x: json.loads(x).get('lifeform'))
df_taxon['climate'] = df_taxon['dynamicproperties'].apply(
    lambda x: json.loads(x).get('climate'))
df_taxon[['climate', 'lifeform', 'family','taxonomicstatus']] = df_taxon[[
    'climate', 'lifeform', 'family','taxonomicstatus']].fillna('')


# %%
if 'climate' not in df_species.columns:
    df_species['climate'] = ''
if 'lifeform' not in df_species.columns:
    df_species['lifeform'] = ''
if 'family' not in df_species.columns:
    df_species['family'] = ''
if 'taxonomicstatus' not in df_species.columns:
    df_species['taxonomicstatus'] = ''

mask_spe = df_species[
    (df_species['Termo'].notna()) &
    (~df_species['Termo'].str.contains('#', na=False))
]

mask_tax = df_taxon[['scientfiicname', 'climate', 'lifeform', 'family','taxonomicstatus']]

for index, row in mask_spe.iterrows():
    lista_similar_c = []
    lista_similar_l = []
    lista_similar_f = []
    lista_similar_s = []

    entidades = [f.strip().lower() for f in row['Termo'].split(',')]

    for entidade in entidades:
        mask_bool = mask_tax['scientfiicname'].str.lower() == entidade
        mask_filtered = mask_tax[mask_bool]

        seen_c = set()
        seen_l = set()
        seen_f = set()
        seen_s = set()


        if not mask_filtered.empty:
            for _, row_taxon in mask_filtered.iterrows():
                c = str(row_taxon['climate']) if pd.notna(
                    row_taxon['climate']) else ''
                l = str(row_taxon['lifeform']) if pd.notna(
                    row_taxon['lifeform']) else ''
                f = str(row_taxon['family']) if pd.notna(
                    row_taxon['family']) else ''
                s = str(row_taxon['taxonomicstatus']) if pd.notna(
                    row_taxon['taxonomicstatus']) else ''

                if c:
                    seen_c.add(c)
                if l:
                    seen_l.add(l)
                if f:
                    seen_f.add(f)
                if s:
                    seen_s.add(s)

            lista_similar_c.append(', '.join(seen_c) if seen_c else '')
            lista_similar_l.append(', '.join(seen_l) if seen_l else '')
            lista_similar_f.append(', '.join(seen_f) if seen_f else '')
            lista_similar_s.append(', '.join(seen_s) if seen_s else '')
            
        else:
            lista_similar_c.append('')
            lista_similar_l.append('')
            lista_similar_f.append('')
            lista_similar_s.append('')

    # Permite repetições globais, mas sem repetir valores para a mesma entidade
    df_species.loc[index, 'climate'] = ', '.join(lista_similar_c)
    df_species.loc[index, 'lifeform'] = ', '.join(lista_similar_l)
    df_species.loc[index, 'family'] = ', '.join(lista_similar_f)
    df_species.loc[index, 'taxonomicstatus'] = ', '.join(lista_similar_s)

df_species.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\contagemSpecies02.csv',
    index=False
)

df_species[['Entities', 'family', 'lifeform']][df_species['family'] != '']
df_species = df_species[~df_species['family'].str.fullmatch(
    r'[,\s]+', na=False) & (df_species['family'] != '')]


df_species[['Entities', 'family', 'lifeform']
           ][df_species['family'].str.fullmatch(r'[,\s]+', na=False)]

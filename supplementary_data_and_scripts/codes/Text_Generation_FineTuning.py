# %% importing libraries
import json
import re
from transformers import pipeline
import pandas as pd
import ast
# %% read files
df_fam = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam.csv')


# %%
df_fam = df_fam[
    df_fam['family2'].isna() | df_fam['family2'].str.fullmatch(
        r'[,\s]+', na=False)
]

# %%

generator = pipeline("text2text-generation", model="google/flan-t5-large")

# %% function to generate response


def generate_response(text):
    prompt = (
        f"From the text below, extract all binomial species names (genus and species epithet):\n"
        f"Text: {text}\n"
        f"If you find one or more species names, reply with the full scientific names separated by commas.\n"
        f"If no species name is found, reply with 'no'."
    )
    result = generator(prompt, max_new_tokens=50)
    resposta = result[0]['generated_text'].strip()
    # Extrai apenas pares de palavras (binomiais) e remove duplicados
    nomes = list(set(re.findall(r'\b[A-Z][a-z]+\s[a-z]+\b', resposta)))
    return nomes


# %% Teste da função
generate_response('Verbascum thapsus Phytochemical composition, phytotoxicity, and ADME modeling of Artemisia absinthium L.: implications for food safety and pharmaceutical applications and Artemisia absinthium" If you find a plant species')
# %%
# Filtra as linhas de interesse (com 'family' vazio ou apenas espaços/vírgulas)
mask = df_fam['family'].isna() | df_fam['family'].str.fullmatch(
    r'[,\s]+', na=False)
mask.sum()
# Aplica generate_response apenas nas linhas filtradas
df_fam.loc[mask, "Entities_T_TGEN"] = df_fam.loc[mask,
                                                 "Article Title"].astype(str).apply(generate_response)
df_fam.loc[mask, "Entities_AB_TGEN"] = df_fam.loc[mask,
                                                  "Abstract"].astype(str).apply(generate_response)
df_fam.loc[mask, "Entities_AK_TGEN"] = df_fam.loc[mask,
                                                  "Author Keywords"].astype(str).apply(generate_response)
df_fam.loc[mask, "Entities_KP_TGEN"] = df_fam.loc[mask,
                                                  "Keywords Plus"].astype(str).apply(generate_response)

# Inicializa a coluna final
df_fam["Entities_TGEN"] = ""

# Prioriza os campos na ordem desejada
df_fam.loc[mask, 'Entities_TGEN'] = df_fam.loc[mask, 'Entities_T_TGEN']
df_fam.loc[mask, 'Entities_TGEN'] = df_fam.loc[mask, 'Entities_TGEN'].where(
    df_fam.loc[mask, 'Entities_TGEN'] != "", df_fam.loc[mask, 'Entities_AB_TGEN'])
df_fam.loc[mask, 'Entities_TGEN'] = df_fam.loc[mask, 'Entities_TGEN'].where(
    df_fam.loc[mask, 'Entities_TGEN'] != "", df_fam.loc[mask, 'Entities_AK_TGEN'])
df_fam.loc[mask, 'Entities_TGEN'] = df_fam.loc[mask, 'Entities_TGEN'].where(
    df_fam.loc[mask, 'Entities_TGEN'] != "", df_fam.loc[mask, 'Entities_KP_TGEN'])

# Salva resultado
df_fam.to_csv(r"C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN.csv",
              index=False, sep=",", encoding="utf-8")

# %%

df_fam = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN.csv')


df_fam['Entities_T_TGEN'].fillna("", inplace=True)
df_fam['Entities_AB_TGEN'].fillna("", inplace=True)
df_fam['Entities_AK_TGEN'].fillna("", inplace=True)
df_fam['Entities_KP_TGEN'].fillna("", inplace=True)
df_fam['Entities_TGEN'].fillna("", inplace=True)

df_fam['Entities_TGEN'].replace("[]", "", inplace=True)
df_fam['Entities_KP_TGEN'].replace("[]", "", inplace=True)
df_fam['Entities_AK_TGEN'].replace("[]", "", inplace=True)
df_fam['Entities_AK_TGEN'].fillna("", inplace=True)

df_fam['Entities_AB_TGEN'].replace("[]", "", inplace=True)
df_fam['Entities_AB_TGEN'].fillna("", inplace=True)

df_fam['Entities_T_TGEN'].replace("[]", "", inplace=True)
df_fam['Entities_T_TGEN'].fillna("", inplace=True)


df_fam['Entities_TGEN'] = df_fam['Entities_TGEN'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)

df_fam['Entities_AK_TGEN'] = df_fam['Entities_AK_TGEN'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)

df_fam['Entities_KP_TGEN'] = df_fam['Entities_KP_TGEN'].apply(
    lambda x: ', '.join(x) if isinstance(x, list) else x
)

df_fam['Entities_TGEN'][0]

# %%

# Função segura que transforma string em lista, se for necessário


def to_list(val):
    if isinstance(val, str) and val.startswith("[") and val.endswith("]"):
        try:
            return ast.literal_eval(val)
        except:
            return []
    return val


# Agora convertemos e aplicamos join em todas as colunas desejadas
for col in ['Entities_TGEN', 'Entities_AK_TGEN', 'Entities_KP_TGEN', 'Entities_AB_TGEN', 'Entities_T_TGEN']:
    # passo 1: converter string para lista
    df_fam[col] = df_fam[col].apply(to_list)
    df_fam[col] = df_fam[col].apply(lambda x: ', '.join(
        x) if isinstance(x, list) else x)  # passo 2: juntar as palavras

# %%
df_fam.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN01.csv', index=False)
# %%

df_fam[['Article Title', 'Abstract', 'Author Keywords', 'Keywords Plus', 'Entities_TGEN', 'Entities_AK_TGEN',
        'Entities_KP_TGEN', 'Entities_AB_TGEN', 'Entities_T_TGEN']][df_fam['Entities_TGEN'] != '']

# %% Procurar familia de novo

# %% import libraries
# %%
df_taxon = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Metabolites\Geral\wcvp_taxon.csv', delimiter='|')
df_species = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN01.csv')


# %%

df_taxon['lifeform'] = df_taxon['dynamicproperties'].apply(
    lambda x: json.loads(x).get('lifeform'))
df_taxon['climate'] = df_taxon['dynamicproperties'].apply(
    lambda x: json.loads(x).get('climate'))
df_taxon[['climate', 'lifeform', 'family']] = df_taxon[[
    'climate', 'lifeform', 'family']].fillna('')


# %%
if 'climate2' not in df_species.columns:
    df_species['climate2'] = ''
if 'lifeform2' not in df_species.columns:
    df_species['lifeform2'] = ''
if 'family2' not in df_species.columns:
    df_species['family2'] = ''

mask_spe = df_species[
    (df_species['Entities_TGEN'].notna()) &
    (~df_species['Entities_TGEN'].str.contains('#', na=False))
]

mask_tax = df_taxon[['scientfiicname', 'climate', 'lifeform', 'family']]

for index, row in mask_spe.iterrows():
    lista_similar_c = []
    lista_similar_l = []
    lista_similar_f = []

    entidades = [f.strip().lower() for f in row['Entities_TGEN'].split(',')]

    for entidade in entidades:
        mask_bool = mask_tax['scientfiicname'].str.lower() == entidade
        mask_filtered = mask_tax[mask_bool]

        seen_c = set()
        seen_l = set()
        seen_f = set()

        if not mask_filtered.empty:
            for _, row_taxon in mask_filtered.iterrows():
                c = str(row_taxon['climate']) if pd.notna(
                    row_taxon['climate']) else ''
                l = str(row_taxon['lifeform']) if pd.notna(
                    row_taxon['lifeform']) else ''
                f = str(row_taxon['family']) if pd.notna(
                    row_taxon['family']) else ''

                if c:
                    seen_c.add(c)
                if l:
                    seen_l.add(l)
                if f:
                    seen_f.add(f)

            lista_similar_c.append(', '.join(seen_c) if seen_c else '')
            lista_similar_l.append(', '.join(seen_l) if seen_l else '')
            lista_similar_f.append(', '.join(seen_f) if seen_f else '')
        else:
            lista_similar_c.append('')
            lista_similar_l.append('')
            lista_similar_f.append('')

    # Permite repetições globais, mas sem repetir valores para a mesma entidade
    df_species.loc[index, 'climate2'] = ', '.join(lista_similar_c)
    df_species.loc[index, 'lifeform2'] = ', '.join(lista_similar_l)
    df_species.loc[index, 'family2'] = ', '.join(lista_similar_f)

df_species.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02.csv',
    index=False
)
# %%
df_species[['Entities_TGEN', 'family2', 'lifeform2']
           ][df_species['family2'] != '']
df_species = df_species[~df_species['family2'].str.fullmatch(
    r'[,\s]+', na=False) & (df_species['family2'] != '')]


df_species[['Entities_TGEN', 'family2', 'lifeform2']
           ][df_species['family2'].str.fullmatch(r'[,\s]+', na=False)]


# %%

df_species = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02.csv')

# Máscaras: queremos linhas onde family e family2 possuem dados "úteis"
mask_fam2 = df_species['family2'].notna(
) & ~df_species['family2'].str.fullmatch(r'[,\s]*', na=False)
mask_fam = df_species['family'].notna(
) & ~df_species['family'].str.fullmatch(r'[,\s]*', na=False)

# Aplicar filtro
filtered_df = df_species[['family2', 'family']][mask_fam2 | mask_fam]


# %%

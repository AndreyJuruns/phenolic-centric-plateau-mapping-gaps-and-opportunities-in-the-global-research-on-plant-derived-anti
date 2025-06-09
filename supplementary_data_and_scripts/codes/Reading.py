# %% Importando bibliotecas
import pandas as pd
import os
import re
import transformers
from transformers import pipeline
import streamlit as st

# %%

pasta_diretorio = r'C:\Users\Andrey\Desktop\Artigo_Maio\Banco_WoS\\'


arquivos = os.listdir(pasta_diretorio)

dfs = []

for arquivo in arquivos:
    if arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(pasta_diretorio, arquivo)
        dfs.append(pd.read_excel(caminho_arquivo))

dfs

concat = pd.concat(dfs, ignore_index=False)
concat['Article Title'].value_counts()
df_sem_duplicatas = concat.drop_duplicates(subset=['Article Title'])
# %%
model_checkpoint = r"C:\Users\Andrey\Desktop\Metabolites\Geral\Modelo"
ner_pipeline = pipeline("token-classification", model=model_checkpoint,
                        tokenizer=model_checkpoint, aggregation_strategy="simple")

# %%


def extract_entities_transf(text):
    result = ner_pipeline(text)
    # Extrai apenas os textos das entidades
    entities = [ent['word'] for ent in result]
    unique_entities = list(set(entities))  # Remove duplicados
    # Junta tudo em uma única string separada por vírgula
    return ", ".join(unique_entities)


# %%
df_sem_duplicatas["Entities_T"] = df_sem_duplicatas["Article Title"].astype(
    str).apply(extract_entities_transf)
df_sem_duplicatas["Entities_AB"] = df_sem_duplicatas["Abstract"].astype(
    str).apply(extract_entities_transf)
df_sem_duplicatas["Entities_AK"] = df_sem_duplicatas["Author Keywords"].astype(
    str).apply(extract_entities_transf)
df_sem_duplicatas["Entities_KP"] = df_sem_duplicatas["Keywords Plus"].astype(
    str).apply(extract_entities_transf)


df_sem_duplicatas['Entities'] = ""

df_sem_duplicatas['Entities'] = df_sem_duplicatas['Entities_T'].where(
    df_sem_duplicatas['Entities_T'] != "", df_sem_duplicatas['Entities_AB'])
df_sem_duplicatas['Entities'] = df_sem_duplicatas['Entities'].where(
    df_sem_duplicatas['Entities'] != "", df_sem_duplicatas['Entities_AK'])
df_sem_duplicatas['Entities'] = df_sem_duplicatas['Entities'].where(
    df_sem_duplicatas['Entities'] != "", df_sem_duplicatas['Entities_KP'])

df_sem_duplicatas.to_csv("df_bert.csv", index=False, sep=",", encoding="utf-8")

# %%
df_final = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert.csv')
df_final.fillna("", inplace=True)

# %%

pesquisar_b = [
    # --- Compostos com espaço (detectados por regex especial) ---
    'essential oil',            # essential oil, essential oils
    'cardiotonic glycoside',    # cardiotonic glycoside(s)
    'cyanogenic glycoside',     # cyanogenic glycoside(s)
    'sesquiterpene lacton',  # sesquiterpene lacton(s)

    # --- Flavonoids e derivados ---
    # flavonoid, isoflavone, neoflavonoid, flavonol, Flavolignans etc.
    'flav',
    'anthocyan',      # anthocyanin, anthocyanidin
    'catechin',       # catechin, epicatechin
    'chalcon',        # chalcone, dihydrochalcone

    # --- Outras classes principais ---
    'alkaloid',
    'tannin',
    'coumar',         # coumarin, dicoumarol, coumarate
    'phenylprop',     # phenylpropanoid, phenylpropanoic
    'saponin',
    'steroid',
    'anthraquin',     # anthraquinone, anthraquinones
    'iridoid',
    'terpen',         # mono/di/tri/terpenes, terpenoid, sesquiterpene
    'glycosid',       # glycoside, glycosides
    'lignan',
    'phenol',         # phenolic, polyphenol
    'quinone',        # quinone, benzoquinone, etc.
    'amine',

    # --- Compostos diversos ---
    'alkamid',        # alkamide, alkamides
    'amide',
    'benzochrom',     # benzochromone, benzochromones
    'benzofuran',
    'capsaicin',      # capsaicinoid, capsaicin
    'caroten',        # carotenoid, carotenes
    'chromon',        # chromone, chromones
    'glucosinolat',   # glucosinolate, glucosinolates
    'kavalacton',     # kavalactone, kavalactones
    'phenylethan',    # phenylethanoid, phenylethanoids
    'phenylpyr',      # phenylpyrone, phenylpyrones
    'phloroglucinol',
    'polyacetylen',   # polyacetylene, polyacetylenes
    'proanthocyanid',  # proanthocyanidin, proanthocyanidins
    'stilben',        # stilbene, stilbenes
    'xanthon'         # xanthone, xanthones
]

len(pesquisar_b)


# %% Função para buscar termos compostos no texto

def buscar_termos_compostos(texto, radicais):
    texto_lower = texto.lower()
    encontrados = set()

    for radical in radicais:
        if ' ' in radical:
            # Regex: match frase com espaço e plural opcional no final da última palavra
            palavras = radical.strip().split()
            if len(palavras) == 2:
                pattern = r'\b' + palavras[0] + r'\s+' + palavras[1] + r's?\b'
                # Captura todos os matches no texto
                matches = re.finditer(pattern, texto_lower)
                for m in matches:
                    encontrados.add(texto[m.start():m.end()])
        else:
            # Palavra simples (radical): procurar dentro de palavras
            palavras_texto = re.findall(r'\b\w+\b', texto_lower)
            for palavra in palavras_texto:
                if radical in palavra:
                    encontrados.add(palavra)

    return list(encontrados)


# %%

df_final['bioactives_t'] = df_final['Article Title'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['bioactives_ab'] = df_final['Abstract'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['bioactives_ak'] = df_final['Author Keywords'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['bioactives_kp'] = df_final['Keywords Plus'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))

df_final['bioactives'] = df_final['bioactives_ab'].where(
    df_final['bioactives_ab'] != 'Não encontrado', df_final['bioactives_t'])
df_final['bioactives'] = df_final['bioactives'].where(
    df_final['bioactives'] != 'Não encontrado', df_final['bioactives_ak'])
df_final['bioactives'] = df_final['bioactives'].where(
    df_final['bioactives'] != 'Não encontrado', df_final['bioactives_kp'])


df_final.to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_Bio.csv',
                index=False, sep=",", encoding="utf-8")


# %%

contagem = {}

for lista in df_final['bioactives']:
    if isinstance(lista, list):
        for item in lista:
            item = item.strip().lower()
            contagem[item] = contagem.get(item, 0) + 1

# Ordenar do mais frequente para o menos
contagem_ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

# Exibir
for termo, freq in contagem_ordenado:
    print(f"{termo}: {freq}")

# %%
df_contagem = pd.DataFrame(contagem_ordenado, columns=['Termo', 'Frequência'])
df_contagem.to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\contagem_termos.csv',
                   index=False, sep=",", encoding="utf-8")

# %%

df = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_Bio_bac.csv')
# %%
df = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02_FUNG_Biosafety01.csv')

df = df.dropna(axis=1, how='all')
df[['Article Title', 'Abstract', 'Author Keywords', 'Keywords Plus', 'Entities', 'Entities_TGEN', 'family', 'family2', 'bioactives', 'Bacteria', 'gram', 'FUNG', 'Biosafety', 'lifeform', 'climate', 'lifeform2', 'climate2', 'Publication Year', 'Authors']].to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02_FUNG_Biosafety02.csv',
                                                                                                                                                                                                                                                                     index=False, sep=",", encoding="utf-8")
# %%

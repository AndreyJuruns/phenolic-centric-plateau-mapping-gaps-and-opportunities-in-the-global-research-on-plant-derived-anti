# %% import libraries
import pandas as pd
import os

# %%

pasta_diretorio = r'C:\Users\Andrey\Desktop\Artigo_Maio\Fungo\\'


arquivos = os.listdir(pasta_diretorio)

dfs = []

for arquivo in arquivos:
    if arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(pasta_diretorio, arquivo)
        dfs.append(pd.read_excel(caminho_arquivo))

dfs

concat = pd.concat(dfs, ignore_index=False)
concat.to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\Lista_fungos.csv',
              index=False, sep=",", encoding="utf-8")
pesquisar_b = concat['Pathogen name'].dropna().astype(str).str.strip()
pesquisar_b = pesquisar_b[pesquisar_b != ""].tolist()
len(pesquisar_b)
# %%


def buscar_termos_compostos(texto, radicais):
    if not isinstance(texto, str):
        return ''

    texto_lower = texto.lower()
    encontrados = set()

    for radical in radicais:
        if isinstance(radical, str) and radical.strip():
            if radical.lower() in texto_lower:
                encontrados.add(radical)

    return list(encontrados)

# %%


df_final = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02.csv')
df_final.fillna("", inplace=True)
# %%
df_final['FUNG_t'] = df_final['Article Title'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['FUNG_ab'] = df_final['Abstract'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['FUNG_ak'] = df_final['Author Keywords'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['FUNG_kp'] = df_final['Keywords Plus'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))

df_final['FUNG'] = df_final['FUNG_ab'].where(
    df_final['FUNG_ab'] != 'Não encontrado', df_final['FUNG_t'])
df_final['FUNG'] = df_final['FUNG'].where(
    df_final['FUNG'] != 'Não encontrado', df_final['FUNG_ak'])
df_final['FUNG'] = df_final['FUNG'].where(
    df_final['FUNG'] != 'Não encontrado', df_final['FUNG_kp'])


df_final.to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02_FUNG.csv',
                index=False, sep=",", encoding="utf-8")

df_final = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\FIltros_Tree\Banco_Dados_Filtrado02.csv')

# %%

contagem = {}

for lista in df_final['Entities_Grouped']:
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
df_contagem.to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\contagem_termos_spicies.csv',
                   index=False, sep=",", encoding="utf-8")

# %%

# %% import libraries
import pandas as pd
import os
import re
# %% ler arquivos
pasta_diretorio = r'C:\Users\Andrey\Desktop\Artigo_Maio\Bacteria\\'


arquivos = os.listdir(pasta_diretorio)

dfs = []

for arquivo in arquivos:
    if arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(pasta_diretorio, arquivo)
        dfs.append(pd.read_excel(caminho_arquivo))

dfs

concat = pd.concat(dfs, ignore_index=False)
pesquisar_b = concat['Pathogen name'].dropna().astype(str).str.strip()
pesquisar_b = pesquisar_b[pesquisar_b != ""].tolist()

# %%


def buscar_termos_compostos(texto, radicais):
    if not isinstance(texto, str):
        return []

    encontrados = set()
    texto_lower = texto.lower()

    for radical in radicais:
        if not isinstance(radical, str):
            continue

        radical = radical.strip()
        radical_lower = radical.lower()

        if ' ' in radical:
            palavras = radical_lower.split()
            if len(palavras) == 2:
                pattern = rf'\b{re.escape(palavras[0])}\s+{re.escape(palavras[1])}s?\b'
                matches = re.finditer(pattern, texto_lower)
                for m in matches:
                    encontrados.add(texto[m.start():m.end()])
        else:
            for match in re.findall(r'\b\w+\b', texto):
                if radical_lower in match.lower():
                    encontrados.add(match)

    return list(encontrados)

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
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_Bio.csv')
df_final.fillna("", inplace=True)
# %%
df_final['Bacteria_t'] = df_final['Article Title'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['Bacteria_ab'] = df_final['Abstract'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['Bacteria_ak'] = df_final['Author Keywords'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))
df_final['Bacteria_kp'] = df_final['Keywords Plus'].apply(
    lambda x: buscar_termos_compostos(x, pesquisar_b))

df_final['Bacteria'] = df_final['Bacteria_ab'].where(
    df_final['Bacteria_ab'] != 'Não encontrado', df_final['Bacteria_t'])
df_final['Bacteria'] = df_final['Bacteria'].where(
    df_final['Bacteria'] != 'Não encontrado', df_final['Bacteria_ak'])
df_final['Bacteria'] = df_final['Bacteria'].where(
    df_final['Bacteria'] != 'Não encontrado', df_final['Bacteria_kp'])


df_final.to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_Bio_bac.csv',
                index=False, sep=",", encoding="utf-8")

# %%

texto = df_final.at[3897, 'Article Title']


resultado = buscar_termos_compostos(texto, pesquisar_b)


df_final['Bacteria']

# %%
import pandas as pd


#df_final = pd.read_csv(
#    r'C:\Users\Andrey\Desktop\Artigo_Maio\FIltros_Tree\Banco_Dados_Filtrado02.csv')

df_final = pd.read_csv(
   r'C:\Users\Andrey\Desktop\Artigo_Maio\FIltros_Tree\Banco_Dados_Filtrado03.csv')

contagem = {}

for lista in df_final['Country']:
    if isinstance(lista, str):
        lista = [item.strip() for item in lista.split(',')]
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
df_contagem.to_csv(r'C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit\contagemPaís.csv',
                   index=False, sep=",", encoding="utf-8")

# %%

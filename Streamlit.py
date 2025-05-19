import pandas as pd
import streamlit as st
import plotly as px
import plotly.graph_objects as go
import numpy as np
# Define layout como wide
st.set_page_config(
    layout="wide", page_title="Frequência de Compostos Bioativos"
)

# Carrega os dados
df_contagem = pd.read_csv('contagem_termos.csv')
df_countsN = pd.read_csv('contagemN.csv')
df_countsP = pd.read_csv('contagemP.csv')

# Agrupamento manual de termos semelhantes
agrupamento = {
    # variações de phenolics

    "phenolic": "phenolics",
    "polyphenols": "phenolics",
    "phenol": "phenolics",
    "polyphenolic": "phenolics",
    "polyphenol": "phenolics",
    "polyphenolics": "phenolics",

    # variações de flavonoids

    "flavonoid": "flavonoids",
    "hydroxyflavones": "flavonoids",
    "hydroxyflavone": "flavonoids",
    "anthocyanins": "flavonoids",
    "flavonols": "flavonoids",
    "anthocyanin": "flavonoids",
    "flavones": "flavonoids",
    "flavonol": "flavonoids",
    "proanthocyanidins": "flavonoids",
    "flavanones": "flavonoids",
    "flavanols": "flavonoids",
    "flavone": "flavonoids",
    "catechins": "flavonoids",
    "proanthocyanidin": "flavonoids",
    "isoflavonoids": "flavonoids",
    "flavanoids": "flavonoids",
    "chalcones": "flavonoids",
    "flavanone": "flavonoids",
    "flavanol": "flavonoids",
    "chalcone": "flavonoids",
    "isoflavones": "flavonoids",
    "dihydroflavonols": "flavonoids",
    "isoflavone": "flavonoids",
    "dimethoxyflavone": "flavonoids",
    "isoflavonoid": "flavonoids",
    "biflavonoids": "flavonoids",
    "flavanoid": "flavonoids",
    "dihydrochalcones": "flavonoids",
    "anthocyanidins": "flavonoids",
    "flavonoides": "flavonoids",
    "dihydrochalcone": "flavonoids",
    "methoxychalcone": "flavonoids",
    "dihydroflavonol": "flavonoids",
    "dihydroxychalcone": "flavonoids",
    "proanthocyanins": "flavonoids",
    "leucoanthocyanins": "flavonoids",
    "flavonones": "flavonoids",
    "trimethoxyflavone": "flavonoids",
    "dimethoxychalcone": "flavonoids",
    "biflavones": "flavonoids",
    "biflavonoid": "flavonoids",
    "isoflavanones": "flavonoids",
    "hexamethoxyflavone": "flavonoids",
    "flavanonols": "flavonoids",
    "anthocyanidin": "flavonoids",
    "trimethoxyflavanone": "flavonoids",
    "pentahydroxyflavane": "flavonoids",
    "dimethoxyisoflavan": "flavonoids",
    "biflavanone": "flavonoids",
    "polymethoxyflavones": "flavonoids",
    "dihydroxyflavanone": "flavonoids",
    "methoxyflavanone": "flavonoids",
    "methoxydihydrochalcone": "flavonoids",
    "methoxyflavones": "flavonoids",
    "flavanonol": "flavonoids",
    "flavane": "flavonoids",
    "furanoflavonoids": "flavonoids",
    "flavonolignans": "flavonoids",
    "flavonic": "flavonoids",
    "flavinoid": "flavonoids",
    "flavons": "flavonoids",
    "isoflavans": "flavonoids",
    "anthocyanosides": "flavonoids",
    "flavonoidic": "flavonoids",
    "trihydroxyflavone": "flavonoids",
    "tetramethoxyflavone": "flavonoids",
    "theaflavins": "flavonoids",
    "anthocyaninic": "flavonoids",
    "anthocyans": "flavonoids",
    "biflavone": "flavonoids",
    "biflavonols": "flavonoids",
    "flavoniod": "flavonoids",
    "flavoniods": "flavonoids",
    "flavonoidal": "flavonoids",
    "flavonoide": "flavonoids",
    "flavonolols": "flavonoids",
    "flavononol": "flavonoids",
    "methoxyflavan": "flavonoids",
    "methoxyisoflavan": "flavonoids",
    "methylflavone": "flavonoids",
    "neoflavones": "flavonoids",
    "neoflavonoids": "flavonoids",
    "abyssinoflavanones": "flavonoids",
    "aglyconflavonols": "flavonoids",
    "aglyconsflavonols": "flavonoids",
    "chalconas": "flavonoids",
    "conyflavone": "flavonoids",
    "deoxyanthocyanidins": "flavonoids",
    "deoxycatechin": "flavonoids",
    "dihydroflavone": "flavonoids",
    "dihydroflavones": "flavonoids",
    "dihydroflavonoids": "flavonoids",
    "dihydropyranoisoflavanone": "flavonoids",
    "dihydroxyflavan": "flavonoids",
    "dihydroxyflavone": "flavonoids",
    "dimethoxyflavan": "flavonoids",
    "dimethoxyflavanone": "flavonoids",
    "dimethoxyisoflavone": "flavonoids",
    "dimethylflavone": "flavonoids",
    "dimiethoxyflavone": "flavonoids",
    # variações de terpenoids

    "terpenes": "terpenoids",
    "terpenoid": "terpenoids",
    # variações de alkaloids

    "alkaloid": "alkaloids",
    "alkaloidal": "alkaloids",
    "glycoalkaloids": "alkaloids",
    "glycoalkaloid": "alkaloids",

    # variações de cyanogenic glycosides
    "cyanogenic glycoside": "cyanogenic glycosides",
    "glucosinolates": "cyanogenic glycosides",
    "glucosinolate": "cyanogenic glycosides",

    # variações de alkamides

    "alkylamides": "alkamides",
    "alkamide": "alkamides",
    "alkanolamine": "alkamides",
    "alkylamines": "alkamides",

    # variações de stibenoids

    "stilbenoid": "stilbenoids",
    "stilbenes": "stilbenoids",
    "stilbene": "stilbenoids",
    "dihydrostilbenes": "stilbenoids",

    # variações de phenylethanoids

    "phenylethanoid": "phenylethanoids",
    "phenylethanol": "phenylethanoids",
    "dihydroxyphenylethanol": "phenylethanoids",

    # variações de iridoids

    "iridoid": "iridoids",
    "secoiridoid": "iridoids",
    "secoiridoids": "iridoids",
    # variações de phenylpropanoids

    "phenylpropanoid": "phenylpropanoids",
    "phenylpropane": "phenylpropanoids",
    "phenylpropan": "phenylpropanoids",
    "phenylpropanes": "phenylpropanoids",
    "phenylpropanoic": "phenylpropanoids",
    "phenylpropanol": "phenylpropanoids",
    "phenylpropanyl": "phenylpropanoids",
    "phenylpropenoate": "phenylpropanoids",
    "phenylpropenoids": "phenylpropanoids",
    "phenylpropiolate": "phenylpropanoids",
    "phenylpropionate": "phenylpropanoids",
    "cinnamoylphenols": "phenylpropanoids",
    "coumaroylquinic": "phenylpropanoids",

    # variações de  xanthones

    "xanthone": "xanthones",
    "dihydrobenzoxanthone": "xanthones",
    "cycloartobiloxanthone": "xanthones",
    "deprenylrheediaxanthone": "xanthones",
    "dihydroxyxanthone": "xanthones",

    # variações de lignans

    "lignan": "lignans",
    "neolignans": "lignans",
    "neolignan": "lignans",
    "lignane": "lignans",

    # variações de diterpenes

    "diterpenes": "diterpenes",
    "diterpenoids": "diterpenes",
    "diterpenoid": "diterpenes",
    "diterpene": "diterpenes",
    "diterpenic": "diterpenes",
    "diterpeneol": "diterpenes",
    "diterpenicacids": "diterpenes",
    "diterpenolactone": "diterpenes",
    # variações de saponins

    "saponin": "saponins",
    "soyasaponin": "saponins",

    # variações de monoterpenenes

    "monoterpenoids": "monoterpenes",
    "monoterpenic": "monoterpenes",
    "monoterpene": "monoterpenes",
    "monoterpenoid": "monoterpenes",
    # variações de steroids

    "steroid": "steroids",
    "steroidal": "steroids",
    "phytosteroids": "steroids",

    # variações de triterpenoids

    "triterpenes": "triterpenoids",
    "triterpenoid": "triterpenoids",
    "triterpene": "triterpenoids",
    "terpenic": "triterpenoids",
    "triterpenic": "triterpenoids",
    "triterpens": "triterpenoids",
    "triterpenoidal": "triterpenoids",
    "acetyltriterpenoids": "triterpenoids",
    "acylglycosides": "triterpenoids",
    # variações de carotenes

    "carotene": "carotenes",
    "carotenoids": "carotenes",
    "carotenoid": "carotenes",
    "carotenes": "carotenes",
    "caroten": "carotenes",
    "apocarotenes": "carotenes",
    "apocarotenoid": "carotenes",
    "apocarotenoids": "carotenes",
    "caroteno": "carotenes",
    "carotenoides": "carotenes",

    # variações de coumarins
    "coumaric": "coumarins",
    "coumarins": "coumarins",
    "coumarin": "coumarins",
    "coumaroyl": "coumarins",
    "hydroxycoumarin": "coumarins",
    "furanocoumarins": "coumarins",
    "pyranocoumarins": "coumarins",
    "furocoumarins": "coumarins",
    "methoxycoumarin": "coumarins",
    "coumarate": "coumarins",
    "pcoumaric": "coumarins",
    "dihydroisocoumarin": "coumarins",
    "dihydroisocoumarins": "coumarins",
    "dihydroxycoumarin": "coumarins",
    "isocoumarin": "coumarins",
    "glycycoumarin": "coumarins",
    "coumarines": "coumarins",
    "furanocoumarin": "coumarins",
    "coumaryl": "coumarins",
    "trimethoxycoumarin": "coumarins",
    "bicoumarin": "coumarins",
    "biscoumarin": "coumarins",
    "coumaranone": "coumarins",
    "coumarates": "coumarins",
    "coumarine": "coumarins",
    "coumarinolignoids": "coumarins",
    "coumaroylglycerol": "coumarins",
    "coumaroylglycosideum": "coumarins",
    "coumaroylhexoside": "coumarins",
    "coumaroyloxyursan": "coumarins",
    "coumaroylspermidines": "coumarins",
    "coumaroyltyramine": "coumarins",
    "coumarylglucoside": "coumarins",
    "coumarylheptanedioic": "coumarins",
    "dicoumarinyl": "coumarins",
    "dihydrocoumaroylhexose": "coumarins",
    "dimethoxycoumarin": "coumarins",

    # variações de sesquiterpenes

    "sesquiterpene": "sesquiterpenes",
    "sesquiterpenoids": "sesquiterpenes",
    "sesquiterpenoid": "sesquiterpenes",
    "sesquiterpenic": "sesquiterpenes",
    "sequisterpenes": "sesquiterpenes",
    "sequiterpene": "sesquiterpenes",
    "sequiterpenoid": "sesquiterpenes",
    "sesqiuterpenoids": "sesquiterpenes",
    "sesquiterpens": "sesquiterpenes",

    # variações de tannins

    "tannin": "tannins",
    "ellagitannins": "tannins",
    "phlobatannins": "tannins",
    "gallotannins": "tannins",
    "phlobatannin": "tannins",
    "phlorotannins": "tannins",
    "phlobotannins": "tannins",
    "ellagatannins": "tannins",
    "ellgitannins": "tannins",

    # variações de antroquinonas

    "quinones": "anthraquinones",
    "anthraquinone": "anthraquinones",
    "benzoquinone": "anthraquinones",
    "quinone": "anthraquinones",
    "naphthoquinones": "anthraquinones",
    "naphthoquinone": "anthraquinones",
    "anthroquinone": "anthraquinones",
    "hydroxyanthraquinone": "anthraquinones",
    "anthroquinones": "anthraquinones",
    "anthraquinon": "anthraquinones",
    "anthraquinons": "anthraquinones",
    "antraquinones": "anthraquinones",
    "azaanthraquinone": "anthraquinones",
    "dihydroanthraquinone": "anthraquinones",

    # variações de sesquiterpenes

    "sesquiterpene": "sesquiterpenes",
    "sesquiterpenoids": "sesquiterpenes",
    "sesquiterpenoid": "sesquiterpenes",
    "sesquiterpenic": "sesquiterpenes",
    "sequisterpenes": "sesquiterpenes",
    "sequiterpene": "sesquiterpenes",
    "sequiterpenoid": "sesquiterpenes",
    "sesqiuterpenoids": "sesquiterpenes",
    "sesquiterpens": "sesquiterpenes",

    # variações de compounds
    "catechin": "isolated compounds",
    "epicatechin": "isolated compounds",
    "thymoquinone": "isolated compounds",
    "epigallocatechin": "isolated compounds",
    "gallocatechin": "isolated compounds",
    "galantamine": "isolated compounds",
    "galanthamine": "isolated compounds",
    "amentoflavone": "isolated compounds",
    "ellagitannin": "isolated compounds",
    "methoxyflavone": "isolated compounds",
    "octadecenamide": "isolated compounds",
    "capsaicin": "isolated compounds",
    "dithymoquinone": "isolated compounds",
    "docosenamide": "isolated compounds",
    "thymohydroquinone": "isolated compounds",
    "piperamide": "isolated compounds",
    "isobavachalcone": "isolated compounds",
    "licochalcone": "isolated compounds",
    "morelloflavone": "isolated compounds",
    "sophoraflavanone": "isolated compounds",
    "dihydrocapsaicin": "isolated compounds",
    "caffeoyltyramine": "isolated compounds",
    "columbamine": "isolated compounds",
    "gallotannin": "isolated compounds",
    "catechine": "isolated compounds",
    "theaflavin": "isolated compounds",
    "agathisflavone": "isolated compounds",
    "methylgallocatechin": "isolated compounds",
    "neobavaisoflavone": "isolated compounds",
    "abyssinoflavanone": "isolated compounds",
    "alangiflavoside": "isolated compounds",
    "allanxanthone": "isolated compounds",
    "artobiloxanthone": "isolated compounds",
    "atalantoflavone": "isolated compounds",
    "aurantiamide": "isolated compounds",
    "avenanthramide": "isolated compounds",
    "avicequinone": "isolated compounds",
    "brachyamide": "isolated compounds",
    "brachystamide": "isolated compounds",
    "brasilixanthone": "isolated compounds",
    "budmunchiamines": "isolated compounds",
    "clausamine": "isolated compounds",
    "cupressoflavone": "isolated compounds",
    "cupressuflavone": "isolated compounds",
    "dehydroabietylamine": "isolated compounds",
    "demethyllycoramine": "isolated compounds",
    "deoxybryaquinone": "isolated compounds",
    "desmoflavanone": "isolated compounds",
    "dihydrocaffeoyltyramine": "isolated compounds",
    "dihydrorescinnamine": "isolated compounds",
    "dodecatetraenamide": "isolated compounds",
    "elastixanthone": "isolated compounds",
    "capsaicinoids": "isolated isolated compounds",
    # variações de ruidos

    "essential oils": "noise",
    "essential oil": "noise",
    "Essential oils": "noise",
    "Essential oil": "noise",
    "glycosides": "noise",
    "glycoside": "noise",
    "flavus": "noise",
    "flavan": "noise",
    "terpene": "noise",
    "amides": "noise",
    "amines": "noise",
    "amine": "noise",
    "phloroglucinol": "noise",
    "sulforhodamine": "noise",
    "phenological": "noise",
    "malignant": "noise",
    "flavoring": "noise",
    "examines": "noise",
    "examine": "noise",
    "examined": "noise",
    "benzofuran": "noise",
    "flavour": "noise",
    "graminearum": "noise",
    "glycosidase": "noise",
    "amide": "noise",
    "hydroquinone": "noise",
    "polyacetylenes": "noise",
    "riboflavin": "noise",
    "phloroglucinols": "noise",
    "flavescens": "noise",
    "flavors": "noise",
    "flava": "noise",
    "chromones": "noise",
    "butylphenol": "noise",
    "diphenols": "noise",
    "monoamine": "noise",
    "aminoglycosides": "noise",
    "glycosidic": "noise",
    "malignancies": "noise",
    "acylphloroglucinol": "noise",
    "flavouring": "noise",
    "glucosamine": "noise",
    "polyacetylene": "noise",
    "vinylphenol": "noise",
    "acylphloroglucinols": "noise",
    "benzamide": "noise",
    "glibenclamide": "noise",
    "dopamine": "noise",
    "acetamide": "noise",
    "terpens": "noise",
    "stamineus": "noise",
    "sulphorhodamine": "noise",
    "thiamine": "noise",
    "glutamine": "noise",
    "cyclophosphamide": "noise",
    "dihydrobenzofuran": "noise",
    "tyramine": "noise",
    "diphenol": "noise",
    "oleamide": "noise",
    "histamine": "noise",
    "chromone": "noise",
    "ethylenediaminetetraacetic": "noise",
    "flavedo": "noise",
    "flavours": "noise",
    "nicotinamide": "noise",
    "diglycosidic": "noise",
    "tanning": "noise",
    "aminoglycoside": "noise",
    "phenolcarboxylic": "noise",
    "phenology": "noise",
    "diphenolase": "noise",
    "benzofurans": "noise",
    "polyamines": "noise",
    "polyamide": "noise",
    "polyacrylamide": "noise",
    "ecdysteroids": "noise",
    "monophenolase": "noise",
    "butylhydroquinone": "noise",
    "diynamide": "noise",
    "hydroxylamine": "noise",
    "ceramides": "noise",
    "diglycosides": "noise",
    "ceramide": "noise",
    "flavum": "noise",
    "cyclopamine": "noise",
    "antihistamine": "noise",
    "acrylamide": "noise",
    "23flavonoids": "noise",
    "8trimethoxyflavone": "noise",
    "anthocyani": "noise",
    "benzofurane": "noise",
    "benzofuranes": "noise",
    "benzofuranyl": "noise",
    "flavonoglycosides": "noise",
    "flavonoidsd": "noise",
    "decatrienamide": "noise",
    "coumaricic": "noise",
    "coumari": "noise",
    "chingchengenamide": "noise",
    "chloroamphetamine": "noise",
    "acetophenole": "noise",
    "acriflavine": "noise",
    "alkylphloroglucinol": "noise",
    "anthraflavic": "noise",
    "aminobutyramide": "noise",
    "aminophenol": "noise",
    "andtannins": "noise",
    "anthramine": "noise",
    "arylamides": "noise",
    "arylbenzofurans": "noise",
    "backgroundanthocyanins": "noise",
    "benzenamine": "noise",
    "benzeneethanamine": "noise",
    "bisphenol": "noise",
    "caboxybenzofuran": "noise",
    "calendulaglycosides": "noise",
    "carbamide": "noise",
    "carboxamide": "noise",
    "casseliflavus": "noise",
    "catecholamines": "noise",
    "cglycosides": "noise",
    "cyclolignan": "noise",
    "dihydrobenzofurane": "noise",
    "emodacidamides": "noise",
    "eicosadienamide": "noise",
    "ecdysteroid": "noise",
    "dyramide": "noise",
    "dopaminergic": "noise",
    "diphenylamine": "noise",
    "diphenethylamine": "noise",
    "dimethoxyphenol": "noise",
    "diisobutyrylphloroglucinol": "noise",
    "dihydroxyphenols": "noise",
    "dihydroxychromone": "noise",
    "desferrioxamine": "noise",
    "diacetylphloroglucinol": "noise",
    "dibenzofuranamine": "noise",
    "dibenzofurans": "noise",
    "diclaidoylphosphatidylethanolamine": "noise",
    "dictamine": "noise",
    "dicyanopropionamide": "noise",
    "dielaidoylphosphatidylethanolamine": "noise",
    "diethylamine": "noise",
    "diethyltoluamide": "noise",
    "entadamide": "noise",
    "eoxyepicatechin": "noise",
    "epigallocatechingallate": "noise",
    "erucamide": "noise",
    "etanolamine": "noise",
    "ethanolamide": "noise",
    "ethylhydroxylamine": "noise",
    "examiners": "noise",
    "famine": "noise",
    "feruloylglycosideum": "noise",
    "feruloyltyramine": "noise",
    "fistulosaponins": "noise",
    "flavanomarein": "noise",
    "flavans": "noise",
    "flavaspidic": "noise",
    "flavellagic": "noise",
    "flaveseens": "noise",
    "flavibasis": "noise",
    "flavicarpa": "noise",
    "flavidum": "noise",
    "flavinoids": "noise",
    "flavipora": "noise",
    "flaviporus": "noise",
    "flavius": "noise",
    "flavo": "noise",
    "flavocetraria": "noise",
    "flavogallonate": "noise",
    "flavogallonic": "noise",
    "flavomycin": "noise",
    "flavon": "noise",
    "flavoncs": "noise",
    "flavored": "noise",
    "flavorful": "noise",
    "flavoured": "noise",
    "flavous": "noise",
    "furanditerpene": "noise",
    "furanochromone": "noise",
    "furanonaphtoquinones": "noise",
    "furanosesquiterpenes": "noise",
    "furanoxanthones": "noise",
    "furanxanthone": "noise",
    "galactosamine": "noise",
    "gallotannines": "noise",
    "galloylglycoside": "noise",
    "gastrodiamide": "noise",
    "gerontoxanthone": "noise",
    "gewurztraminer": "noise",
    "glabrisoflavone": "noise",
    "glycerophosphoethanolamines": "noise",
    "glycosideum": "noise",
    "glycosids": "noise",
    "glycosylflavones": "noise",
    "hederasaponin": "noise",
    "heliamine": "noise",
    "hexadecanamide": "noise",
    "hexahydroxyflavone": "noise",
    "hexosamine": "noise",
    "higenamine": "noise",
    "homoisoflavones": "noise",
    "homoisoflavonoid": "noise",
    "hydroquinones": "noise",
    "hydroxybenzofuran": "noise",
    "hydroxycalothorexanthone": "noise",
    "hydroxychalcones": "noise",
    "hydroxycoumarins": "noise",
    "hydroxysteroid": "noise",
    "hydroxytryptamine": "noise",
    "hynokiflavone": "noise",
    "ilwensisaponin": "noise",
    "indolamine": "noise",
    "isobutylamides": "noise",
    "isocoumarins": "noise",
    "isoflav": "noise",
    "isoflavanoids": "noise",
    "isoflavanone": "noise",
    "isoflavonids": "noise",
    "isoflavonoides": "noise",
    "isopropyamine": "noise",
    "isopropylbutyramide": "noise",
    "kaikasaponin": "noise",
    "kavalactone": "noise",
    "kavalactones": "noise",
    "lauramide": "noise",
    "leucoanthocyanidins": "noise",
    "lichexanthone": "noise",
    "lignanoids": "noise",
    "loperamide": "noise",
    "lophenol": "noise",
    "lumiflavin": "noise",
    "luteaceramide": "noise",
    "lysicamine": "noise",
    "maesaquinone": "noise",
    "malignancy": "noise",
    "mannosamine": "noise",
    "menaquinone": "noise",
    "meroterpenes": "noise",
    "meroterpenoid": "noise",
    "methoxycoumaroylaloeresin": "noise",
    "methoxyphenol": "noise",
    "methoxyxanthone": "noise",
    "methylamine": "noise",
    "methylanthraquinone": "noise",
    "methylenedioxyflavonol": "noise",
    "methylethanolamine": "noise",
    "methylphenol": "noise",
    "methylpropylamide": "noise",
    "methyltyramide": "noise",
    "methylxanthone": "noise",
    "monoglycosides": "noise",
    "monomethoxyflavone": "noise",
    "monoynamide": "noise",
    "moschamine": "noise",
    "murrayamine": "noise",
    "naphthoflavone": "noise",
    "naphthylamide": "noise",
    "naphtoquinone": "noise",
    "nigellamine": "noise",
    "nonterpene": "noise",
    "nonterpenic": "noise",
    "nonterpenoid": "noise",
    "norfenfluramine": "noise",
    "norflavaspidic": "noise",
    "norlignan": "noise",
    "norsesquiterpene": "noise",
    "nortriterpenes": "noise",
    "octadecanamide": "noise",
    "octadecanamine": "noise",
    "octadecylamine": "noise",
    "oglycoside": "noise",
    "oligostilbene": "noise",
    "oliveriflavone": "noise",
    "oterpenes": "noise",
    "pachysamine": "noise",
    "paminophenol": "noise",
    "paxanthone": "noise",
    "pcoumaroyl": "noise",
    "pentadecatrienamide": "noise",
    "pentahydroxyflavonol": "noise",
    "pentamethoxyflavone": "noise",
    "phenanthrenequinone": "noise",
    "phenolamides": "noise",
    "phenoxychromones": "noise",
    "phenylanthroquinones": "noise",
    "phenylenediamine": "noise",
    "phenylethylamine": "noise",
    "phenylethylamines": "noise",
    "phenylpyridinium": "noise",
    "phenylpyruvic": "noise",
    "phloroglucinolysis": "noise",
    "phlorotannin": "noise",
    "phosphatidylethanolamine": "noise",
    "phylloquinone": "noise",
    "phytoecdysteroids": "noise",
    "piperidinamine": "noise",
    "piptadenamide": "noise",
    "polemoniumsaponins": "noise",
    "polyamides": "noise",
    "polyphenolcarboxylic": "noise",
    "polyphenoles": "noise",
    "polyterpenes": "noise",
    "prenylflavanone": "noise",
    "prenylflavanones": "noise",
    "prenylflavonoids": "noise",
    "prenyloxyanthraquinones": "noise",
    "prenylstilbene": "noise",
    "proanthocyanadin": "noise",
    "proanthocyandins": "noise",
    "proanthocyanidins919": "noise",
    "proflavine": "noise",
    "propenylbenzofuran": "noise",
    "propionamide": "noise",
    "pseudograminearum": "noise",
    "pterocarpanquinones": "noise",
    "pterostilbene": "noise",
    "punicatannin": "noise",
    "pyranocoumarin": "noise",
    "pyrazinamide": "noise",
    "quinonemethide": "noise",
    "quinonemethides": "noise",
    "reexamined": "noise",
    "rescinnamine": "noise",
    "resultiridoid": "noise",
    "resultsanthocyanins": "noise",
    "retamine": "noise",
    "rheediaxanthone": "noise",
    "rhodamine": "noise",
    "rhodamine123": "noise",
    "rhodioflavonoside": "noise",
    "rubraxanthone": "noise",
    "saponines": "noise",
    "saponinss": "noise",
    "scopolamine": "noise",
    "secolignans": "noise",
    "sesquiterpenyl": "noise",
    "solophenol": "noise",
    "sotusflavone": "noise",
    "soyaysaponin": "noise",
    "stenocarpoquinone": "noise",
    "steroidals": "noise",
    "steroidogenesis": "noise",
    "stilbenoid": "noise",
    "sulfonamide": "noise",
    "sulphonamide": "noise",
    "tanninrich": "noise",
    "terpenoidic": "noise",
    "terpenyl": "noise",
    "tetradecylamine": "noise",
    "tetrahydrocolumbamine": "noise",
    "tetrahydroxyflavane": "noise",
    "tetrahydroxyflavanone": "noise",
    "tetrahydroxyxanthone": "noise",
    "tetramethylamentoflavone": "noise",
    "tetraterpenes": "noise",
    "thiocarboxamide": "noise",
    "totalflavonoids": "noise",
    "tricoumarin": "noise",
    "trienamide": "noise",
    "triethylenediamine": "noise",
    "triglycosides": "noise",
    "trihydroxyflavan": "noise",
    "trihydroxyflavon": "noise",
    "trihydroxylchalcone": "noise",
    "trihydroxymethoxyflavone": "noise",
    "trimethoxychalcone": "noise",
    "trimethoxyisoflavan": "noise",
    "trimethoxyisoflavone": "noise",
    "trimethoxyisoflavone7": "noise",
    "trimethoxyphenol": "noise",
    "trimethylamentoflavone": "noise",
    "trinortriterpenoid": "noise",
    "triphenolic": "noise",
    "triterpenene": "noise",
    "triterpenoides": "noise",
    "tryptamine": "noise",
    "tymoquinone": "noise",
    "unexamined": "noise",
    "veratramine": "noise",
    "vernoguinoflavone": "noise",
    "viridiflava": "noise",
    "vismiaquinone": "noise",
    "volkensiflavone": "noise",
    "xanthonic": "noise",
    "ylphenol": "noise",
    "ylphenols": "noise",
    "flavor": "noise",
    "flavors": "noise",

    "cardiotonic glycosides": "noise",
    "piperamide": "noise",
}

# Cria nova coluna com os termos padronizados
df_contagem["Termo Agrupado"] = ''
df_countsN["Termo Agrupado"] = ''
df_countsP["Termo Agrupado"] = ''
df_contagem["Termo Agrupado"] = df_contagem["Termo"].replace(agrupamento)
df_countsN['Termo Agrupado'] = df_countsN["bioactives"].replace(agrupamento)
df_countsP['Termo Agrupado'] = df_countsP["bioactives"].replace(agrupamento)

# Agrupa e soma as frequências
df_contagem = (
    df_contagem.groupby("Termo Agrupado", as_index=False)["Frequência"]
    .sum()
    .sort_values(by="Frequência", ascending=False)
)

df_countsN = (
    df_countsN.groupby("Termo Agrupado", as_index=False)["count"]
    .sum()
    .sort_values(by="count", ascending=False)
)

df_countsP = (
    df_countsP.groupby("Termo Agrupado", as_index=False)["count"]
    .sum()
    .sort_values(by="count", ascending=False)
)

df_contagem = df_contagem[df_contagem['Termo Agrupado'] != 'noise']
df_countsN = df_countsN[df_countsN['Termo Agrupado'] != 'noise']
df_countsP = df_countsP[df_countsP['Termo Agrupado'] != 'noise']

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
top_n_data = df_contagem.head(top_n).set_index('Termo Agrupado')

# Container: gráfico principal
with st.container():
    st.subheader(f"Gráfico Principal")

    if grafico_principal == "Área":
        st.area_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Linha":
        st.line_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Barra":
        st.bar_chart(top_n_data, use_container_width=True)


# %%

df_contagem_02 = pd.read_csv('contagem_termos_bacte.csv')


# ----- CONTEÚDO PRINCIPAL -----
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

# Container: gráfico principal
with st.container():
    st.subheader(f"Gráfico Principal")

    if grafico_principal == "Área":
        st.area_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Linha":
        st.line_chart(top_n_data, use_container_width=True)
    elif grafico_principal == "Barra":
        st.bar_chart(top_n_data, use_container_width=True)


df_countsN = df_countsN.head(top_n).set_index('Termo Agrupado')
df_countsP = df_countsP.head(top_n).set_index('Termo Agrupado')


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

# Ajustes

df_cont_bacte = pd.read_csv('contagem_fam_bio_bacte_gram.csv')
df_cont_fam01 = pd.read_csv('contagem_fam_bio_NER.csv')
df_cont_fam02 = pd.read_csv('contagem_fam_bio_textgen.csv')

df_cont_fam01 = df_cont_fam01[df_cont_fam01['family'].notna()]
df_cont_fam02 = df_cont_fam02[df_cont_fam02['family2'].notna()]

# Somar somente as colunas numéricas (os compostos)
df_cont_fam01['total_compostos'] = df_cont_fam01.select_dtypes(
    include='number').sum(axis=1)
df_cont_fam02['total_compostos'] = df_cont_fam02.select_dtypes(
    include='number').sum(axis=1)
df_cont_bacte['total_compostos'] = df_cont_bacte.select_dtypes(
    include='number').sum(axis=1)

# Remover a coluna 'noise' se existir
df_cont_fam01 = df_cont_fam01.drop(columns=['noise'])
df_cont_fam02 = df_cont_fam02.drop(columns=['noise'])
df_cont_bacte = df_cont_bacte.drop(columns=['noise'])


df_cont_fam01 = df_cont_fam01.drop(columns=['Unnamed: 12'])

df_cont_fam01 = df_cont_fam01.sort_values(
    by='total_compostos', ascending=False)
df_cont_fam02 = df_cont_fam02.sort_values(
    by='total_compostos', ascending=False)
df_cont_bacte = df_cont_bacte.sort_values(
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
    title='Heatmap Interativo dos Compostos NER Model',
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
df_heat = df_cont_fam02.set_index('family2')
df_heat = df_heat.select_dtypes(include='number')  # Apenas dados numéricos

# Seleção interativa de quantidade de compostos

# Seleciona as top_n colunas (compostos) com base na soma total
top_columns = df_heat.sum().sort_values(ascending=False).head(top_n).index
df_filtered = df_heat[top_columns]
# Criação do heatmap com Plotly fam_02

zmin = df_filtered.values.min()
zmax = np.percentile(df_filtered.values, 95)

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
    title='Heatmap Interativo dos Compostos TEXT_GEN Model',
    xaxis_nticks=top_n,
    yaxis_nticks=top_n,
    height=1000

)

# Exibe o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)

with st.container():

    st.title("📊 Compostos Bioativos e familias")

    # Exibe a tabela
    st.dataframe(df_cont_fam02)
    # Botão de download
    st.download_button(
        label="⬇️ Baixar planilha CSV",
        data=df_cont_fam02.to_csv(index=False).encode('utf-8'),
        file_name='compostos_bioativos_familiasTEXT_GEN Model.csv',
        mime='text/csv',
    )
# _______________________________________________________________________________________
# Supondo que você já tenha o DataFrame df_cont_fam01
df_heat = df_cont_bacte.set_index(['Bacteria', 'gram'])
df_heat = df_heat.select_dtypes(include='number')  # Apenas dados numéricos

# Seleção interativa de quantidade de compostos

# Seleciona as top_n colunas (compostos) com base na soma total
top_columns = df_heat.sum().sort_values(ascending=False).head(top_n).index
df_filtered = df_heat[top_columns]
# Criação do heatmap com Plotly fam_02
zmin = df_filtered.values.min()
zmax = np.percentile(df_filtered.values, 95)

sort_option = st.selectbox(
    "Ordenar bactérias por:",
    options=["Total de compostos",
             "Gram positivo primeiro", "Gram negativo primeiro"]
)

# Lógica para ordenar
if sort_option == "Total de compostos":
    df_filtered = df_filtered.loc[df_filtered.sum(
        axis=1).sort_values(ascending=False).index]
elif sort_option == "Gram positivo primeiro":
    df_filtered = df_filtered.sort_index(level='gram', ascending=False)
elif sort_option == "Gram negativo primeiro":
    df_filtered = df_filtered.sort_index(level='gram', ascending=True)

# Criação do heatmap com Plotly fam01
fig = go.Figure(data=go.Heatmap(
    z=df_filtered.values,
    x=df_filtered.columns,
    y=[f'{idx[0]} ({idx[1]})' for idx in df_filtered.index],
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
        file_name='compostos_bioativos_familias.csv',
        mime='text/csv',
    )

# cd "C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit"
# streamlit run Streamlit.py

# %%

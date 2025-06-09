# %% importando bibliotecas
import pandas as pd

# %
agrupamento = {
    # variações de phenolics

    "phenolic": "phenolics",
    "polyphenols": "phenolics",
    "phenol": "phenolics",
    "phenols": "phenolics",
    "polyphenolic": "phenolics",
    "polyphenol": "phenolics",
    "polyphenolics": "phenolics",

    # variações de flavonoids

    "flavonoid": "flavonoids",
    "anthocyanins": "flavonoids",
    "hydroxyflavones": "flavonoids",
    "hydroxyflavone": "flavonoids",
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

    # variações de isolated compounds
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
    "capsaicinoids": "isolated compounds",
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
    "Essential Oil": "noise",

    "cardiotonic glycosides": "noise",
    "piperamide": "noise",

}

len(agrupamento)
# %% lendo arquivo

df_species = pd.read_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\Saidas_Banco\df_bert_bio_bac_gram_01_fam_TGEN02.csv')


def substituir_bioativos(texto):
    if pd.isna(texto):
        return texto
    compostos = [x.strip() for x in texto.split(',')]
    compostos_substituidos = [agrupamento.get(x, x) for x in compostos]
    return ', '.join(compostos_substituidos)


df_species["bioactives"] = df_species["bioactives"].apply(substituir_bioativos)
len(df_species['bioactives'].unique())
# %% aplicando filtro
# Máscaras: queremos linhas onde family e family2 possuem dados "úteis"
mask_fam2 = df_species['family2'].notna(
) & ~df_species['family2'].str.fullmatch(r'[,\s]*', na=False)
mask_fam = df_species['family'].notna(
) & ~df_species['family'].str.fullmatch(r'[,\s]*', na=False)

# Aplicar filtro
filtered_df = df_species[['family', 'bioactives']][mask_fam2 | mask_fam]
filtered_df.fillna('', inplace=True)
filtered_df01 = df_species[['family2', 'bioactives']][mask_fam2 | mask_fam]
filtered_df01.fillna('')
filtered_df02 = df_species[['Bacteria', 'gram',
                            'bioactives']][mask_fam2 | mask_fam]
filtered_df01.fillna('')
# %%ver lista de bioativos
pd.DataFrame(filtered_df['bioactives'].dropna()
             .str.split(',')
             .explode()
             .str.strip()
             .unique())


# %%
k = filtered_df['bioactives'].dropna().str.split(
    ',').explode().str.strip().unique()

df = pd.DataFrame(columns=k)
df.insert(0, 'family', '')

for _, linha in filtered_df.iterrows():
    if pd.notna(linha['family']) and pd.notna(linha['bioactives']):
        familias = [f.strip() for f in linha['family'].split(',')]
        bioativos = [b.strip() for b in linha['bioactives'].split(',')]

        for fam in familias:
            if fam not in df['family'].values:
                nova_linha = dict.fromkeys(df.columns, 0)
                nova_linha['family'] = fam
                df = pd.concat([df, pd.DataFrame([nova_linha])],
                               ignore_index=True)
            for bio in bioativos:
                if bio in df.columns:
                    df.loc[df['family'] == fam, bio] += 1

df.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit\contagem_fam_bio_NER.csv', index=False)

# %%

k = filtered_df01['bioactives'].dropna().str.split(
    ',').explode().str.strip().unique()

df01 = pd.DataFrame(columns=k)
df01.insert(0, 'family2', '')

for _, linha in filtered_df01.iterrows():
    if pd.notna(linha['family2']) and pd.notna(linha['bioactives']):
        familias = [f.strip() for f in linha['family2'].split(',')]
        bioativos = [b.strip() for b in linha['bioactives'].split(',')]

        for fam in familias:
            if fam not in df01['family2'].values:
                nova_linha = dict.fromkeys(df01.columns, 0)
                nova_linha['family2'] = fam
                df01 = pd.concat([df01, pd.DataFrame([nova_linha])],
                                 ignore_index=True)
            for bio in bioativos:
                if bio in df01.columns:
                    df01.loc[df01['family2'] == fam, bio] += 1

df01.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit\contagem_fam_bio_textgen.csv', index=False)
# %%

k = filtered_df02['bioactives'].dropna().str.split(
    ',').explode().str.strip().unique()

df02 = pd.DataFrame(columns=k)
df02.insert(0, 'Bacteria', '')
df02.insert(1, 'gram', '')

for _, linha in filtered_df02.iterrows():
    if pd.notna(linha['Bacteria']) and pd.notna(linha['bioactives']) and pd.notna(linha['gram']):
        bacterias = [b.strip() for b in linha['Bacteria'].split(',')]
        bioativos = [b.strip() for b in linha['bioactives'].split(',')]
        gramas = [g.strip() for g in linha['gram'].split(',')]

        for bact, gram in zip(bacterias, gramas):
            if bact not in df02['Bacteria'].values:
                nova_linha = dict.fromkeys(df02.columns, 0)
                nova_linha['Bacteria'] = bact
                nova_linha['gram'] = gram
                df02 = pd.concat(
                    [df02, pd.DataFrame([nova_linha])], ignore_index=True)
            for bio in bioativos:
                if bio in df02.columns:
                    df02.loc[df02['Bacteria'] == bact, bio] += 1

df02.to_csv(
    r'C:\Users\Andrey\Desktop\Artigo_Maio\StreamLit\contagem_fam_bio_bacte_gram.csv', index=False)
# %%

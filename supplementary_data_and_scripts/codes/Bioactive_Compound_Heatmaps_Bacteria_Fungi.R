# ==========================================================================
# Supplementary Script – Bioactive Compound Heatmaps for Bacteria and Fungi
# Contact: Carlos Carollo – carlos.carollo@ufms.br
# Purpose: Generate heatmaps of the relative abundance of major bioactive compound
# classes found in plant extracts tested against the most studied bacteria and fungi.
# Requirements: R (>=4.0), packages: tidyverse, ComplexHeatmap, circlize
# ==========================================================================

# ===========================
# 1. LOAD REQUIRED PACKAGES
# ===========================
# Uncomment installation lines below if needed:
# install.packages("BiocManager")
# BiocManager::install("ComplexHeatmap")
# install.packages("circlize")
library(tidyverse)
library(ComplexHeatmap)
library(circlize)

# ===========================
# 2. HEATMAP: BACTERIA
# ===========================

# --- Load bacteria data ---
bacteria_data <- read_csv("compounds_by_family_bacteria.csv")  # <-- Set your path

# Select columns with compound counts (excluding metadata)
compound_cols_bact <- setdiff(names(bacteria_data), c("bacteria", "gram", "isolated compounds", "total_compostos"))

# Select top 20 bacteria by total compound reports
bact_top <- bacteria_data %>%
  mutate(total = rowSums(select(., all_of(compound_cols_bact)), na.rm = TRUE)) %>%
  arrange(desc(total)) %>%
  slice_head(n = 20)

# For each bacterium, select top 10 most represented compounds
top10_compounds_per_bact <- apply(bact_top[, compound_cols_bact], 1, function(x) {
  names(sort(x, decreasing = TRUE))[1:10]
})
compounds_bact_top10 <- unique(as.character(unlist(top10_compounds_per_bact)))

# Filter dataset to only top 10 compounds per bacterium
bact_filtered <- bact_top %>%
  select(bacteria, gram, all_of(compounds_bact_top10)) %>%
  mutate(bacteria = make.unique(bacteria))

# Normalize values by row (relative %)
bact_numeric <- bact_filtered %>% select(-bacteria, -gram)
bact_norm <- as.data.frame(bact_numeric / rowSums(bact_numeric) * 100)
rownames(bact_norm) <- bact_filtered$bacteria

# Compound biosynthetic classification
compound_groups <- list(
  "Shikimate/Polyketide" = c("phenylpropanoids", "coumarins", "flavonoids", "tannins", "stilbenoids",
                             "lignans", "xanthones", "anthraquinones", "phenylethanoids"),
  "Terpenoids" = c("monoterpenes", "sesquiterpenes", "diterpenes", "triterpenoids", "steroids",
                   "carotenes", "iridoids", "saponins", "terpenoids"),
  "Nitrogen-containing" = c("alkaloids", "piperamides", "alkamides", "cyanogenic glycosides")
)
compound_origin_bact <- rep(NA, length(compounds_bact_top10))
names(compound_origin_bact) <- compounds_bact_top10
for (group in names(compound_groups)) {
  hits <- intersect(compounds_bact_top10, compound_groups[[group]])
  compound_origin_bact[hits] <- group
}
compound_origin_bact <- compound_origin_bact[!is.na(compound_origin_bact)]
compound_origin_bact <- sort(compound_origin_bact)
bact_mat <- bact_norm[, names(compound_origin_bact)]
bact_mat <- bact_mat[, names(compound_origin_bact)]

# Sort bacteria by Gram type and alphabetical order
bact_row_annot <- data.frame(Gram = bact_filtered$gram)
rownames(bact_row_annot) <- bact_filtered$bacteria
bact_row_annot <- bact_row_annot[order(bact_row_annot$Gram, rownames(bact_row_annot)), , drop = FALSE]
bact_mat <- bact_mat[rownames(bact_row_annot), ]

# Column annotation (compound origin)
ha_col_bact <- HeatmapAnnotation(
  Origin = compound_origin_bact,
  col = list(
    Origin = c(
      "Shikimate/Polyketide" = "#4E79A7",
      "Terpenoids" = "#F28E2B",
      "Nitrogen-containing" = "#59A14F"
    )
  ),
  annotation_name_side = "left"
)
# Row annotation (Gram type)
ha_row_bact <- rowAnnotation(
  Gram = bact_row_annot$Gram,
  col = list(
    Gram = c("positive" = "#65839B", "negative" = "#AE2E2C")
  ),
  annotation_name_side = "top"
)

# --- Plot heatmap (bacteria) ---
pdf("heatmap_bacteria.pdf", width = 10, height = 8)
Heatmap(
  as.matrix(bact_mat),
  name = "Relative (%)",
  top_annotation = ha_col_bact,
  left_annotation = ha_row_bact,
  col = colorRamp2(c(0, max(bact_mat)), c("white", "red4")),
  cluster_rows = FALSE,
  cluster_columns = FALSE,
  row_names_gp = gpar(fontsize = 8),
  column_names_gp = gpar(fontsize = 9),
  heatmap_legend_param = list(title = "Bioactive Compounds")
)
dev.off()

# ===========================
# 3. HEATMAP: FUNGI
# ===========================

# --- Load fungi data ---
fungi_data <- read_csv("compounds_by_family_fungi.csv")  # <-- Set your path

# Select columns with compound counts (excluding metadata)
compound_cols_fungi <- setdiff(names(fungi_data), c("FUNG", "total_compostos"))

# Select top 20 fungi by total compound reports
fungi_top <- fungi_data %>%
  mutate(total = rowSums(select(., all_of(compound_cols_fungi)), na.rm = TRUE)) %>%
  arrange(desc(total)) %>%
  slice_head(n = 20)

# For each fungus, select top 10 most represented compounds
top10_compounds_per_fungus <- apply(fungi_top[, compound_cols_fungi], 1, function(x) {
  names(sort(x, decreasing = TRUE))[1:10]
})
compounds_fungi_top10 <- unique(as.character(unlist(top10_compounds_per_fungus)))

# Filter dataset to only top 10 compounds per fungus
fungi_filtered <- fungi_top %>%
  select(FUNG, all_of(compounds_fungi_top10))

# Normalize values by row (relative %)
fungi_numeric <- fungi_filtered %>% select(-FUNG)
fungi_norm <- as.data.frame(fungi_numeric / rowSums(fungi_numeric) * 100)
rownames(fungi_norm) <- fungi_filtered$FUNG

# Compound biosynthetic classification
compound_origin_fungi <- rep(NA, length(compounds_fungi_top10))
names(compound_origin_fungi) <- compounds_fungi_top10
for (group in names(compound_groups)) {
  hits <- intersect(compounds_fungi_top10, compound_groups[[group]])
  compound_origin_fungi[hits] <- group
}
compound_origin_fungi <- compound_origin_fungi[!is.na(compound_origin_fungi)]
compound_origin_fungi <- sort(compound_origin_fungi)
fungi_mat <- fungi_norm[, names(compound_origin_fungi)]
fungi_mat <- fungi_mat[, names(compound_origin_fungi)]

# No Gram annotation for fungi, alphabetical order
fungi_mat <- fungi_mat[order(rownames(fungi_mat)), ]

# Column annotation (compound origin)
ha_col_fungi <- HeatmapAnnotation(
  Origin = compound_origin_fungi,
  col = list(
    Origin = c(
      "Shikimate/Polyketide" = "#4E79A7",
      "Terpenoids" = "#F28E2B",
      "Nitrogen-containing" = "#59A14F"
    )
  ),
  annotation_name_side = "left"
)

# --- Plot heatmap (fungi) ---
pdf("heatmap_fungi.pdf", width = 10, height = 8)
Heatmap(
  as.matrix(fungi_mat),
  name = "Relative (%)",
  top_annotation = ha_col_fungi,
  col = colorRamp2(c(0, max(fungi_mat)), c("white", "red4")),
  cluster_rows = FALSE,
  cluster_columns = FALSE,
  row_names_gp = gpar(fontsize = 8),
  column_names_gp = gpar(fontsize = 9),
  heatmap_legend_param = list(title = "Bioactive Compounds")
)
dev.off()

# ==========================================================================
# End of script
# ==========================================================================

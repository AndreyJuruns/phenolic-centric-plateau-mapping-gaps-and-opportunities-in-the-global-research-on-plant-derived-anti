# =======================================================================
# Supplementary Script – Phylogenetic Heatmap of Compound Classes by Family
# Contact: Carlos Carollo – carlos.carollo@ufms.br
# Purpose: To generate a circular phylogenetic tree with a heatmap
# showing the relative abundance of major compound classes in the 50
# most represented plant families of the dataset.
# Requirements: R (>=4.0), packages: ggtree, dplyr, tidyr, readr, purrr,
# tibble, ape, V.PhyloMaker2
# =======================================================================

# =============================
# LOAD PACKAGES
# =============================
library(ggtree)
library(dplyr)
library(tidyr)
library(readr)
library(purrr)
library(tibble)
library(ape)
library(V.PhyloMaker2)

# =============================
# 1. LOAD DATA
# =============================

# Path to CSV with family/compound class counts
compound_df <- read_csv("compounds_by_family.csv")
# Path to species list
species_list <- read_csv2("families_list_min5.csv")

# Standardize species names (use underscores as in the phylogeny)
species_list$species <- gsub(" ", "_", species_list$species)

# =============================
# 2. LOAD AND RUN V.PhyloMaker2
# =============================
data("GBOTB.extended.TPL")
data("nodes.info.1.TPL")

phylo_result <- phylo.maker(
  sp.list = species_list,
  tree = GBOTB.extended.TPL,
  nodes = nodes.info.1.TPL,
  scenarios = "S3"
)

# =============================
# 3. FILTER THE 50 MOST REPRESENTED FAMILIES
# =============================

top_families <- compound_df %>%
  arrange(desc(total_compounds)) %>%
  slice(1:50)

# Long format (exclude 'total' and 'isolated')
compound_long <- top_families %>%
  pivot_longer(cols = -c(family, total_compounds),
               names_to = "compound_class", values_to = "count") %>%
  filter(!compound_class %in% c("total_compounds", "isolated_compounds"))

# Select the four most frequent compound classes for each family
top_classes <- compound_long %>%
  group_by(family) %>%
  slice_max(order_by = count, n = 4) %>%
  ungroup()

# Wide format for heatmap, remove unnecessary columns
heatmap_data <- top_classes %>%
  pivot_wider(names_from = compound_class, values_from = count, values_fill = 0) %>%
  select(-any_of(c("total_compounds", "isolated_compounds")))

# =============================
# 4. BUILD FAMILY-LEVEL PHYLOGENY
# =============================

# Choose a representative species per family (matching species in tree)
tip_map <- species_list %>%
  filter(species %in% phylo_result$scenario.3$tip.label,
         family %in% heatmap_data$family) %>%
  distinct(family, .keep_all = TRUE)

# Reduce tree to one tip per family
family_tree <- drop.tip(
  phylo_result$scenario.3,
  setdiff(phylo_result$scenario.3$tip.label, tip_map$species)
)

# Replace tip labels with family names
family_tree$tip.label <- tip_map$family[match(family_tree$tip.label, tip_map$species)]

# =============================
# 5. PREPARE HEATMAP MATRIX (PERCENTAGE)
# =============================

# Match order of heatmap rows to tree tip labels
heatmap_data <- as.data.frame(heatmap_data)
rownames(heatmap_data) <- heatmap_data$family
heatmap_data <- heatmap_data[family_tree$tip.label, ]
heatmap_data$family <- NULL  # remove redundant column, if present

# Convert counts to percentages per family
heatmap_percent <- heatmap_data / rowSums(heatmap_data) * 100

# Order columns (compound classes) by overall abundance (inner: rare, outer: common)
col_sums <- colSums(heatmap_percent)
heatmap_percent <- heatmap_percent[, order(col_sums)]

# =============================
# 6. PLOT CIRCULAR TREE + HEATMAP
# =============================

p_circular <- ggtree(family_tree, layout = "circular", size = 0.1) +
  geom_tiplab2(aes(angle = angle), hjust = 0, size = 3.5) +
  theme_void()

g_circular <- gheatmap(
  p_circular,
  heatmap_percent,
  offset = 80,
  width = 1,
  colnames_angle = 90,
  colnames_position = "top",
  font.size = 3.0
) +
  scale_fill_gradient(low = "white", high = "blue", name = "%")

# Display the plot
print(g_circular)

# =============================
# 7. SAVE FINAL FIGURE
# =============================
ggsave("phylogenetic_heatmap_compounds.pdf", plot = g_circular, width = 11, height = 11)
ggsave("phylogenetic_heatmap_compounds.png", plot = g_circular, width = 14, height = 14, dpi = 600)

# =======================================================================
# End of script
# =======================================================================

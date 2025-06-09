# ========================================================================
# Supplementary Script – Phylogenetic Tree of Plant Families
# Contact: Carlos Carollo – carlos.carollo@ufms.br
# Purpose: Build and visualize a circular phylogenetic tree with family labels
# Requirements: R (>=4.0), packages: V.PhyloMaker2, ggtree, tidytree, dplyr, purrr, ape, readr, ggplot2
# ========================================================================

# ===============================
# LOAD PACKAGES
# ===============================
library(V.PhyloMaker2)
library(ggtree)
library(tidytree)
library(dplyr)
library(purrr)
library(ape)
library(readr)
library(ggplot2)

# ===============================
# 1. LOAD SPECIES LIST
# ===============================
# Replace with your correct path:
sp_list <- read_csv2("families_list_min5.csv")
sp_list$species <- gsub(" ", "_", sp_list$species)  # Standardize format

# ===============================
# 2. LOAD V.PhyloMaker2 DATA
# ===============================
data("GBOTB.extended.TPL")
data("nodes.info.1.TPL")

# ===============================
# 3. GENERATE PHYLOGENY
# ===============================
result <- phylo.maker(
  sp.list = sp_list,
  tree = GBOTB.extended.TPL,
  nodes = nodes.info.1.TPL,
  scenarios = "S3"
)
phylo_tree <- result$scenario.3

# ===============================
# 4. FILTER VALID SPECIES
# ===============================
sp_valid <- sp_list %>%
  filter(species %in% phylo_tree$tip.label)

# ===============================
# 5. GET MRCA (MOST RECENT COMMON ANCESTOR) OF EACH FAMILY
# ===============================
family_nodes <- sp_valid %>%
  group_by(family) %>%
  filter(n() >= 2) %>%
  group_split() %>%
  map_dfr(function(df) {
    mrca <- getMRCA(phylo_tree, df$species)
    if (!is.null(mrca) && mrca %in% phylo_tree$edge[,1]) {
      tibble(family = unique(df$family), mrca = mrca)
    }
  })

# ===============================
# 6. CALCULATE FAMILY ABUNDANCE AND LABELS
# ===============================
family_percent <- sp_valid %>%
  group_by(family) %>%
  summarise(n = n()) %>%
  mutate(percent = round(100 * n / sum(n), 1))

family_nodes <- left_join(family_nodes, family_percent, by = "family")
family_nodes$label <- paste0(family_nodes$family, " (", family_nodes$percent, "%)")

# ===============================
# 7. PLOT CIRCULAR PHYLOGENY WITH FAMILY LABELS
# ===============================
p <- ggtree(phylo_tree, layout = "circular") +
  theme_void()

for (i in seq_len(nrow(family_nodes))) {
  p <- p + geom_cladelabel(
    node = family_nodes$mrca[i],
    label = family_nodes$label[i],
    offset = 1,
    barsize = 0,
    fontsize = 3,
    angle = "auto",
    color = "blue"
  )
}

print(p)

# ===============================
# 8. EXPORT FIGURE
# ===============================
ggsave("tree_families.png", plot = p, width = 18, height = 18, dpi = 600)
ggsave("tree_families.pdf", plot = p, width = 18, height = 18)

# ========================================================================
# End of script
# ========================================================================

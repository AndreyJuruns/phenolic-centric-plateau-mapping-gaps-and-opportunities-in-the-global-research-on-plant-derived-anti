# =======================================================================
# Supplementary Script – Taxonomic Coverage Heatmap (Top Families)
# Contact: Carlos Carollo – carlos.carollo@ufms.br
# Purpose: Calculate and visualize the proportion of studied species for
# the most studied plant families, based on the WFO taxonomic backbone.
# Requirements: R (>=4.0), packages: readr, dplyr, ggplot2, scales
# =======================================================================

# =============================
# LOAD PACKAGES
# =============================
library(readr)
library(dplyr)
library(ggplot2)
library(scales)

# =============================
# 1. LOAD AND PREPARE DATA
# =============================

# Path to input files
survey_path <- "species_per_family.csv"            # Results from your species list
wfo_path    <- "classification.csv"                # WFO taxonomic backbone

# Load family species counts from your survey
survey <- read_csv(survey_path)
# Load WFO classification data
wfo_data <- read_tsv(wfo_path)

# Standardize column names
names(survey)   <- tolower(trimws(names(survey)))
names(wfo_data) <- tolower(trimws(names(wfo_data)))

# Count total number of accepted species per family in WFO
wfo_family_counts <- wfo_data %>%
  filter(taxonrank == "species", !is.na(family)) %>%
  count(family, name = "n_species")

# Merge with your survey data
data <- left_join(survey, wfo_family_counts, by = "family") %>%
  rename(studied = species_count, total = n_species) %>%
  mutate(proportion = studied / total) %>%
  filter(!is.na(proportion), total > 0)

# =============================
# 2. SELECT TOP 40 FAMILIES (BY ABSOLUTE STUDIED COUNT)
# =============================
top_families <- data %>%
  arrange(desc(studied)) %>%
  slice(1:40)

# Highlight top 10 and bottom 10 families by proportional coverage
top_families <- top_families %>%
  mutate(
    highlight = case_when(
      proportion %in% sort(proportion, decreasing = TRUE)[1:10] ~ " ↑",
      proportion %in% sort(proportion, decreasing = FALSE)[1:10] ~ " ↓",
      TRUE ~ ""
    ),
    label = paste0(family, highlight),
    label = factor(label, levels = rev(label))
  )

# =============================
# 3. PLOT TAXONOMIC COVERAGE HEATMAP
# =============================
p <- ggplot(top_families, aes(x = "Proportion studied", y = label, fill = proportion)) +
  geom_tile(color = "white", height = 0.8) +
  scale_fill_gradient2(
    low = "#2c7bb6", mid = "white", high = "#d7191c",
    midpoint = median(top_families$proportion, na.rm = TRUE),
    labels = percent_format(accuracy = 1),
    name = "Studied species (%)"
  ) +
  labs(
    title = "Top 40 Most Studied Families",
    subtitle = "↑ Top 10 Highest | ↓ Bottom 10 Lowest\nColor intensity indicates the proportion of studied species within each family.",
    x = NULL,
    y = "Family"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    axis.text.y = element_text(size = 10, margin = margin(r = 4)),
    plot.title = element_text(face = "bold", size = 14),
    plot.subtitle = element_text(size = 10, margin = margin(b = 10)),
    legend.position = "right"
  )

# =============================
# 4. SAVE FIGURE
# =============================
ggsave(
  filename = "heatmap_taxonomic_coverage.png",
  plot = p,
  width = 9, height = 18, units = "cm", dpi = 600
)

ggsave(
  filename = "heatmap_taxonomic_coverage.pdf",
  plot = p,
  width = 9, height = 18, units = "cm", device = cairo_pdf
)

# =======================================================================
# End of script
# =======================================================================

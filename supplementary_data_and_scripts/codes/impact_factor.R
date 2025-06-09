# =====================================================================
# Supplementary Script - Journal Impact Factor (JIF) Matching and Binning
# Contact: Carlos Carollo – carlos.carollo@ufms.br
# Purpose: Match article journals to JIF, bin results, and summarize
# Requirements: R (>=4.0), packages: readxl, dplyr, stringr, fuzzyjoin, writexl, stringdist
# =====================================================================

# Load required packages
library(readxl)
library(dplyr)
library(stringr)
library(fuzzyjoin)
library(writexl)
library(stringdist)

# --- 1. Read and clean JCR Impact Factor list ---
jcr <- read_excel("2023impactfactor-only.xlsx") %>%
  rename(Impact_Factor = `2022 JIF`) %>%
  mutate(journal_clean = str_to_lower(str_trim(`Journal name`)))

# --- 2. Read and clean user journal list ---
my_journals <- read_excel("minhas_revistas.xlsx", col_names = FALSE) %>%
  rename(Journal = ...1) %>%
  mutate(journal_clean = str_to_lower(str_trim(Journal)))

# --- 3. Fuzzy join: Match journals using Jaro-Winkler distance ---
matched_table <- stringdist_inner_join(
  my_journals, jcr,
  by = "journal_clean",
  method = "jw", max_dist = 0.15,
  distance_col = "dist"
)

# --- 4. Retain best match per user journal ---
best_match <- matched_table %>%
  group_by(Journal) %>%
  slice_min(order_by = dist, n = 1, with_ties = FALSE) %>%
  ungroup() %>%
  select(User_Journal = Journal,
         JCR_Journal = `Journal name`,
         Impact_Factor)

# --- 5. Export result for later use or visualization ---
write_xlsx(best_match, "matched_journals_jif.xlsx")

# --- 6. (Optional) Bin JIFs for visualization (not shown here) ---
# You may bin the Impact_Factor column and plot as in Figure X.
# Example binning (for future extension):
# best_match <- best_match %>%
#   mutate(JIF_bin = case_when(
#     is.na(Impact_Factor) ~ "No JIF",
#     Impact_Factor < 1 ~ "JIF <1",
#     Impact_Factor < 2 ~ "JIF 1–2",
#     Impact_Factor < 3 ~ "JIF 2–3",
#     Impact_Factor < 4 ~ "JIF 3–4",
#     Impact_Factor < 5 ~ "JIF 4–5",
#     Impact_Factor < 6 ~ "JIF 5–6",
#     Impact_Factor < 7 ~ "JIF 6–7",
#     Impact_Factor < 8 ~ "JIF 7–8",
#     Impact_Factor < 9 ~ "JIF 8–9",
#     Impact_Factor < 10 ~ "JIF 9–10",
#     Impact_Factor >= 10 ~ "JIF >10"
#   ))

# =====================================================================
# End of script
# =====================================================================

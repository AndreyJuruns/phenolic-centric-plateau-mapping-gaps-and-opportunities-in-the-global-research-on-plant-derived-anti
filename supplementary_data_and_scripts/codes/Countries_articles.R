# ================== INSTALL AND LOAD PACKAGES ==================
# (Run installation only once)
# install.packages(c("readr", "dplyr", "wbstats", "countrycode", "stringr", "readxl", "ggplot2", "writexl", "rnaturalearth", "sf", "forcats"))
library(readr)
library(dplyr)
library(wbstats)
library(countrycode)
library(stringr)
library(readxl)
library(ggplot2)
library(writexl)
library(rnaturalearth)
library(sf)
library(forcats)

# ================== DATA PROCESSING ==================

# 1. Read table of article counts by country
article_counts <- read_csv("G:/Meu Drive/ARTIGOS/2025/Micro_research/contagemPaís.csv")
colnames(article_counts) <- c("country", "n_articles")

# 2. Standardize country names and add ISO3 codes
article_counts$country <- str_to_title(article_counts$country)
article_counts$iso3c <- countrycode(article_counts$country, origin = "country.name", destination = "iso3c")

# 3. Retrieve World Bank metadata (income group, region)
wb_meta <- wb_countries() %>%
  select(iso3c, country, income_group = income_level, region)

# 4. Get most recent R&D investment (% GDP) from the last 20 years
year_end <- as.numeric(format(Sys.Date(), "%Y"))
year_start <- year_end - 19
rd_data <- wb(
  indicator = "GB.XPD.RSDV.GD.ZS",
  country = unique(article_counts$iso3c),
  startdate = year_start,
  enddate = year_end
)
rd_latest <- rd_data %>%
  filter(!is.na(value)) %>%
  group_by(iso3c) %>%
  arrange(desc(date)) %>%
  slice(1) %>%
  ungroup() %>%
  select(iso3c, rd_pct_gdp = value)

# 5. Merge all datasets
main_data <- article_counts %>%
  left_join(wb_meta, by = "iso3c") %>%
  left_join(rd_latest, by = "iso3c")

# 6. Table: Distribution by income group
income_table <- main_data %>%
  group_by(income_group) %>%
  summarise(
    articles = sum(n_articles, na.rm = TRUE),
    prop_articles = round(100 * articles / sum(main_data$n_articles, na.rm = TRUE), 1)
  ) %>%
  arrange(desc(articles))
write_xlsx(income_table, "C:/Users/carlo/OneDrive/Documents/table_income_group.xlsx")

# 7. Classify countries by R&D investment terciles
main_data_rd <- main_data %>% filter(!is.na(rd_pct_gdp))
breaks <- quantile(main_data_rd$rd_pct_gdp, probs = c(0, 1/3, 2/3, 1), na.rm = TRUE)
main_data <- main_data %>%
  mutate(
    rd_class = case_when(
      is.na(rd_pct_gdp) ~ "No data",
      rd_pct_gdp <= breaks[2] ~ "Low R&D",
      rd_pct_gdp <= breaks[3] ~ "Medium R&D",
      rd_pct_gdp > breaks[3] ~ "High R&D"
    )
  )
rd_table <- main_data %>%
  group_by(rd_class) %>%
  summarise(
    articles = sum(n_articles, na.rm = TRUE),
    prop_articles = round(100 * articles / sum(main_data$n_articles, na.rm = TRUE), 1)
  ) %>%
  arrange(desc(articles))
write_xlsx(rd_table, "C:/Users/carlo/OneDrive/Documents/table_rd_class.xlsx")

# Save merged data for reproducibility
write_xlsx(main_data, "C:/Users/carlo/OneDrive/Documents/data_merged.xlsx")

# 8. Print summary for manuscript (update values after run)
cat(sprintf(
  "Of the %d articles analyzed, %.1f%% were produced in countries classified as 'Low income' or 'Lower middle income' by the World Bank, while %.1f%% came from countries in the lowest tercile of R&D investment (%%GDP).",
  sum(main_data$n_articles),
  sum(income_table$prop_articles[income_table$income_group %in% c("Low income", "Lower middle income")]),
  rd_table$prop_articles[rd_table$rd_class == "Low R&D"]
))

# ================== FIGURE GENERATION ==================

# 1. Barplot: Sample vs. global (UNESCO) income group distribution
income_table$group <- "Sample"
global_table <- data.frame(
  income_group = c("Low income", "Lower middle income", "Upper middle income", "High income"),
  prop_articles = c(0.5, 7, 23, 69),  # UNESCO Science Report 2021
  group = "Global"
)
plot_table <- bind_rows(
  income_table %>% select(income_group, prop_articles, group),
  global_table
)
# Set explicit order for income groups
plot_table$income_group <- fct_relevel(
  plot_table$income_group,
  "High income", "Upper middle income", "Lower middle income", "Low income", "Not classified", "NA"
)
# Bar plot
p_bar <- ggplot(plot_table, aes(x = income_group, y = prop_articles, fill = group)) +
  geom_bar(stat = "identity", position = "dodge") +
  geom_text(aes(label = paste0(round(prop_articles,1),"%")),
            position = position_dodge(width = 0.9), vjust = -0.2, size = 3.5) +
  labs(
    title = "Distribution of articles by income group: Sample vs. Global",
    y = "% of articles",
    x = "World Bank income group",
    fill = ""
  ) +
  scale_fill_manual(values = c("Global" = "grey50", "Sample" = "#0072B2")) +
  theme_minimal(base_size = 14)
ggsave("C:/Users/carlo/OneDrive/Documents/figure_bars_global_vs_sample.png", plot = p_bar, width = 8, height = 5, dpi = 300)

# 2. World map of articles by country
world <- ne_countries(scale = "medium", returnclass = "sf")
main_data$iso3c <- toupper(main_data$iso3c)
world_data <- left_join(world, main_data, by = c("iso_a3" = "iso3c"))
p_map <- ggplot(world_data) +
  geom_sf(aes(fill = n_articles), color = "grey80", size = 0.1) +
  scale_fill_viridis_c(option = "plasma", na.value = "grey95", trans = "sqrt") +
  theme_void() +
  labs(fill = "Articles", title = "Global distribution of articles by country")
ggsave("C:/Users/carlo/OneDrive/Documents/figure_map_articles.png", plot = p_map, width = 10, height = 6, dpi = 300)

# 3. Barplot: Articles by R&D investment class (absolute)
p_rd <- ggplot(rd_table, aes(x = rd_class, y = articles, fill = rd_class)) +
  geom_bar(stat = "identity") +
  labs(x = "R&D investment class", y = "Number of articles",
       title = "Articles by R&D investment (terciles)") +
  theme_minimal(base_size = 14) +
  theme(legend.position = "none")
ggsave("C:/Users/carlo/OneDrive/Documents/figure_bar_rd_absolute.png", plot = p_rd, width = 7, height = 5, dpi = 300)

# 4. Barplot: Articles by R&D investment class (proportional)
p_rd_prop <- ggplot(rd_table, aes(x = rd_class, y = prop_articles, fill = rd_class)) +
  geom_bar(stat = "identity") +
  labs(x = "R&D investment class", y = "% of articles",
       title = "Proportion of articles by R&D investment (terciles)") +
  theme_minimal(base_size = 14) +
  theme(legend.position = "none")
ggsave("C:/Users/carlo/OneDrive/Documents/figure_bar_rd_prop.png", plot = p_rd_prop, width = 7, height = 5, dpi = 300)

# Print plots in RStudio viewer
print(p_bar)      # Sample vs. Global barplot
print(p_map)      # World map of articles
print(p_rd)       # R&D (absolute) barplot
print(p_rd_prop)  # R&D (proportional) barplot

# ================== TOP 10 COUNTRIES BY ARTICLE COUNT ==================

top10 <- article_counts %>%
  arrange(desc(n_articles)) %>%
  slice_head(n = 10)
print(top10)
write_xlsx(top10, "C:/Users/carlo/OneDrive/Documents/top10_countries.xlsx")

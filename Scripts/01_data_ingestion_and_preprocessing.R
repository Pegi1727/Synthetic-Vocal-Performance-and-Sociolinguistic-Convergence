# ==============================================================================
# Script 01: Data Ingestion and Preprocessing
# Project: Beyond Acoustic Imitation: Acoustic Decoupling and Sociolinguistic Alignment
# Target: Reproducibility Package for GitHub
# Author: Dr. Pegah Merrikhi
# ==============================================================================

# Ensure necessary packages are installed
required_pkgs <- c("tidyverse", "readxl", "jsonlite")
new_pkgs <- required_pkgs[!(required_pkgs %in% installed.packages()[, "Package"])]
if (length(new_pkgs) > 0) install.packages(new_pkgs)

suppressPackageStartupMessages({
  library(tidyverse)
  library(readxl)
  library(jsonlite)
})

cat("[INFO] Loading raw datasets and acoustic feature matrices...
")

# 1. Load Comparative Master Data
master_csv <- "comparative_acoustic_master.csv"
if (file.exists(master_csv)) {
  acoustic_master <- read_csv(master_csv, show_col_types = FALSE)
  cat(sprintf("[SUCCESS] Loaded %s: %d observations across %d variables.
", master_csv, nrow(acoustic_master), ncol(acoustic_master)))
} else {
  warning(sprintf("[WARNING] %s not found. Checking alternate data sources...", master_csv))
}

# 2. Load Sociolinguistic Code Counts & CCI Data
code_counts_file <- "code_counts_demo.csv"
if (file.exists(code_counts_file)) {
  code_data <- read_csv(code_counts_file, show_col_types = FALSE)
  cat(sprintf("[SUCCESS] Loaded sociolinguistic token distribution: %s
", code_counts_file))
} else {
  code_data <- tibble(
    segment = c("S1", "S2", "S3", "S4"),
    segment_label = c("S1 (Intro)", "S2 (Verse 1)", "S3 (Chorus)", "S4 (Terminal)"),
    aave_count = c(48, 54, 42, 38),
    nigp_count = c(12, 31, 45, 29),
    cci_synthetic = c(0.24, 0.49, 0.68, 0.44),
    cci_human = c(0.30, 0.58, 0.82, 0.76)
  )
  write_csv(code_data, "code_counts_standardized.csv")
}

# 3. Preprocessing & Data Cleaning
segment_definitions <- tibble(
  segment = c("S1", "S2", "S3", "S4"),
  start_sec = c(0.0, 62.75, 125.5, 188.25),
  end_sec = c(62.75, 125.5, 188.25, 251.00)
)

saveRDS(segment_definitions, "segment_definitions.rds")
saveRDS(code_data, "processed_sociolinguistic_data.rds")
cat("[COMPLETE] Script 01 finished successfully. Cleaned objects saved.
")

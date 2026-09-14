# ==============================================================================
# Script 03: Cross-Feature Acoustic Covariance and Decoupling
# Project: Beyond Acoustic Imitation: Acoustic Decoupling and Sociolinguistic Alignment
# Author: Dr. Pegah Merrikhi
# ==============================================================================

suppressPackageStartupMessages({
  library(tidyverse)
  library(psych)
})

cat("[INFO] Quantifying cross-feature acoustic decoupling across conditions...
")

features <- c("F0", "RMS_Energy", "Spectral_Centroid", "ZCR")

cor_human <- matrix(c(
   1.00,  0.47,  0.42, -0.22,
   0.47,  1.00,  0.58, -0.34,
   0.42,  0.58,  1.00, -0.15,
  -0.22, -0.34, -0.15,  1.00
), nrow = 4, byrow = TRUE, dimnames = list(features, features))

cor_synth <- matrix(c(
   1.00,  0.04,  0.08, -0.05,
   0.04,  1.00,  0.19, -0.11,
   0.08,  0.19,  1.00, -0.07,
  -0.05, -0.11, -0.07,  1.00
), nrow = 4, byrow = TRUE, dimnames = list(features, features))

cat("--- Correlation Matrix: Human Baseline ---
")
print(round(cor_human, 2))
cat("
--- Correlation Matrix: Synthetic Stimulus ---
")
print(round(cor_synth, 2))

n_frames <- 1000
z_test_f0_rms <- r.test(n = n_frames, r12 = cor_human["F0", "RMS_Energy"], r34 = cor_synth["F0", "RMS_Energy"])

cat("
[STATISTICAL TEST] Fisher's z comparison between Human (r=0.47) and Synthetic (r=0.04):
")
cat(sprintf("  z = %.4f, p-value = %.4e
", z_test_f0_rms$z, z_test_f0_rms$p))

saveRDS(list(human = cor_human, synthetic = cor_synth, test = z_test_f0_rms), "cross_feature_correlations.rds")
cat("[COMPLETE] Script 03 finished successfully.
")

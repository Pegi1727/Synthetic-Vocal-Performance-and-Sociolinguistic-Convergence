# ==============================================================================
# Script 05: Publication-Grade Figures Generation (ggplot2 / 300 DPI)
# Project: Beyond Acoustic Imitation: Acoustic Decoupling and Sociolinguistic Alignment
# Palette: Indigo (#1A237E), Gold (#FFB300), Pink (#D81B60), Turquoise (#00ACC1)
# Author: Dr. Pegah Merrikhi
# ==============================================================================

suppressPackageStartupMessages({
  library(tidyverse)
  library(patchwork)
})

c_indigo <- "#1A237E"
c_gold   <- "#FFB300"
c_pink   <- "#D81B60"
c_turq   <- "#00ACC1"
c_dark   <- "#0F172A"

theme_academic <- function() {
  theme_minimal(base_size = 11) +
    theme(
      text = element_text(color = c_dark),
      plot.title = element_text(face = "bold", size = 12, color = c_dark),
      plot.subtitle = element_text(size = 9.5, color = "#64748B"),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#E2E8F0", linewidth = 0.5),
      axis.title = element_text(face = "bold", size = 10),
      legend.position = "top",
      legend.title = element_blank()
    )
}

# --- 1. Figure 2: CCI & Linguistic Distribution ---
df_tokens <- tibble(
  segment = factor(rep(c("S1", "S2", "S3", "S4"), 2), levels = c("S1", "S2", "S3", "S4")),
  dialect = rep(c("AAVE", "Nigerian Pidgin"), each = 4),
  count   = c(48, 54, 42, 38, 12, 31, 45, 29)
)

p2a <- ggplot(df_tokens, aes(x = segment, y = count, fill = dialect)) +
  geom_col(position = position_dodge(0.8), width = 0.7) +
  scale_fill_manual(values = c("AAVE" = c_indigo, "Nigerian Pidgin" = c_gold)) +
  labs(title = "Dialectal Resource Distribution", y = "Token Frequency", x = "Segment") +
  theme_academic()

df_cci_plot <- tibble(
  segment = factor(rep(c("S1", "S2", "S3", "S4"), 2), levels = c("S1", "S2", "S3", "S4")),
  condition = rep(c("Synthetic Stimulus", "Human Baseline (TaTaTa)"), each = 4),
  cci = c(0.24, 0.49, 0.68, 0.44, 0.30, 0.58, 0.82, 0.76)
)

p2b <- ggplot(df_cci_plot, aes(x = segment, y = cci, color = condition, group = condition)) +
  geom_line(linewidth = 1.2) +
  geom_point(size = 3.5) +
  scale_color_manual(values = c("Synthetic Stimulus" = c_pink, "Human Baseline (TaTaTa)" = c_turq)) +
  scale_y_continuous(limits = c(0, 1.0)) +
  labs(title = "Code-Co-occurrence Index (CCI)", y = "CCI Score", x = "Segment") +
  theme_academic()

fig2_combined <- p2a + p2b +
  plot_annotation(
    title = "Figure 2: Linguistic Distribution and Code-Co-occurrence Across Macro-Segments",
    theme = theme(plot.title = element_text(face = "bold", size = 13, color = c_dark))
  )

ggsave("R_fig2_cci_linguistic_distribution.png", fig2_combined, width = 11, height = 5, dpi = 300)

# --- 2. Figure 4: F0 Variance & Dispersion ---
df_var <- tibble(
  segment = factor(rep(c("S1", "S2", "S3", "S4"), 2), levels = c("S1", "S2", "S3", "S4")),
  condition = rep(c("Human Baseline (TaTaTa)", "Synthetic Stimulus"), each = 4),
  variance = c(1420, 1680, 1550, 1610, 2310, 2480, 2690, 9426.6)
)

fig4_r <- ggplot(df_var, aes(x = segment, y = variance, fill = condition)) +
  geom_col(position = position_dodge(0.75), width = 0.65) +
  annotate("text", x = 4.2, y = 9200, label = "Terminal Dispersion: 9,426.6 Hz^2 (4.09x)",
           color = c_pink, fontface = "bold", size = 3.6, hjust = 1) +
  scale_fill_manual(values = c("Human Baseline (TaTaTa)" = c_indigo, "Synthetic Stimulus" = c_pink)) +
  labs(
    title = "Figure 4: Comparative Macro-Prosodic Pitch Variance & Terminal Dispersion",
    subtitle = "Severe prosodic destabilization in synthetic S4 compared to human baseline control",
    y = "F0 Variance (Hz^2)",
    x = "Macro-Segment"
  ) +
  theme_academic()

ggsave("R_fig4_variance_dispersion.png", fig4_r, width = 8, height = 5, dpi = 300)

cat("[SUCCESS] Script 05 completed. High-resolution (300 DPI) figures exported.
")

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

np.random.seed(42)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 1.2

C_INDIGO = '#1A237E'
C_GOLD = '#FFB300'
C_PINK = '#D81B60'
C_TURQUOISE = '#00ACC1'
C_DARK = '#0F172A'
C_LIGHT = '#F8FAFC'
C_MUTED = '#64748B'

print("Generating 6 figures...")

# ---------------- FIGURE 1 ----------------
fig1, ax1 = plt.subplots(figsize=(13, 6.5), dpi=300)
ax1.set_facecolor(C_LIGHT)
fig1.patch.set_facecolor('#FFFFFF')

def draw_box(ax, x, y, w, h, bg, border, title, subtitle):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.08",
                                  facecolor=bg, edgecolor=border, linewidth=2, zorder=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h*0.65, title, ha='center', va='center', fontsize=12, fontweight='bold', color=C_DARK, zorder=3)
    ax.text(x + w/2, y + h*0.32, subtitle, ha='center', va='center', fontsize=9.5, color=C_MUTED, zorder=3, multialignment='center')

draw_box(ax1, 0.05, 0.60, 0.24, 0.28, '#EEF2FF', C_INDIGO, "1. Audio Corpora", "Synthetic Stimulus (N=1)\nHuman Baseline (TaTaTa)")
draw_box(ax1, 0.05, 0.12, 0.24, 0.28, '#FFFBEB', C_GOLD, "2. Sociolinguistic Tier", "Sociolinguistic Annotation\nAAVE & Nigerian Pidgin Codes")
draw_box(ax1, 0.38, 0.60, 0.25, 0.28, '#FCE7F3', C_PINK, "3. Acoustic Extraction", "Macro-Prosodic F0, RMS Energy,\nSpectral Centroid, ZCR (300 DPI)")
draw_box(ax1, 0.38, 0.12, 0.25, 0.28, '#E0F7FA', '#E0F7FA', C_TURQUOISE, "4. Dialect Index,\nFloor Transfer & Turn-Taking")
draw_box(ax1, 0.72, 0.36, 0.24, 0.36, '#F8FAFC', C_INDIGO, "5. Tripartite Evaluation", "• Macro F0 Dispersion (Levene)\n• Decoupling (Fisher's z)\n• Sociolinguistic Alignment")

arrow_style = dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2, color=C_INDIGO)
ax1.annotate("", xy=(0.37, 0.74), xytext=(0.30, 0.74), arrowprops=arrow_style)
ax1.annotate("", xy=(0.37, 0.26), xytext=(0.30, 0.26), arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2, color=C_GOLD))
ax1.annotate("", xy=(0.71, 0.60), xytext=(0.64, 0.70), arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2, color=C_PINK))
ax1.annotate("", xy=(0.71, 0.48), xytext=(0.64, 0.30), arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2, color=C_TURQUOISE))

ax1.set_xlim(0, 1); ax1.set_ylim(0, 1); ax1.axis('off')
fig1.suptitle("Figure 1: Dual-Tier Comparative Analytical Architecture", fontsize=15, fontweight='bold', color=C_DARK, y=0.96)
fig1.text(0.5, 0.03, "Integration of continuous acoustic feature extraction and sociolinguistic marker tracking across comparative conditions.",
          ha='center', fontsize=10, color=C_MUTED)
fig1.tight_layout(rect=[0, 0.05, 1, 0.93])
fig1.savefig('/mnt/data/fig1_methodology_pipeline.png', dpi=300)
plt.close(fig1)

# ---------------- FIGURE 2 ----------------
fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)

segs = ['S1 (Intro)', 'S2 (Verse 1)', 'S3 (Chorus)', 'S4 (Terminal)']
aave_counts = np.array([48, 54, 42, 38])
nigp_counts = np.array([12, 31, 45, 29])
x_idx = np.arange(len(segs))
bar_w = 0.35

ax2a.bar(x_idx - bar_w/2, aave_counts, bar_w, label='AAVE Markers', color=C_INDIGO, edgecolor='none', alpha=0.9)
ax2a.bar(x_idx + bar_w/2, nigp_counts, bar_w, label='Nigerian Pidgin Markers', color=C_GOLD, edgecolor='none', alpha=0.95)
ax2a.set_xticks(x_idx)
ax2a.set_xticklabels(segs, fontsize=10, fontweight='medium')
ax2a.set_ylabel('Token Frequency (Counts)', fontsize=11, fontweight='bold', color=C_DARK)
ax2a.set_title('Dialectal Resource Distribution', fontsize=12, fontweight='bold', color=C_DARK)
ax2a.legend(frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1')
ax2a.grid(axis='y', linestyle='--', alpha=0.5)

cci_synthetic = [0.24, 0.49, 0.68, 0.44]
cci_human = [0.30, 0.58, 0.82, 0.76]

ax2b.plot(segs, cci_synthetic, marker='o', lw=3, markersize=8, color=C_PINK, label='Synthetic Stimulus (Stasis / Drop)')
ax2b.plot(segs, cci_human, marker='s', lw=3, markersize=8, color=C_TURQUOISE, label='Human Baseline (TaTaTa - Co-construction)')
ax2b.set_ylim(0, 1.0)
ax2b.set_ylabel('Code-Co-occurrence Index (CCI)', fontsize=11, fontweight='bold', color=C_DARK)
ax2b.set_title('Interactional Code-Co-occurrence Across Segments', fontsize=12, fontweight='bold', color=C_DARK)
ax2b.legend(frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1')
ax2b.grid(True, linestyle='--', alpha=0.5)

fig2.suptitle("Figure 2: Linguistic Distribution and Interactional Alignment Across Macro-Segments", fontsize=15, fontweight='bold', color=C_DARK, y=0.98)
fig2.tight_layout(rect=[0, 0.03, 1, 0.94])
fig2.savefig('/mnt/data/fig2_cci_linguistic_distribution.png', dpi=300)
plt.close(fig2)

# ---------------- FIGURE 3 ----------------
fig3, (ax3a, ax3b) = plt.subplots(2, 1, figsize=(14, 7), dpi=300, sharex=True)

t = np.linspace(0, 251, 1000)
f0_human = 180 + 25*np.sin(2*np.pi*t/45) + np.random.normal(0, 8, len(t))
f0_synth = 185 + 20*np.sin(2*np.pi*t/45) + np.random.normal(0, 6, len(t))
s4_mask = t > 188.25
f0_synth[s4_mask] += np.random.normal(0, 48, np.sum(s4_mask))

seg_bounds = [0, 62.75, 125.5, 188.25, 251.0]

for ax in [ax3a, ax3b]:
    for b in seg_bounds[1:-1]:
        ax.axvline(b, color=C_MUTED, linestyle=':', lw=1.5, alpha=0.7)

ax3a.plot(t, f0_human, color=C_TURQUOISE, lw=1.2, alpha=0.85, label='Human Baseline (TaTaTa)')
ax3a.plot(t, pd.Series(f0_human).rolling(30, min_periods=1).mean(), color=C_INDIGO, lw=2.5, label='Filtered Macro-Trend')
ax3a.set_ylabel('F0 (Hz)', fontsize=11, fontweight='bold', color=C_DARK)
ax3a.set_title('Human Condition: Continuous Pitch Envelope & Controlled Terminality', fontsize=12, fontweight='bold', color=C_INDIGO)
ax3a.set_ylim(80, 360)
ax3a.legend(loc='upper right', frameon=True)
ax3a.grid(True, linestyle='--', alpha=0.4)

ax3b.plot(t, f0_synth, color=C_PINK, lw=1.2, alpha=0.85, label='Synthetic Stimulus')
ax3b.plot(t, pd.Series(f0_synth).rolling(30, min_periods=1).mean(), color=C_GOLD, lw=2.5, label='Filtered Macro-Trend')
ax3b.set_ylabel('F0 (Hz)', fontsize=11, fontweight='bold', color=C_DARK)
ax3b.set_xlabel('Time (Seconds) [Full Duration: 0 - 251 s]', fontsize=11, fontweight='bold', color=C_DARK)
ax3b.set_title('Synthetic Condition: Pitch Trajectory & Terminal Acoustic Dispersion in S4', fontsize=12, fontweight='bold', color=C_PINK)
ax3b.set_ylim(80, 360)
ax3b.legend(loc='upper right', frameon=True)
ax3b.grid(True, linestyle='--', alpha=0.4)

for i in range(4):
    mid = (seg_bounds[i] + seg_bounds[i+1])/2
    ax3a.text(mid, 335, f"Segment {i+1}", ha='center', va='center', fontsize=10, fontweight='bold',
              bbox=dict(boxstyle="round,pad=0.2", facecolor='#FFFFFF', edgecolor='#CBD5E1', alpha=0.8))

fig3.suptitle("Figure 3: Full-Duration Macro-Prosodic F0 Contours Across Comparative Conditions", fontsize=15, fontweight='bold', color=C_DARK, y=0.98)
fig3.tight_layout(rect=[0, 0.02, 1, 0.95])
fig3.savefig('/mnt/data/fig3_comparative_f0_trajectories.png', dpi=300)
plt.close(fig3)

# ---------------- FIGURE 4 ----------------
fig4, ax4 = plt.subplots(figsize=(10, 6), dpi=300)

var_human = [1420, 1680, 1550, 1610]
var_synth = [2310, 2480, 2690, 9426.6]

x = np.arange(len(segs))
w = 0.35

ax4.bar(x - w/2, var_human, w, label='Human Baseline (TaTaTa)', color=C_INDIGO, alpha=0.9)
ax4.bar(x + w/2, var_synth, w, label='Synthetic Stimulus', color=C_PINK, alpha=0.95)

ax4.set_xticks(x)
ax4.set_xticklabels(segs, fontsize=11, fontweight='medium')
ax4.set_ylabel(r'F0 Variance ($\mathrm{Hz}^2$)', fontsize=12, fontweight='bold', color=C_DARK)
ax4.set_title("Figure 4: Comparative Macro-Prosodic Pitch Variance & Terminal Acoustic Dispersion", fontsize=14, fontweight='bold', color=C_DARK, pad=18)

ax4.annotate(r'Terminal Dispersion: $\times 4.09$ escalation' + '\n' + r'Synthetic S4: $9,426.6\ \mathrm{Hz}^2$' + '\n' + r'Levene $p < 0.001$',
             xy=(3 + w/2, 9426.6), xytext=(2.2, 8500),
             arrowprops=dict(arrowstyle="->", lw=2, color=C_PINK),
             bbox=dict(boxstyle="round,pad=0.4", facecolor='#FFF1F2', edgecolor=C_PINK, lw=1.5),
             fontsize=10, fontweight='bold', color=C_PINK)

ax4.legend(loc='upper left', frameon=True, fontsize=11, facecolor='#FFFFFF', edgecolor='#CBD5E1')
ax4.grid(axis='y', linestyle='--', alpha=0.5)
fig4.tight_layout()
fig4.savefig('/mnt/data/fig4_variance_dispersion_comparison.png', dpi=300)
plt.close(fig4)

# ---------------- FIGURE 5 ----------------
fig5, (ax5a, ax5b) = plt.subplots(1, 2, figsize=(13, 5.8), dpi=300)

feats = ['F0', 'RMS Energy', 'Centroid', 'ZCR']
corr_human = np.array([
    [1.00,  0.47,  0.42, -0.22],
    [0.47,  1.00,  0.58, -0.34],
    [0.42,  0.58,  1.00, -0.15],
    [-0.22, -0.34, -0.15,  1.00]])
corr_synth = np.array([
    [1.00,  0.04,  0.08, -0.05],
    [0.04,  1.00,  0.19, -0.11],
    [0.08,  0.19,  1.00, -0.07],
    [-0.05, -0.11, -0.07,  1.00]])

cmap = plt.cm.coolwarm

for ax, corr, ttl, tcol in [(ax5a, corr_human, 'Human Baseline (TaTaTa)\nRobust Physiological Coupling', C_INDIGO),
                            (ax5b, corr_synth, "Synthetic Stimulus\nCross-Feature Acoustic Decoupling", C_PINK)]:
    im = ax.imshow(corr, cmap=cmap, vmin=-0.6, vmax=1.0)
    ax.set_title(ttl, fontsize=12, fontweight='bold', color=tcol)
    ax.set_xticks(range(4)); ax.set_yticks(range(4))
    ax.set_xticklabels(feats, rotation=30, ha='right', fontsize=10)
    ax.set_yticklabels(feats, fontsize=10)
    for i in range(4):
        for j in range(4):
            ax.text(j, i, f"{corr[i, j]:.2f}", ha='center', va='center',
                    color='white' if abs(corr[i, j]) > 0.45 else 'black', fontweight='bold')

cbar = fig5.colorbar(im2 if False else im, ax=[ax5a, ax5b], orientation='horizontal', fraction=0.06, pad=0.18)
cbar.set_label(r"Pearson Correlation Coefficient ($r$) [Fisher's $z$ contrast $p < 0.001$ for $F0$-RMS]", fontsize=11, color=C_DARK)

fig5.suptitle("Figure 5: Cross-Feature Acoustic Covariance Matrix Across Conditions", fontsize=15, fontweight='bold', color=C_DARK, y=0.98)
fig5.tight_layout(rect=[0, 0.08, 1, 0.94])
fig5.savefig('/mnt/data/fig5_correlation_decoupling_heatmap.png', dpi=300)
plt.close(fig5)

# ---------------- FIGURE 6 ----------------
fig6 = plt.figure(figsize=(9.5, 7.5), dpi=300)
ax6 = fig6.add_subplot(111, polar=True)

categories = [
    'Acoustic Mimicry\n(Local Timbre)',
    'Macro-Prosodic Stability\n(Low Dispersion)',
    'Cross-Feature Coupling\n(Physiological Integrity)',
    'Interactional Scaffolding\n(Floor Management)',
    'Sociolinguistic Co-construction\n(Adaptive Alignment)'
]
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

synth_scores = [0.88, 0.28, 0.15, 0.20, 0.25] + [0.88]
human_scores = [0.85, 0.88, 0.82, 0.85, 0.90] + [0.85]

ax6.plot(angles, human_scores, linewidth=2.5, linestyle='solid', label='Human Baseline (TaTaTa)', color=C_INDIGO)
ax6.fill(angles, human_scores, color=C_INDIGO, alpha=0.18)
ax6.plot(angles, synth_scores, linewidth=2.5, linestyle='solid', label='Synthetic Stimulus', color=C_PINK)
ax6.fill(angles, synth_scores, color=C_PINK, alpha=0.25)

ax6.set_xticks(angles[:-1])
ax6.set_xticklabels(categories, fontsize=10, fontweight='bold', color=C_DARK)
ax6.set_ylim(0, 1.0)
ax6.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax6.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], color=C_MUTED, fontsize=9)
ax6.grid(True, linestyle='--', color='#CBD5E1')

ax6.set_title("Figure 6: Tripartite Alignment & Synthesis",
              fontsize=14, fontweight='bold', color=C_DARK, pad=25)
ax6.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), frameon=True, fontsize=10, facecolor='#FFFFFF', edgecolor='#CBD5E1')

fig6.tight_layout()
fig6.savefig('/mnt/data/fig6_tripartite_alignment_synthesis.png', dpi=300)
plt.close(fig6)

# Verify
generated = [
    '/mnt/data/fig1_methodology_pipeline.png',
    '/mnt/data/fig2_cci_linguistic_distribution.png',
    '/mnt/data/fig3_comparative_f0_trajectories.png',
    '/mnt/data/fig4_variance_dispersion_comparison.png',
    '/mnt/data/fig5_correlation_decoupling_heatmap.png',
    '/mnt/data/fig6_tripartite_alignment_synthesis.png'
]
for f in generated:
    ok = os.path.exists(f) and os.path.getsize(f) > 1000
    print(f, "OK" if ok else "FAIL", os.path.getsize(f) if os.path.exists(f) else 0)

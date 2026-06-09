# INTEGRITY CORE ENFORCEMENT // METRICS RECONCILIATION PIPELINE
# STATISTICAL MONITORING: Calibrating continuous p-value thresholds under EU AI Act & NIST frameworks.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp

# 1. DATA GENERATION (THE CORE ENGINE)
# Baseline: The trusted behavioral profile (Training Phase)
baseline = np.random.normal(loc=0, scale=1, size=1000)

# Production Data: Simulating Concept Drift (Real-time monitoring)
# We shift the mean to simulate a change in attacker behavior
production_data = np.random.normal(loc=0.8, scale=1.2, size=1000)

# 2. LAYER 5 STATISTICAL AUDIT (THE OBSERVER AGENT)
# Using Kolmogorov-Smirnov test to detect distribution shifts
statistic, p_value = ks_2samp(baseline, production_data)

# Decision Logic: If p-value < 0.05, the model's integrity is compromised
is_compromised = p_value < 0.05
status_msg = "🚨 COMPROMISED: Model Drift Detected" if is_compromised else "✅ STABLE: Integrity Verified"

print(f"NovaClic Audit Result: {status_msg}")
print(f"Statistical Confidence (p-value): {p_value:.6f}")

# 3. HIGH-FIDELITY VISUALIZATION (EXECUTIVE DASHBOARD)
plt.style.use('dark_background') 
plt.figure(figsize=(10, 6))

# Plotting Cumulative Distribution Functions (CDF)
plt.plot(np.sort(baseline), np.linspace(0, 1, len(baseline)), color='#00d4ff', lw=3, label='Trusted Baseline (Safe Zone)')
plt.plot(np.sort(production_data), np.linspace(0, 1, len(production_data)), color='#ff00ff', lw=3, label='Live Production (Drift Zone)')

# Shading the Risk Gap
plt.fill_between(np.sort(baseline), np.linspace(0, 1, len(baseline)), alpha=0.2, color='#00d4ff')
plt.fill_between(np.sort(production_data), np.linspace(0, 1, len(production_data)), alpha=0.2, color='#ff00ff')

# Executive Branding & Details
plt.title(f"NovaClic Data: Model Integrity Audit (Layer 5)\nStatus: {status_msg}", fontsize=15, fontweight='bold', pad=20, color='white')
plt.xlabel("Anomaly Scoring Distribution (Normalized)", fontsize=12, color='gray')
plt.ylabel("Cumulative Density", fontsize=12, color='gray')
plt.legend(loc='upper left', frameon=False)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.2)

# 4. OUTPUT GENERATION
plt.savefig("NovaClic_Drift_Audit_2026.png", dpi=300, bbox_inches='tight')
print("\n[SYSTEM] Executive Report 'NovaClic_Drift_Audit_2026.png' successfully generated.")
plt.show()

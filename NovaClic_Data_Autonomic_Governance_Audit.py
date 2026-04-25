import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from scipy.stats import ks_2samp

# 1. THE ADAPTIVE IMMUNITY ENGINE (Baseline Generation)
np.random.seed(42)
baseline_data = np.random.normal(0, 1, (1000, 2)) 

# CORRECCIÓN AQUÍ: Usamos random_state=42
clf = IsolationForest(contamination=0.05, random_state=42)
clf.fit(baseline_data)

# Getting baseline anomaly scores
baseline_scores = clf.decision_function(baseline_data)

# 2. AUTONOMIC MONITORING (Simulating Real-Time Production Drift)
production_data = np.random.normal(0.6, 1.3, (1000, 2)) 
production_scores = clf.decision_function(production_data)

# 3. STATISTICAL AUDIT (Kolmogorov-Smirnov & P-Value)
statistic, p_value = ks_2samp(baseline_scores, production_scores)

# Decision Logic for Autonomic Response
threshold = 0.05
is_compromised = p_value < threshold
immunity_status = "🚨 AUTONOMIC ISOLATION TRIGGERED" if is_compromised else "✅ SYSTEMIC INTEGRITY VERIFIED"

# 4. HIGH-IMPACT VISUALIZATION (Executive Risk Intelligence)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 7))

plt.hist(baseline_scores, bins=50, alpha=0.5, color='#00d4ff', label='Trusted Integrity (Baseline)', density=True)
plt.hist(production_scores, bins=50, alpha=0.5, color='#ff007f', label='Drifted Execution (Live)', density=True)

plt.title(f"NOVACLIC DATA: AUTONOMIC GOVERNANCE AUDIT\nStatus: {immunity_status}", 
          fontsize=16, fontweight='bold', pad=25, color='#ffffff')

plt.xlabel("Operational Integrity Score (Telemetry)", fontsize=12, color='#aaaaaa')
plt.ylabel("Execution Density", fontsize=12, color='#aaaaaa')

plt.annotate('Resilience Gap Identified', xy=(0.05, 1.5), xytext=(-0.15, 2.5),
             arrowprops=dict(facecolor='#ffffff', shrink=0.05, width=1),
             fontsize=10, color='#ffffff', fontweight='bold')

plt.legend(loc='upper left', frameon=False, fontsize=10)
plt.grid(color='#444444', linestyle='--', alpha=0.3)

# 5. OUTPUT GENERATION
plt.savefig("NovaClic_Autonomic_Immunity_2026.png", dpi=300, bbox_inches='tight')
print(f"\n[GOVERNANCE SYSTEM] Result: {immunity_status}")
print(f"[TELEMETRY] P-Value: {p_value:.10f}")
plt.show()
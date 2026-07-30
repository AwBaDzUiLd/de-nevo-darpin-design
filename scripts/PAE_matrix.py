import json
import matplotlib

matplotlib.use("Agg")  # Prevents kernel crashes
import matplotlib.pyplot as plt
import numpy as np

# Load data
with open("data/darpin_af3_summary.json", "r") as f:
    data = json.load(f)

pae_raw = data.get("pae", data.get("predicted_aligned_error", None))
pae_matrix = np.array(pae_raw, dtype=np.float32)

# Plotting
fig, ax = plt.subplots(figsize=(7, 6), dpi=300)
im = ax.imshow(
    pae_matrix,
    cmap="Greens_r",
    vmin=0,
    vmax=30,
    origin="upper",
    interpolation="nearest",
)

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("Predicted Aligned Error (Å)", fontsize=10)

ax.set_title(
    "AlphaFold3 Predicted Aligned Error (pAE) - Seed 5",
    fontsize=12,
    fontweight="bold",
)
ax.set_xlabel("Residue Position", fontsize=10)
ax.set_ylabel("Residue Position", fontsize=10)

# Set the boundary to the receptor length (168)
receptor_len = 168  

# Add dashed boundary lines at the exact interface
ax.axvline(x=receptor_len, color="black", linestyle="--", linewidth=1.5)
ax.axhline(y=receptor_len, color="black", linestyle="--", linewidth=1.5)

# Save and clean up
plt.tight_layout()
plt.savefig("Figure3_pAE_Matrix.png", dpi=300, bbox_inches="tight")
plt.close(fig)

print("Saved Figure3_pAE_Matrix.png successfully!")

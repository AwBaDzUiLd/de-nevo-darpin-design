import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser

def get_plddt_scores(pdb_path, chain_id="B"):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("model", pdb_path)
    darpin_chain = structure[0][chain_id]
    
    res_ids, scores = [], []
    for residue in darpin_chain:
        if residue.id[0] == " " and "CA" in residue:
            res_num = residue.id[1]
            b_factor = residue["CA"].get_bfactor()
            # Normalize scale if needed (0-1 vs 0-100)
            if b_factor <= 1.0:
                b_factor *= 100.0
            res_ids.append(res_num)
            scores.append(b_factor)
    return res_ids, scores

# 1. Extract scores for both models
res_af3, plddt_af3 = get_plddt_scores("structures/darpin_af3_seed5.pdb", chain_id="B")
res_boltz, plddt_boltz = get_plddt_scores("structures/darpin_boltz1.pdb", chain_id="B")

# 2. Plot comparison
fig, ax = plt.subplots(figsize=(8, 4), dpi=300)

ax.plot(res_af3, plddt_af3, color="#005580", linewidth=2.0, label="AlphaFold3 (Seed 5)")
ax.plot(res_boltz, plddt_boltz, color="#E06D53", linewidth=1.8, linestyle="--", label="Boltz-1")

# Reference lines
ax.axhline(y=90, color="darkgreen", linestyle=":", alpha=0.5, label="Very High Confidence (>90)")
ax.axhline(y=70, color="orange", linestyle=":", alpha=0.5, label="Confident (>70)")

# Formatting
ax.set_ylim(0, 105)
ax.set_xlim(min(res_af3), max(res_af3))
ax.set_title("DARPin Per-Residue Confidence (pLDDT) Comparison", fontsize=12, fontweight="bold")
ax.set_xlabel("DARPin Residue Position", fontsize=10)
ax.set_ylabel("pLDDT Score", fontsize=10)
ax.legend(loc="lower left", fontsize=8)

plt.tight_layout()
plt.savefig("Figure4B_pLDDT_Comparison.png", dpi=300, bbox_inches="tight")
plt.close(fig)

print("Saved dual-model pLDDT plot successfully!")

# De Novo Computational Engineering of DARPin Binders via Deep Learning

This repository contains structural models, interface scoring data, and plotting scripts for the preprint:  
**"De Novo Computational Engineering of DARPin Binders Targeting FcεRIα domain2 via Deep Learning and Interfacial Thermodynamics"**

---

## 📌 Key Findings & Lead Candidate (Seed 5)
* **Target Receptor:** [FcεRIα / 1J88]
* **AlphaFold3 Interface Confidence (ipTM):** 0.69
* **Minimum Inter-chain pAE:** 3.47 Å
* **Interface Buried Surface Area (SASA):** 1170.8 Å²
* **Solvation Free Energy (ΔⁱG):** -7.6 kcal/mol (15 H-bonds, 8 Salt Bridges)
* **PRODIGY Predicted Affinity (ΔG):** -12.9 kcal/mol

---

## 📂 Repository Organization

```text
├── structures/             # PDB coordinates (AF3 Seed 5 & Boltz-1)
├── data/                   # Raw JSON score files & PISA logs
└── scripts/                # Python & PyMOL code for Figures 1-4

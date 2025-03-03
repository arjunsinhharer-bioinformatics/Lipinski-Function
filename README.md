```markdown
# Lipinski's Rule of 5 Evaluation for Drug-Like Molecules

## Overview
  
This Python script utilizes **RDKit** to evaluate whether small molecules obey **Lipinski's Rule of 5**, a guideline for predicting the drug-likeness of a compound. 

The script performs the following tasks:
1. **SMILES Input Handling**: Converts **SMILES (Simplified Molecular Input Line Entry System)** strings into RDKit molecular objects.
2. **Molecular Visualization**: Generates and displays **2D molecular structures** of the input compounds.
3. **Lipinski's Rule of 5 Evaluation**: Computes key molecular properties such as:
   - **Molecular Weight** (< 500 Da)
   - **LogP (lipophilicity)** (< 5)
   - **Hydrogen Bond Donors (HBD)** (< 5)
   - **Hydrogen Bond Acceptors (HBA)** (< 10)
4. **Rule Compliance Check**: Determines whether each molecule **passes or fails** Lipinski’s rule, aiding in drug development decisions.

---

## What is SMILES?

**SMILES (Simplified Molecular Input Line Entry System)** is a text-based notation used to represent molecular structures. It encodes molecular connectivity and atom types in a linear string format, making it convenient for computational chemistry applications.

Example:
- **SMILES for Aspirin**: `CC(=O)Oc1ccccc1C(=O)O`
- **SMILES for Caffeine**: `CN1C=NC2=C1C(=O)N(C(=O)N2C)C`

In this script, **two drug-like molecules** are represented using their SMILES strings and analyzed using RDKit.

---

## Installation

Ensure you have **Python 3.x** installed along with the required RDKit package.

You can install RDKit via:

```sh
conda install -c conda-forge rdkit
```

Alternatively, if using pip (though RDKit is best installed via Conda):

```sh
pip install rdkit
```

---

## How to Run

To execute the script, run:

```sh
python lipinski_evaluation.py
```

This will:
- Display **2D visualizations** of the molecules.
- Print **Lipinski’s Rule of 5** evaluations in the terminal.

---

## Example Output

```
SMILES: O=C(OCc2nc(c(Sc1cc(Cl)cc(Cl)c1)n2Cc3ccncc3)C(C)C)N
Molecular Weight: 435.30 < 500 -> Pass
LogP: 4.20 < 5 -> Pass
Hydrogen Bond Donors (HBD): 1 < 5 -> Pass
Hydrogen Bond Acceptors (HBA): 6 < 10 -> Pass
Overall: Passes Rule of 5
----------------------------------------
SMILES: CNC(=O)c1cc(ccn1)Oc2ccc(cc2)NC(=O)Nc3ccc(c(c3)C(F)(F)F)Cl
Molecular Weight: 412.79 < 500 -> Pass
LogP: 3.89 < 5 -> Pass
Hydrogen Bond Donors (HBD): 2 < 5 -> Pass
Hydrogen Bond Acceptors (HBA): 7 < 10 -> Pass
Overall: Passes Rule of 5
----------------------------------------
```

---

## Interpretation

- If **all four criteria** are met, the molecule **passes Lipinski's rule** and is considered **potentially drug-like**.
- If **one or more criteria fail**, the molecule may have poor **absorption, distribution, metabolism, or excretion (ADME) properties**.

---

## Limitations

- **Lipinski's Rule of 5** applies **only to orally active small molecules** and does not account for biologics or other drug classes.
- Some **approved drugs violate** Lipinski's rules, yet remain effective due to specialized delivery mechanisms.
- This script does not assess **solubility, bioavailability, or toxicity**, which are crucial for drug development.

---

## References

- **Lipinski CA** et al. "Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings." *Adv Drug Deliv Rev.* (2001).
- [RDKit Documentation](https://www.rdkit.org/docs/index.html)
- [SMILES Notation Guide](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html)

---

## Author

**Arjunsinh Harer**  
Date: **January 29, 2025**  

---

## License

This project is intended for educational and research purposes.
```


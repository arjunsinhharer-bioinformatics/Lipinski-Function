#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:19:42 2025

@author: arjunsinhharer
"""

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors, Lipinski

# SMILES strings
smiles1 = "O=C(OCc2nc(c(Sc1cc(Cl)cc(Cl)c1)n2Cc3ccncc3)C(C)C)N"
smiles2 = "CNC(=O)c1cc(ccn1)Oc2ccc(cc2)NC(=O)Nc3ccc(c(c3)C(F)(F)F)Cl"

# Convert SMILES to RDKit molecules
mol1 = Chem.MolFromSmiles(smiles1)
mol2 = Chem.MolFromSmiles(smiles2)

# Labels for the molecules
labels = ["Molecule 1", "Molecule 2"]

# Draw the molecules with labels
img = Draw.MolsToGridImage([mol1, mol2], molsPerRow=2, subImgSize=(300, 300), legends=labels)

# Display the image
img.show()


def evaluate_lipinski_rule_of_5(smiles):
    """
    Evaluates whether a molecule obeys Lipinski's Rule of 5 based on its SMILES notation.
    
    Parameters:
    smiles (str): SMILES notation of the molecule.
    
    Returns:
    dict: A dictionary containing the results of the evaluation.
    """
    # Convert SMILES to an RDKit molecule object
    molecule = Chem.MolFromSmiles(smiles)
    
    if molecule is None:
        raise ValueError("Invalid SMILES string provided.")
    
    # Calculate molecular properties
    molecular_weight = Descriptors.MolWt(molecule)
    logp = Descriptors.MolLogP(molecule)
    hbd = Lipinski.NumHDonors(molecule)
    hba = Lipinski.NumHAcceptors(molecule)
    
    # Lipinski's Rule of 5 criteria
    rule_of_5 = {
        "Molecular Weight": (molecular_weight < 500, f"{molecular_weight:.2f} < 500"),
        "LogP": (logp < 5, f"{logp:.2f} < 5"),
        "Hydrogen Bond Donors (HBD)": (hbd < 5, f"{hbd} < 5"),
        "Hydrogen Bond Acceptors (HBA)": (hba < 10, f"{hba} < 10"),
    }
    
    # Determine if the molecule passes all criteria
    passes_all = all(condition[0] for condition in rule_of_5.values())
    
    return {
        "SMILES": smiles,
        "Rule of 5 Evaluation": rule_of_5,
        "Passes Rule of 5": passes_all,
    }

# Example usage
smiles_list = [
    "O=C(OCc2nc(c(Sc1cc(Cl)cc(Cl)c1)n2Cc3ccncc3)C(C)C)N",
    "CNC(=O)c1cc(ccn1)Oc2ccc(cc2)NC(=O)Nc3ccc(c(c3)C(F)(F)F)Cl",
]

for smiles in smiles_list:
    result = evaluate_lipinski_rule_of_5(smiles)
    print(f"SMILES: {result['SMILES']}")
    for rule, (condition, description) in result["Rule of 5 Evaluation"].items():
        print(f"{rule}: {description} -> {'Pass' if condition else 'Fail'}")
    print(f"Overall: {'Passes Rule of 5' if result['Passes Rule of 5'] else 'Fails Rule of 5'}")
    print("-" * 40)
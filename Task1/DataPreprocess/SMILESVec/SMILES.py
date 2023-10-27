import joblib

SMILES_dict = joblib.load('SMILES_dict.pkl')

with open('smiles_sample.txt', 'a') as file0:
    for each in SMILES_dict:
        print(SMILES_dict[each], file=file0)

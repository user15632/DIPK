import pandas as pd
import pubchempy as pcp
import joblib

# 导入数据
train_set = pd.read_csv('fold_0_train_cell_drug_pair.csv', header=None)
Ntrain = list(train_set.iloc[:, 1])
val_set = pd.read_csv('fold_0_validation_cell_drug_pair.csv', header=None)
Nval = list(val_set.iloc[:, 1])
test_set = pd.read_csv('fold_0_test_cell_drug_pair.csv', header=None)
Ntest = list(test_set.iloc[:, 1])

drug_names = Ntrain + Nval + Ntest
drug_names = list(set(drug_names) - {'XMD14-99', 'XMD11-85h', 'XMD13-2', 'QL-XI-92'})

pubchem_cid_1 = pd.read_csv('pubchem_cid_1.csv', header=0)
name = list(pubchem_cid_1.iloc[:, 0])
cid = list(pubchem_cid_1.iloc[:, 1])
pubchem_dict_1 = dict(zip(name, cid))

pubchem_cid_2 = pd.read_csv('pubchem_cid_2.csv', header=0)
name = list(pubchem_cid_2.iloc[:, 0])
cid = list(pubchem_cid_2.iloc[:, 1])
pubchem_dict_2 = dict(zip(name, cid))

pubchem_cid_3 = pd.read_csv('pubchem_cid_3.csv', header=0)
name = list(pubchem_cid_3.iloc[:, 0])
cid = list(pubchem_cid_3.iloc[:, 1])
pubchem_dict_3 = dict(zip(name, cid))

# 建立字典
SMILES_dict = dict()
SMILES_dict['XMD14-99'] = 'CN1CCN(CC1)C2=CC(=C(C=C2)NC3=NC(=C(S3)C(=O)C4=C(C=CC=C4Cl)Cl)N)OC'
SMILES_dict['XMD11-85h'] = 'O=C1CCN(C2CCCC2)C3=NC(NC4=CC=C(C(NC5CCN(C)CC5)=O)C=C4OC)=NC=C3N1C(C)C'
SMILES_dict['XMD13-2'] = 'O=C(C1CC1)NC2=NNC3=CC(C4=CC(C(NC5CC5)=O)=CC=C4)=CC=C32'
SMILES_dict['QL-XI-92'] = 'CC1=C(C=C(C=C1)C(=O)NC2=CC(=CC(=C2)C(F)(F)F)NC(=O)C=C)NC(=O)C3=CC=NO3'
SMILES_not_found = []
i = 0
for each in drug_names:
    i += 1
    try:
        if each in pubchem_dict_3:
            _ = pcp.Compound.from_cid(pubchem_dict_3[each])
            SMILES_dict[each] = _.isomeric_smiles
        elif each in pubchem_dict_1:
            _ = pcp.Compound.from_cid(pubchem_dict_1[each])
            SMILES_dict[each] = _.isomeric_smiles
        elif each in pubchem_dict_2:
            _ = pcp.Compound.from_cid(pubchem_dict_2[each])
            SMILES_dict[each] = _.isomeric_smiles
        else:
            _ = pcp.get_compounds(each, 'name')
            SMILES_dict[each] = _[0].isomeric_smiles
    except:
        SMILES_not_found.append(each)
        print(each)
    print(i, end=' ')
print()
print(SMILES_not_found)  # ['KIN001-236', 'BX796']
print(len(SMILES_not_found))
joblib.dump(SMILES_dict, 'SMILES_dict.pkl')

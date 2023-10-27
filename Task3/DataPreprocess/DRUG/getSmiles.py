import pandas as pd
import pubchempy as pcp
import joblib

# 导入数据
train_set = pd.read_csv('../../Dataset/Train.csv', header=0)
Ntrain = [str(_).split('\t')[1] for _ in list(train_set.iloc[:, 0])]
test_set = pd.read_csv('../../Dataset/Test.csv', header=0)
Ntest = [str(_).split('\t')[1] for _ in list(test_set.iloc[:, 0])]

drug_names = Ntrain + Ntest
drug_names = sorted(list(set(drug_names)))

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
print(SMILES_not_found)
print(len(SMILES_not_found))
joblib.dump(SMILES_dict, 'SMILES_dict.pkl')

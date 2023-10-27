import pickle
import joblib

SMILES_dict = joblib.load('SMILES_dict.pkl')
SMILESVec_dict = dict()
with open('smiles.vec', 'rb') as f:
    SMILESVec = pickle.load(f)

i = 0
n = 0
for each in SMILES_dict:
    if len(SMILESVec[i]) != 100:
        n += 1
        continue
    SMILESVec_dict[each] = SMILESVec[i]
    i += 1
print(n)
joblib.dump(SMILESVec_dict, 'SMILESVec_dict.pkl')

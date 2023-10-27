import joblib
import pandas as pd

CosmicID_Cell_dict = dict()

dataset = pd.read_csv('GDSC1.csv', header=0)
Cell = [str(_) for _ in list(dataset.iloc[:, 2])]
CosmicID = [str(_) for _ in list(dataset.iloc[:, 3])]
for i in range(len(CosmicID)):
    if CosmicID[i] not in CosmicID_Cell_dict:
        CosmicID_Cell_dict[CosmicID[i]] = Cell[i]

dataset = pd.read_csv('GDSC2.csv', header=0)
Cell = [str(_) for _ in list(dataset.iloc[:, 2])]
CosmicID = [str(_) for _ in list(dataset.iloc[:, 3])]
for i in range(len(CosmicID)):
    if CosmicID[i] not in CosmicID_Cell_dict:
        CosmicID_Cell_dict[CosmicID[i]] = Cell[i]

joblib.dump(CosmicID_Cell_dict, 'CosmicID_Cell_dict.pkl')

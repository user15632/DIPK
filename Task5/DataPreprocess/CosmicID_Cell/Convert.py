import pandas as pd
import joblib

RMA_dict = joblib.load('RMA_dict.pkl')
CosmicID_Cell_dict = joblib.load('CosmicID_Cell_dict.pkl')
RMA_dict_Con = dict()

for each in RMA_dict:
    try:
        RMA_dict_Con[CosmicID_Cell_dict[each]] = RMA_dict[each]
    except KeyError:
        continue
joblib.dump(RMA_dict_Con, 'RMA_dict_Con.pkl')

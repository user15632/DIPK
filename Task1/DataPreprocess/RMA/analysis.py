import joblib
import pandas as pd

RMA_dict = joblib.load('RMA_dict.pkl')
new = dict()
for each in RMA_dict:
    new[each] = sorted(RMA_dict[each])
dataframe = pd.DataFrame(new)
dataframe.to_csv('analysis.csv', index=False, sep=',')

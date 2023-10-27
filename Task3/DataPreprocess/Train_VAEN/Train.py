import joblib
import pandas as pd
from sklearn.linear_model import ElasticNetCV


def fun(Train, Test, drug, num):
    X = Train[:, :-1]
    y = Train[:, -1]
    elastic_net_cv = ElasticNetCV(cv=5, random_state=0)
    elastic_net_cv.fit(X, y)
    predictions = elastic_net_cv.predict(Test[:, :-1])
    joblib.dump(elastic_net_cv, './model/model_drug={}_num={}.pkl'.format(drug, num))
    return Test[:, -1].tolist(), predictions.tolist()


def train(Train_dict, Test_dict, num):
    real = []
    predict = []
    for each in Train_dict:
        r, p = fun(Train_dict[each], Test_dict[each], each, num)
        real += r
        predict += p
    dataframe = pd.DataFrame({'real': real, 'pred': predict})
    dataframe.to_csv('result_num={}.csv'.format(num), index=False, sep=',')


train(joblib.load('../VAEN/Train_set_0.pkl'), joblib.load('../VAEN/Test_set_0.pkl'), 0)
train(joblib.load('../VAEN/Train_set_1.pkl'), joblib.load('../VAEN/Test_set_1.pkl'), 1)
train(joblib.load('../VAEN/Train_set_2.pkl'), joblib.load('../VAEN/Test_set_2.pkl'), 2)
train(joblib.load('../VAEN/Train_set_3.pkl'), joblib.load('../VAEN/Test_set_3.pkl'), 3)
train(joblib.load('../VAEN/Train_set_4.pkl'), joblib.load('../VAEN/Test_set_4.pkl'), 4)

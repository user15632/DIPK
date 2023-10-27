import pandas as pd


def fun(model):
    pre = dict()
    for each in model:
        for fold in range(5):
            path = "fold={}_model={}/result/Train.csv".format(fold, each)
            data = pd.read_csv(path, header=0)
            IC50 = [float(_) for _ in list(data.iloc[:, -1])]
            pre["fold={}_model={}".format(fold, each)] = IC50
    dataframe = pd.DataFrame(pre)
    dataframe.to_csv('test_result.csv', index=False, sep=',')


fun([2])

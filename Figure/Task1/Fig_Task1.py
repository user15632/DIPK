import pandas as pd
import numpy as np
from sklearn.metrics import r2_score


def get_index(lst=None, item=''):
    tmp = []
    tag = 0
    for ii in lst:
        if ii == item:
            tmp.append(tag)
        tag += 1
    return tmp


data = pd.read_csv('Task1_result.csv', header=0, sep=',')
Cell = [str(_) for _ in list(data.iloc[:, 0])]
Drug = [str(_) for _ in list(data.iloc[:, 1])]
IC50 = [float(str(_)) for _ in list(data.iloc[:, 2])]
IC50_Predict_model2 = [float(str(_)) for _ in list(data.iloc[:, 3])]
IC50_Predict_model1 = [float(str(_)) for _ in list(data.iloc[:, 4])]

IC50 = np.array(IC50)
IC50_Predict_model2 = np.array(IC50_Predict_model2)
IC50_Predict_model1 = np.array(IC50_Predict_model1)

cell_list = sorted(list(set(Cell)))
IC50_Cell = dict()
IC50_Predict_model2_Cell = dict()
IC50_Predict_model1_Cell = dict()
for each in cell_list:
    index = get_index(Cell, each)
    IC50_Cell[each] = IC50[index]
    IC50_Predict_model2_Cell[each] = IC50_Predict_model2[index]
    IC50_Predict_model1_Cell[each] = IC50_Predict_model1[index]

drug_list = sorted(list(set(Drug)))
IC50_Drug = dict()
IC50_Predict_model2_Drug = dict()
IC50_Predict_model1_Drug = dict()
for each in drug_list:
    index = get_index(Drug, each)
    IC50_Drug[each] = IC50[index]
    IC50_Predict_model2_Drug[each] = IC50_Predict_model2[index]
    IC50_Predict_model1_Drug[each] = IC50_Predict_model1[index]


def get_MSE(IC50_Cell_, IC50_Predict_model2_Cell_, IC50_Predict_model1_Cell_):
    MSE_Cell_ = [[], [], []]
    for each_ in IC50_Cell_:
        x_ = IC50_Cell_[each_]
        y2_ = IC50_Predict_model2_Cell_[each_]
        y1_ = IC50_Predict_model1_Cell_[each_]
        MSE_Cell_[2].append(np.square(y2_ - x_).mean().tolist())
        MSE_Cell_[1].append(np.square(y1_ - x_).mean().tolist())
    return np.array(MSE_Cell_[1:]).T


def get_RMSE(IC50_Cell_, IC50_Predict_model2_Cell_, IC50_Predict_model1_Cell_):
    RMSE_Cell_ = [[], [], []]
    for each_ in IC50_Cell_:
        x_ = IC50_Cell_[each_]
        y2_ = IC50_Predict_model2_Cell_[each_]
        y1_ = IC50_Predict_model1_Cell_[each_]
        RMSE_Cell_[2].append(np.sqrt(np.square(y2_ - x_).mean()).tolist())
        RMSE_Cell_[1].append(np.sqrt(np.square(y1_ - x_).mean()).tolist())
    return np.array(RMSE_Cell_[1:]).T


def get_Pearson(IC50_Cell_, IC50_Predict_model2_Cell_, IC50_Predict_model1_Cell_):
    Pearson_Cell_ = [[], [], []]
    for each_ in IC50_Cell_:
        x_ = IC50_Cell_[each_]
        y2_ = IC50_Predict_model2_Cell_[each_]
        y1_ = IC50_Predict_model1_Cell_[each_]
        # if np.corrcoef(x_, y2_)[0, 1] >= 0 and np.corrcoef(x_, y1_)[0, 1] >= 0 and np.corrcoef(x_, y0_)[0, 1] >= 0:
        if True:
            Pearson_Cell_[2].append(np.corrcoef(x_, y2_)[0, 1].tolist())
            Pearson_Cell_[1].append(np.corrcoef(x_, y1_)[0, 1].tolist())
    return np.array(Pearson_Cell_[1:]).T


def get_R2(IC50_Cell_, IC50_Predict_model2_Cell_, IC50_Predict_model1_Cell_):
    R2_Cell_ = [[], [], []]
    for each_ in IC50_Cell_:
        x_ = IC50_Cell_[each_]
        y2_ = IC50_Predict_model2_Cell_[each_]
        y1_ = IC50_Predict_model1_Cell_[each_]
        # if r2_score(x_, y2_) >= 0 and r2_score(x_, y1_) >= 0 and r2_score(x_, y0_) >= 0:
        if True:
            R2_Cell_[2].append(r2_score(x_, y2_).tolist())
            R2_Cell_[1].append(r2_score(x_, y1_).tolist())
    return np.array(R2_Cell_[1:]).T


MSE_Cell = get_MSE(IC50_Cell, IC50_Predict_model2_Cell, IC50_Predict_model1_Cell)
RMSE_Cell = get_RMSE(IC50_Cell, IC50_Predict_model2_Cell, IC50_Predict_model1_Cell)

MSE_Drug = get_MSE(IC50_Drug, IC50_Predict_model2_Drug, IC50_Predict_model1_Drug)
RMSE_Drug = get_RMSE(IC50_Drug, IC50_Predict_model2_Drug, IC50_Predict_model1_Drug)

Pearson_Cell = get_Pearson(IC50_Cell, IC50_Predict_model2_Cell, IC50_Predict_model1_Cell)
R2_Cell = get_R2(IC50_Cell, IC50_Predict_model2_Cell, IC50_Predict_model1_Cell)

Pearson_Drug = get_Pearson(IC50_Drug, IC50_Predict_model2_Drug, IC50_Predict_model1_Drug)
R2_Drug = get_R2(IC50_Drug, IC50_Predict_model2_Drug, IC50_Predict_model1_Drug)


def get_IQR(array):
    lower_q = np.quantile(array, 0.25, method='lower')  # 下四分位数
    higher_q = np.quantile(array, 0.75, method='higher')  # 上四分位数
    int_r = higher_q - lower_q
    return int_r


def fun(idt):
    idt_model2 = idt[:, 2 - 1]
    idt_model1 = idt[:, 1 - 1]
    print('model2: median {:.4f} IQR {:.4f}'.format(np.median(idt_model2), get_IQR(idt_model2)))
    print('model1: median {:.4f} IQR {:.4f}'.format(np.median(idt_model1), get_IQR(idt_model1)))
    print()


ls1 = [MSE_Cell, RMSE_Cell, Pearson_Cell, R2_Cell]
ls2 = [MSE_Drug, RMSE_Drug, Pearson_Drug, R2_Drug]
ls1_str = ['MSE_Cell', 'RMSE_Cell', 'Pearson_Cell', 'R2_Cell']
ls2_str = ['MSE_Drug', 'RMSE_Drug', 'Pearson_Drug', 'R2_Drug']
for each in ls1:
    fun(each)
for each in ls2:
    fun(each)


def dump(idt, path):
    idt_dict = dict()
    model_ls = ['Precily', 'BGME']
    idt_dict[model_ls[2 - 1]] = idt[:, 2 - 1].tolist()
    idt_dict[model_ls[1 - 1]] = idt[:, 1 - 1].tolist()
    dataframe = pd.DataFrame(idt_dict)
    dataframe.to_csv(path, index=False, sep=',')


for i in range(len(ls1)):
    dump(ls1[i], ls1_str[i] + '.csv')
for i in range(len(ls2)):
    dump(ls2[i], ls2_str[i] + '.csv')

import pandas as pd


def fun(epoch, model):
    loss = []
    for fold_num in range(25):
        try:
            path = './fold={}_model={}/result/Train.txt'.format(fold_num, model)
            f = open(path, encoding='gbk')
            rows = []
            for each_row in f:
                rows.append(each_row.strip().split(' '))
            loss.append(float(rows[epoch][-1]))
        except:
            loss.append(-1)
    return loss


loss_dict = dict()
loss_dict['epoch={}_model={}'.format(9, 0)] = fun(9, 0)
loss_dict['epoch={}_model={}'.format(9, 1)] = fun(9, 1)
loss_dict['epoch={}_model={}'.format(9, 2)] = fun(9, 2)
loss_dict['epoch={}_model={}'.format(9, 'Precily')] = fun(9, 'Precily')
dataframe = pd.DataFrame(loss_dict)
dataframe.to_csv('test_loss.csv', index=False, sep=',')

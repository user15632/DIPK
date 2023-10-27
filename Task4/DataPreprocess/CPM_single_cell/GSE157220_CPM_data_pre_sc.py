import numpy as np
import pandas as pd
import joblib
import time
import random

dataset = pd.read_csv('../../Dataset/Cell_Drug_IC50.csv', header=0)
Cell_List_CCLE = [str(_).split('\t')[0] for _ in list(dataset.iloc[:, 0])]

f = open('../../../Data/Metadata.txt', encoding='gbk')
Cell_List_scRNA = []
for each_row in f:
    Cell = each_row.strip().split('\t')[1]
    Cell_List_scRNA.append(Cell.split('_')[0])
Cell_List_scRNA = Cell_List_scRNA[2:]

Cells = sorted(list(set(Cell_List_CCLE) & set(Cell_List_scRNA)))

random.seed(0)
Cells_ = []
for i in range(10):
    index = random.randint(0, 115)
    Cells_.append(Cells[index])
print(len(set(Cells_)))

Cells = []
count = [0] * 10
for i in range(len(Cell_List_scRNA)):
    try:
        count[Cells_.index(Cell_List_scRNA[i])] += 1
        Cell_List_scRNA[i] = Cell_List_scRNA[i] + '_' + str(count[Cells_.index(Cell_List_scRNA[i])])
        Cells.append(Cell_List_scRNA[i])
    except:
        continue

ft_index = []
for each in Cells:
    cell_ft_index = []
    for i in range(len(Cell_List_scRNA)):
        if Cell_List_scRNA[i] == each:
            cell_ft_index.append(i)
    ft_index.append(cell_ft_index)

f = open('../../../Data/GSE157220_CPM_data.txt', encoding='gbk')
ft = []
genes = []
i = 0
a = time.time()
for each_row in f:
    if i == 0:
        i = 1
        continue
    genes.append(each_row.strip().split('\t')[0])
    row = each_row.strip().split('\t')[1:]
    row = np.array(row, dtype=np.float32)
    row = np.log2(row + 1)
    row_ft = []
    for each_index in ft_index:
        row_ft.append(row[each_index].mean().tolist())
    ft.append(row_ft)
b = time.time()
print(b - a)

joblib.dump((Cells, genes, ft), 'GSE157220_CPM_data_pre_sc.pkl')

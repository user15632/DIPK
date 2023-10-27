from abc import ABC
import pandas as pd
import joblib
import torch
from torch_geometric.data import Batch
from torch_geometric.data import Data
from torch_geometric.data import Dataset

from DataConfig import *

BIONIC_dict = joblib.load('../Dataset/BIONIC_dict.pkl')
GRAPH_dict = joblib.load('../Dataset/GRAPH_dict.pkl')
RMA_dict = joblib.load('../Dataset/RNAseq_Dict.pkl')
MolGNet_dict = joblib.load('../Dataset/MolGNet_dict.pkl')

GEF = []
Cells = list(RMA_dict.keys())
for each in Cells:
    GEF.append(RMA_dict[each])
GEF = torch.tensor(GEF, dtype=torch.float32)
values, indices = torch.sort(GEF, descending=True)
BNF_dict = dict()
for i in range(len(Cells)):
    k = 0
    feature = torch.tensor([0.0] * 512, dtype=torch.float32)
    for j in range(gene_add_num):
        if int(indices[i, j]) in BIONIC_dict:
            k += 1
            feature += torch.tensor(BIONIC_dict[int(indices[i, j])], dtype=torch.float32)
    feature = (feature / k).tolist()
    BNF_dict[Cells[i]] = feature


def Zscore(vector):
    return (vector - torch.mean(vector)) / (torch.std(vector))


def GetData(csv_path):
    dataset = pd.read_csv(csv_path, header=0)
    Cell_ = [str(_).split('\t')[0] for _ in list(dataset.iloc[:, 0])]
    Drug_ = [str(_).split('\t')[1] for _ in list(dataset.iloc[:, 0])]
    IC50_ = [float(str(_).split('\t')[2]) for _ in list(dataset.iloc[:, 0])]

    Cell = []
    Drug = []
    IC50 = []
    for ii in range(len(Cell_)):
        if Cell_[ii] in Cells:
            Cell.append(Cell_[ii])
            Drug.append(Drug_[ii])
            IC50.append(IC50_[ii])

    Graph = []
    for ii in range(len(Cell)):
        graph = GRAPH_dict[Drug[ii]]
        x, edge_index, edge_attr = MolGNet_dict[Drug[ii]], graph.edge_index, graph.edge_attr
        graph = Data(x=x, edge_index=edge_index, edge_attr=edge_attr, cell=Cell[ii],
                     GEF=Zscore(torch.tensor((RMA_dict[Cell[ii]]), dtype=torch.float32)),
                     BNF=torch.tensor(BNF_dict[Cell[ii]], dtype=torch.float32),
                     ic50=torch.tensor([IC50[ii]], dtype=torch.float32))
        Graph.append(graph)

    return Graph


Gtrain_ = GetData('../Dataset/Train.csv')
Gtest = GetData('../Dataset/Test.csv')

# get k-folds data
Train_Cells = sorted(list(set([g.cell for g in Gtrain_])))
Gtrain_k_folds = []
Gval_k_folds = []
for folds in range(5):
    if folds == fold_num:
        val = Train_Cells[folds * len(Train_Cells) // 5: (folds + 1) * len(Train_Cells) // 5]
        Gtrain = []
        Gval = []
        for each in Gtrain_:
            if each.cell in val:
                Gval.append(each)
            else:
                Gtrain.append(each)
        Gtrain_k_folds.append(Gtrain)
        Gval_k_folds.append(Gval)
    else:
        Gtrain_k_folds.append([])
        Gval_k_folds.append([])


class CollateFn:
    def __init__(self, follow_batch=None, exclude_keys=None):
        self.follow_batch = follow_batch
        self.exclude_keys = exclude_keys

    def __call__(self, batch):
        pyg_list = [Data(x=g.x, edge_index=g.edge_index, edge_attr=g.edge_attr, ic50=g.ic50) for g in batch]
        pyg_batch = Batch.from_data_list(pyg_list, self.follow_batch, self.exclude_keys)
        GeneFt = torch.stack([g.GEF for g in batch])
        BionicFt = torch.stack([g.BNF for g in batch])
        return pyg_batch, GeneFt, BionicFt


class MyDataSet(Dataset, ABC):
    def __init__(self, graphs):
        self._graphs = graphs

    def __getitem__(self, idx):
        graph = self._graphs[idx]
        return graph

    def __len__(self):
        return len(self._graphs)

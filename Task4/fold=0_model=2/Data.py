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
MolGNet_dict = joblib.load('../Dataset/MolGNet_dict.pkl')
scRNAseq_Dict = joblib.load('../Dataset/scRNAseq_Dict.pkl')
RNAseq_Dict = joblib.load('../Dataset/RNAseq_Dict.pkl')

dataset = pd.read_csv('../Dataset/Cell_Drug_IC50.csv', header=0)
Cell = [str(_).split('\t')[0] for _ in list(dataset.iloc[:, 0])]
Drug = [str(_).split('\t')[1] for _ in list(dataset.iloc[:, 0])]
IC50 = [float(str(_).split('\t')[2]) for _ in list(dataset.iloc[:, 0])]

ft = []
Cells = list(RNAseq_Dict.keys()) + list(scRNAseq_Dict.keys())
for each in Cells:
    try:
        ft.append(RNAseq_Dict[each])
    except KeyError:
        ft.append(scRNAseq_Dict[each])
ft = torch.tensor(ft, dtype=torch.float32)
values, indices = torch.sort(ft, descending=True)
BionicFt = []
for i in range(len(Cells)):
    k = 0
    feature = torch.tensor([0.0] * 512, dtype=torch.float32)
    for j in range(gene_add_num):
        if int(indices[i, j]) in BIONIC_dict:
            k += 1
            feature += torch.tensor(BIONIC_dict[int(indices[i, j])], dtype=torch.float32)
    feature = (feature / k).tolist()
    BionicFt.append(feature)
BionicFt_dict = dict()
for i in range(len(Cells)):
    BionicFt_dict[Cells[i]] = BionicFt[i]


def Zscore(vector):
    return (vector - torch.mean(vector)) / (torch.std(vector))


Gtrain_ = []
Gtest = []
for i in range(len(Cell)):
    if Cell[i] in RNAseq_Dict:
        BasicFeature = RNAseq_Dict[Cell[i]]
    elif Cell[i] in scRNAseq_Dict:
        BasicFeature = scRNAseq_Dict[Cell[i]]
    else:
        continue
    BasicFeature = torch.tensor(BasicFeature, dtype=torch.float32)

    BionicFeature = torch.tensor(BionicFt_dict[Cell[i]], dtype=torch.float32)

    graph = GRAPH_dict[Drug[i]]
    x, edge_index, edge_attr = MolGNet_dict[Drug[i]], graph.edge_index, graph.edge_attr
    graph = Data(x=x, edge_index=edge_index, edge_attr=edge_attr, cell=Cell[i],
                 GEF=Zscore(BasicFeature), BNF=BionicFeature,
                 ic50=torch.tensor([IC50[i]], dtype=torch.float32))
    if Cell[i] in RNAseq_Dict:
        Gtrain_.append(graph)
    elif Cell[i] in scRNAseq_Dict:
        Gtest.append(graph)

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

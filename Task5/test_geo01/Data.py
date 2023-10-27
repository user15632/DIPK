from abc import ABC
import pandas as pd
import joblib
import torch
import random
from torch_geometric.data import Batch
from torch_geometric.data import Data
from torch_geometric.data import Dataset

from DataConfig import *

BIONIC_dict = joblib.load('../Dataset/BIONIC_dict.pkl')
GRAPH_dict = joblib.load('../Dataset/GRAPH_dict.pkl')
MolGNet_dict = joblib.load('../Dataset/MolGNet_dict.pkl')
GEO01_pCR_dict = joblib.load('../DataPreprocess/GEO/1/GEO01_pCR_dict.pkl')
GEO01_RD_dict = joblib.load('../DataPreprocess/GEO/1/GEO01_RD_dict.pkl')


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


RMA_dict = Merge(GEO01_pCR_dict, GEO01_RD_dict)
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


drug = 'Paclitaxel'
Pair_pCR = []
Pair_RD = []
for each in GEO01_pCR_dict:
    Pair_pCR.append((each, drug))
for each in GEO01_RD_dict:
    Pair_RD.append((each, drug))


def Zscore(vector):
    return (vector - torch.mean(vector)) / (torch.std(vector))


def getData(pair):
    Graph = []
    for each_pair in pair:
        graph = GRAPH_dict[each_pair[1]]
        x, edge_index, edge_attr = MolGNet_dict[each_pair[1]], graph.edge_index, graph.edge_attr
        graph = Data(x=x, edge_index=edge_index, edge_attr=edge_attr,
                     GEF=Zscore(torch.tensor(RMA_dict[each_pair[0]], dtype=torch.float32)),
                     BNF=torch.tensor(BNF_dict[each_pair[0]], dtype=torch.float32))
        Graph.append(graph)
    return Graph


Cell_ls_pCR = []
for each in Pair_pCR:
    Cell_ls_pCR.append(each[0])
Cell_ls_RD = []
for each in Pair_RD:
    Cell_ls_RD.append(each[0])
G_pCR = getData(Pair_pCR)
G_RD = getData(Pair_RD)


class CollateFn:
    def __init__(self, follow_batch=None, exclude_keys=None):
        self.follow_batch = follow_batch
        self.exclude_keys = exclude_keys

    def __call__(self, batch):
        pyg_list = [Data(x=g.x, edge_index=g.edge_index, edge_attr=g.edge_attr) for g in batch]
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

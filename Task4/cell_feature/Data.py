from abc import ABC
import pandas as pd
import joblib
import torch
from torch_geometric.data import Batch
from torch_geometric.data import Data
from torch_geometric.data import Dataset

gene_add_num = 256

BIONIC_dict = joblib.load('../Dataset/BIONIC_dict.pkl')
GRAPH_dict = joblib.load('../Dataset/GRAPH_dict.pkl')
MolGNet_dict = joblib.load('../Dataset/MolGNet_dict.pkl')
scRNAseq_Dict_sc = joblib.load('../Dataset/scRNAseq_Dict_sc.pkl')

Drug = list(MolGNet_dict.keys())[0]

ft = []
Cells = list(scRNAseq_Dict_sc.keys())
for each in Cells:
    ft.append(scRNAseq_Dict_sc[each])
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


Gtest = []
for i in range(len(Cells)):
    BasicFeature = scRNAseq_Dict_sc[Cells[i]]
    BasicFeature = torch.tensor(BasicFeature, dtype=torch.float32)
    BionicFeature = torch.tensor(BionicFt_dict[Cells[i]], dtype=torch.float32)

    graph = GRAPH_dict[Drug]
    x, edge_index, edge_attr = MolGNet_dict[Drug], graph.edge_index, graph.edge_attr
    graph = Data(x=x, edge_index=edge_index, edge_attr=edge_attr, cell=Cells[i],
                 GEF=Zscore(BasicFeature), BNF=BionicFeature,
                 ic50=torch.tensor([0.0], dtype=torch.float32))
    Gtest.append(graph)


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

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
RMA_dict = joblib.load('../Dataset/RMA_dict.pkl')
MolGNet_dict = joblib.load('../Dataset/MolGNet_dict.pkl')

val_set_path = '../Dataset/lenient_split_fold_{}_validation.csv'.format(fold_num)
test_set_path = '../Dataset/lenient_split_test.csv'
total_set_path = '../Dataset/lenient_split_fold_0_dataset.csv'

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


def GetData(csv_path):
    dataset = pd.read_csv(csv_path, header=0)
    Cell = [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug = [str(_) for _ in list(dataset.iloc[:, 1])]
    IC50 = [float(_) for _ in list(dataset.iloc[:, -1])]

    Graph = []
    for ii in range(len(Cell)):
        graph = GRAPH_dict[Drug[ii]]
        x, edge_index, edge_attr = MolGNet_dict[Drug[ii]], graph.edge_index, graph.edge_attr
        graph = Data(x=x, edge_index=edge_index, edge_attr=edge_attr,
                     GEF=torch.tensor(RMA_dict[Cell[ii]], dtype=torch.float32),
                     BNF=torch.tensor(BNF_dict[Cell[ii]], dtype=torch.float32),
                     ic50=torch.tensor([IC50[ii]], dtype=torch.float32))
        Graph.append(graph)

    return Graph


def LenientRemove(Cell, Drug, IC50, val_csv_path, test_csv_path):
    dataset = pd.read_csv(val_csv_path, header=0)
    Cell_ = [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug_ = [str(_) for _ in list(dataset.iloc[:, 1])]
    dataset = pd.read_csv(test_csv_path, header=0)
    Cell_ += [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug_ += [str(_) for _ in list(dataset.iloc[:, 1])]

    Pair_ = []
    for ii in range(len(Drug_)):
        pair_ = (Cell_[ii], Drug_[ii])
        Pair_.append(pair_)

    CellList = []
    DrugList = []
    IC50List = []
    for ii in range(len(Drug)):
        pair = (Cell[ii], Drug[ii])
        if pair not in Pair_:
            CellList.append(Cell[ii])
            DrugList.append(Drug[ii])
            IC50List.append(IC50[ii])

    return CellList, DrugList, IC50List


def GetTrainData(total_csv_path, val_csv_path, test_csv_path):
    dataset = pd.read_csv(total_csv_path, header=0)
    Cell = [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug = [str(_) for _ in list(dataset.iloc[:, 1])]
    IC50 = [float(_) for _ in list(dataset.iloc[:, -1])]

    Cell, Drug, IC50 = LenientRemove(Cell, Drug, IC50, val_csv_path, test_csv_path)

    Graph = []
    for ii in range(len(Cell)):
        graph = GRAPH_dict[Drug[ii]]
        x, edge_index, edge_attr = MolGNet_dict[Drug[ii]], graph.edge_index, graph.edge_attr
        graph = Data(x=x, edge_index=edge_index, edge_attr=edge_attr,
                     GEF=torch.tensor(RMA_dict[Cell[ii]], dtype=torch.float32),
                     BNF=torch.tensor(BNF_dict[Cell[ii]], dtype=torch.float32),
                     ic50=torch.tensor([IC50[ii]], dtype=torch.float32))
        Graph.append(graph)

    return Graph


if debug == 0:
    Gtrain = GetTrainData(total_set_path, val_set_path, test_set_path)
else:
    Gtrain = GetData(val_set_path)
# Gval = GetData(val_set_path)
Gtest = GetData(test_set_path)


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

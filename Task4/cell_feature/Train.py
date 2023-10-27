import joblib
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import time

from Model import *
from Model_DAE import Encoder, Decoder
from Data import *
from TrainConfig import *

sampler = setup_seed(seed)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def test(model_path):
    # create model
    _, model, encoder, _ = joblib.load(model_path)
    model = model.to(DEVICE)
    encoder = encoder.to(DEVICE)

    # load data
    my_collate = CollateFn()
    test_loader = DataLoader(MyDataSet(Gtest), batch_size=batch_size, shuffle=False, collate_fn=my_collate)
    # testing
    model.eval()
    encoder.eval()
    cell_ft = []
    with torch.no_grad():
        for it, (pyg_batch, GeneFt, BionicFT) in enumerate(test_loader):
            pyg_batch, GeneFt, BionicFT = pyg_batch.to(DEVICE), GeneFt.to(DEVICE), BionicFT.to(DEVICE)
            GeneFt = encoder(GeneFt)
            prediction, cft = model(pyg_batch.x, pyg_batch, GeneFt, BionicFT)
            cell_ft += cft.cpu().tolist()
    return torch.tensor(cell_ft)


ft = test('../fold=0_model=2/result/Train.pkl')
ft += test('../fold=1_model=2/result/Train.pkl')
ft += test('../fold=2_model=2/result/Train.pkl')
ft += test('../fold=3_model=2/result/Train.pkl')
ft += test('../fold=4_model=2/result/Train.pkl')
ft /= 5

ft_d = dict()
cell = list(scRNAseq_Dict_sc.keys())
print(len(ft))
print(len(ft[0]))
for i in range(len(cell)):
    ft_d[cell[i]] = ft[i, :].tolist()
joblib.dump(ft_d, 'single_cell_ft.pkl')

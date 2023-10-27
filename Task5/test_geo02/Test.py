import torch.optim as optim
from torch.utils.data import DataLoader
import time

from Model import *
from Model_DAE import Encoder, Decoder
from Data import *
from TrainConfig import *

sampler = setup_seed(seed)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
test_pre_rec_1 = dict()
test_pre_rec_2 = dict()

# create model
_, model_1, encoder_1, _ = joblib.load('../fold=0_model=2/result/Train.pkl')
_, model_2, encoder_2, _ = joblib.load('../fold=1_model=2/result/Train.pkl')
_, model_3, encoder_3, _ = joblib.load('../fold=2_model=2/result/Train.pkl')
_, model_4, encoder_4, _ = joblib.load('../fold=3_model=2/result/Train.pkl')
_, model_5, encoder_5, _ = joblib.load('../fold=4_model=2/result/Train.pkl')

# load data
my_collate = CollateFn()
test_loader_1 = DataLoader(MyDataSet(G_pCR), batch_size=batch_size, shuffle=False, collate_fn=my_collate)
test_loader_2 = DataLoader(MyDataSet(G_RD), batch_size=batch_size, shuffle=False, collate_fn=my_collate)


# testing
def test(model, encoder, test_loader):
    model.eval()
    encoder.eval()
    test_pre = []
    with torch.no_grad():
        for it, (pyg_batch, GeneFt, BionicFt) in enumerate(test_loader):
            pyg_batch, GeneFt, BionicFt = pyg_batch.to(DEVICE), GeneFt.to(DEVICE), BionicFt.to(DEVICE)
            GeneFt = encoder(GeneFt)
            prediction = model(pyg_batch.x, pyg_batch, GeneFt, BionicFt)
            test_pre += torch.squeeze(prediction).cpu().tolist()
    return test_pre


pCR_pre = np.array(test(model_1, encoder_1, test_loader_1), dtype=np.float32)
pCR_pre += np.array(test(model_2, encoder_2, test_loader_1), dtype=np.float32)
pCR_pre += np.array(test(model_3, encoder_3, test_loader_1), dtype=np.float32)
pCR_pre += np.array(test(model_4, encoder_4, test_loader_1), dtype=np.float32)
pCR_pre += np.array(test(model_5, encoder_5, test_loader_1), dtype=np.float32)
pCR_pre /= 5

RD_pre = np.array(test(model_1, encoder_1, test_loader_2), dtype=np.float32)
RD_pre += np.array(test(model_2, encoder_2, test_loader_2), dtype=np.float32)
RD_pre += np.array(test(model_3, encoder_3, test_loader_2), dtype=np.float32)
RD_pre += np.array(test(model_4, encoder_4, test_loader_2), dtype=np.float32)
RD_pre += np.array(test(model_5, encoder_5, test_loader_2), dtype=np.float32)
RD_pre /= 5

dataframe = pd.DataFrame({'Cell': Cell_ls_pCR, 'pCR': pCR_pre.tolist()})
dataframe.to_csv('predict_pCR.csv', index=False, sep=',')
dataframe = pd.DataFrame({'Cell': Cell_ls_RD, 'RD': RD_pre.tolist()})
dataframe.to_csv('predict_RD.csv', index=False, sep=',')

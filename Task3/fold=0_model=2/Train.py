import torch.optim as optim
from torch.utils.data import DataLoader
import time

from Model import *
from Model_DAE import Encoder, Decoder
from Data import *
from TrainConfig import *

sampler = setup_seed(seed)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
test_pre_rec = dict()

# create model
encoder, _ = joblib.load('../PreTrain/PreTrain.pkl')
encoder = encoder.to(DEVICE)

model = Predictor(embedding_dim, heads, fc_layer_num, fc_layer_dim, dropout_rate).to(DEVICE)

loss_func = nn.MSELoss()
params = [
    {'params': encoder.parameters(), 'lr': 0.5 * lr},
    {'params': model.parameters()}
]
optimizer = optim.Adam(params, lr=lr)

# load data
my_collate = CollateFn()
train_loader = DataLoader(MyDataSet(Gtrain), batch_size=batch_size, shuffle=True, collate_fn=my_collate)
test_loader = DataLoader(MyDataSet(Gtest), batch_size=batch_size, shuffle=False, collate_fn=my_collate)
# train model
for epoch in range(EPOCHS):
    start = time.time()
    # training
    model.train()
    encoder.train()
    epoch_loss = 0
    for it, (pyg_batch, GeneFt, BionicFt) in enumerate(train_loader):
        pyg_batch, GeneFt, BionicFt = pyg_batch.to(DEVICE), GeneFt.to(DEVICE), BionicFt.to(DEVICE)
        GeneFt = encoder(GeneFt)
        prediction = model(pyg_batch.x, pyg_batch, GeneFt, BionicFt)
        loss = loss_func(torch.squeeze(prediction), pyg_batch.ic50)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.detach().item()
    epoch_loss /= (it + 1)
    print('Epoch {}, loss {:.8f}'.format(epoch, epoch_loss), end=' ')
    with open(save_path_log, 'a') as file0:
        print('Epoch {}, loss {:.8f}'.format(epoch, epoch_loss), end=' ', file=file0)
    # testing
    model.eval()
    encoder.eval()
    test_epoch_loss = 0
    test_real = []
    test_pre = []
    with torch.no_grad():
        for it, (pyg_batch, GeneFt, BionicFt) in enumerate(test_loader):
            pyg_batch, GeneFt, BionicFt = pyg_batch.to(DEVICE), GeneFt.to(DEVICE), BionicFt.to(DEVICE)
            GeneFt = encoder(GeneFt)
            prediction = model(pyg_batch.x, pyg_batch, GeneFt, BionicFt)
            loss = loss_func(torch.squeeze(prediction), pyg_batch.ic50)
            test_real += pyg_batch.ic50.cpu().tolist()
            test_pre += torch.squeeze(prediction).cpu().tolist()
            test_epoch_loss += loss.detach().item()
        test_epoch_loss /= (it + 1)
        print('test loss {:.8f}'.format(test_epoch_loss), end=' ')
        with open(save_path_log, 'a') as file0:
            print('test loss {:.8f}'.format(test_epoch_loss), file=file0)
    end = time.time()
    print(end - start)
    # saving
    if epoch == 0:
        test_pre_rec['real'] = test_real
    test_pre_rec[epoch] = test_pre
    dataframe = pd.DataFrame(test_pre_rec)
    dataframe.to_csv(save_path_prediction, index=False, sep=',')
    if epoch == 99:
        joblib.dump((epoch, model, encoder, test_pre_rec), save_path_model)

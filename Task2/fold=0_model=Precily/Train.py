import torch.optim as optim
from torch.utils.data import DataLoader
import time

from Model import *
from Data import *
from TrainConfig import *

sampler = setup_seed(seed)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
test_pre_rec = dict()

model = DenseLayers(fc_layer_num, fc_layer_dim, dropout_rate).to(DEVICE)

loss_func = nn.MSELoss()
params = [
    {'params': model.parameters()}
]
optimizer = optim.Adam(params, lr=lr)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.1)

# load data
my_collate = CollateFn()
train_loader = DataLoader(MyDataSet(Gtrain), batch_size=batch_size, shuffle=True, collate_fn=my_collate)
test_loader = DataLoader(MyDataSet(Gtest), batch_size=batch_size, shuffle=False, collate_fn=my_collate)
# train model
for epoch in range(EPOCHS):
    start = time.time()
    # training
    model.train()
    epoch_loss = 0
    for it, Ft in enumerate(train_loader):
        Ft = Ft.to(DEVICE)
        prediction = model(Ft[:, :-1])
        loss = loss_func(torch.squeeze(prediction), Ft[:, -1])
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.detach().item()
    scheduler.step()
    epoch_loss /= (it + 1)
    print('Epoch {}, loss {:.8f}'.format(epoch, epoch_loss), end=' ')
    with open(save_path_log, 'a') as file0:
        print('Epoch {}, loss {:.8f}'.format(epoch, epoch_loss), end=' ', file=file0)
    # testing
    model.eval()
    test_epoch_loss = 0
    test_real = []
    test_pre = []
    with torch.no_grad():
        for it, Ft in enumerate(test_loader):
            Ft = Ft.to(DEVICE)
            prediction = model(Ft[:, :-1])
            loss = loss_func(torch.squeeze(prediction), Ft[:, -1])
            test_real += Ft[:, -1].cpu().tolist()
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
    if epoch == 9:
        joblib.dump((epoch, model, test_pre_rec), save_path_model)

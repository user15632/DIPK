
EPOCHS = 10
batch_size = 64
lr = 1e-05

seed = 14946934

embedding_dim = None
heads = None
fc_layer_num = 3
fc_layer_dim = [256, 128, 1, 1, 1, 1]
dropout_rate = 0.3

save_path_log = './result/Train.txt'
save_path_prediction = './result/Train.csv'
save_path_model = './result/Train.pkl'

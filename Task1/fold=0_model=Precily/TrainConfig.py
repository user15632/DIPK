from Data import fold_num

EPOCHS = 100
batch_size = 128

seed = 14946934

if fold_num == 0:
    lr = 1e-04
    fc_layer_num = 3
    fc_layer_dim = [140, 200, 1, 1, 1, 1]
    dropout_rate = 0.1
elif fold_num == 1:
    lr = 1e-04
    fc_layer_num = 6
    fc_layer_dim = [196, 196, 200, 148, 144, 1]
    dropout_rate = 0.1
elif fold_num == 2:
    lr = 1e-04
    fc_layer_num = 3
    fc_layer_dim = [204, 204, 1, 1, 1, 1]
    dropout_rate = 0.2
elif fold_num == 3:
    lr = 1e-04
    fc_layer_num = 4
    fc_layer_dim = [156, 156, 168, 1, 1, 1]
    dropout_rate = 0.1
elif fold_num == 4:
    lr = 1e-03
    fc_layer_num = 5
    fc_layer_dim = [160, 152, 212, 200, 1, 1]
    dropout_rate = 0.1

save_path_log = './result/Train.txt'
save_path_prediction = './result/Train.csv'
save_path_model = './result/Train.pkl'

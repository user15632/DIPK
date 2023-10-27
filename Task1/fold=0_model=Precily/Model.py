import torch
import random
import numpy as np
from optuna.samplers import TPESampler
import torch.nn as nn
import torch.nn.functional as F

features_dim = 1429
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class DenseLayers(nn.Module):
    def __init__(self, fc_layer_num, fc_layer_dim, dropout_rate):
        super(DenseLayers, self).__init__()
        self.fc_layer_num = fc_layer_num
        self.fc_input = nn.Linear(features_dim, features_dim)
        self.fc_layers = torch.nn.Sequential(
            nn.Linear(features_dim, 512),
            nn.Linear(512, fc_layer_dim[0]),
            nn.Linear(fc_layer_dim[0], fc_layer_dim[1]),
            nn.Linear(fc_layer_dim[1], fc_layer_dim[2]),
            nn.Linear(fc_layer_dim[2], fc_layer_dim[3]),
            nn.Linear(fc_layer_dim[3], fc_layer_dim[4]),
            nn.Linear(fc_layer_dim[4], fc_layer_dim[5])
        )
        self.dropout_layers = torch.nn.ModuleList(
            [nn.Dropout(p=dropout_rate) for _ in range(fc_layer_num)]
        )
        self.fc_output = nn.Linear(fc_layer_dim[fc_layer_num - 2], 1)

    def forward(self, f):
        f = F.relu(self.fc_input(f))
        for layer_index in range(self.fc_layer_num):
            f = F.relu(self.fc_layers[layer_index](f))
            f = self.dropout_layers[layer_index](f)
        f = self.fc_output(f)
        return f


def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    sampler = TPESampler(seed=seed)
    return sampler

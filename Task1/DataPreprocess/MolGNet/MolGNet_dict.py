import joblib

from Model_GNN import *
from util import *
Self_loop = Self_loop()
Add_seg_id = Add_seg_id()

GRAPH_dict = joblib.load('../DRUG/GRAPH_dict.pkl')
MolGNet_dict = dict()

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
gnn = MolGNet(num_layer=5, emb_dim=768, heads=12, num_message_passing=3, drop_ratio=0)
gnn.load_state_dict(torch.load('../../../Data/MolGNet.pt'))
gnn = gnn.to(DEVICE)
gnn.eval()
with torch.no_grad():
    for each in GRAPH_dict:
        graph = GRAPH_dict[each]
        graph = Self_loop(graph)
        graph = Add_seg_id(graph)
        graph = graph.to(DEVICE)
        MolGNet_dict[each] = gnn(graph).cpu()
joblib.dump(MolGNet_dict, 'MolGNet_dict.pkl')

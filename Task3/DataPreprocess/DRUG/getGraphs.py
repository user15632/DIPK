import joblib
from rdkit import Chem
from loader import mol_to_graph_data_obj_complex

SMILES_dict = joblib.load('SMILES_dict.pkl')
GRAPH_dict = dict()
for each in SMILES_dict:
    GRAPH_dict[each] = mol_to_graph_data_obj_complex(Chem.MolFromSmiles(SMILES_dict[each]))
    # Data(x=[num_nodes, 8], edge_index=[2, num_edges], edge_attr=[num_edges, 5])
joblib.dump(GRAPH_dict, 'GRAPH_dict.pkl')


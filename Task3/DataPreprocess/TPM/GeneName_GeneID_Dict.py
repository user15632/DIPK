import joblib

f = open('gene_list_sel.txt', encoding='gbk')
gene_name = []
for each_row in f:
    gene_name.append(each_row.strip())

f = open('../../../Data/gencode.v19.genes.v7_model.patched_contigs.gtf.txt', encoding='gbk')
gene_id_list = []
gene_name_list = []
for each_row in f:
    row = each_row.strip().split(';')
    id = row[0].split("\"")[-2]
    name = row[4].split("\"")[-2]
    if id not in gene_id_list:
        gene_id_list.append(id)
        gene_name_list.append(name)

Dict = dict()
for each in gene_name:
    ID_list = []
    for i in range(len(gene_id_list)):
        if each == gene_name_list[i]:
            ID_list.append(gene_id_list[i])
    Dict[each] = ID_list
joblib.dump(Dict, 'GeneName_GeneID_Dict.pkl')

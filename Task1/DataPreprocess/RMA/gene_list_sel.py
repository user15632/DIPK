import pandas as pd

f = open('../../../Data/key.genes.txt', encoding='gbk')
gene_list_1 = []
for each_row in f:
    gene_list_1.append(each_row.strip())

dataset = pd.read_csv('../../../Data/Cell_line_RMA_proc_basalExp.txt', header=None, sep='\t', low_memory=False)
gene_list_2 = [str(_) for _ in list(dataset.iloc[1:, 0])]

genes = sorted(list(set(gene_list_1) & set(gene_list_2)))

for each in genes:
    with open('gene_list_sel.txt', 'a') as file0:
        print(each, file=file0)

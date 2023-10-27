
f = open('../../../Data/key.genes.txt', encoding='gbk')
gene_list_1 = []
for each_row in f:
    gene_list_1.append(each_row.strip())

f = open('../../../Data/gencode.v19.genes.v7_model.patched_contigs.gtf.txt', encoding='gbk')
gene_list_2 = []
for each_row in f:
    row = each_row.strip().split(';')
    gene_list_2.append(row[4].split("\"")[-2])

f = open('../../../Data/GSE157220_CPM_data.txt', encoding='gbk')
gene_list_3 = []
for each_row in f:
    gene_list_3.append(each_row.strip().split('\t')[0])

genes = sorted(list((set(gene_list_1) & set(gene_list_2)) & set(gene_list_3)))

for each in genes:
    with open('gene_list_sel.txt', 'a') as file0:
        print(each, file=file0)

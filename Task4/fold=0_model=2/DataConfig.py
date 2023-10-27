import os
import re

gene_add_num = 256
debug = 0

folder = os.path.dirname(os.path.abspath('__file__'))
folder = folder.split('/')[-1].split('\\')[-1]
num = re.findall("\d+\.?\d*", folder)
fold_num = int(num[0])
print(fold_num)

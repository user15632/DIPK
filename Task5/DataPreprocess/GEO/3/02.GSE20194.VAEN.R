setwd("D:/desktop/Code/AI_PY310/Model/Task5/DataPreprocess/GEO/3")

### key genes
cur.genes = read.table("gene_list_sel.txt", as.is=T)
cur.genes = cur.genes[,1]

###
load("GSE20194.RData")
val.RPKM = expr.mat

match(cur.genes, rownames(val.RPKM)) -> ii

#> summary(ii)
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's
#      2    3081    5960    6082    9145   12546    1567


new.RPKM = val.RPKM[ii, ]
apply(new.RPKM, 2, function(u){u[is.na(u)] = 0; u} ) -> raw.RPKM
rownames(raw.RPKM) = cur.genes

write.csv(raw.RPKM, 'raw.RPKM.csv')

setwd("D:/desktop/Code/AI_PY310/Model/Task5/DataPreprocess/GEO/2")

### key genes
cur.genes = read.table("gene_list_sel.txt", as.is=T)
cur.genes = cur.genes[,1]

load("GSE32646.RData")
val.RPKM = expr.mat

match(cur.genes, rownames(val.RPKM)) -> ii
summary(ii)

#> summary(ii)
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's
#      5    5061   11324   10604   16771   21652     302

new.RPKM = val.RPKM[ii, ]
apply(new.RPKM, 2, function(u){u[is.na(u)] = 0; u} ) -> raw.RPKM
rownames(raw.RPKM) = cur.genes

write.csv(raw.RPKM, 'raw.RPKM.csv')

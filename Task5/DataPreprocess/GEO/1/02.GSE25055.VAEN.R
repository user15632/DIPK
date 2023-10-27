setwd("D:/desktop/Code/AI_PY310/Model/Task5/DataPreprocess/GEO/1")

### key genes
cur.genes = read.table("gene_list_sel.txt", as.is=T)
cur.genes = cur.genes[,1]

load("GSE25055.RData")
val.RPKM = expr.mat

grep("^RPS", rownames(val.RPKM)) -> ii.1
grep("^RPL", rownames(val.RPKM)) -> ii.2
val.RPKM = val.RPKM[-c(ii.1, ii.2),]


match(cur.genes, rownames(val.RPKM)) -> ii
new.RPKM = val.RPKM[ii, ]
apply(new.RPKM, 2, function(u){u[is.na(u)] = 0; u} ) -> raw.RPKM
rownames(raw.RPKM) = cur.genes

write.csv(raw.RPKM, 'raw.RPKM.csv')

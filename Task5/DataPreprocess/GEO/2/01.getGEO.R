setwd("D:/desktop/Code/AI_PY310/Model/Task5/DataPreprocess/GEO/2")
library("GEOquery")
library("limma")

###################################################################################################
# code chunk: GSE32646
###################################################################################################
rm(list=ls())

gse <- read.table("GSE32646_series_matrix.txt", header = TRUE, sep = "\t", skip = 81, row.names=1)
data.matrix(gse) -> datExpr0
# gse <- getGEO("GSE32646", GSEMatrix = TRUE)
# exprs(gse[[1]]) -> datExpr0

########## section 1

library('preprocessCore')
normalize.quantiles(datExpr0) -> datExprLQ
dimnames(datExprLQ) = dimnames(datExpr0)

########## section 1 end

########## section 2
gpl = getGEO("GPL570")
Table(gpl) -> anno

anno[,11] -> ss
grep("/", anno[,11] ) -> ii
anno = anno[-ii, ]

datExprLQ = datExprLQ[which(rownames(datExprLQ) %in% anno[,1]),]

match(rownames(datExprLQ), anno[,1]) -> ii
symbol = anno[ii, 11]

apply(datExprLQ, 2, function(u)tapply(u, symbol, median)) -> expr.mat

# pData(gse[[1]]) -> pheno.anno

# save(expr.mat, pheno.anno, file="GSE32646.RData")

save(expr.mat, file="GSE32646.RData")

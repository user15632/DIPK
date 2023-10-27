setwd("D:/desktop/Code/AI_PY310/Model/Task5/DataPreprocess/GEO/3")
library("GEOquery")
library("limma")
library("preprocessCore")

###################################################################################################
# code chunk: GSE20194
###################################################################################################
rm(list=ls())

gse <- read.table("GSE20194_series_matrix.txt", header = TRUE, sep = "\t", skip = 81, row.names=1)
data.matrix(gse) -> datExpr0
# gse <- getGEO("GSE20194", GSEMatrix = TRUE)
# exprs(gse[[1]]) -> datExpr0

normalize.quantiles(datExpr0) -> datExprLQ
dimnames(datExprLQ) = dimnames(datExpr0)

########## section 2

gpl = getGEO("GPL96")
Table(gpl) -> anno

grep("/", anno[,11]) -> check
anno = anno[-check,]
anno = anno[anno[,11]!="", ]


datExprLQ = datExprLQ[which(rownames(datExprLQ) %in% anno[,1]),]
match(rownames(datExprLQ), anno[,1]) -> ii
symbol = anno[ii, 11]

apply(datExprLQ, 2, function(u)tapply(u, symbol, median)) -> expr.mat

# pData(gse[[1]]) -> pheno.anno

# save(expr.mat, pheno.anno, file="GSE20194.RData")

save(expr.mat, file="GSE20194.RData")

setwd("D:/desktop/Code/AI_PY310/Model/Task1/DataPreprocess/Pathway")

library(GSEABase)
library(GSVA)
library(impute)
library(ggpubr)

df <- read.csv('RMA_N_dict.csv', header=1, row.names=1, sep=',')
df = data.matrix(df)
geneSets = getGmt("c2.cp.v6.1.symbols.gmt")
enrichment.scores <- gsva(df, geneSets, method="gsva")

write.csv(enrichment.scores, 'Pathway.csv')

setwd("C:/Users/19844/Desktop/aModel/Figure/Task4")

library(ggplot2)
library(RColorBrewer)
library(patchwork)
library(foreign)
library(grid)
library(gridExtra)
library(ggpubr)

my_colors <- brewer.pal(3, "Set2")
model_ls = c('Precily', 'BGME')

FigBar <- function(csv_path, my_colors, xlabel, ylim, model_ls, tag, labels){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(df, aes(x = df[,'category'], y = df[,'value'], 
                        fill = factor(df[,'group'], levels=model_ls))) +
    geom_bar(stat = "identity", position = "dodge", color = "black") +
    scale_fill_manual(values = my_colors, labels = c('Precily', 'DIPK')) +
    labs(x = " \n ", tag = tag) +
    coord_cartesian(ylim = ylim) +
    scale_x_discrete(labels = labels)+
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          axis.title.x = element_blank(),
          axis.title.y = element_blank(),
          legend.title = element_blank())
  return(Fig)
}

bar_t1_1 = FigBar('Task4_Result_1.csv', my_colors, NULL, c(0.45, 2.25), model_ls, 'a', c('MSE', 'RMSE'))
bar_t1_2 = FigBar('Task4_Result_2.csv', my_colors, NULL, c(0.585, 0.885), model_ls, 'b', c('PCC', 'R2'))
p1 = grid.arrange(bar_t1_1, bar_t1_2, nrow = 2)

library(ggplot2)
library(tidyverse)
library(Rtsne)

data <- read.csv("single_cell_ft.csv")
df <- read.csv("single_cell_ft_.csv")

set.seed(0)
tsne <- Rtsne(as.matrix(t(data)), dims = 2)

tsne_df <- data.frame(tsne$Y, label = t(df[1,]))
colnames(tsne_df) <- c("tSNE_1", "tSNE_2", "label")

p2 = ggplot(tsne_df, aes(x = tsne_df[,"tSNE_1"], y = tsne_df[,"tSNE_2"], color = tsne_df[,"label"])) +
    scale_color_brewer(palette = "Spectral") +
    geom_point(size = 0.9, alpha = 0.8) +
    labs(x = "tSNE_1") +
    labs(y = "tSNE_2") +
    labs(tag = "c") +
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          legend.title = element_blank(),
          axis.title.x = element_blank(),
          axis.title.y = element_blank())

p = grid.arrange(p1, p2, nrow = 1, widths = c(1, 2.9))
ggsave("Fig_Task4.pdf", plot = p, units = "cm", width = 28, height = 17, dpi = 5000)

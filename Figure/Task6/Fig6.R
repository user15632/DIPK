setwd("C:/Users/19844/Desktop/aModel/Figure/AE")

library(ggplot2)
library(RColorBrewer)
library(patchwork)
library(foreign)
library(grid)
library(gridExtra)
library(ggpubr)

my_colors <- brewer.pal(3, "Set2")

model_ls = c('BME', 'GME', 'BGME')

FigBar2 <- function(csv_path, my_colors, xlabel, ylim, model_ls, tag, labels){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(df, aes(x = df[,'category'], y = df[,'value'], 
                        fill = factor(df[,'group'], levels=model_ls))) +
    geom_bar(stat = "identity", position = "dodge", color = "black") +
    scale_fill_manual(values = my_colors, labels = c('DIM', 'DEM', 'DIPK')) +
    labs(x = xlabel, tag = tag) +
    coord_cartesian(ylim = ylim) +
    scale_x_discrete(labels = labels)+
    theme(text = element_text(family = "serif", color = "black", size = 14),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 14),
          axis.title.y = element_blank(),
          legend.title = element_blank(),
          legend.position="none")
  return(Fig)
}

FigBar <- function(csv_path, my_colors, xlabel, ylim, model_ls, tag, labels){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(df, aes(x = df[,'category'], y = df[,'value'], 
                        fill = factor(df[,'group'], levels=model_ls))) +
    geom_bar(stat = "identity", position = "dodge", color = "black") +
    scale_fill_manual(values = my_colors, labels = c('DIM', 'DEM', 'DIPK')) +
    labs(x = xlabel, tag = tag) +
    coord_cartesian(ylim = ylim) +
    scale_x_discrete(labels = labels)+
    theme(text = element_text(family = "serif", color = "black", size = 14),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 14),
          axis.title.y = element_blank(),
          legend.title = element_blank(),
          legend.position = "left")
  return(Fig)
}

FigBox <- function(csv_path, my_colors, xlabel, ylim, model_ls, num, tag){
  df <- read.csv(csv_path, header = 1, sep=',')
  ls = factor(c(rep(model_ls[1], num), rep(model_ls[2], num), rep(model_ls[3], num)), 
              levels=model_ls)
  df <- data.frame(
    x = ls,
    y = c(df[,model_ls[1]], df[,model_ls[2]], df[,model_ls[3]]),
    group = ls
  )
  Fig <- ggplot(df, aes(x = x, y = y, fill = x)) +
    geom_boxplot(outlier.shape = NA) +
    scale_fill_manual(values = my_colors) +
    coord_cartesian(ylim = ylim) +
    labs(x = xlabel, tag = tag) +
    scale_x_discrete(labels = c('DIM', 'DEM', 'DIPK'))+
    theme(text = element_text(family = "serif", color = "black", size = 14),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 14),
          axis.title.y = element_blank(),
          legend.title = element_blank(),
          legend.position="none")
  return(Fig)
}

# in Task1
cell_num = 953
drug_num = 206

box_cell_t1_1 = FigBox('MSE_Cell.csv', my_colors, 'MSE for each cell line', c(0, 1.9), model_ls, cell_num, 'c')
box_cell_t1_2 = FigBox('Pearson_Cell.csv', my_colors, 'PCC for each cell line', c(0.8, 1), model_ls, cell_num, 'd')
box_cell_t1_3 = FigBox('R2_Cell.csv', my_colors, 'R2 for each cell line', c(0.56, 1), model_ls, cell_num, 'e')

box_drug_t1_1 = FigBox('MSE_Drug.csv', my_colors, 'MSE for each drug', c(0.15, 1.85), model_ls, drug_num, 'f')
box_drug_t1_2 = FigBox('Pearson_Drug.csv', my_colors, 'PCC for each drug', c(0.38, 0.95), model_ls, drug_num, 'g')
box_drug_t1_3 = FigBox('R2_Drug.csv', my_colors, 'R2 for each drug', c(0.03, 0.9), model_ls, drug_num, 'h')

bar_t1_1 = FigBar('Task1_Result_1.csv', my_colors, ' ', c(0.5, 0.95), model_ls, 'a', c('MSE', 'RMSE'))
bar_t1_2 = FigBar('Task1_Result_2.csv', my_colors, ' ', c(0.8, 0.95), model_ls, 'b', c('PCC', 'R2'))

# in Task2
cell_num = 98
drug_num = 20
model_num = 25

box_cell_t2 = FigBox('MSE_Cell_Task2.csv', my_colors, 'MSE for each cell line', c(1, 8.3), model_ls, cell_num, 'k')
box_drug_t2 = FigBox('MSE_Drug_Task2.csv', my_colors, 'MSE for each drug', c(0.75, 7.85), model_ls, drug_num, 'l')

box_t2 = FigBox('Task2_Result_2.csv', my_colors, 'MSE for each model', c(3, 6.8), model_ls, model_num, 'j')
bar_t2 = FigBar2('Task2_Result_1.csv', my_colors, ' ', c(0, 4.5), model_ls, 'i', c('MSE', 'RMSE'))

p = grid.arrange(bar_t1_1, box_cell_t1_1, box_cell_t1_2, box_cell_t1_3, bar_t2, box_t2,
                 bar_t1_2, box_drug_t1_1, box_drug_t1_2, box_drug_t1_3, box_cell_t2, box_drug_t2, nrow = 2, 
                 widths = c(1.45, 1, 1, 1, 1, 1))

ggsave("Fig6.pdf", plot = p, units = "cm", width = 36.5, height = 17, dpi = 5000)

setwd("C:/Users/19844/Desktop/response/Paper1结果图/Task1&2&3")

library(ggplot2)
library(RColorBrewer)
library(patchwork)
library(foreign)
library(grid)
library(gridExtra)
library(ggpubr)
library(ggpointdensity)
library(viridis)

my_colors <- brewer.pal(3, "Set2")
model_ls = c('Precily', 'BGME')

FigPoint <- function(csv_path, my_colors, xlabel, ylabel, tag){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(data = df, mapping = aes(x = df[,'IC50'], y = df[,'IC50_Predict'])) +
    geom_pointdensity(size = 0.8) +
    scale_color_gradientn(colors = my_colors) +
    labs(x = xlabel, y = ylabel, tag = tag) + 
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          legend.title = element_blank(),
          legend.position = c(1, 0),
          legend.justification = c(1, 0)
          )
  return(Fig)
}

FigBar1 <- function(csv_path, my_colors, xlabel, ylim, model_ls, tag, labels){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(df, aes(x = df[,'category'], y = df[,'value'], 
                        fill = factor(df[,'group'], levels=model_ls))) +
    geom_bar(stat = "identity", position = "dodge", color = "black") +
    scale_fill_manual(values = my_colors, labels = c('Precily', 'DIPK')) +
    labs(x = xlabel, tag = tag) +
    coord_cartesian(ylim = ylim) +
    scale_x_discrete(labels = labels)+
    geom_errorbar(data=df, aes(x=df[,'category'], ymin = df[,'value'] - df[,'std'], ymax = df[,'std'] + df[,'value'], group=factor(df[,'group'], levels=model_ls)),
                  position = position_dodge(width = 0.9), width = 0.25, color = "black")+
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          axis.title.y = element_blank(),
          legend.title = element_blank())
  return(Fig)
}

FigBar2 <- function(csv_path, my_colors, xlabel, ylim, model_ls, tag, labels){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(df, aes(x = df[,'category'], y = df[,'value'], 
                        fill = factor(df[,'group'], levels=model_ls))) +
    geom_bar(stat = "identity", position = "dodge", color = "black") +
    scale_fill_manual(values = my_colors, labels = c('Precily', 'DIPK')) +
    labs(x = xlabel, tag = tag) +
    coord_cartesian(ylim = ylim) +
    scale_x_discrete(labels = labels)+
    geom_errorbar(data=df, aes(x=df[,'category'], ymin = df[,'value'] - df[,'std'], ymax = df[,'std'] + df[,'value'], group=factor(df[,'group'], levels=model_ls)),
                  position = position_dodge(width = 0.9), width = 0.25, color = "black")+
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          axis.title.y = element_blank(),
          legend.title = element_blank(),
          legend.position="none")
  return(Fig)
}

FigBox <- function(csv_path, my_colors, xlabel, ylim, model_ls, num, tag){
  df <- read.csv(csv_path, header = 1, sep=',')
  ls = factor(c(rep(model_ls[1], num), rep(model_ls[2], num)), 
              levels=model_ls)
  df <- data.frame(
    x = ls,
    y = c(df[,model_ls[1]], df[,model_ls[2]]),
    group = ls
  )
  Fig <- ggplot(df, aes(x = x, y = y, fill = x)) +
    geom_boxplot(outlier.shape = NA) +
    scale_fill_manual(values = my_colors) +
    coord_cartesian(ylim = ylim) +
    labs(x = xlabel, tag = tag) +
    scale_x_discrete(labels = c('Precily', 'DIPK'))+
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          axis.title.y = element_blank(),
          legend.title = element_blank(),
          legend.position="none")
  return(Fig)
}

cell_num = 953
drug_num = 206

fig = FigPoint('Task1_model=2_result.csv', my_colors, 'Observed LN IC50', 'Predicted LN IC50', 'a')
bar_t1 = FigBar2('Task1_Result_Collate.csv', my_colors, ' ', c(0.5, 1.0), model_ls, 'b', c('MSE', 'PCC', 'R2'))
bar_t2 = FigBar1('Task3_Result_Collate.csv', my_colors, ' ', c(0.6, 1.9), model_ls, 'd', c('MSE', 'PCC', 'R2'))

box_sp = FigBox('MSE_SP.csv', my_colors, 'MSE on novel\ncells and drugs', c(2, 7), model_ls, 25, 'c')

box_cell_t1_1 = FigBox('MSE_Cell.csv', my_colors, 'MSE for\neach cell line', c(0, 2.1), model_ls, cell_num, 'e')
box_cell_t1_2 = FigBox('Pearson_Cell.csv', my_colors, 'PCC for\neach cell line', c(0.76, 1), model_ls, cell_num, 'f')
box_cell_t1_3 = FigBox('R2_Cell.csv', my_colors, 'R2 for\neach cell line', c(0.5, 1), model_ls, cell_num, 'g')

box_drug_t1_1 = FigBox('MSE_Drug.csv', my_colors, 'MSE for\neach drug', c(0.15, 2.03), model_ls, drug_num, 'h')
box_drug_t1_2 = FigBox('Pearson_Drug.csv', my_colors, 'PCC for\neach drug', c(0.27, 0.95), model_ls, drug_num, 'i')
box_drug_t1_3 = FigBox('R2_Drug.csv', my_colors, 'R2 for\neach drug', c(-0.1, 0.9), model_ls, drug_num, 'j')

p1 = grid.arrange(fig, bar_t1, box_sp, bar_t2, nrow = 1, widths = c(1, 0.5, 0.4, 0.8))
p2 = grid.arrange(box_cell_t1_1, box_cell_t1_2, box_cell_t1_3, box_drug_t1_1, box_drug_t1_2, box_drug_t1_3, nrow = 1)
p = grid.arrange(p1, p2, nrow = 2)
ggsave("Fig_Task1.pdf", plot = p, units = "cm", width = 25.8, height = 17, dpi = 5000)

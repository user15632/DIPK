setwd("C:/Users/19844/Desktop/aModel/Figure/Task3")

library(ggplot2)
library(RColorBrewer)
library(patchwork)
library(foreign)
library(grid)
library(gridExtra)
library(ggpubr)

my_colors <- brewer.pal(3, "Set2")
model_ls = c('Precily', 'VAEN', 'BGME')

FigBar <- function(csv_path, my_colors, xlabel, ylim, model_ls, tag, labels){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(df, aes(x = df[,'category'], y = df[,'value'], 
                        fill = factor(df[,'group'], levels=model_ls))) +
    geom_bar(stat = "identity", position = "dodge", color = "black") +
    scale_fill_manual(values = my_colors, labels = c('Precily', 'VAEN', 'DIPK')) +
    labs(x = " \n ", tag = tag) +
    coord_cartesian(ylim = ylim) +
    scale_x_discrete(labels = labels)+
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          axis.title.x = element_blank(),
          axis.title.y = element_blank(),
          legend.title = element_blank(),
          legend.position="none")
  return(Fig)
}

FigBar2 <- function(csv_path, my_colors, xlabel, ylim, model_ls, tag, labels){
  df <- read.csv(csv_path, header = 1, sep=',')
  Fig <- ggplot(df, aes(x = df[,'category'], y = df[,'value'], 
                        fill = factor(df[,'group'], levels=model_ls))) +
    geom_bar(stat = "identity", position = "dodge", color = "black") +
    scale_fill_manual(values = my_colors, labels = c('Precily', 'VAEN', 'DIPK')) +
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

bar_t1_1 = FigBar('Task3_Result_1.csv', my_colors, NULL, c(1.4, 1.85), model_ls, 'a', 'MSE')
bar_t1_2 = FigBar('Task3_Result_2.csv', my_colors, NULL, c(0.8565, 0.8865), model_ls, 'b', 'PCC')
bar_t1_3 = FigBar2('Task3_Result_3.csv', my_colors, NULL, c(0.74, 0.785), model_ls, 'c', 'R2')

p = grid.arrange(bar_t1_1, bar_t1_2, bar_t1_3, nrow = 1, widths = c(1, 1, 1.74))
ggsave("Fig_Task3.pdf", plot = p, units = "cm", width = 14.2, height = 7.4, dpi = 5000)

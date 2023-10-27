setwd("C:/Users/19844/Desktop/aModel/Figure/Task5")

library(ggplot2)
library(RColorBrewer)
library(patchwork)
library(foreign)
library(grid)
library(gridExtra)
library(ggpubr)

my_colors <- brewer.pal(3, "Set2")

FigBox <- function(csv_path, my_colors, xlabel, ylabel, ylim, model_ls, num, tag){
  df1 <- read.csv(csv_path, header = 1, sep=',')
  df <- data.frame(
    x = factor(df1[,2], levels=model_ls),
    y = df1[,1],
    group = factor(df1[,2], levels=model_ls)
  )
  Fig <- ggplot(df, aes(x = x, y = y, fill = x)) +
    geom_boxplot(outlier.shape = NA) +
    scale_fill_manual(values = my_colors) +
    coord_cartesian(ylim = ylim) +
    labs(x = xlabel, y = ylabel, tag = tag) +
    labs(x = xlabel, tag = tag) +
    theme(text = element_text(family = "serif", color = "black", size = 13),
          axis.text = element_text(color = "black", size = 13),
          plot.tag = element_text(size = 18),
          axis.title = element_text(size = 13),
          legend.title = element_blank(),
          legend.position="none")
  return(Fig)
}

model_ls = c('RD', 'pCR')
cell_num = 310
box_1 = FigBox('result_geo01.csv', my_colors, 'p = 5.16e-29', '- LN IC50', c(1.75, 2.9), model_ls, cell_num, 'a')

model_ls = c('nCR', 'pCR')
cell_num = 115
box_2 = FigBox('result_geo02.csv', my_colors, 'p = 5.68e-05', '- LN IC50', c(2.35, 3.8), model_ls, cell_num, 'b')

model_ls = c('RD', 'pCR')
cell_num = 278
box_3 = FigBox('result_geo03.csv', my_colors, 'p = 5.60e-08', '- LN IC50', c(1.65, 2.85), model_ls, cell_num, 'c')

p = grid.arrange(box_1, box_2, box_3, nrow = 1)
ggsave("Fig_Task5.pdf", plot = p, units = "cm", width = 14.8, height = 7.9, dpi = 5000)

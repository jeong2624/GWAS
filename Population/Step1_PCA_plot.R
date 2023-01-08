#!/usr/bin/Rscript
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step1_PCA_plot.R
# Running code : /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step1_PCA_plot.R /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline

# Running code explanation : There are convert_PCA.eigenvec file and Data_P9.ind file in the directory

# Before running R code, you should remove # from #FID in PCA.eigenvec file.

args = commandArgs(trailingOnly=TRUE)

PCA = paste0(args[1], "/convert_PCA.eigenvec")

IND = paste0(args[1], "/Data_P9.ind")

a = read.table(PCA, header = T)

b = read.table(IND, header = F)

c = merge(a,b, by.x = "IID", by.y = "V1")

pdf(paste0(args[1],"/PCA_PC1PC2.pdf"))

plot(c$PC1, c$PC2, col = factor(c$V3), cex = 1.0, xlab = "PC1", ylab = "PC2", main = "Scatter Plot of PC1 vs PC2")

legend("bottomleft", legend = levels(factor(c$V3)), text.col = seq_along(levels(factor(c$V3))))

dev.off()

pdf(paste0(args[1], "/PCA_PC3PC4.pdf"))

plot(c$PC3, c$PC4, col = factor(c$V3), cex = 1.0, xlab = "PC3", ylab = "PC4", main = "Scatter Plot of PC3 vs PC4")

legend("bottomleft", legend = levels(factor(c$V3)), text.col = seq_along(levels(factor(c$V3))))

dev.off()


#!/usr/bin/Rscript
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step2_MDS_plot.R
# Running code : /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step2_MDS_plot.R /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline

# Running code explanation : There are MDS.mds file and Data_P9.ind file in the directory

args = commandArgs(trailingOnly=TRUE)

MDS = paste0(args[1], "/MDS.mds")

IND = paste0(args[1], "/Data_P9.ind")

a = read.table(MDS, header = T)

b = read.table(IND, header = F)

c = merge(a,b, by.x = "IID", by.y = "V1")

pdf(paste0(args[1],"/MDS_C1C2.pdf"))

plot(c$C1, c$C2, col = factor(c$V3), cex = 1.0, xlab = "C1", ylab = "C2", main = "Scatter Plot of C1 vs C2")

legend("bottomleft", legend = levels(factor(c$V3)), text.col = seq_along(levels(factor(c$V3))))

dev.off()

pdf(paste0(args[1], "/MDS_C3C4.pdf"))

plot(c$C3, c$C4, col = factor(c$V3), cex = 1.0, xlab = "C3", ylab = "C4", main = "Scatter Plot of C3 vs C4")

legend("bottomleft", legend = levels(factor(c$V3)), text.col = seq_along(levels(factor(c$V3))))

dev.off()


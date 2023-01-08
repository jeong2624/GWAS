#!/usr/bin/Rscript
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_QQplot.R
# Running code : /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_QQplot.R /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline

# Running code explanation : There are Result.assoc file and Logistic_result.assoc.logistic file in the directory.

args = commandArgs(trailingOnly=TRUE)

library(qqman)

result_assoc = paste0(args[1], "/Result.assoc")

assoc = read.table(result_assoc, header = TRUE)

jpeg(paste0(args[1], "/QQ-Plot_assoc.jpeg"))

qq(assoc$P, main = "Q-Q plot of GWAS p-values : log")

dev.off()

result_logistic = paste0(args[1], "/Logistic_result.assoc.logistic")

logistic = read.table(result_logistic, header = TRUE)

jpeg(paste0(args[1], "/QQ-Plot_logistic.jpeg"))

qq(logistic$P, main = "Q-Q plot of GWAS p-values : log")

dev.off()


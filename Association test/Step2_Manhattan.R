#!/usr/bin/Rscript
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_Manhattan.R
# Running code : /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_Manhattan.R /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline

# Running code explanation : There are Result.assoc file and Logistic_result.assoc.logistic file in the directory.

args = commandArgs(trailingOnly=TRUE)

library(qqman)

result_assoc = paste0(args[1], "/Result.assoc")

assoc = read.table(result_assoc, header = TRUE)

jpeg(paste0(args[1], "/assoc_manhattan.jpeg"))

manhattan(assoc,chr="CHR",bp="BP",p="P",snp="SNP", main = "Manhattan plot: assoc")

dev.off()

result_logistic = paste0(args[1], "/Logistic_result.assoc.logistic")

logistic = read.table(result_logistic, header = TRUE)

jpeg(paste0(args[1], "/Logistic_manhattan.jpeg"))

manhattan(logistic, chr="CHR",bp="BP",p="P",snp="SNP", main = "Manhattan plot: assoc")

dev.off()


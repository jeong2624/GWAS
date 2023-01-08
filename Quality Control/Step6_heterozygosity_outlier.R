#!/usr/bin/Rscript
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step6_heterozygosity_outlier.R
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step6_heterozygosity_outlier.R /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Running code explanation : There is Data_P7.het file in raw_data directory

args = commandArgs(trailingOnly=TRUE)

HET = paste0(args[1], "/Data_P7.het")

## Generate plots to visualize the distribution of heterozygosity rate.

het = read.table(file=HET, header = TRUE)

het$HET_RATE = (het$"N.NM." - het$"O.HOM.")/het$"N.NM."

het_fail = subset(het, (het$HET_RATE < mean(het$HET_RATE)-3*sd(het$HET_RATE)) | (het$HET_RATE > mean(het$HET_RATE)+3*sd(het$HET_RATE)))

het_fail$HET_DST = (het_fail$HET_RATE-mean(het$HET_RATE))/sd(het$HET_RATE)

write.table(het_fail, paste0(args[1], "/Data_P7_fail-het-qc.txt"), row.names=FALSE)

# output : It will automatically make Step10_result_fail-het-qc.txt file.

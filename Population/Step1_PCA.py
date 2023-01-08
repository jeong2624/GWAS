#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step1_PCA.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step1_PCA.py /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline

# Explanation : We have already basic QC for raw data. (Data_P9.bed, Data_P9.bim, Data_P9.fam)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P9.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

IND = "awk 'NR>1{print $2, $5, $7}' " + sys.argv[1] + "/pops_HapMap_3_r3 > " + sys.argv[1] + "/"+ Data_name + ".ind"

sub.call(IND, shell = True)

small_PCA = "plink2 --bfile " + sys.argv[1] + "/" + Data_name + " --pca 10 --out " + sys.argv[1] + "/PCA" # less than 5000 samples.

large_PCA = "plink2 --bfile " + sys.argv[1] + "/" + Data_name + " --pca approx 10 --out " + sys.argv[1] + "/PCA" # more than 5000 samples.

sub.call(small_PCA, shell = True)

convert = "sed 's/#//' " + sys.argv[1] + "/PCA.eigenvec > " + sys.argv[1] + "/convert_PCA.eigenvec"

sub.call(convert, shell = True)

plot = "/home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step1_PCA_plot.R " + sys.argv[1]

sub.call(plot, shell = True)




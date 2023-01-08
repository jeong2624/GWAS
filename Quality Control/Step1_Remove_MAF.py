#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step1_Remove_MAF.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step1_Remove_MAF.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are three raw data in the directory. (Data.bed, Data.fam, Data.bim)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

QCdrop = "awk '{if($1==0) print}' " + sys.argv[1] + "/" + Data_name + ".bim > " + sys.argv[1] + "/QCdrop.SNPs"
sub.call(QCdrop, shell = True)

Remove = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --exclude " + sys.argv[1] + "/QCdrop.SNPs --maf 0.05 --make-bed --out " + sys.argv[1] + "/Data_P2 --noweb"
sub.call(Remove, shell = True)

Pre = "plink --bfile " + sys.argv[1] + "/Data_P2 --logistic --adjust --out " + sys.argv[1] + "/Data_P2_GIF --noweb"
sub.call(Pre, shell = True)

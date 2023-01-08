#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step2_Remove_Genotyping.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step2_Remove_Genotyping.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are three raw data in the directory. (Data_P2.bed, Data_P2.fam, Data_P2.bim)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P2.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

Missing = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --missing --out " + sys.argv[1] + "/Data_P2 --noweb"
sub.call(Missing, shell = True)

QCdrop = "awk '{if($1>22) print}' " + sys.argv[1] + "/Data.bim > " + sys.argv[1] + "/nonAUT.SNPs"
sub.call(QCdrop, shell = True)

individual = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --mind 0.01 --exclude " + sys.argv[1] + "/nonAUT.SNPs --make-bed --out " + sys.argv[1] + "/Data_P2.1 --noweb"

sub.call(individual, shell = True)

fam = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --keep " + sys.argv[1] + "/Data_P2.1.fam --make-bed --out " + sys.argv[1] + "/Data_P3 --noweb"

delete = "rm -rf " + sys.argv[1] + "/Data_P2.1*"
sub.call(fam, shell = True); sub.call(delete, shell = True)

snp = "plink --bfile " + sys.argv[1] + "/Data_P3 --geno 0.01 --make-bed --out " + sys.argv[1] + "/Data_P4 --noweb"
sub.call(snp, shell = True)

#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step5_Calculate_LD.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step5_Calculate_LD.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are three raw data in the directory. (Data_P6.bed, Data_P6.fam, Data_P6.bim)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P6.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

LD = "plink --bfile " + sys.argv[1] + "/Data_P6 --r2 --out " + sys.argv[1] + "/Data_P6 --noweb"
sub.call(LD, shell = True)

high_LD = "awk 'NR>1 {if($7 >= 0.8) print $1, $2, $5, $4}' " + sys.argv[1] + "/Data_P6.ld > " + sys.argv[1] + "/high_LD_regions.txt"
sub.call(high_LD, shell = True)

exclude = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --exclude " + sys.argv[1] + "/high_LD_regions.txt --range --indep-pairwise 50 5 0.2 --out Data_P6 --noweb"
sub.call(exclude, shell = True)

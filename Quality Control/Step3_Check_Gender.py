#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step3_Check_Gender.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step3_Check_Gender.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are three raw data in the directory. (Data_P4.bed, Data_P4.fam, Data_P4.bim)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P4.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

Sex_check = "plink --bfile " + sys.argv[1] + "/Data_P4 --check-sex --out " + sys.argv[1] + "/Data_P4 --noweb"
sub.call(Sex_check, shell = True)

Sex_fail = "awk '{if($5=='PROBLEM') print $1, $2}' " + sys.argv[1] + "/Data_P4.sexcheck > " + sys.argv[1] + "/sexfail"
sub.call(Sex_fail, shell = True)

Remove = "plink --bfile " + sys.argv[1] + "/Data_P4 --remove " + sys.argv[1] + "/sexfail --make-bed --out " + sys.argv[1] + "/Data_P5 --noweb"
sub.call(Remove, shell = True)

#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step4_HWE.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step4_HWE.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are three raw data in the directory. (Data_P5.bed, Data_P5.fam, Data_P5.bim)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P5.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

hwe = "plink --bfile " + sys.argv[1] + "/Data_P5 --hwe 1e-5 --make-bed --out " + sys.argv[1] + "/Data_P6 --noweb"
sub.call(hwe, shell = True)


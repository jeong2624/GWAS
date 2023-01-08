#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step8_GIF.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step8_GIF.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are five raw data in the directory. (Data_P9.bed, Data_P9.fam, Data_P9.bim)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P9.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

Post = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --logistic --adjust --out " + sys.argv[1] + "/Data_P9_GIF --noweb"

sub.call(Post, shell = True)


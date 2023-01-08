#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step2_MDS.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step2_MDS.py /home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline

# Explanation : We have already basic QC for raw data. (Data_P9.bed, Data_P9.bim, Data_P9.fam)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P9.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

MDS = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --filter-founders --genome --mds-plot 4 --out " + sys.argv[1] + "/MDS --noweb" # less than 5000 samples.

sub.call(MDS, shell = True)

plot = "/home/pjw/Desktop/Wonee/GWAS/Population_stratification_Pipeline/Step2_MDS_plot.R " + sys.argv[1]

sub.call(plot, shell = True)




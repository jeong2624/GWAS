#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step6_heterozygosity.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step6_heterozygosity.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are five raw data in the directory. (Data_P6.bed, Data_P6.fam, Data_P6.bim, Data_P6.prune.in, Data_P6.prune.out)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P6.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

heterozygosity = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --extract " + sys.argv[1] + "/Data_P6.prune.in --het --out " + sys.argv[1] + "/Data_P7 --noweb"
sub.call(heterozygosity, shell = True)

outlier = "/home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step6_heterozygosity_outlier.R " + sys.argv[1]
sub.call(outlier, shell = True)

compatible = "sed 's" + '/"' + "// g' " + sys.argv[1] + "/Data_P7_fail-het-qc.txt | awk '{print $1, $2}' > " + sys.argv[1] + "/Data_P7_het-fail_ind.txt"
sub.call(compatible, shell = True)

Remove = "plink --bfile " + sys.argv[1] + "/Data_P6 --remove " + sys.argv[1] + "/Data_P7_het-fail_ind.txt --make-bed --out " + sys.argv[1] + "/Data_P8 --noweb"
sub.call(Remove, shell = True)

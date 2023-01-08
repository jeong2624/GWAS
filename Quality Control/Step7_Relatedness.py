#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step7_Relatedness.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline/Step7_Relatedness.py /home/pjw/Desktop/Wonee/GWAS/QC_Pipeline

# Explanation : There are five raw data in the directory. (Data_P8.bed, Data_P8.fam, Data_P8.bim)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P8.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

pihat = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --genome --out " + sys.argv[1] + "/Data_P8_IBD --noweb"

#sub.call(pihat, shell = True)

drops = "awk 'NR>1 {if ($10 >= 0.25) print }' " + sys.argv[1] + "/Data_P8_IBD.genome > " + sys.argv[1] + "/drops"

sub.call(drops, shell = True)

MZ_twins = "awk '{if($10 > 0.95) print }' " + sys.argv[1] + "/drops > " + sys.argv[1] + "/MZ_twins"

sub.call(MZ_twins, shell = True)

relatedness = "awk '{if($10 < 0.95) print }' " + sys.argv[1] + "/drops > " + sys.argv[1] + "/other_relatedness"

sub.call(relatedness, shell = True)

twins1 = "awk '{if(NR != 1) print $1, $2 }' " + sys.argv[1] + "/MZ_twins > " + sys.argv[1] + "/MZ_twins_list1"

twins2 = "awk '{if(NR != 1) print $3, $4 }' " + sys.argv[1] + "/MZ_twins > " + sys.argv[1] + "/MZ_twins_list2"

sub.call(twins1, shell = True); sub.call(twins2, shell = True)

twins_list = "cat " + sys.argv[1] + "/MZ_twins_list1 " + sys.argv[1] + "/MZ_twins_list2 > " + sys.argv[1] + "/MZ_twins_list"

sub.call(twins_list, shell = True)

sort = "sort " + sys.argv[1] + "/MZ_twins_list | uniq > " + sys.argv[1] + "/unique_MZ_twins_drop_list"

sub.call(sort, shell = True)

other = "awk '{print $1, $2}' " + sys.argv[1] + "/other_relatedness > " + sys.argv[1] + "/other_drop_list"

sub.call(other, shell = True)

all_drop = "cat " + sys.argv[1] + "/other_drop_list " + sys.argv[1] + "/unique_MZ_twins_drop_list > " + sys.argv[1] + "/all_drop_list"

sub.call(all_drop, shell = True)

remove = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --remove " + sys.argv[1] + "/all_drop_list --make-bed --out " + sys.argv[1] + "/Data_P9 --noweb"

sub.call(remove, shell = True)



#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step1_Association.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step1_Association.py /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline

# Explanation : We have already basic QC for raw data and covariate file. (Data_P9.bed, Data_P9.bim, Data_P9.fam, covariate.txt)

import sys; import os; import subprocess as sub

Data_name = filter(lambda x: "Data_P9.bed" in x, os.listdir(sys.argv[1]))[0].replace(".bed", "")

Association = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --assoc --out " + sys.argv[1] + "/Result --noweb" # Basic case/control association test. 

# Note, the --assoc option does not allow to correct covariates such as principal components (PC's)/ MDS components, which makes it less suited for association analyses.

sub.call(Association, shell = True)

# We will be using 10 principal components as covariates in this logistic analysis.

# These two features allow for multiple covariates when testing for both quantitative trait and disease trait SNP association, and for interactions with those covariates.

Logistic = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --covar " + sys.argv[1] + "/PCA.eigenvec --logistic --out " + sys.argv[1] + "/Logistic_result --noweb"

sub.call(Logistic, shell = True) # For disease traits.

Linear = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --linear --out " + sys.argv[1] + "/Linear_result --noweb"

# sub.call(Linear, shell = True) # For quantitative traits.

#### Multiple testing

Multiple = "plink --bfile " + sys.argv[1] + "/" + Data_name + " -assoc --adjust --out " + sys.argv[1] + "/adjusted_assoc_results --noweb"

#sub.call(Multiple, shell = True)

## Generate subset of SNPs

subset = "awk '{ if ($4 >= 21595000 && $4 <= 21605000) print $2 }' " + sys.argv[1] + "/" + Data_name + ".bim > " + sys.argv[1] + "/subset_snp_chr_22.txt"

#sub.call(subset, shell = True)

## Filter your bfile based on the subset of SNPs generated in the step above.
Filter = "plink --bfile " + sys.argv[1] + "/" + Data_name + " --extract " + sys.argv[1] + "/subset_snp_chr_22.txt --make-bed --out " + sys.argv[1] + "/Data_subset_for_perm --noweb"

#sub.call(Filter, shell = True)

## Perform 1000000 permutations.
permutation = "plink --bfile " + sys.argv[1] + "/Data_subset_for_perm --assoc --mperm 1000000 --out " + sys.argv[1] + "/subset_1M_perm_result --noweb"

#sub.call(permutation, shell = True)

## Order your data, from lowest to highest p-value.
sort = "sort -gk 4 " + sys.argv[1] + "/subset_1M_perm_result.assoc.mperm > " + sys.argv[1] + "/sorted_subset.txt"

#sub.call(sort, shell = True)



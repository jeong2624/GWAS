#!/usr/bin/env python
# chmod +x /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_Output.py
# Running code : /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_Output.py /home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline

# Explanation : There are Result.assoc file and Logistic_result.assoc.logistic file in the directory.

import sys; import os; import subprocess as sub

Manhattan = "/home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_Manhattan.R " + sys.argv[1]

sub.call(Manhattan, shell = True)

QQ = "/home/pjw/Desktop/Wonee/GWAS/Association_GWAS_Pipeline/Step2_QQplot.R " + sys.argv[1]

sub.call(QQ, shell = True)

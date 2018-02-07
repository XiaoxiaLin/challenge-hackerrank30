
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.pearsonr.html

from scipy.stats.stats import pearsonr

Physics_Scores = [15,12,8,8,7,7,7,6,5,3]
History_Scores =[10,25,17,11,13,17,20,13,9,15]

print (pearsonr(Physics_Scores, History_Scores))

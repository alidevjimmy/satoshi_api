import numpy as np
from numpy import unravel_index
 
def max_corr(dataframe):
    to_corr = dataframe.corr()
    length = len(to_corr)
    ith , jth = 0 , 1
    maximum = to_corr.iloc[ith][jth]
    for i in range(length):
        for j in range(length):
            if i != j:
                to_corr.iloc[i][j] = to_corr.iloc[i][j]*-1 if to_corr.iloc[i][j] < 0 else None
                if to_corr.iloc[i][j] > maximum:
                    maximum = to_corr.iloc[i][j]
                    ith , jth = i , j
    output = sorted({to_corr.columns[ith] ,to_corr.columns[jth]} , reverse=True)
    return output
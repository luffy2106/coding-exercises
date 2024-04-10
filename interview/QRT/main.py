import pandas
import numpy as np
from typing import List
from queue import Queue













def getMaxProfit(pnl, k):
    all_sublist= []
    for e in range(1,k+1):
        sublist_e = [pnl[i:i+e] for i in range(len(pnl)-e + 1)]
        all_sublist.extend(sublist_e)
    max_sum = 0
    for sublist in all_sublist:
        sum_sublist = sum(sublist)
        if sum_sublist > max_sum:
            max_sum = sum_sublist
    return max_sum
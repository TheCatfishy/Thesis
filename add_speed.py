import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('seqwriteext4.csv')
    print(irisdf.columns)
    irisdf['SPEED'] = (irisdf['BYTES']) / (irisdf['LAT(ms)'] / 1000)
    print(irisdf.columns)
    irisdf.to_csv("seqwriteext4.csv", index=False)
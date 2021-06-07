import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('smallfileserverext4.csv')
    print(irisdf.columns)
    #add red for writes, add blue for reads according to a read or write command.

    irisdf['color'] = ['red' if x == 'W' else 'blue' for x in irisdf['T']]
    print(irisdf.columns)
    irisdf.to_csv("smallfileserverext4.csv", index=False)
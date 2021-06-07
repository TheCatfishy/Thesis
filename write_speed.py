import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('smallwritedeletef2fs.csv')
    minRange = 0
    maxRange = 110
    multiplier = 10
    speedy = irisdf[irisdf['TIME(s)'].between(minRange, maxRange)]
    iops = len(speedy.index)
    read = speedy[(speedy['T'] == 'W')]
    print("iops: ", iops)
    max = read['TIME(s)'].max()
    min = read['TIME(s)'].min()
    print('total written prac: ', read['BYTES'].sum(axis=0))
    print('total time: ', (max - min))
    print("size written: ", 2147.483648)
    print("theoratical MB/s: ", (2147.483648/(max-min)))
    givenRange = np.linspace(0, (int(max)+30), ((int(max)+30)*multiplier))
    df = pd.DataFrame(columns=['Time'])
    for x in givenRange:
        new_row = {'Time': x}
        df = df.append(new_row, ignore_index=True)

    dftest = pd.DataFrame(columns=['MB','MB/s'])

    for x in givenRange:
       df2 = read[read['TIME(s)'].between(x-(0.5/multiplier), x+(0.5/multiplier))]
       new_row = {'MB': (df2['BYTES'].sum(axis=0)/1000000),'MB/s': (df2['BYTES'].sum(axis=0) / (1000000/multiplier))}
       dftest = dftest.append(new_row, ignore_index=True)
    df['MB'] = dftest['MB']
    df['writespeed'] = dftest['MB/s']
    print("practically written: ", df['MB'].sum(axis=0))
    print("practically MB/s: ", (df['MB'].sum(axis=0)) / (max - min))
    ax = df.plot.line(x='Time', y='writespeed', c='red')
    ax.set_title('Sequential write & remove speed ext4')
    ax.set_xlabel("Time in seconds")
    plt.ylim([0, 1700])
    plt.xlim([0, 10])
    ax.set_ylabel("MB/s")
    plt.show()

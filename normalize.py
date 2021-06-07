import pandas as pd

if __name__ == '__main__':
    irisdf = pd.read_csv('smallfileserverext4.csv')
    minSectorF2fs = 492646400
    minSectorExt4 = 1126400
    irisdf['NormSector'] = irisdf['SECTOR']
    irisdf.to_csv("smallfileserverext4.csv", index=False)


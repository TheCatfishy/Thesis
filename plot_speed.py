import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    irisdf = pd.read_csv('sample.csv')
    print(irisdf.columns)
    irisdf["SPEED"].hist(bins=64);
    plt.show()

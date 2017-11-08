#   DataPreparation.py

#import numpy as np
import sys
import CleanData # reading data
from sklearn.model_selection import train_test_split # splitting data

# Check commandline arguments:
if len(sys.argv) != 2:
    print('usage: python3 DataPreparation.py filename.csv')
    sys.exit(1)
else: 
    fname = sys.argv[1]
    for i, a in enumerate(sys.argv): # debugging
        print('argv[{:02d}]: {}'.format(i, a))

# Create a numpy data array and a pandas dataframe
pd,np = CleanData.readCSV(filename=fname, verbose=True)
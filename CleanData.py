# module part1_helper
import numpy, pandas

def readCSV(filename, verbose):
    """ reads csv file and returns pandas data frame and numpy array """
    # Create pandas data frame from .csv 
    pdf = pandas.read_csv(filename,sep=',',header=None) 

    # Use pandas data frame to create numpy array of strings:
    npa = numpy.asarray(pdf.values, dtype=None) 

    # If debugging, output data table's information:
    if (verbose == True):
        print("rows = ", len(pdf), "cols = ", len(pdf[0]))
        print("rows = ", len(npa), "cols = ", len(npa[0]))
    return pdf,npa

def writeCSV(filename, array, verbose):
    """ writes numpy array to csv file """
    numpy.savetxt(filename, array, delimiter=',', fmt='%d')
    return

def create_splits(pdframe, nparray):
    """ Does nothing right now """
    '''
    cleaner.writeCSV(filename = out_fname, array = data, verbose = False)

    # Now separate out the data into attributes and results:
    X = data[:,1:10] # was 0:9
    y = data[:,10] # if one wants to keep IDs, use data[:,(1,10)]

    # Set up testing and training
    sz_train = 0.75 ; sz_test = 0.25
    X_train, X_test, y_train, y_test =\
        train_test_split(X, y, train_size=sz_train, test_size=sz_test) # this defaults to 0.75 for X/y testing

    # saving to files
    X_train_fname = 'X_training-' + in_fname
    X_test_fname = 'X_testing-' + in_fname
    cleaner.writeCSV(filename = X_train_fname, array = X_train, verbose = False)
    cleaner.writeCSV(filename = X_test_fname,  array = X_test,  verbose = False)

    # saving to files
    y_train_fname = 'y_training-' + in_fname
    y_test_fname = 'y_testing-' + in_fname
    cleaner.writeCSV(filename = y_train_fname, array = y_train,  verbose = False)
    cleaner.writeCSV(filename = y_test_fname,  array = y_test, verbose = False)
    '''
    return

def read_splits_from_CSV(filename):
    # reading attribute data from files
    X_train_path = 'X_training-' + filename + '.csv'
    X_test_path  = 'X_testing-' + filename + '.csv'
    X_train = numpy.genfromtxt(X_train_path, delimiter=',') 
    X_test  = numpy.genfromtxt(X_test_path,  delimiter=',') 

    # read outcome data from file
    y_train_path = 'y_training-' + filename + '.csv'
    y_test_path  = 'y_test-' + filename + '.csv'
    y_train = numpy.genfromtxt(y_train_path, delimiter=',') 
    y_test  = numpy.genfromtxt(y_test_path,  delimiter=',') 

    return X_train, X_test, y_train, y_test
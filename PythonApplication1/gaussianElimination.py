import numpy as np
import csv

#
# settings.json has the file settings

with open('settings.json') as json_file:  
    settings = json.load(json_file)
    infile = settings['gaussian']['infile']
    outfile = settings['gaussian']['outfile']

def readcsv():
    matrix = []
    rowData = []
    vector = []
    vectorRow = []

    with open(inFile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            for i in list(row):
               rowData.append(float(i))
            print(', '.join(row))
            vectorRow.append (rowData.pop(0))
            vector.append (vectorRow)
            matrix.append (rowData)
            rowData = []
            vectorRow = []

    return np.array(matrix), np.array(vector)

def GEPP(A, b, doPricing = True):
    '''
    Gaussian elimination with partial pivoting.
    
    input: A is an n x n numpy matrix
           b is an n x 1 numpy array
    output: x is the solution of Ax=b 
            with the entries permuted in 
            accordance with the pivoting 
            done by the algorithm
    post-condition: A and b have been modified.
    '''
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between"+
                         "A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the 
    # upper right triangle, we also use k for indicating the k-th diagonal 
    # column index.
    
    # Elimination
    for k in range(n-1):
        if doPricing:
            # Pivot
            maxindex = abs(A[k:,k]).argmax() + k
            if A[maxindex, k] == 0:
                raise ValueError("Matrix is singular.")
            # Swap
            if maxindex != k:
                A[[k,maxindex]] = A[[maxindex, k]]
                b[[k,maxindex]] = b[[maxindex, k]]
        else:
            if A[k, k] == 0:
                raise ValueError("Pivot element is zero. Try setting doPricing to True.")
        #Eliminate
        for row in range(k+1, n):
            multiplier = A[row,k]/A[k,k]
            A[row, k:] = A[row, k:] - multiplier*A[k, k:]
            b[row] = b[row] - multiplier*b[k]
    # Back Substitution
    x = np.zeros(n)
    fileData = []
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        fileData.append((b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k])
    f=open(outFile,"w")

    for k in range(n):
        f.write(str(x[k]) + ',\n')
    f.close()
    return x


if __name__ == "__main__":
    A, b = readcsv()
    #A = np.array([[1.,-1.,1.,-1.],
    #              [1.,0.,0.,0.],
    #              [1.,1.,1.,1.],
    #              [1.,2.,4.,8.]])
    #b =  np.array([[14.],
    #               [4.],
    #               [2.],
    #               [2.]])
    print(GEPP(np.copy(A), np.copy(b), doPricing = False))
    print(GEPP(A,b))


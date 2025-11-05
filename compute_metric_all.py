import csv
import numpy as np

with open('results.csv', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        C = (row['C'])
        print("C=",C)
        A = (row['A'])
        print("A=",A)
        rough = float(C) / (2*np.pi * np.sqrt(float(A)/np.pi))
        print("rough= ",rough)


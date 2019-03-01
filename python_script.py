#/usr/bin/env python

# 1. load a dataset from files
# 2. organize the data
# 3. summary statistics
# 4. print results
from argparse import ArgumentParser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

parser = ArgumentParser(description="parser")
parser.add_argument("filename", help='path to the file')
args = parser.parse_args()
filename = args.filename

# load data and print first rows
df = pd.read_csv(filename, sep=',', header=None)
print(df.head())

# insert headers and print first rows
types = ['Mean', 'SD', 'Worst']
feature_names =['Radius', 'Texture', 'Perimeter', 'Area', 'Smoothness', 'Compactness', 'Concavity', 'Concavity Points', 'Symmetry', 'Fractal Dimension']
header = ['Id number', 'Diagnosis'] + [type + ' ' + feature  for type in types for feature in feature_names]
header = pd.Series(header)
df.columns = header
print(df.head())

# Display statistical summary
print('Statistical Summary:')
static = pd.DataFrame({'Mean': np.mean(df.iloc[:,2:]), 'Standard Deviation': np.std(df.iloc[:,2:])})
print(static)

# One-feature visualization
cols = df.columns.values[2:].tolist()
for col in cols:
    plt.hist(df[col])
    plt.title('histogram of '+ str(col))
    plt.ylabel(col)
    plt.savefig('one-feature: '+ str(col)+'.pdf')
    # plt.show()

# Two-feature visualization
all_cols = cols
for col1 in cols:
    all_cols.remove(col1)
    for col2 in all_cols:
        plt.scatter(df[col1], df[col2])
        plt.title('scatter plot of ' + str(col1) +' vs feature ' + str(col2))
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.savefig('two-features: ' + str(col1)+ 'vs' + str(col2) + '.pdf')
        # plt.show()

# Many-feature visualization
sns.heatmap(df.iloc[:,3:6],cmap="YlGnBu")
# plt.show()
plt.savefig('many-features.pdf')






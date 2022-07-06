# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:06:50 2022

@author: jo585802
"""

import os
import pandas as pd

##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\jo585802\\OneDrive - University of Central Florida\\Documents\\GitHub\\ECO5445\\'
os.chdir(git_path + '\\11-ReadingDataWithPandas\\data')
# Check that the change was successful.
os.getcwd()

# Bringing in the data (.csv vs .txt)
housing1 = pd.read_csv("prop_prices.csv", delimiter=',')
housing2 = pd.read_csv("prop_prices.txt", delimiter='\t')

# If you do not have names on the dataset, you can define them as you bring them in

colNames = ["sale_def","saleyymm","bed","bath","area_heated","area","dist_cbd","dist_lakes","pool","property_id","pcode"]

housing3 = pd.read_csv("prop_prices_no_labels.csv", names = colNames, delimiter=',')
housing4 = pd.read_csv("prop_prices_no_labels.txt", names = colNames, delimiter='\t')

# Exporting data is similar, sep defaults to 0 meaning csv, 
# "\t" is for tab delimited files

housing3.to_csv("Housing3.csv")


# Searching dataframe
housing = pd.read_csv("prop_prices.csv", delimiter=',')

# Select a column
housing["sale_def"]

# Select a row
housing.iloc[0,]

# Select a chunk
housing.iloc[9:25, 2:5]

# Conditional statements evaluate argument on each row of dataframe
housing["bed"] > 3

# You can use this to select only things you are interested in
homes_with_pool = housing[housing["pool"] == 1]

# More information can be found at this link: 
# https://pandas.pydata.org/docs/getting_started/index.html#getting-started
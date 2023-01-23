#!usr/bin/python3
import pandas as pd

# list of file names to be merged
files = ["/home/olive/customer/strides/apollo-contacts-export.csv",
"/home/olive/customer/strides/apollo-contacts-export (1).csv","/home/olive/customer/strides/apollo-contacts-export (2).csv","/home/olive/customer/strides/apollo-contacts-export (3).csv"]

# read in each file and store them in a list
dfs = [pd.read_csv(file) for file in files]

# merge all the files into one
merged_df = pd.concat(dfs)

# write the merged data to a new csv file
merged_df.to_csv('merged.csv', index=False)

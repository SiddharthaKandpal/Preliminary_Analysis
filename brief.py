#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def overview(df):
    """
    Reads in a CSV file and analyzes it for missing values, total number of columns, basic statistics and mode.
    file_path: A string representing the file path to the CSV file.
    """
    # Read in the CSV file
    #dataset = pd.read_csv(file_path)

    # Check for missing values
    print("Missing values:\n", df.isnull().sum())

    # Calculate basic statistics for each feature
    print("Basic statistics:\n", df.describe())

    # Total number of columns
    print("Total number of columns:", len(df.columns))

    # Mode
    print("Mode:\n", df.mode().iloc[0])   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





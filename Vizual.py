#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_visualizations(df, plot_type='histogram', x_col=None, y_col=None, hue=None, palette='Dark2'):
    '''
    Create visualizations using Seaborn and Matplotlib.

    Parameters:
    df (pandas.DataFrame): The dataset to be visualized.
    plot_type (str): The type of plot to be created. Options: 'pairplot', 'scatter', 'histogram', 'barchart'
    x_col (str): The column to use as the x-axis for the plot.
    y_col (str): The column to use as the y-axis for the plot.
    hue (str): The column to use for grouping data by color.
    palette (str): The color palette to use for the plot.

    Returns:
    None
    '''
    if plot_type == 'pairplot':
        # Create a pairplot
        sns.pairplot(df, hue=hue, palette=palette)
        plt.show()

    elif plot_type == 'scatter':
        # Create a scatterplot
        sns.scatterplot(x=x_col, y=y_col, hue=hue, data=df, palette=palette)
        plt.show()

    elif plot_type == 'histogram':
        # Create a histogram
        sns.histplot(x=x_col, hue=hue, data=df, multiple='stack', palette=palette)
        plt.show()

    elif plot_type == 'barchart':
        # Create a bar chart
        sns.countplot(x=x_col, hue=hue, data=df, palette=palette)
        plt.show()

    else:
        print('Invalid plot_type parameter.')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





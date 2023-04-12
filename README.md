# Preliminary Analysis
## Overview
The project demonstrates how to use Python and various libraries (including Pandas, Matplotlib, and Seaborn) to perform data analysis and create visualizations using Penguin dataset. This reason for making this project is to create functions so as to enable me to perform a very basic preliminary analysis on the dataset.
## Data
I used the penguin dataset.  
Dataset i used - https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data  
Original source - https://allisonhorst.github.io/palmerpenguins/
## Technologies Used
[.matpolib](https://matplotlib.org/)  

[.seaborn](https://seaborn.pydata.org/)
## Visualization
I did a brief analysis on the dataset by using breif function -
![breif_penguin](https://user-images.githubusercontent.com/78250442/231426545-0ab6391a-4a40-4c43-8e95-f225df23a23f.jpg)  
Visualizations using Seaborn and Matplotlib.  
a) Scatterplot of filpper length and body mass  
![scatter](https://user-images.githubusercontent.com/78250442/231428644-2141d22f-673f-425e-84dc-aa9764e71588.jpg)  
b) Pairplot  
![pairplot](https://user-images.githubusercontent.com/78250442/231428713-166b2840-8a37-417e-81f2-3a1c40047aa2.jpg)  
c) Histogram of flipper length  
![histogram](https://user-images.githubusercontent.com/78250442/231429296-2c692675-8431-4a05-94d7-669eb3d236e6.jpg)  
d) Bar chart of penguin counts by island  
![barchart](https://user-images.githubusercontent.com/78250442/231429471-9907ffe6-8c62-4fa3-b81d-a3c21d6ab7ff.jpg)

## Steps
1.Defined a function called brief
This function takes a pandas dataframe as input and performs the following operations:

. Checks for missing values using Pandas isnull function

. Calculates total number of columns.

. Prints the calculated statis.

. Calculates mode.  

2.Defined a function called Vizual
This function takes a pandas dataframe and create visualizations using Seaborn and Matplotlib.

Parameters:
    df (pandas.DataFrame): The dataset to be visualized.
    plot_type (str): The type of plot to be created. Options: 'pairplot', 'scatter', 'histogram', 'barchart'
    x_col (str): The column to use as the x-axis for the plot.
    y_col (str): The column to use as the y-axis for the plot.
    hue (str): The column to use for grouping data by color.
    palette (str): The color palette to use for the plot.


3.Then i used read_csv function from Pandas to load it into a DataFrame

4.Then I called the brief function to basic analysis.

5.Then i created some visualizations using Vizual function.

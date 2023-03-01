# -*- coding: utf-8 -*-

"""

@author: Kashir
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Function to read the dataset
"""
def read_dataSet(path):
    """
    Read dataset
    
    using the path from local
    
    """
    df = pd.read_csv(path)
    return df

"""
Function for the line plot graph
"""
def draw_line_plot_graph(dataset):
    """
    Line plot graph 
    
    for year and consumption
    """
    df_actual_dataset = dataset.groupby("YEAR")['EMISSIONS'].sum().reset_index()

    plt.plot(df_actual_dataset['YEAR'], df_actual_dataset['EMISSIONS'])
    plt.xticks(np.arange(2000,2022,2))
    plt.show()
    return 0

df = read_dataSet('Fuel_Consumption_2000-2022.csv')
draw_line_plot_graph(df)
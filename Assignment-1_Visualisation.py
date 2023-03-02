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
    df_actual_dataset = (dataset
                         .groupby("YEAR")['FUEL CONSUMPTION']
                         .sum()
                         .reset_index()
                         )
    
    plt.plot(df_actual_dataset['YEAR']
             , df_actual_dataset['FUEL CONSUMPTION'])
    plt.xticks(np.arange(2000,2022,2))
    plt.show()

"""
Function for the pie plot graph
"""
def draw_pie_plot_graph(dataset):
    """
    Pie plot graph 
    
    for year and consumption
    """
    df_actual_dataset = (dataset
                         .groupby("YEAR")['FUEL CONSUMPTION']
                         .sum().sort_values(ascending = False)
                         .reset_index())
    plt.pie(df_actual_dataset['FUEL CONSUMPTION'][:5]
          , labels = df_actual_dataset['YEAR'][:5]
          , autopct = "%1.2f%%")
    plt.show()
    
"""
Function for the Bar plot graph
"""
def draw_bar_plot_graph(dataset):
    """
    Bar plot graph 
    
    for year and consumption
    """
    df_actual_dataset = (dataset
                         .groupby("MAKE")['FUEL CONSUMPTION']
                         .sum().sort_values(ascending = False)
                         .reset_index())
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(df_actual_dataset['MAKE'][:5]
            ,df_actual_dataset['FUEL CONSUMPTION'][:5])
    plt.show()
    
    
df = read_dataSet('Fuel_Consumption_2000-2022.csv')
draw_line_plot_graph(df)
draw_pie_plot_graph(df)
draw_bar_plot_graph(df)
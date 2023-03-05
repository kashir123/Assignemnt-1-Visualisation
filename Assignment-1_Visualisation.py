# -*- coding: utf-8 -*-

"""

@author: Kashir Waseem Assignment-1 Data Visualisation
Student id : 22031825
Course : Applied Data Science 1 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_dataSet(path):
    """
    Dataset Reading Function
    
    I use pandas and get the data
    from the local directory
    """
    df = pd.read_csv(path)
    return df


def draw_line_plot_graph(x,y,y1):
    """
    Line plot graph 
    
    I am using the column Year and fuel Consumption
    to plot the line graph this will conslude that 
    how the consumption of fuel goes over the years
    
    The function accept two parameter x and y
    x contain the value which will draw on 
    x-axis and y will contain the value will
    draw on y axis. On X axis we have a Years
    and on Y axis we have of all the fuel consumption
    over the year
    """
    #set the size of the figure
    plt.figure(figsize=(15,10))
    #labels
    plt.title("Fuel consumption and Emissions over the year 2000-2022"
              , fontweight = "bold")
    plt.xlabel("YEAR")
    plt.ylabel("Fuel Consumption and Emission")
    #yticks
    plt.yticks(np.arange(0,300000,50000))
    # plot
    plt.plot(x, y, label = "Fuel Consumption")
    plt.plot(x,y1, label = "Emissions")
    
    #legend
    plt.legend(loc = "upper left")
  
    # setting xticks
    plt.xticks(np.arange(2000,2022,2))
    # show plot
    plt.show()


def draw_pie_plot_graph(x, y, title):
    """
    Pie plot graph 
    
    The function accept 2 parameter one for the value
    associated with each category and the second for 
    the labels for each category. This function will
    plot the top five fuel consumption year
    """
    #set the size of the figure
    plt.figure(figsize=(14,9))
    
    #labels
    plt.title(title, fontweight = "bold")
    
    # plot
    plt.pie(x
          , labels = y
          , autopct = "%1.2f%%")
    
    # plot show
    plt.show()
    

def draw_bar_plot_graph(x, y):
    """
    Bar plot graph 
    
    This function will accept 2 parameter one for the X
    axis and the second for the Y axis to draw a plot.
    X parameter contains the top five Make of the cars who consume 
    the most of the fuel over the years and the second
    Y parameter contains the fuel consumption values
    for the y axis
    """
    #set the size of the figure
    plt.figure(figsize=(14,9))
    
    fig = plt.figure()
    
    #adding axes
    ax = fig.add_axes([0,0,1,1])
    
    #labels
    ax.set_title("Top five Make who consume most of the fuel between 2000-2022"
                 , fontweight = "bold")
    ax.set_xlabel("Make")
    ax.set_ylabel("Fuel Consumption")
    
    
    # plot
    ax.bar(x, y)
    
    #show plot
    plt.show()
    
if __name__=="__main__":
    # calling the function to read dataset
    df = read_dataSet('Fuel_Consumption_2000-2022.csv')
    
    #Grouping the dataset at years and get sum of the Fuel consumption
    dataset_line_plot = (df
                          .groupby("YEAR")['FUEL CONSUMPTION']
                          .sum()
                          .reset_index()
                          )
    #Grouping the dataset at years and get sum of the EMISSIONS by the vehicle
    dataset_line_plot_emission = (df
                          .groupby("YEAR")['EMISSIONS']
                          .sum()
                          .reset_index()
                          )
    
    """
    Grouping the dataset at years and fuel consumption but sorted 
    it in descending order used top five for pie plot
    """
    dataset_pie_plot_consumption = (df
                         .groupby("YEAR")['FUEL CONSUMPTION']
                         .sum().sort_values(ascending = False)
                         .reset_index())
    
    """
    Grouping the dataset at years and EMISSIONS but sorted 
    it in descending order used top five for pie plot
    """
    dataset_pie_plot_emission = (df
                         .groupby("YEAR")['EMISSIONS']
                         .sum().sort_values(ascending = False)
                         .reset_index())
    
    """
    Grouping the datset at make and fuel consumption in descending
    order and pass top five values on the x and y axis to plot bar chat
    """
    dataset_bar_plot = (df
                        .groupby("MAKE")['FUEL CONSUMPTION']
                        .sum().sort_values(ascending = False)
                        .reset_index())
    
    
    # calling the function for line plot
    draw_line_plot_graph(dataset_line_plot['YEAR']
                         , dataset_line_plot['FUEL CONSUMPTION']
                         , dataset_line_plot_emission['EMISSIONS'])
    
    # calling the function for pie plot
    draw_pie_plot_graph(dataset_pie_plot_consumption['FUEL CONSUMPTION'][:5]
                        , dataset_pie_plot_consumption['YEAR'][:5]
                        , "Top Five years fuel consumption")
    
    # calling the function for pie plot
    draw_pie_plot_graph(dataset_pie_plot_emission['EMISSIONS'][:5]
                        , dataset_pie_plot_emission['YEAR'][:5]
                        , "Top Five years Emissions by the vehicle")
    
    # calling function for the bar plot
    draw_bar_plot_graph(dataset_bar_plot['MAKE'][:5]
                        , dataset_bar_plot['FUEL CONSUMPTION'][:5])
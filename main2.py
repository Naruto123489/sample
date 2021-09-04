import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random

df = pd.read_csv('data2.csv')
data = df['url'].tolist()

population_mean = statistics.mean(data)
print("Population Mean: ", population_mean)

std_dev = statistics.stdev(data)
print("Standard Deviation: ", std_dev)

def random_set_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)  
    return mean 

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    figure = ff.create_distplot([df], [''], show_hist= False)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution: ", mean)
    figure.add_trace(go.Scatter(x = [mean, mean], y = (0,1), mode = "lines", name = "MEAN"))
    figure.show()

#function to get the mean of 100 data points 1000 times and plot the graph
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()

# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)
standard_deviation()
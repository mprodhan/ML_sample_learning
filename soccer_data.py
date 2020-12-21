import pandas as pd
# The use of pandas is significant here for its use of data analytics. This is the first tool used to break down
# data.
import seaborn as sns
# The reason why seaborn was used in place of matplotlib, is due to the simplicity of the library, when it comes
# to pltting a graph.
from bokeh.plotting import figure,show
# The use of bokeh seemed like a personal choice, in the creation of an interactive graph, including the use
# of a hovering toool that extrapolates data about the plot on the graph.
from bokeh.models import HoverTool

data = pd.read_csv('data.csv')
# To Begin, always start every code with this point in reading the file, when using pandas.
# print(data)
# print(data.shape)
# print(data.describe)
# print(data.values)
# data.values results in values that are displayed inside of a list(array)
# print(data[data['Age']>40].head())
# The data call above results in the first five data sets to be called and displayed

data_prime = pd.DataFrame(data, columns=['Name', 'Wage', 'Value'])
# This code takes the entire data.csv file and searches for just the specific data that is needed for 
# the purpose of this project. The purpose here is so that data about how much a soccer player gets paid, 
# is conveyed as a means to check the stats of a players strength as a forward and the cost to employ them
# for a particular soccer club.

# The purpose of this function is to reduce the data to numbers only, by eliminating the number as a
# string, and then the letters and symbols attached to their values. In this case, a euro symbol and quotes 
# are attached to the values and must be removed, in order to extrapolate their values as quantitative data.

def string_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '') * 1000000000)
    return 0.0

# The variable for wage and value does two seperate work in one code. First, the regex, detects the 
# pattern for the euro symbol and removes them, befcause the prior funciton only removed the end symbol.
# Then, the .apply() translates a string into a numeric float, or decimal.

wage = data_prime['Wage'].replace('[\€]', '', regex=True).apply(string_float)
value = data_prime['Value'].replace('[\€]', '', regex=True).apply(string_float)
# The dictionary value to equate to the value of a float is demostrated here, so that, the calculation 
# for data_prime['difference], is then calculated.
data_prime['Wage'] = wage
data_prime['Value'] = value
data_prime['difference'] = data_prime['Value'] - data_prime['Wage']
print(data_prime.dtypes)
data_sorted = data_prime.sort_values('difference', ascending=False)
print(data_sorted)

sns.set()
dataprime_graph = sns.scatterplot(x='Wage', y='Value', data=data_sorted)
print(dataprime_graph)

TOOLTIPS = HoverTool(tooltips=[
    ("index", "$index"),
    ("(Wage, Value)", "(@Wage,@Value)"),
    ("Name", "@Name")
])
plot_read = figure(title='Soccer 2019', x_axis_label='Wage', y_axis_label='Value',
                    plot_width=700, plot_height=700, tools=[TOOLTIPS])
plot_read.circle('Wage', 'Value', size=10, source=data_sorted)
show(plot_read)
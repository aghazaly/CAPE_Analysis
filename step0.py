from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.plotting import figure

import pandas as pd

total = pd.read_csv('total.csv',index_col='Date')

def get_data(df,x,y):
    return df.loc[:,[x,y]]


datasource = ColumnDataSource(total['Rate'])

plot = figure(title="Correlation Plot", plot_width=500, plot_height=500)
plot.circle("Rate", size=1, source=datasource)

plot.title.text_font_size = "25px"
plot.title.align = "center"

# Define the layout

curdoc().add_root(plot)
curdoc().title = "CAPE Analysis"



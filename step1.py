from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.plotting import figure

import pandas as pd

total = pd.read_csv('total.csv',index_col="Date")

def get_data(df,x,y):
	newdf = df.loc[:,[x,y]]
	newdf['x'] = newdf[x]
	newdf['y'] = newdf[y]
	return newdf


datasource = ColumnDataSource(get_data(total,"Rate","CAPE"))

plot = figure(title="**CAPE**", plot_width=500, plot_height=500)
plot.circle('x', 'y', size=2, source=datasource)

plot.title.text_font_size = "25px"
plot.title.align = "center"

STRATEGIES = ['Rate', 'CAPE', 'rRate', 'rCAPE']
x = Select(value="Rate", options=STRATEGIES)
y = Select(value="CAPE", options=STRATEGIES)

# Define the layout
layout = row(column(x, y), plot)

curdoc().add_root(layout)
curdoc().title = "CAPE Analysis"


def ticker_update(attribute, old, new):
    t1, t2 = x.value, y.value
    data = get_data(total,t1, t2)
    datasource.data = ColumnDataSource.from_df(data[['x','y']])

x.on_change("value", ticker_update)
y.on_change("value", ticker_update)



from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.plotting import figure

import pandas as pd


def get_data(symbol1, symbol2):

	data = pd.read_csv('total.csv') 

	data['Rate'] = data[symbol1]
	data['CAPE'] = data[symbol2]
	data['rRate'] = data['r'+symbol1]
	data['rCAPE'] = data['r'+symbol2]
	return data


datasource = ColumnDataSource(get_data('Rate','CAPE'))

plot = figure(title="Correlation Plot", plot_width=500, plot_height=500)
plot.circle("Rate", "CAPE", size=2, source=datasource)

plot.title.text_font_size = "25px"
plot.title.align = "center"

STRATEGIES = ['Rate', 'CAPE', 'rRate', 'rCAPE']
Rate = Select(value="Rate", options=STRATEGIES)
CAPE = Select(value="CAPE", options=STRATEGIES)

# Define the layout
layout = row(column(Rate, CAPE), plot)

curdoc().add_root(layout)
curdoc().title = "Stock Correlations"


def ticker_update(attribute, old, new):
    t1, t2 = Rate.value, CAPE.value
    data = get_data(t1, t2)
    datasource.data = ColumnDataSource.from_df(data[['Rate', 'CAPE', 'rRate', 'rCAPE']])

Rate.on_change("value", ticker_update)
CAPE.on_change("value", ticker_update)



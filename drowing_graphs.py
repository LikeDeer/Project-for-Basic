from bokeh.io import show
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import Toggle
from bokeh.layouts import layout
import pandas as pd

# COVID_log
df_conf = pd.read_csv('datas/코로나 일별 확진자 수 전처리 후파일.csv')
conf_date = pd.to_datetime(df_conf['date'], format='%Y%m%d', errors='ignore')

conf_data = {'conf_num': df_conf['confirmed'], 'conf_date': conf_date}

source = ColumnDataSource(data=conf_data)


p_DateConfirmed = figure(
    tools='',
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
    x_axis_type="datetime"
)

COVID_log = p_DateConfirmed.line(
    x='conf_date',
    y='conf_num',
    color='#FC4F4F',
    alpha=0.5,
    source=source
)

toggle = Toggle(label="Pink Line", button_type="success", active=True)
toggle.js_link('active', COVID_log, 'visible')

show(layout([p_DateConfirmed], [toggle]))

# COVID_log finish

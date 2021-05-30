from bokeh.io import show
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import Toggle
from bokeh.layouts import layout
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap
from bokeh.embed import components
import pandas as pd

# =========================== COVID_log ===========================
df_conf = pd.read_csv('datas_temp/코로나 일별 확진자 수 전처리 후파일.csv')
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

toggle = Toggle(label="코로나 상황", button_type="success", active=True)
toggle.js_link('active', COVID_log, 'visible')

# ======================= COVID_log finish ==========================

# ======================= Work From Home ============================
df_WFH = pd.read_csv('datas_temp/재택지수 전처리 후파일.csv')
WFH_date = pd.to_datetime(df_WFH['dt'], format='%Y%m%d', errors='ignore')

WFH_data = {'WFH_ratio': df_WFH['h0d1h1_dur_r'], 'WFH_date': WFH_date}

mapper_WFH = linear_cmap(
    field_name='WFH_ratio',
    palette=Spectral6,
    low=min(WFH_data['WFH_ratio']),
    high=max(WFH_data['WFH_ratio'])
)

source = ColumnDataSource(data=WFH_data)

p_WFH = figure(
    tools='',
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
    x_axis_type="datetime"
)

Graph_WFH = p_WFH.circle(
    x='WFH_date',
    y='WFH_ratio',
    line_color=mapper_WFH,
    color=mapper_WFH,
    alpha=0.5,
    source=source
)

show(layout([p_DateConfirmed], [toggle], [p_WFH]))
# ================== Work From Home finish ==========================

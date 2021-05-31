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
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
    x_axis_type="datetime",
    tools=''
)

Graph_COVIDlog = p_DateConfirmed.line(
    x='conf_date',
    y='conf_num',
    color='#FC4F4F',
    alpha=0.5,
    source=source
)

toggle = Toggle(label="코로나 상황", button_type="success", active=True)
toggle.js_link('active', Graph_COVIDlog, 'visible')

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
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
    x_axis_type="datetime",
    toolbar_location=None,
    tools=''
)

Graph_WFH = p_WFH.circle(
    x='WFH_date',
    y='WFH_ratio',
    line_color=mapper_WFH,
    color=mapper_WFH,
    alpha=0.5,
    source=source
)


# ================== Work From Home finish ==========================

# ==================== Restaurant ===================================

Restaurant_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
Restaurant_sales = [13.2, 12.3, 11.3, 13.4, 16.2, 14.2]

p_Restaurant = figure(
    x_range=Restaurant_month,
    max_width=500,
    plot_height=250,
    toolbar_location=None,
    tools=''
)

Graph_Restaurant = p_Restaurant.vbar(
    x=Restaurant_month,
    top=Restaurant_sales,
    width=0.9
)

p_Restaurant.xgrid.grid_line_color = None
p_Restaurant.y_range.start = 10

show(layout([p_DateConfirmed], [toggle], [p_WFH], [p_Restaurant]))
# ==================== Restaurant finish =================================

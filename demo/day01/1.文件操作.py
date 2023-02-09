from pyecharts.charts import Line

line = Line()
line.add_xaxis(['长沙', '株洲', '湘潭'])
line.add_yaxis('GDP', [30, 40, 40])
line.render()

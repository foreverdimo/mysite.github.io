from pyecharts.charts import WordCloud,Bar,PictorialBar,Pie,Geo,Map,Timeline,Grid,Line
from pyecharts import options as opts
from pyecharts.globals import SymbolType,GeoType,ChartType


##-------从文件中读出关键词频------------------
src_filename = './data/时间简史词频.csv'
src_file = open(src_filename, 'r')
line_list = src_file.readlines() 
src_file.close()
wordfreq_list = []  
key_words = []
words_freq = []
for line in line_list:
    line = line.strip()  
    line_split = line.split(',') 
    wordfreq_list.append((line_split[0],line_split[1]))
    key_words.append(line_split[0])
    words_freq.append(line_split[1])

print(wordfreq_list)
del wordfreq_list[0]
del key_words[0]
del words_freq[0] 

## 柱状图
bar = (
    Bar()
    .add_xaxis(key_words)
    .add_yaxis("",words_freq)
    .set_global_opts(
        title_opts = opts.TitleOpts(title= "时间简史词频柱状图",subtitle="仅统计前40个关键词"),
        toolbox_opts=opts.ToolboxOpts(),
        visualmap_opts=opts.VisualMapOpts(min_ = 30,max_ = 700, orient = "vertical"),
        datazoom_opts=opts.DataZoomOpts(range_start= 20,range_end= 50)
    )
)
out_filename = './output/bar_keywords.html'
bar.render(out_filename)
print('生成结果文件：' + out_filename)

##象形柱状图
pictorialbar = (
    PictorialBar()
    .add_xaxis(key_words)
    .add_yaxis(
        "",
        words_freq,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title= "时间简史词频象形柱状图",subtitle="仅统计前40个关键词"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
        toolbox_opts=opts.ToolboxOpts(),
        visualmap_opts=opts.VisualMapOpts(min_ = 30,max_ = 700, orient = "vertical",dimension = 0),
        datazoom_opts=opts.DataZoomOpts(range_start= 20,range_end= 50, orient = "vertical", pos_left = "right")
    )
)
out_filename = './output/pictorialbar_keywords.html'
pictorialbar.render(out_filename)
print('生成结果文件：' + out_filename)

##饼状图
pie = (
    Pie(opts.InitOpts(width="1080px",height="720px"))
    .add("", wordfreq_list)
    .set_global_opts(title_opts=opts.TitleOpts(title= "时间简史词饼状图",subtitle="仅统计前40个关键词",pos_left = "middle", pos_top = "bottom"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    
)

out_filename = './output/pie_keywords.html'
pie.render(out_filename)
print('生成结果文件：' + out_filename)

##词云图
cloud = WordCloud() 
# 向词云中添加内容，第一个参数可以设为空，第二个参数为元组列表（词和词频）
cloud.add('', wordfreq_list,word_size_range=[10, 100], shape=SymbolType.DIAMOND)
# render会生成HTML文件。默认是当前目录render.html，也可以指定文件名参数
out_filename = './output/wordcloud_keywords.html'
cloud.render(out_filename)
print('生成结果文件：' + out_filename)


##地理连线图
geo = (
    Geo((
        opts.InitOpts(
            width="1500px",
            height="750px",
            # bg_color= "#103f8b",
        )
    ))
    .set_global_opts(
        title_opts= opts.TitleOpts(
            title="模拟疫情期间人口流动",
            subtitle="数据纯属虚构",
            pos_left="center",
            # title_textstyle_opts= opts.TextStyleOpts(
            #     color="#fff"
            # )
        ),
        tooltip_opts=opts.TooltipOpts(
            formatter="{b}"
        ),
        legend_opts = opts.LegendOpts(
            selected_mode= "single",
            orient="vertical",
            pos_left="left",
            legend_icon="arrow",
            # textstyle_opts=opts.TextStyleOpts(
            #     color="#fff"
            # )
        ),
        toolbox_opts=opts.ToolboxOpts(
            orient="vertical",
            pos_left="left",
            pos_top="middle",
        ),
        visualmap_opts= opts.VisualMapOpts(
            max_= 200,
            min_= 0,
            is_calculable= True,
            range_color=['#ff3333', 'orange', 'yellow','lime','aqua'],
            # textstyle_opts = opts.TextStyleOpts(
            #     color= "#fff"
            # )
        )
    )
    .add_coordinate_json("./data/city_coordinates.json")
    .add_schema(
        maptype="china",
    )
    .add("",[   ("北京",200),
            ("上海",78),
            ("武汉",22),
            ("青海",55),
            ("广州",95),
            ("西藏",25),
            ("成都",25),
         ],
         type_=ChartType.EFFECT_SCATTER,
         symbol="emptyCircle"
    )
    .add("人员流向",[
        ("北京","上海"),
        ("北京","青海"),
        ("北京","武汉"),
        ("北京","广州"),
        ("北京","西藏"),
        ("北京","成都"),
    ],
    type_= GeoType.LINES,
    effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                symbol_size=6,color="red"),
    linestyle_opts=opts.LineStyleOpts(curve=0.2,color={
                            'type': 'linear',
                            'x': 0,
                            'y': 0,
                            'x2': 0,
                            'y2': 1,
                            'colorStops': [
                                {'offset': 0, 'color': 'cyan' }, 
                                {'offset': 1, 'color': 'orange'}],
                            'global': False  # 缺省为 false
                        })
    )
)
out_filename = './output/personal_movement.html'
geo.render(out_filename)
print('生成结果文件：' + out_filename)

##中国地图
data_2020 ={
"广东":110760,
"山东":73129,
"河南":54997,
"四川":48598,
"江苏":102700,
"河北":36207,
"湖南":41781,
"安徽":38681,
"湖北":43443,
"浙江":64613,
"广西":22156,
"云南":24500,
"江西":25691,
"辽宁":25115,
"福建":43903,
"陕西":26181,
"黑龙江":13698,
"山西":17650,
"贵州":17826,
"重庆":25002,
"吉林":12311,
"甘肃":9016,
"内蒙古":17360,
"新疆":13798,
"上海":38700,
"北京":36102,
"天津":14083,
"海南":5532,
"青海":3920,
"西藏":1903,
"宁夏":3921
}
data_2019 ={
"广东":107671,
"山东":71067,
"河南":54259,
"四川":46615,
"江苏":99632,
"河北":35104,
"湖南":39752,
"安徽":37114,
"湖北":45828,
"浙江":62352,
"广西":21237,
"云南":23223,
"江西":24757,
"辽宁":24907,
"福建":42395,
"陕西":25793,
"黑龙江":13613,
"山西":17026,
"贵州":16769,
"重庆":23605,
"吉林":11726,
"甘肃":8718,
"内蒙古":17213,
"新疆":13597,
"上海":38155,
"北京":35371,
"天津":14104,
"海南":5309,
"青海":2966,
"西藏":1698,
"宁夏":3748
}
data_2018 ={
"广东":97278,
"山东":76470,
"河南":48055,
"四川":40678,
"江苏":92595,
"河北":36010,
"湖南":33263,
"安徽":30006,
"湖北":39366,
"浙江":56197,
"广西":20352,
"云南":17881,
"江西":21985,
"辽宁":25315,
"福建":35804,
"陕西":24438,
"黑龙江":16361,
"山西":16818,
"贵州":14806,
"重庆":20363,
"吉林":15074,
"甘肃":8246,
"内蒙古":17289,
"新疆":12199,
"上海":32680,
"北京":30320,
"天津":18810,
"海南":4832,
"青海":2865,
"西藏":1478,
"宁夏":3705
}

data = [data_2018,data_2019,data_2020]


tl = Timeline()
for i in range(0,3):
    map_data = list(data[i].items()) 
    gdp = (
        Map()
        .add("20"+str(i+18)+"年GDP（单位：亿元）", 
            data_pair=map_data, 
            maptype="china",
            is_map_symbol_show=False,    
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="20"+str(i+18)+"年全国GDP数据分级设色图",subtitle="单位：亿元"),
            visualmap_opts=opts.VisualMapOpts(min_=1200, max_=120000, is_piecewise=True),
        )
    )
    tl.add(gdp,"{}年".format(i+2018))
out_filename = './output/gdp_map.html'
tl.render(out_filename)
print('生成结果文件：' + out_filename)

##组合图表
##数据参考pyecharts gallery
bar = (
    Bar()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "蒸发量",
        [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
        yaxis_index=0,
        color="#d14a61",
    )
    .add_yaxis(
        "降水量",
        [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
        yaxis_index=1,
        color="#5793f3",
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="蒸发量",
            type_="value",
            min_=0,
            max_=250,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="温度",
            min_=0,
            max_=25,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="降水量",
            min_=0,
            max_=250,
            position="right",
            offset=80,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        title_opts=opts.TitleOpts(title="Grid-Overlap-多 X/Y 轴示例"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="25%"),
    )
)

line = (
    Line()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "平均温度",
        [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        yaxis_index=2,
        color="#675bba",
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar1 = (
    Bar()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "蒸发量 1",
        [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
        color="#d14a61",
        xaxis_index=1,
        yaxis_index=3,
    )
    .add_yaxis(
        "降水量 2",
        [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
        color="#5793f3",
        xaxis_index=1,
        yaxis_index=3,
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="蒸发量",
            type_="value",
            min_=0,
            max_=250,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="温度",
            min_=0,
            max_=25,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(grid_index=1),
        yaxis_opts=opts.AxisOpts(
            name="降水量",
            min_=0,
            max_=250,
            position="right",
            offset=80,
            grid_index=1,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="65%"),
    )
)

line1 = (
    Line()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "平均温度 1",
        [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        color="#675bba",
        label_opts=opts.LabelOpts(is_show=False),
        xaxis_index=1,
        yaxis_index=5,
    )
)

overlap_1 = bar.overlap(line)
overlap_2 = bar1.overlap(line1)

grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add(
        overlap_1, grid_opts=opts.GridOpts(pos_right="58%"), is_control_axis_index=True
    )
    .add(overlap_2, grid_opts=opts.GridOpts(pos_left="58%"), is_control_axis_index=True)
)

out_filename = './output/rain_map.html'
grid.render(out_filename)
print('生成结果文件：' + out_filename)

# Pandas

Python 里进行数据操作（manipulation）和数据处理的函数库。

核心功能：DataFrame, Series, 图表，统计等。

# DataFrame

DataFrame 类似于数据库的表，利用 DataFrame 可以对各种数据进行统一的处理。

Pandas 支持从多种数据格式创建 DataFrame，例如 Excel 表格：

```python
import pandas
data_frame = pandas.read_excel("data.xsls")
```

# 绘制曲线图

```
data_frame.plot()
```

# 绘制直方图

```
data_frame.hist("chart title")
```

## 理解数据

理解数据的几个层次：

- 形式理解：了解数据文件的格式
- 逻辑理解：理解数据的逻辑组织方式，哪个字段代表什么意思
- 统计理解：理解数据的分布，是否异常，是否可以解释等等，有些可以通过绘图直观的表达

常见的数据格式：

- Excel 数据表格，文档结构复杂，需要用专门的库去解析。Pandas 集成了读写 Excel 文件的库。
- CSV 源文件容易阅读的数据表格，首行是表头，从第二行起每行是一条记录。
- JSON 如前述，可以用 Python 自带的 JSON 库去处理。
- XML 类似于 HTML，但是标签需要严格闭合，也可以用 BeautifulSoup 处理。

## 应用示例（提取信息）

示例：从免费词典资源提取一个简化版（只含单词和定义）的词典。

假设我们能下载到这么一个词典数据 https://raw.githubusercontent.com/skywind3000/ECDICT/master/ecdict.csv

下载：

```python
import request
response = request("https://raw.githubusercontent.com/skywind3000/ECDICT/master/ecdict.csv")
with open("ecdict.csv", "w") as f:
    f.write(response.text)
```

它是一个 CSV 文件，用编辑器或者表格处理软件打开，观察文件的结构：

```csv
word,phonetic,definition,translation,pos,collins,oxford,tag,bnc,frq,exchange,detail,audio
hood,hʊd,,"n. 罩；风帽；（布质）面罩；学位连领帽（表示学位种类）\nv. 覆盖；用头巾包；使(马,鹰等)戴头罩；给…加罩\n[网络] 胡德；兜帽；引擎盖",,,,,0,0,,,
...
```

由第一行表头信息可知，单词（word）是第一列（对应下标 0），定义（definition）是第三列（对应下标 2）。

Python 内建了处理 CSV 的库函数，我们可以写一个循环去提取这两列：

```python
# encoding: utf-8
import csv
result = {}
with open("ecdict.csv", "r") as f:
    for row in csv.reader(f):
        word = row[0]
        definition = row[2]
        result[word] = definition
```

然后把结果写进文件里：

```python
with open("simplifided.csv", "w") as f:
    for word, definition in result.items():
        f.write(word)
        f.write(":")
        f.write(definition)
        f.write("\n")
```

注：此示例参考了 https://blog.plover.com/lang/ambiguous.html

思考：如果这是一个英语到中文的词典，而我们想要得到中文到英文的解释，可以怎么做？

延伸阅读：网上搜索"倒排索引"，并尝试理解。

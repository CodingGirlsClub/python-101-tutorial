# 数据处理初步

最基本的数据处理可以用 Python 直接完成。一些例子如下。

**处理一**：排序

```python
li.sort()                   # 纯粹的排序
li.sort(key=lambda x: x[2]) # 按照第二列排序
```

上面的排序使用了 lambda 函数。lambda 语法定义了一个匿名的函数，写法为

    lambda 参数1, 参数2, ...: 表达式

表达式的值会作为函数的返回值。

**处理二**：过滤 - 去掉不需要的数据

```python
result = []
for e in li:
    if ...
        result.append(e)
```

**处理三**：转换 - 通过循环生成新的集合数据

```python
value = []
for key, value in dict.items():
    result.append(value)
```

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

## 应用示例（倒排索引）

如果我们只有一个英汉字典，可以在这个的基础上生成一个汉英字典吗？

数据位于 https://raw.githubusercontent.com/skywind3000/ECDICT/master/ecdict.csv

这个词典是一个 CSV 的文件格式，我们可以先把它下载下来。

```python
import request
response = request("https://raw.githubusercontent.com/skywind3000/ECDICT/master/ecdict.csv")
with open("ecdict.csv", "w") as f:
    f.write(response.text)
```

用编辑器或者表格处理软件打开，观察 CSV 文件的结构：

```csv
word,phonetic,definition,translation,pos,collins,oxford,tag,bnc,frq,exchange,detail,audio
hood,hʊd,,"n. 罩；风帽；（布质）面罩；学位连领帽（表示学位种类）\nv. 覆盖；用头巾包；使(马,鹰等)戴头罩；给…加罩\n[网络] 胡德；兜帽；引擎盖",,,,,0,0,,,
...
```

由第一行表头信息可知，单词（word）是第一列（对应下标 0），定义（definition）是第三列（对应下标 2）。Python 内建了处理 CSV 的库函数，我们可以写一个循环去提取这两列：

```python
import csv
reverse_index = {}
with open("ecdict.csv", "r") as f:
    for row in csv.reader(f):
        english_word = row[0]
        definition = row[2]
        for chinese_word in definition.split(" ")[1].split(";")[0].split(",")[0]: # 这里只取了第一个解释，可以更准确点吗？
            if not (chinse_word in reverse_index):
                reverse_index[chinese_word] = english_word
            else:
                reverse_index[chinese_word] += "," + english_word
```

然后把倒排索引写进文件里：

```python
with open("cedict.csv", "w") as f:
    for chinese_word, english_words in reverse_index:
        f.write(chinese_word)
        f.write(":")
        f.write(english_words)
        f.write("\n")
```

倒排索引（invert index）是一个重要的技巧，方便我们按照需要的维度去查询数据。常用于搜索引擎中。

注：此示例参考了 https://blog.plover.com/lang/ambiguous.html

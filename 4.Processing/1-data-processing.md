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

## 应用示例

下面我们来利用一个中英词典，来回答一个问题：中文的同义词多还是英文的同义词多？

数据位于
https://raw.githubusercontent.com/skywind3000/ECDICT/master/ecdict.csv

这个词典是一个表格，我们可以用 Requests 把它下载下来。然后观察它的结构：

```python
```

分析代码：

```python
with open('dict.txt') as f:
    lines = f.read()
reverse_dict = {}
for line in lines.split("\n"):
    en_word, es_words = line.split(" ", 1)
    for es_word in es_words.split(","):
        if es_word not in reverse_dict:
            reverse_dict[es_word] = []
        reverse_dict[es_word].append(en_word)
for es_word, en_words in reverse_dict.items():
    if len(en_words) > 1:
        en_words = ",".join(en_words)
        print(f"{es_word}: {en_words}")
```

此示例参考了 https://blog.plover.com/lang/ambiguous.html

反向索引（invert index）是一个重要的技巧，方便我们按照需要的维度去查询数据。常用于搜索引擎中。

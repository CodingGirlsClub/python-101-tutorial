# 数据处理初步

我们收集的数据，往往不符合我们需要的格式，带有不同的噪音，看不出本质…… 需要对数据进行转换加工才能获得有用的信息。

爬虫获取的是原料，要经过数据处理的加工，最后才能获得产品。

## Python 字符串

很多人会说最重要的数据结构是数组，但最常用的数据结构却是字符串。数据处理中使用最多的操作也是字符串操作。

按分隔符拆分字符串（split）

```python
"a b c d".split(" ") # ["a", "b", "c", "d"]
```

用分隔符合并字符串（join）

```python
" ".join(["a", "b", "c", "d"]) # "a b c d"
```

取子字符串

```python
"this is good"[5:]
```

找到子字符串的位置

```python
"foo bar baz".index('bar')
"foo".index("bar") # ValueError
```

子字符串判断:

```python
"sub" in "string with sub"
str.startswith("prefix")
str.endswith("suffix")
```

## 类型转换

前面 Python 基础提到，数据有不同的类型，有时它的类型不是我们想要的。

例如从网页中提取出来的内容是字符串：

```python
a = "1234"
b = "3.4"
c = "-12"
```

而我们想把它表示的数值加起来。这样做是不行的：

```python
a + b + c # "12343.4-12"
```

注意对字符串做的 `+` 运算只是把它们串连起来。

为了进行数值计算，需要先把它们转换成数值类型。试试下面的代码:

```python
int("123")
float("3.4")
```

转换成数值类型后，就能进行数值计算了：

```python
a = "1234"
b = "3.4"
c = "-12"
int(a) + float(b) + float(c) # 1225.4
```

## 容器类型的处理

`list`，`dict`，`set` 等数据类型的处理。

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

**处理三**：重塑 - 通过循环生成新的集合数据

```python
value = []
for key, value in dict.items():
    result.append(value)
```

## 数据统计

假设我们有一个 `list`，赋予了变量 `lst`，里面包含若干项数据，我们要计算它的

最大值：

```python
max(lst)
```

最小值

```python
min(lst)
```

和

```python
sum = 0
for n in lst:
  sum += n
```

平均值

```python
float(sum) / len(lst)
```

注：如果 `sum` 是整数相加得来，那它还是个整数对象（`int`），为了除法可以得到小数结果，需要先转换成浮点数。

# Python 字符串

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

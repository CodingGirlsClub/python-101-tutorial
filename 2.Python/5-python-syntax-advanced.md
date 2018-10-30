# Python 语法进阶

> Cooking time: 15 mins active / 20 mins passive

> **Learning by Doing**:
> - 提示：切换到英文输入法编程可以避免一些用错符号的错误。
> - **Tasks for Learners**: 请学员创建第3个Python文件 `python_advanced_syntax_practice.py`, 对下列Python语法进行练习。
> - **Tasks for Coaches**: 请教练对学员的练习提供一定的辅助，请控制好时间。

下面介绍更多的 Python 语法。

如果对某个语法不熟悉，推荐到 Python 的官方网站寻找详细的 Python 语法参考：https://docs.python.org/3.7/reference/index.html 。

## 拼接字符串

使用 `f"..."` 和 `{}` 可以把变量的值拼接到字符串中去。试试下面的例子：

```python
me = "程序员"
sentence = f"hello, {me}"
print(sentence)
```

## 列表

列表 (`list`) 是一种顺序的数据。列表中的每个元素都对应一个整数下标，从 0 数起。

创建一个空的列表：

```python
li = []
```

创建一个带 3 个元素的列表：

```python
li = ["zero", "one", "two"]
```

查看列表的长度：

```python
len(li)
```

取出列表中的元素：

```python
li[1]
```

往列表中添加成员：

```python
li.append(1)
```

用 `for`……`in` 遍历列表：

```python
for e in li:
    print(e)
```

这个循环也可以用 `while` 来写，相当于：

```python
i = 0
while i < len(li):
    print(li[i])
    i = i + 1
```

`for` 比较方便迭代列表。

## 字典

创建一个字典（注意用英文花括号，不要用中文的花括号）：

```python
di = {}
```

用 `for`……`in` 遍历字典：

```python
for key, value in di.items():
    print(f"{key} {value}")
```

## 方法

方法（method）是定义在对象上的函数，可以通过 `.` 语法调用一个方法。

## 你可能会疑惑……

**问**：程序员都记得所有的语法和函数吗？  
**答**：并不！程序员也经常需要查阅文档，重新学习各种库和函数的用法，甚至到网上提问。网上还有不少问答网站，例如 [StackOverflow](https://stackoverflow.com) 和 [SegmentFault](https://segmentfault.com) 都记录了很多常见的问答。如果找不到需要的答案，你也可以在上面提出自己的问题。

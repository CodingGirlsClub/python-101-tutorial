# 数据处理初步

最基本的数据处理可以用 Python 直接完成。

处理一：排序

```python
li.sort()                   # 纯粹的排序
li.sort(key=lambda x: x[2]) # 按照第二列排序
```

上面的 `lambda` 语法



处理二：过滤 - 去掉不需要的数据

```python
result = []
for e in li:
    if ...
        result.append(e)
```

处理三：转换 - 通过循环生成新的集合数据

```python
value = []
for key, value in dict.items():
    result.append(value)
```

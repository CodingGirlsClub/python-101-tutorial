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

# Python 数据处理例子

https://blog.plover.com/lang/ambiguous.html -- 使用词典找出西班牙语里的多义词, 改写成对应的 python 版是：

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

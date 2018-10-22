# JSON 简介

JSON 是一种数据格式。

最准确又简洁的介绍： https://json.org/json-zh.html

# 处理 JSON 的库

标准的 JSON 库可以把 JSON 类型和 Python 类型相互转换

```python
import json

json_string = json.dumps([1, 2, {"foo": true, "bar": None}])
json.loads(json_string)
```

# 获取 JSON 响应

```python
response = requests.get("http://some.website.com/data.json")
response.json()
```

# Web API

API -- 应用程序编程接口（Application Programming Interface）的缩写。

很多网站提供了基于 JSON 和 HTTP 的 API，你可以通过阅读文档，学习其 API 的使用方法。

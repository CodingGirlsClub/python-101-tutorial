# 教学目标

- 对数据工程，数据科学获得大体的印象
- 了解数据工程师的成长路径，知道如何去获取相关资源
- 掌握相关工具完成数据获取和分析的任务

# 知识点目标

- 了解 Python 的语法，基本数据结构，会使用条件，循环和输入/输出，知道如何输出数据到文件
- 了解网站、网页、请求、响应的大致原理
- 掌握 HTML 的基本元素，类和 id，选择器
- 使用浏览器查看 DOM 和选择器
- 了解什么是 Web Service, JSON 的基本结构
- 了解 Python 发请求，处理 HTML 和 JSON 的相应库的使用
- 了解一些 web 服务或者信息网站，知道如何搜索常见网站的 API
- 学习基本的数据处理方式
- 在教练的帮助下，设计一个爬虫应用，并展示爬取的数据（可以用 excel 画出图表）

# 教学大纲

- 数据工程和数据科学概览
- 数据获取和分析的几个步骤
- 例子：今晚看什么电影
- 例子：公司的增长方向决策

- Python 简介
- Python 的基本语法，基本类型，控制，循环，基本数据结构，函数。
- 练习：一个简单的计数程序
- 几个错误程序分析 - 学习如何从程序的输出知道哪里出了问题

- 爬虫和数据处理概览: 能做什么，怎么做。
- 爬虫案例简介：搜索引擎、商品比价、抢票、网站营销、大数据分析等。
- 介绍网站和网址，请求和响应。Python 处理 HTTP 请求的库。
- 练习：使用 Python 对某个网站发请求并得到响应。使用 print 输出数据以了解程序的执行状态。

- HTML 简介和 HTML 元素
- 类，id, 选择器
- 练习：使用浏览器 inspect 找到一个元素对应的选择器
- 练习：修改刚才的程序，使用 Python 库 (beautifulsoup) 提取爬取的数据

- JSON 简介和语法
- 常见免费 web service 介绍
- 练习：爬取一个 web service，并且从结果中提取出需要的信息

- 数据处理工具概览 (每种简介和 API 示例)
- 数据分析和画图：pandas
- 数据清洗和转换：openrefine
- 信息提取：newspaper
- 图像识别：tesseract (看图说话的简单例子)
- 自然语言处理: nltk (情感分析的 api 或者分词 api?)

- 全站爬虫构造概览：入口页面 -> 发现新的链接 -> 继续爬取，使用 Set 避免重复爬取，汇总信息
- 练习：从主页起完整爬取一个小网站

- 扩展阅读和参考资料：
  - Python 可以做什么，可能有用的 Python 库
  - 文明的爬虫：不要对网站造成过大负担，尊重 robots.txt 等
  - 错误处理
  - 爬虫框架
  - 反爬虫和应对措施、云代理服务、纯 js 渲染页面的爬取。
  - 数据挖掘，pandas 等工具

# 工具

- Chrome, 插件 JSON View
- 编辑器
- Python3
- Pip
- Jupyter Notebooks

# 辅助材料

Cheatsheet

- 正面：Python 语法和常用函数
- 反面：Pandas 和各种工具函数, Chrome 拷贝选择器的图示

# Show Case

- Jupyter Notebook?
- A server for upload and compile?

# Python 数据处理例子

https://blog.plover.com/lang/ambiguous.html -- 使用词典找出西班牙语里的多义词, 改写成对应的 python 版是：

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

涉及知识点：打印，文件读取，基本字符串操作（split, join)，迭代 list / dict, 格式化字符串

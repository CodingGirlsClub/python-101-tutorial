# 爬虫实战

- 如果网站提供了 API，那么用 API 比从网页解析要更简单。
- 如果 API 不能满足需求，再去考虑做网页爬虫。
- 总结网址的规律，写成循环。

# 总结规律

例如贴吧的一个帖子，首页，第二页，第三页的网址分别如下：

https://tieba.baidu.com/p/1433563243

https://tieba.baidu.com/p/1433563243?pn=2

https://tieba.baidu.com/p/143b3563243?pn=3

那么只要我们知道一共有多少页，然后循环迭代 `pn=...`，就能遍历所有的页面。我们可以用 `range(from, to)` 构造一个迭代器，从 `from` 迭代到 `to - 1`:

```python
for page in range(1, 4)
    url = f"https://tieba.baidu.com/p/1433563243?pn={page}"
```

# 网站的结构

网站由一个或者多个网页组成，各个网页之间以超链连接起来，画成图会像这样：

![](https://upload.wikimedia.org/wikipedia/commons/8/83/Main_Page_Usability.png)

# 全站爬虫的构造

爬虫分为定向爬虫和全站爬虫。

定向爬虫只关注特定的内容，全站爬虫的目标却是爬下整个网站。

全站爬虫一般应用于搜索引擎、发现新内容、保存网络快照等目的。

为了实现爬虫的连续工作，我们可以把任务分解开来。

编程中如何分解任务？一种思维模式是：

- 可以先考虑简单的、特殊的情况。
- 把简单情况的代码写出来后，再把它改成更通用的情况 -- 例如改成一个函数。
- 把分解的函数组装起来，调试完成任务。

最简单的状况，网站只有一个页面的时候，我们回忆 requests 的用法，直接发出请求就可以了。

稍微复杂一点的情况，网站有一个入口页和多个次级页面，我们分析入口页的所有链接，得到次级页面的链接爬取汇总。

```python
links = BeautifulSoup(page).select('a')
urls = []
for link in links:
    urls.append(link['href'])
```

再复杂一点，网站的次级页面上还有到更次一级的页面的链接，我们可以把上面的代码提炼成一个函数：

```python
def extract_links(page):
    links = BeautifulSoup(page).select('a')
    urls = []
    for link in links:
        urls.append(link['href'])
    return urls
```

把请求网页的代码也组合到一起：

```python
def get_page(url):
    page = requests.get(url)
    urls = extract_links(page.text)
    for sub_url in urls:
        get_page(sub_url)
```

这个函数调用了自己，叫做 **递归函数**。

上面的代码还有一些问题，如果子页面恰好链接到了父页面，它就停不下来了（实际上会出现一个栈溢出错误）。我们可以用集合来保证不会爬取相同的网页。

```python
crawled = set()
def get_page(url):
    if url in crawled:
        return # 下次碰到相同的网页，它就不会再爬取了
    crawled.add(url)
    page = requests.get(url)
    urls = extract_links(page.text)
    for sub_url in urls:
        get_page(sub_url)
```

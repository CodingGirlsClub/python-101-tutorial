# Demo 练习
> Cooking time: 45 mins active / 60 mins passive

> **Learning by Doing**:
> - **Tasks for Learners**: 请学员创建Python文件 `demo.py`, 对下列Python语法进行练习。在练习过程中，请弄懂demo中每一行代码的意义。`先学会阅读，接着模仿，再自己创造。`
> - **Tasks for Coaches**: 请教练对学员的练习提供一定的辅助，请控制好时间。

### 题目

假如我想把 xkcd.com 上的漫画图片爬下来 100 张。能写一个 Python 脚本完成吗？

> 【提示】数学家波利亚在[怎样解题](https://book.douban.com/subject/2124114/)一书中讲到，解决一个问题的四个步骤：
>
> - 理解题目：我们有什么，目标是什么？
> - 拟定方案：通过什么思路去解决问题？条件和结果之间还有哪些缺失的环节？
> - 执行方案：roll your sleeve，付诸行动。期间可能会需要修改方案中不合理的地方，请保持尝试和练习。
> - 回顾：得到的结果是否符合预期？有什么收获？
>
> 工程是结合了整体和细节的技术。工程师通常先把总体规划分解成很多个细节，然后集中注意力解决每一个细节，然后再把细节组合成新的整体，重新理解和调整。
>

爬虫的任务可以大致划分为；遍历链接、分析页面、下载数据、输出结果。

1. 遍历链接
  - 问题：页面的链接有什么规律？ 

    > 访问网站点几下 "prev"，观察地址栏的变化发现链接的格式是 `https://xkcd.com/{数字}/`
  - 问题：如何用 Python 生成所有的链接？（回顾[字符串拼接](./2.Python/5-python-syntax-advanced.md#拼接字符串)） 
    > ```python
    > for n in range(100):
    >   link = f"https://xkcd.com/{n}/"
    > ```
2. 分析和下载
  - 问题：如何获得页面或者图片？（回顾 [Requests 的使用](./2.Python/4-python-request.md#requests-的使用)）
  - 问题：漫画图片的选择器是什么？（回顾[选择器](./3.Crawler/1-python-html.md#css-选择器)） 

    > 用 Chrome 开发者工具，复制选择器，得到 `#comic > img`
  - 问题：如何用 Python 提取图片元素的 `src` 属性？如何补足成完整的图片地址？（回顾 [BeautifulSoup 的使用](./3.Crawler/1-python-html.md#用-python-解析-html)） 
    > ```python
    > src = Beautiful(page).select("#comic > img")[0]["src"]
    > image_link = f"http:{src}"
    > ```
3. 输出结果
  - 问题：结果格式是图片，如何保存二进制文件？（回顾[保存文件的方法](./2.Python/3-python-syntax.md#读写文件)）
  - 问题：保存多个文件如何命名？（回顾[循环语句](./2.Python/3-python-syntax.md#循环)）


编程是一项需要注意力和细心的工作，大部分程序员也不能一次就把程序写对，除了阅读出错信息以外，往往还需要编写一些代码帮助了解程序的执行状况。

4. 问题：输出些什么让你知道程序正在运行？ 

  > 使用 `print()` 打印程序在做的事情，做到了哪一步。



[Demo 参考代码](./demos/crawl_xkcd.py) ：你能读懂每行代码吗？



**Learning by Thinking**：

- 每个图片都有一个 `title` 属性，能否把它也顺便保存下来？
- 你有没有过一些想法，不知道如何去实现，掌握了简单的爬虫技术后，是否变得可能？（如果感觉掌握的知识技能还不足以支撑实现，可向教练请教或者组队完成）
- 你掌握了写程序解决问题的思路吗？是否从中掌握了新的思维方式？

### Demo 2

[LibreOJ](https://loj.ac) 是一个 Online Judge 网站。尝试获取上面的题库？

[Demo 2 参考代码 - 作者：张未波](./demos/crawl_loj.py)

爬虫使用了正则表达式提取文本。请尝试通过阅读文档学习正则表达式：[Python Regular Expression HOWTO](https://docs.python.org/3.7/howto/regex.html)。

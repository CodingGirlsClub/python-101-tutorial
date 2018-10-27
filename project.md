# 大作业和分享

下面任选一题，或者有自己的想法也可以在教练的指导下另外选题。

### 选题 1

假如我想把 xkcd.com 上的漫画图片爬下来 100 张。能写一个 Python 脚本完成吗？

提示：

1. 页面的链接有什么规律？
  > 访问网站点几下 "prev"，观察地址栏的变化发现链接的格式是 `https://xkcd.com/{数字}/`
2. 如何用 Python 循环和字符串拼接遍历链接？
  > ```python
  > for n in range(100):
  >   link = f"https://xkcd.com/{n}/"
  > ```
3. 漫画图片的选择器是什么？
  > 用 Chrome 开发者工具，复制选择器，得到 `#comic > img`
4. 如何用 Python 提取图片元素的 `src` 属性？如何补足成完整的图片地址？
  > ```python
  > src = Beautiful(page).select("#comic > img")["src"]
  > image_link = f"http:{src}"
  > ```
5. Python 如何保存文件？
  > ```python
  > with open("image.jpg", "wb") as f:
  >   f.write(data)
  > ```
6. 保存多个文件如何命名？
  > 使用 `for` 循环的循环变量，拼接字符串。
7. 输出些什么让你知道程序正在运行？
  > 使用 `print()` 打印程序在做的事情，做到了哪一步。

进阶：

每个图片都有一个 `title` 属性，能否把它也顺便保存下来？

[Demo 代码](./project1_demo.py)

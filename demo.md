# Demo 练习
> Cooking time: 45 mins active / 60 mins passive

> **Learning by Doing**:
> - **Tasks for Learners**: 请学员创建Python文件 `demo.py`, 对下列Python语法进行练习。在练习过程中，请弄懂demo中每一行代码的意义。`先学会阅读，接着模仿，再自己创造。`
> - **Tasks for Coaches**: 请教练对学员的练习提供一定的辅助，请控制好时间。

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
  > src = Beautiful(page).select("#comic > img")[0]["src"]
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

**进阶**：

每个图片都有一个 `title` 属性，能否把它也顺便保存下来？

[Demo 代码](./demo1.py)

> **Learning by Thinking**: 这里每一步我们都用问号结尾引导大家，教程这么设计是想让大家学会什么？
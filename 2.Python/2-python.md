# Python 简介

> Cooking time: 15 mins active / 20 mins passive

Python 是计算机入门首选语言之一，编写简单，有丰富的生态系统和库，在很多行业和学科都有出色的表现。当前的稳定版本是 3.7。

运行 Python 程序需要 Python 解释器（其实是编译+执行）。

**Task for Coaches**:
- 解释什么是解释器
- 解释什么是编译
- 解释什么是执行

## 第一个 Python 程序

1. 使用IDE Anaconda打开 spyder

  ![image-20181023182654100](https://ws4.sinaimg.cn/large/006tNbRwly1fwic0c9oomj310y0m4785.jpg)

2. 新建python文件：

   - 点击 spyder 右上角第一个图标
   - 或者，使用快捷键（ Mac ：CMD + n； Windows ：ctrl + n）

   ![image-20181023182937635](https://ws4.sinaimg.cn/large/006tNbRwly1fwic35u3eqj30kh03hwf3.jpg)

3. 我们先看看spyder的界面，spyder包含多个单独的窗口（标有红色方框），每个窗口都有赞成的标签（标有绿色圆框）

   ![image-20181023183934643](https://ws4.sinaimg.cn/large/006tNbRwly1fwichbrto1j30va0nvwhv.jpg)

4. 在编辑器中输入`import this`

5. 保存Python文件（注意Python文件都是以 `.py`结尾的文件）：
  > Task for Learners：请使用搜索引擎搜索[「Python文件命名规范」](https://www.bing.com/search?q=python%E6%96%87%E4%BB%B6%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83&qs=n&form=QBRE&sp=-1&pq=python%E6%96%87%E4%BB%B6%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83&sc=0-12&sk=&cvid=B1875E99BD0E444FA38C9A35911A955A)，随意阅读几篇介绍Python命名规范的文章。

  - 点击 spyder 右上角第三个图标
  - 或者，使用快捷键（ Mac ：CMD + s； Windows ：ctrl + s）
  ![image-20181023183230195](https://ws3.sinaimg.cn/large/006tNbRwly1fwic69r6aoj30kh03haao.jpg)

6. 运行Python文件：
   - 点击 spyder 右上角第七个图标
   - 或者，使用快捷键（ Mac ：F5； Windows ：F5）
   
   ![Spyder__Python_3_6_](https://ws4.sinaimg.cn/large/006tNbRwly1fwid2kg2f3j30vb0nv795.jpg)

可以看到 Python 的哲学，描述于一首诗中。上面的代码中，`import` 语句的作用是引入一个包，而这个包 `this` 的作用是打印这首诗。

## 编程思维 - 任务分解
编程的第一步就是把要做的事情分解成一步一步，用计算机语言讲清楚，让计算机可以执行。

![图片来于[Computational Thinking:Decomposition | Abstraction | Patterns | Algorithms](https://www.computationalthinkers.com/product/computationalthinking/)](https://ws4.sinaimg.cn/large/006tNbRwly1fwict5oyqdj31kw1kw124.jpg)

Donald Knuth 说过：一个人并不真正了解一件事，除非他把一件事教给计算机 —— 特别是用算法把它描述出来。

> It has often been said that a person does not really
> understand something until he teaches it to someone else.
> Actually a person does not really understand something
> until after teaching it to a computer, i.e., express it
> as an algorithm.

**Learning by Additional Reading**:  [Google for Education: Computational Thinking](https://edu.google.com/resources/programs/exploring-computational-thinking/) (需要科学上网，拓展阅读，非本工作坊所需)

## 程序出错

有一个说法叫：计算机很笨却听话（The computer is very dumb but obedient）。当遇到语法错误时，即使是很微小的错误，它也不会自己修正它。程序员每天都会遇到很多各种语法错误。只要仔细阅读错误信息，找到并修正就可以了。

**Learning by Additional Reading**:  [Introduction to Computer Programming - What Is It](http://guyhaas.com/bfoit/Intro_to_Programming/Programming.html) 

## 打印一段话

**Learning by Doing**: 

Python 的 `print` 函数不是打印到纸上，而是打印到屏幕上（确切来说是标准输出流）

```
print("I can program!")
```



# Python 简介

Python 是计算机入门首选语言之一，编写简单，有丰富的生态系统和库，在很多行业和学科都有出色的表现。当前的稳定版本是 3.7。

运行 Python 程序需要 Python 解释器（其实是编译+执行）。

# 第一 Python 程序

打开 Jupyter notebook，输入：

```python
import this
```

然后回车。可以看到 Python 的哲学，描述于一首诗中。

`import` 语句的作用是引入一个包，而这个包 `this` 的作用是打印这首诗。

# 编程

编程就是把要做的事情，分解成一步一步，用计算机语言讲清楚，让计算机可以执行。

** 编程思维 **

Donald Knuth 说过：一个人并不真正了解一件事，除非他把一件事教给计算机 —— 特别是用算法把它描述出来。

> It has often been said that a person does not really
> understand something until he teaches it to someone else.
> Actually a person does not really understand something
> until after teaching it to a computer, i.e., express it
> as an algorithm.

** 程序出错 **

有一个说法叫：计算机很笨却听话（The computer is very dumb but obedient）。当遇到语法错误时，即使是很微小的错误，它也不会自己修正它。程序员每天都会遇到很多各种语法错误。只要仔细阅读错误信息，找到并修正就可以了。

参考阅读: http://guyhaas.com/bfoit/Intro_to_Programming/Programming.html

# 打印一段话

Python 的 `print` 函数不是打印到纸上，而是打印到屏幕上（确切来说是标准输出流）

```
print("I can program!")
```

# IPython

IPython 是 Interactive Python 的缩写。它提供了自动完成（按 tab 键），查看文档，多行编辑等功能并且易于扩展。

在 IPython 中可以输入 `?` 查看所有命令。

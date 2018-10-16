# 组装字符串

使用 `f"..."` 和 `{}` 构造字符串。试试下面的例子：

    me = "程序员"
    sentence = f"hello, {me}"
    print(sentence)

# 列表

创建一个列表：

    li = [1, 2, 3]

往列表中添加成员：

    li.append(1)

用 `for`……`in` 遍历列表：

    for e in li:
        print(e)

# 字典

创建一个字典：

    di = {}

用 `for`……`in` 遍历字典：

    for key, value in di.items():
        print(f"{key} {value}")

# 函数

之前我们学习了用一个词代表值（变量），在 Python 中我们也能用一个词代表一段代码。

定义函数用 `def` 关键字，接上函数名称，参数列表和冒号。试理解下面的代码：

    def double(x):
        return x * 2

在缩进的代码块中编写函数体，使用 `return` 返回需要的内容。

之前我们学习的 `print` 也是一个函数。

调用函数：

    double(4)

也可以嵌套的调用函数：

    print(double(4))

小提示：Python 的运算符 `+`，`-`，`*`，`/` 等等其实都是函数。

(todo 更多综合性的例子)
(todo 小问题和练习)


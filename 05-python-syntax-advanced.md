# 拼接字符串

使用 `f"..."` 和 `{}` 可以把变量的值拼接到字符串中去。试试下面的例子：

    me = "程序员"
    sentence = f"hello, {me}"
    print(sentence)

# 列表

列表 (`list`) 是一种顺序的数据。列表中的每个元素都对应一个整数下标，从 0 数起。

创建一个空的列表：

    li = []

创建一个带 3 个元素的列表：

    li = ["zero", "one", "two"]

查看列表的长度：

    len(li)

取出列表中的元素：

    li[1]

往列表中添加成员：

    li.append(1)

用 `for`……`in` 遍历列表：

    for e in li:
        print(e)

这个循环也可以用 `while` 来写，相当于：

    i = 0
    while i < len(li):
        print(li[i])
        i = i + 1

`for` 比较方便迭代列表。

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

之前我们学习的 `print`, `len` 都是函数，而且是是 Python 自带的函数 (built-in functions)。

调用函数：

    double(4)

由于函数返回的是一个值，这个值也可以赋予给变量：

    twice = double(4)
    four_times = double(twice)

函数返回的值也可以传递给下一个函数：

    print(double(4))

小提示：Python 的运算符 `+`，`-`，`*`，`/` 等等其实都是函数。

(todo 更多综合性的例子)

(todo 小问题和练习)


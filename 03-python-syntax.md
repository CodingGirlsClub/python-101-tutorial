# 注释

一行中以 `#` 开始直到行末的部分都属于注释

    # 可以在代码中穿插写一些笔记，不影响程序的执行

# 数据类型

整数

    1
    1234

小数（浮点数）

    3.1415

字符串 -- 注意要用半角英文引号包起来:

    "双引号字符串"
    '单引号字符串'

转义字符:

    "\n" # 换行
    "\r" # 回车
    "\t" # tab

以上的字符串写法限制只能写在一行内。Python 支持三个引号的多行字符串语法，方便书写多行的内容：

    """
    床前明月光
    疑是地上霜
    举头望明月
    低头思故乡
    """

特殊量 -- 代表什么都没有

    None

查看数据的类型

    type(3) # int

# 运算

在 Jupyter 中输入下面的表达式试试：

    1 + 1
    2.5 * 3
    4 / 2

除以 0 会得到 Not a Number

    1 / 0 # NaN

字符串也可以进行连接运算（使用 `+` 运算符）

    "hello" + " world"

注意：全角符号和半角符号的区别。

# 变量

用一个符号代表一个值（`=` 叫做赋值运算符）

    a = 3
    some_value = "一个值"

这个符号代表的值可以重新赋值，所以这个量称为变量 -- variable。

运算的结果可以赋予变量，变量也可以参加运算，例如下面计算平均值的代码：

    sum = 1 + 2 + 3 + 4 + 5
    average = sum / 5.0
    print(average)

# 条件

在 Python 中表达逻辑：“如果” 满足某种条件 “那么” 你就给我做这件事情。

布尔类型（注意大小写）

    True
    False

条件语法

    if True:
        print("真")
    if False:
        print("假")

注意：

- 「如果」部分以关键字 `if` 开始，接着是条件表达式，后面必须再加上冒号 `:`
- 「那么」部分的缩进要比 `if` 行深，推荐用 4 个空格缩进（参考 [PEP8](https://www.python.org/dev/peps/pep-0008/#indentation)）

上面两个条件内容互斥，我们可以用双路条件 `if`……`else`：

    t = True
    if t:
        print(“真”)
    else:
        print("假")

布尔类型上可以用布尔运算:

- 而且 `and`
- 或者 `or`
- 否定 `not`

例如：

    True and True
    not False

比较运算符

- `==` 等于（两个等号，注意和赋值运算的不同）
- `>` 大于
- `<` 小于
- `!=` 不等于
- `>=` 大于或者等于
- `<=` 小于或者等于

综合应用例：「如果天气晴朗并且低于 30 度就出去玩」

    weather = "rainy"
    temperature = 20

    if weather == "sunny" and temperature < 30:
        print("lets go out!")

# 循环

计算机是处理数据的机器。循环（迴圈）告诉机器重复做相同的工作。

`while` 循环打印 0 到 100

    a = 0
    while a <= 100：
        print(a)
        a = a + 1

同样注意别忘了 `:` 和缩进

循环一般由循环条件和循环体组成。（todo: 补充 while 循环执行的动图）

死循环：不会结束的循环。

    import time
    while True:
        print("I am stuck")
        time.sleep(1)

要结束程序，可以按 Ctrl + C 退出。(一个手指按住 Ctrl 键，然后另一个手指按 C 键，退出时解释器会报告一段错误，意思是收到了中断信号)。

循环控制：

- `continue` 进入下一个轮回
- `break` 结束循环

(todo 循环控制例子)

# 函数

我们学习了用一个词代表值（变量），在 Python 中我们也能用一个词代表一段代码。

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

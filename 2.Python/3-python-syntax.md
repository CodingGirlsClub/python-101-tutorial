# Python 语法

提示：切换到英文输入法编程可以避免一些用错符号的错误。

## 魔法注释

惯例：把这一行写在 Python 文件的头一行，表达这个文件的非 ASCII 字符的编码为 UTF-8，不然遇到中文会出现编码错误。

```python
# encoding: utf-8
```

## 注释

注释是写给阅读代码的人看的，计算机会忽略注释。一行中以 `#` 开始直到行末的部分都属于注释。

```python
# 可以在代码中穿插写一些笔记，不影响程序的执行。
```

## 基本数据类型

整数，类型为 `int`

```python
1234
-1234
```

小数（浮点数），类型为 `float`

```python
3.1415926
```

字符串，类型为 `str`

```python
"双引号字符串" # 注意要用半角英文引号包起来
'单引号字符串'
```

字符串中，空格也是字符：

```python
" " # 这也是一个字符串
```

有一些字符也是没有对应的字形（Glyph），但是可以用 **转义字符** 表达:

```python
"\n" # 换行
"\r" # 回车
"\t" # tab
```

以上的字符串写法有个限制：只能写在一行内。Python 支持三个引号的多行字符串语法，方便书写多行的内容：

```python
"""
床前明月光
疑是地上霜
举头望明月
低头思故乡
"""
```

特殊量 -- 代表什么都没有

```python
None
```

查看数据的类型

```python
type(3) # int
```

## 运算

在 Jupyter 中输入下面的表达式试试：

```python
1 + 1
2.5 * 3
4 / 2
```

除以 0 会得到 NaN（Not a Number）

```python
1 / 0 # NaN
```

字符串也可以进行连接运算（使用 `+` 运算符）

```python
"hello" + " world"
```

注意：全角符号和半角符号的区别。

## 变量

用一个名称代表一个值（`=` 叫做赋值运算符）

```python
a = 3
some_variable_1 = "一个值" # 变量名可以包含字母、数字和下划线，但不能以数字打头
```

这个符号代表的值可以重新赋值，所以这个量称为变量 -- variable。

运算的结果可以赋予变量，变量也可以参加运算，例如下面计算平均值的代码：

```python
sum = 1 + 2 + 3 + 4 + 5
average = sum / 5.0
print(average)
```

## 条件

在 Python 中表达逻辑：“如果” 满足某种条件 “那么” 你就给我做这件事情。

布尔类型（注意大小写）

```python
True
False
```

条件语法

```python
if True:
    print("真")
if False:
    print("假")
```

注意：

- 「如果」部分以关键字 `if` 开始，接着是条件表达式，后面必须再加上冒号 `:`
- 「那么」部分的缩进要比 `if` 行深，推荐用 4 个空格缩进（参考 [PEP8](https://www.python.org/dev/peps/pep-0008/#indentation)）

上面两个条件内容互斥，我们可以用双路条件 `if`……`else`：

```python
t = True
if t:
    print(“真”)
else:
    print("假")
```

布尔类型上可以用布尔运算:

- 而且 `and`
- 或者 `or`
- 否定 `not`

练习：思考下面几个表达式的值并在 IPython 验证：

```python
True and True
not False
False or True
```

比较运算符可以判断两个值是否相等或者孰大孰小：

- `==` 等于（两个等号，注意和赋值运算的不同）
- `>` 大于
- `<` 小于
- `!=` 不等于
- `>=` 大于或者等于
- `<=` 小于或者等于

练习：思考下面几个表达式的值并在 IPython 验证：

```python
1 <= 3
5 > 4 and 4 > 3
```

综合运用条件语句和比较运算符：「如果天气晴朗并且低于 30 度就出去玩」

```python
weather = "rainy"
temperature = 20

if weather == "sunny" and temperature < 30:
    print("lets go out!")
```

## 循环

计算机是处理数据的机器。循环（迴圈）告诉机器重复做相同的工作。

`while` 循环打印 0 到 100

```python
a = 0
while a <= 100：
    print(a)
    a = a + 1
```

同样注意别忘了 `:` 和缩进

循环一般由循环条件和循环体组成。（todo: 补充 while 循环执行的动图）

**死循环** 的意思是：不会结束的循环。

```python
import time
while True:
    print("I am stuck")
    time.sleep(1)
```

要结束程序，可以按 Ctrl + C 退出。(一个手指按住 Ctrl 键，然后另一个手指按 C 键，退出时解释器会报告一段错误，意思是收到了中断信号)。

循环控制：

- `continue` 进入下一个轮回
- `break` 结束循环

(todo 循环控制例子)

## 函数

我们学习了用一个词代表值（变量），在 Python 中我们也能用一个词代表一段代码。

定义函数用 `def` 关键字，接上函数名称，参数列表和冒号。试理解下面的代码：

```python
def double(x):
    return x * 2
```

在缩进的代码块中编写函数体，使用 `return` 返回需要的内容。

之前我们学习的 `print`, `len` 都是函数，而且是是 Python 自带的函数 (built-in functions)。

调用函数：

```python
double(4)
```

由于函数返回的是一个值，这个值也可以赋予给变量：

```python
twice = double(4)
four_times = double(twice)
```

函数返回的值也可以传递给下一个函数：

```python
print(double(4))
```

小提示：Python 的运算符 `+`，`-`，`*`，`/` 等等其实都是函数。

(todo 更多综合性的例子)

(todo 小问题和练习)

## 输入和输出简介

IO 是输入/输出（input / output）的缩写。

IO 是程序能从真实世界获取信息 (输入)，对真实世界产生影响（输出）的基础。

典型的输入包括：用户键盘输入，鼠标点击，读取文件，读取网络数据，获取传感器的读数，……

典型的输出包括：在屏幕显示文字，在屏幕绘制图像，输出到打印机，发出声音，发送数据到网络端口，……

## 读写文件

读写文件是 Python 里最基本的 IO 操作之一。

`open` 函数打开一个文件，`"r"` 模式是读取，`"w"` 模式是写入。

以读取模式打开一个文件 "foo.csv"，并返回对应的文件对象：

```python
f = open("foo.csv", "r")
```

关闭一个文件对象：

```python
f.close()
```

下面的代码打开文件，读取文件的内容，然后关闭文件。

```python
f = open("foo.csv", "r")
data = f.read()
f.close()

print(data)
```

但是，在对文件操作的时候有可能发生异常！例如文件编码不正确，或者出现了没考虑到的某种状况，就会出错。

> 没处理各种异常情况的一段程序，不能成为一个产品

Python 提供了 `with .. as` 语法， 不用处理异常和写 `close`，就能保证处理文件后能自动关闭它。

读取一个文件

```python
with open("foo.csv", "r") as f:
    data = f.read()
```

写入一个文件

```python
with open("foo.csv", "w") as f:
    f.write(data)
```

# 光学字符识别

人可以轻松辨认一张图片上的文字，但是计算机却没这么容易。

思考：为何有些文字可以选中并复制，而图片上的文字却不能选中？

从图片辨认出里面包含的文字的技术，叫做 OCR。OCR 是光学字符识别（Optical Character Recognition）的缩写。

爬虫有时会需要用到 OCR 技术：

- 识别验证码
- 获得图片数据中的文本内容

最常用的 OCR 软件是开源的 Tesseract。另外还有很多商用的 OCR 软件和服务。

# 使用 Tesseract

先使用 PIL 打开图片

```python
from PIL import Image
image = Image.open('1-intro.001.png')
```

然后进行识别。识别时需要告诉 tesseract 用什么语言文字模型。如 `lang="chi_sim"` 是简体中文，`lang="chi_tra"` 是繁体中文。

```python
import pytesseract
pytesseract.image_to_string(image, lang="chi_sim")
```

可用的语言代码参见：https://github.com/tesseract-ocr/tessdata_best 。

# 命名参数语法

上面的 `lang="chi_sim"` 参数使用了 Python 函数的命名参数语法。

下面定义一个函数，带命名参数 `a` 和 `b`：

```python
def add(a=1, b=3):
    return a + b
```

在定义时，命名参数都会带一个默认值，如果在调用时不给出来，就使用默认值代替。

使用上面的函数：

```python
add()     # 4
add(b=0)  # 1
add(a=0)  # 3
add(5, 7) # 12 -- 只要位置对应，也可以省略参数的名字
```

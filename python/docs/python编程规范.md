# python 编程规范

编程语言不是艺术，而是工作或者说是工具，所以整理并遵循一套编码规范是十分必要的。

## 一、代码编排

### 1、缩进。

* 使用4个空格进行缩进，
* 不使用Tap，
* 更不能混合使用Tap和空格。

### 2、分号。

* 不要在行尾加分号`;`，
* 也不要用分号将两条命令放在同一行。

### 3、行长度。

* 每行不超过80个字符。
* 换行可以使用反斜杠`\`。
* 换行点要在操作符的后边敲回车。

### 4、空行

* 类定义和函数定义之间**空两行**;
* 类中的方法定义之间**空一行**；
* 函数内逻辑无关段落之间**空一行**；
* 其他地方尽量不要再空行。

### 5、空格

* 总体原则，避免不必要的空格。
* 右括号前不要加空格。
* 逗号、冒号、分号前不要加空格。
* 函数的左括号前不要加空格。如`Func(1)`
* 序列的左括号前不要加空格。如`list[1]`
* 函数默认参数使用的赋值符左右省略空格。
* 操作符左右各加一个空格，不要为了对齐增加空格。

## 二、注释

### 0、总体原则

* 错误的注释不如没有注释。所以当一段代码发生变化时，第一件事就是修改注释。

### 1、文件起始位置

* 大部分.py文件不必以`#!`作为文件的开始。
* 程序的main文件应该以`#!/usr/bin/env python`开始。
* Python2文件起始位置应注明文件字符编码方式。例如如`# coding: utf-8`
* 注明创建时间。
* 注明版本号。
* 注明作者。
* 每个文件应该包含一个许可样板。根据项目使用的许可（例如，Apache2.0，BSD，GPL），选择合适的样板。

### 2、文档字符串

* 为所有的共有模块、类、方法写docstrings；非共有的没有必要，但是可以写注释。
* 文档字符串的惯例是使用三重引号''''''

下文所指的函数，包括函数，方法，以及生成器。

* 文档字符串应该包含函数做什么，以及输入和输出的详细描述。
* 通常不应该描述“怎么做”，除非是一些复杂的算法。
* 关于函数的几个方面应该在特定的小节中进行描述记录。
  * 每节应该以一个标题行开始。
  * 标题行以冒号结尾。
  * 除标题行外，节的其他内容应该被缩进。
  * Args:列出参数的名字，并在名字后面使用一个冒号和一个空格，分隔对该参数的描述。
  * Returns:(或者Yields:用于生成器):描述返回值的类型和语义，如果函数返回None，这一部分可以省略。
  * Raises:列出与接口有关的所有异常。

* 如果你的类有公共属性(Attributes),那么该类的文档字符串中应该有一个属性(Attributes)段，并且应该遵守和函数参数相同的格式。

### 3、块注释和行注释

* 如果你在下次代码审查的时候必须解释一下，那么你应该现在就给它写注释。
* 注释应该至少离开代码2个空格。
* 尽量少使用行注释。
* 绝不要描述代码。

## 三、命名规范

### 1、应该避免的名称

* 单字符名称，除了计数器和迭代器。
* 包/模块名中的连字符(-)。
* 双下划线开头并结尾的名称(Python保留,例如`__init__`)

### 2、命名约定

* 所谓“内部(Internal)”表示仅模块内可用，或者，在类内是保护或者私有的。
* 用单下划线开头表示模块变量或函数是protected的(使用`import * from`时不会包含)。
* 用双下划线开头的实例变量或方法表示类内私有。
* 将相关的类和顶级函数放在同一个模块里。不像Java，没有必要限制一个类一个模块。
* 对类名使用大写字母开头的单词(如`CapWords`,即Pascal风格),但是模块名应该用小写加下划线的方式(如`lower_with_under.py`)。

### 3、推荐的命名规范

|Type                       |Public            |Internal                                                     |
|:--------------------------|:-----------------|:------------------------------------------------------------|
|Modules                    |lower_with_under  |_lower_with_under                                            |
|Packages                   |lower_with_under  |                                                             |
|Classes                    |CapWords          |_CapWords                                                    |
|Exceptions                 |CapWords          |                                                             |
|Functions                  |lower_with_under()|_lower_with_under()                                          |
|Global/Class Constants     |CAPS_WITH_UNDER   |_CAPS_WITH_UNDER                                             |
|Global/Class Variables     |lower_with_under  |_lower_with_under                                            |
|Instance Variables         |lower_with_under  |_lower_with_under(protected)or__lower_with_under(private)    |
|Method Names               |lower_with_under()|_lower_with_under()(protected)or__lower_with_under()(private)|
|Functions/Method Parameters|lower_with_under  |                                                             |
|Local Variables            |lower_with_under  |                                                             |
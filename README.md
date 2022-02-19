# PKU中文系编译实习（2022年春）在线文档
欢迎各位同学选修编译原理课程并参与相应的编码实习！

本实习分为两个部分。第一部分，你将熟悉yacc和lex工具的基本使用，并在此基础上利用词法分析和语法分析的相关知识实现一个简易的计算器。第二部分，你将进一步完成对C语言的子集的词法分析和语法分析，并构建出抽象语法树（Abstract Syntax Tree）。

## Ⅰ）环境说明与工具介绍
### 编程语言与运行环境
考虑到大家对各种语言的熟悉程度，本次实习统一使用Python语言。

使用Windows系统或Mac系统来完成本lab都可以。

### Lex & Yacc
Lex和Yacc是最流行的对目标语言进行词法分析和语法分析的工具。其详细使用说明可参考当前目录下的 `lex&yacc_manual.pdf` 文件。**注意**：由于lex和yacc是由c语言实现的，而在本次实习中我们统一使用Python语言，因此在实际操作中我们用python包PLY（见下）来实现同样的功能，对于lex和yacc的具体使用只需简单了解即可。
### PLY
Python包PLY提供了对Lex和Yacc的纯Python实现。本次实习推荐使用3.11版本的PLY包。其安装过程如下：
> 1.下载当前目录下的ply-3.11.zip文件  
> 2.解压此zip文件  
> 3.打开终端（即windows电脑的cmd/powershell，或mac电脑的terminal）进入文件夹ply-3.11中  
> 4.执行如下指令：python setup.py install  
> 5.完成上述指令后，你可以通过 import ply.lex 等方式简单地判断是否安装成功。

PLY包的详细使用说明参见[以下链接](https://www.dabeaz.com/ply/ply.html)。
## Ⅱ） 实习1：简易计算器

## Ⅲ） 实习2：简化的C语言编译器


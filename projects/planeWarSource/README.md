此项目是使用python开发的飞机大战游戏项目,主要学习python的语法和面向对象设计的思想,以及pygame游戏开发的使用和pyinstaller的打包工具。

参考链接:https://mengbaoliang.cn/archives/tag/plane/

1. python语法和面向对象设计
2. pygame游戏开发
3. pyinstaller打包工具
>    首先，进入到项目根目录下
然后，在项目根目录下执行命令：pyinstaller –noconsole –onefile –name plane App.py
接着，拷贝 source 目录到 dist 目录下，保证和 exe 同级目录
最后，可以将 exe 和 source 目录拷贝、分发给没有 Python 环境的机器就可以直接运行
'''
包管理器

支持网络的开发板包含`mip`模块，它可以从 [micropython-lib](https://docs.micropython.org/en/latest/reference/glossary.html#term-micropython-lib)
和第三方站点（包括 GitHub、GitLab）安装软件包。

`mip`（“mip 安装包”）在概念上类似于 Python 的`pip`工具，但它不使用 PyPI 索引，
而是默认使用`micropython-lib`作为索引。

从`micropython-lib`下载时，`mip`将自动获取已编译的`.mpy`文件。

[查看文档](https://docs.micropython.org/en/latest/reference/packages.html)
'''
def install(package: str, index=None, target: str = None,
	version: str = None, mpy: bool = True): ...

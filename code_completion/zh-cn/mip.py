'''
Package management

Installing packages with mip

Network-capable boards include the mip module, which can install packages from
micropython-lib and from third-party sites (including GitHub, GitLab).

mip ("mip installs packages") is similar in concept to Python’s pip tool, however
it does not use the PyPI index, rather it uses micropython-lib as its index by
default.

mip will automatically fetch compiled .mpy file when downloading from
micropython-lib.

[View Doc](https://docs.micropython.org/en/latest/reference/packages.html)
'''
def install(package: str, index=None, target: str = None,
	version: str = None, mpy: bool = True): ...

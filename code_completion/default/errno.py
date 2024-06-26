'''
system error codes

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: [errno](https://docs.python.org/3.5/library/errno.html#module-errno).

This module provides access to symbolic error codes for `OSError` exception.

A particular inventory of codes depends on MicroPython port.

[View Doc](https://docs.micropython.org/en/latest/library/errno.html)
'''
# Constants
errorcode: dict = ...
'''Dictionary mapping numeric error codes to strings with symbolic error code.'''

# Error codes, based on ANSI C/POSIX standard.
# All error codes start with "E".
# As mentioned above, inventory of the codes depends on MicroPython port.
# Errors are usually accessible as `exc.errno` where `exc` is an instance of
# `OSError`. 
EPERM: int = ...
ENOENT: int = ...
EIO: int = ...
EBADF: int = ...
EAGAIN: int = ...
ENOMEM: int = ...
EACCES: int = ...
EEXIST: int = ...
ENODEV: int = ...
EISDIR: int = ...
EINVAL: int = ...
EOPNOTSUPP: int = ...
EADDRINUSE: int = ...
ECONNABORTED: int = ...
ECONNRESET: int = ...
ENOBUFS: int = ...
ENOTCONN: int = ...
ETIMEDOUT: int = ...
ECONNREFUSED: int = ...
EHOSTUNREACH: int = ...
EALREADY: int = ...
EINPROGRESS: int = ...

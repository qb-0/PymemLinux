import ctypes

libc = ctypes.CDLL("libc.so.6")

class IOVec(ctypes.Structure):
    _fields_ = [
        ("iov_base", ctypes.c_void_p),
        ("iov_len", ctypes.c_size_t)
    ]

process_vm_readv = libc.process_vm_readv
process_vm_readv.argtypes = [
    ctypes.c_int, 
    ctypes.POINTER(IOVec), 
    ctypes.c_ulong, 
    ctypes.POINTER(IOVec), 
    ctypes.c_ulong, 
    ctypes.c_ulong
]
process_vm_readv.restype = ctypes.c_ssize_t

process_vm_writev = libc.process_vm_writev
process_vm_writev.argtypes = [
    ctypes.c_int, 
    ctypes.POINTER(IOVec), 
    ctypes.c_ulong, 
    ctypes.POINTER(IOVec), 
    ctypes.c_ulong, 
    ctypes.c_ulong
]
process_vm_writev.restype = ctypes.c_ssize_t
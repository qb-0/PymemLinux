import ctypes, struct
import ressources

def read_bytes(pid, address, byte):
    if not isinstance(address, int):
        raise TypeError("Address must be int: {}".format(address))

    if pid == -1:
        raise Exception("You must open a process before calling this method")

    buff = ctypes.create_string_buffer(byte)
    io_dst = ressources.IOVec(ctypes.cast(ctypes.byref(buff), ctypes.c_void_p), byte)
    io_src = ressources.IOVec(ctypes.c_void_p(address), byte)

    if ressources.process_vm_readv(pid, ctypes.byref(io_dst), 1, ctypes.byref(io_src), 1, 0) == -1:
        raise OSError(ctypes.get_errno())

    return buff.raw

def read_vec3(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("3f"))
    bytes = struct.unpack("3f", bytes)
    return {"x": bytes[0], "y": bytes[1], "z": bytes[2]}

def read_vec2(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("2f"))
    bytes = struct.unpack("2f", bytes)
    return {"x": bytes[0], "y": bytes[1]}

def read_bool(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("?"))
    bytes = struct.unpack("?", bytes)[0]
    return bytes

def read_char(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("c"))
    bytes = struct.unpack("<c", bytes)[0]
    bytes = bytes.decode()
    return bytes

def read_uchar(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("B"))
    bytes = struct.unpack("<B", bytes)[0]
    return bytes

def read_short(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("h"))
    bytes = struct.unpack("<h", bytes)[0]
    return bytes

def read_ushort(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("H"))
    bytes = struct.unpack("<H", bytes)[0]
    return bytes

def read_int(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("i"))
    bytes = struct.unpack("<i", bytes)[0]
    return bytes

def read_uint(pid, address):
    raw = read_bytes(pid, address, struct.calcsize("I"))
    raw = struct.unpack("<I", raw)[0]
    return raw

def read_float(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("f"))
    bytes = struct.unpack("<f", bytes)[0]
    return bytes

def read_long(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("l"))
    bytes = struct.unpack("<l", bytes)[0]
    return bytes

def read_ulong(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("L"))
    bytes = struct.unpack("<L", bytes)[0]
    return bytes

def read_longlong(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("q"))
    bytes = struct.unpack("<q", bytes)[0]
    return bytes

def read_ulonglong(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("Q"))
    bytes = struct.unpack("<Q", bytes)[0]
    return bytes

def read_double(pid, address):
    bytes = read_bytes(pid, address, struct.calcsize("d"))
    bytes = struct.unpack("<d", bytes)[0]
    return bytes

def read_string(pid, address, byte=50):
    buff = read_bytes(pid, address, byte)
    i = buff.find(b"\x00")
    if i != -1:
        buff = buff[:i]
    buff = buff.decode()
    return buff

def write_bytes(pid, address, data, length):
    if not isinstance(address, int):
        raise TypeError("Address must be int: {}".format(address))

    if pid == -1:
        raise Exception("You must open a process before calling this method")

    buff = ctypes.create_string_buffer(length)
    buff.raw = data
    io_src = ressources.IOVec(ctypes.cast(ctypes.byref(buff), ctypes.c_void_p), length)
    io_dst = ressources.IOVec(ctypes.c_void_p(address), length)
    ret = ressources.process_vm_writev(pid, ctypes.byref(io_src), 1, ctypes.byref(io_dst), 1, 0)
    if ret == -1:
        raise OSError(ctypes.get_errno())
    return ret

def write_bool(pid, address, value):
    value = struct.pack("?", value)
    length = struct.calcsize("?")
    res = write_bytes(pid, address, value, length)
    return res

def write_char(pid, address, value):
    value = struct.pack("c", value)
    length = struct.calcsize("c")
    res = write_bytes(pid, address, value, length)
    return res

def write_uchar(pid, address, value):
    value = struct.pack("B", value)
    length = struct.calcsize("B")
    res = write_bytes(pid, address, value, length)
    return res

def write_short(pid, address, value):
    value = struct.pack("h", value)
    length = struct.calcsize("h")
    res = write_bytes(pid, address, value, length)
    return res

def write_ushort(pid, address, value):
    value = struct.pack("H", value)
    length = struct.calcsize("H")
    res = write_bytes(pid, address, value, length)
    return res

def write_int(pid, address, value):
    value = struct.pack("i", value)
    length = struct.calcsize("i")
    res = write_bytes(pid, address, value, length)
    return res

def write_uint(pid, address, value):
    value = struct.pack("I", value)
    length = struct.calcsize("I")
    res = write_bytes(pid, address, value, length)
    return res

def write_float(pid, address, value):
    value = struct.pack("f", value)
    length = struct.calcsize("f")
    res = write_bytes(pid, address, value, length)
    return res

def write_long(pid, address, value):
    value = struct.pack("l", value)
    length = struct.calcsize("l")
    res = write_bytes(pid, address, value, length)
    return res

def write_ulong(pid, address, value):
    value = struct.pack("L", value)
    length = struct.calcsize("L")
    res = write_bytes(pid, address, value, length)
    return res

def write_longlong(pid, address, value):
    value = struct.pack("q", value)
    length = struct.calcsize("q")
    res = write_bytes(pid, address, value, length)
    return res

def write_ulonglong(pid, address, value):
    value = struct.pack("Q", value)
    length = struct.calcsize("Q")
    res = write_bytes(pid, address, value, length)
    return res

def write_double(pid, address, value):
    value = struct.pack("d", value)
    length = struct.calcsize("d")
    res = write_bytes(pid, address, value, length)
    return res

def write_string(pid, address, value):
    bytecode = value.encode()
    length = len(bytecode)
    res = write_bytes(pid, address, bytecode, length)
    return res

def write_vec3(pid, address, value):
    value = struct.pack("3f", *value.values())
    length = struct.calcsize("3f")
    res = write_bytes(pid, address, value, length)
    return res

def write_vec2(pid, address, value):
    value = struct.pack("2f", *value.values())
    length = struct.calcsize("2f")
    res = write_bytes(pid, address, value, length)
    return res
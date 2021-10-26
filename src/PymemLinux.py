import os
import memory

class PymemLinux:
    def __init__(self, process_name=None):
        self.process_id = -1

        if os.getuid() != 0:
            raise OSError("Pymem requires root privileges")

        if process_name:
            self.open_process_from_name(process_name)

    def open_process_from_name(self, name):
        try:
            self.process_id = int(os.popen(f"pidof -s {name}").read().strip())
        except ValueError:
            raise Exception("Process not found")

    def open_process_from_id(self, id):
        self.process_id = id

    def module_base(self, name):
        if not self.process_id:
            raise Exception("You must open a process before calling this method")
        
        for l in open(f"/proc/{self.process_id}/maps"):
            if name in l:
                return int("0x" + l.split("-")[0], 0)
        raise Exception("Module not found")

    def list_processes(self):
        ps = os.popen("ps -aux").read().splitlines()
        for p in ps:
            i = p.split()
            try:
                yield (int(i[1]), " ".join(i[10:]))
            except:
                continue

    def read_bytes(self, address, length):
        return memory.read_bytes(self.process_id, address, length)

    def read_vec3(self, address):
        return memory.read_vec3(self.process_id, address)

    def read_vec2(self, address):
        return memory.read_vec2(self.process_id, address)

    def read_bool(self, address):
        return memory.read_bool(self.process_id, address)
    
    def read_char(self, address):
        return memory.read_char(self.process_id, address)
    
    def read_uchar(self, address):
        return memory.read_uchar(self.process_id, address)

    def read_short(self, address):
        return memory.read_short(self.process_id, address)

    def read_ushort(self, address):
        return memory.read_ushort(self.process_id, address)

    def read_int(self, address):
        return memory.read_int(self.process_id, address)

    def read_uint(self, address):
        return memory.read_uint(self.process_id, address)

    def read_float(self, address):
        return memory.read_float(self.process_id, address)

    def read_long(self, address):
        return memory.read_long(self.process_id, address)

    def read_ulong(self, address):
        return memory.read_ulong(self.process_id, address)

    def read_longlong(self, address):
        return memory.read_longlong(self.process_id, address)

    def read_ulonglong(self, address):
        return memory.read_ulonglong(self.process_id, address)

    def read_double(self, address):
        return memory.read_double(self.process_id, address)
    
    def read_string(self, address, length=50):
        return memory.read_string(self.process_id, address, length)

    def write_bytes(self, address, value, length):
        return memory.write_bytes(self.process_id, address, value, length)

    def write_bool(self, address, value):
        return memory.write_bool(self.process_id, address, value)

    def write_char(self, address, value):
        return memory.write_char(self.process_id, address, value)

    def write_uchar(self, address, value):
        return memory.write_uchar(self.process_id, address, value)

    def write_short(self, address, value):
        return memory.write_short(self.process_id, address, value)

    def write_ushort(self, address, value):
        return memory.write_ushort(self.process_id, address, value)

    def write_int(self, address, value):
        return memory.write_int(self.process_id, address, value)

    def write_uint(self, address, value):
        return memory.write_uint(self.process_id, address, value)

    def write_float(self, address, value):
        return memory.write_float(self.process_id, address, value)

    def write_long(self, address, value):
        return memory.write_long(self.process_id, address, value)

    def write_ulong(self, address, value):
        return memory.write_ulong(self.process_id, address, value)

    def write_longlong(self, address, value):
        return memory.write_longlong(self.process_id, address, value)

    def write_ulonglong(self, address, value):
        return memory.write_ulonglong(self.process_id, address)

    def write_double(self, address, value):
        return memory.write_double(self.process_id, address, value)

    def write_string(self, address, value):
        return memory.write_string(self.process_id, address, value)

    def write_vec3(self, address, value):
        return memory.write_vec3(self.process_id, address, value)
        
    def write_vec2(self, address, value):
        return memory.write_vec2(self.process_id, address, value)
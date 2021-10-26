import PymemLinux

# Reads Entity Data from Assault Cube (x64)

class Offsets:
    ent_list = 0x12E330
    pos = 0x0008
    health = 0x0110
    name = 0x023D


def main():
    pml = PymemLinux.PymemLinux("linux_64_client")
    base = pml.module_base("linux_64_client")

    ent_list_ptr = pml.read_int(base + Offsets.ent_list)
    for i in range(32):
        try:
            ent_ptr = pml.read_int(ent_list_ptr + i * 8)
            health = pml.read_uint(ent_ptr + Offsets.health)
            if health > 0 and health < 101:
                pos = pml.read_vec3(ent_ptr + Offsets.pos)
                name = pml.read_string(ent_ptr + Offsets.name)

                print(f"Name: {name} - Health: {health} - Position: {pos}")
        except Exception as e:
            continue


if __name__ == "__main__":
    main()
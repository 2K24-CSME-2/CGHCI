def display_memory_bytes(width: int, height: int, bpp: int) -> int:
    bytes_used = width * height * bpp // 8
    return bytes_used


width = 1920
height = 1080
bpp = 24

memory = display_memory_bytes(width, height, bpp)

print("Image Memory:", memory, "bytes")

expected = 1920 * 1080 * 24 // 8

assert memory == expected

print("Problem 2 passed!")
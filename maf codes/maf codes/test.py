KEY  = 0x00 # UNKNOWN
FLAG = b"Guessy"

def mix(data: bytes, num: int) -> bytes:
    b = num & 0xFF
    return bytes(x ^ b for x in data)

out = mix(FLAG, KEY)
print(out.hex())
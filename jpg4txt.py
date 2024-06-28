from typing import List
from bitstring import BitStream, Bits
from scipy.fft import dct, idct
import numpy as np

Encoded = bytes

dct_kwargs = {"norm": "ortho", "orthogonalize": True}

def ints_to_bytes(ints: List[int]) -> bytes:
    # Golomb encoding for now, pretty dumb but works
    s = Bits().join(f"se={i}" for i in ints)
    # print(s.pp())
    # bitstring automatically pads with 0s so we add a 1 to mark the end
    s += "0b1"
    return s.tobytes()

def bytes_to_ints(bs: bytes) -> List[int]:
    s = Bits(bs)
    (last_1,) = s.rfind("0b1")
    s = s[:last_1]
    # print(s.pp())
    s = BitStream(s)
    l = []
    while s.pos < len(s):
        l.append(s.read("se"))
    return l

def encode_block(plaintext: bytes) -> Encoded:
    l = list(plaintext)
    d = dct(l, **dct_kwargs)
    # todo: reduce precision in some other way than just rounding the numbers off
    # todo also compress using RLE or something idk
    compressed = [round(x) for x in d]
    return ints_to_bytes(compressed)

def decode_block(encoded: Encoded) -> bytes:
    l = bytes_to_ints(encoded)
    d = idct(l, **dct_kwargs)
    # todo uncompress
    np.clip(d, 0, 255, out=d)
    text = [round(x) for x in d]
    return bytes(text)

def encode(plaintext: bytes) -> Encoded:
    return encode_block(plaintext)

def decode(encoded: Encoded) -> bytes:
    return decode_block(encoded)

if __name__ == "__main__":
    import sys
    a = sys.argv
    if len(a) < 2:
        t = bytes(input("Enter text: "), encoding="utf8")
    else:
        t = bytes(a[1], encoding="utf8")
    e = encode_block(t)
    print(f"Encoded: {e}")
    d = decode_block(e)
    print(f"Decoded:  {d}") # there's an extra space on purpose to line the text up in the terminal
    print(f"Input length: {len(d)}, encoded length {len(e)}")

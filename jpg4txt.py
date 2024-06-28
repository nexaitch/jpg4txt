from typing import List
from scipy.fft import dct, idct
import numpy as np
from struct import pack, unpack

Encoded = List[int]

dct_kwargs = {"norm": "ortho", "orthogonalize": True}

def encode_block(plaintext: bytes) -> Encoded:
    l = list(plaintext)
    d = dct(l, **dct_kwargs)
    # todo: reduce precision in some other way than just rounding the numbers off
    # todo also compress using RLE or something idk
    compressed = [round(x) for x in d]
    return compressed

def decode_block(encoded: Encoded) -> bytes:
    l = list(encoded)
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
    t = bytes(input("Enter text: "), encoding="utf8")
    e = encode_block(t)
    print(f"Encoded: {e}")
    d = decode_block(e)
    print(f"Decoded:  {d}") # there's an extra space on purpose to line the text up in the terminal

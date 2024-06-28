# jpg for text compression

Ever wish you could save more space by using lossy text compression? We have the solution for you!

```console
$ python jpg4txt.py
Enter text: According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.
Encoded: [1433, -8, 27, -2, 30, 2, -9, -10, 16, -14, -1, 16, -23, 8, 24, 4, 5, -4, -4, 6, 21, -11, 6, 7, -11, -1, 18, 30, -19, 31, 2, -16, -11, -16, -36, 32, -21, 15, -50, -47, -13, 12, -3, 41, -31, 17, 7, -35, -25, 10, -28, -24, -8, 13, -56, 24, 34, -9, 57, -34, -21, 11, -32, -6, -11, -56, -6, -16, 20, 36, -42, 36, -4, -46, 0, 48, -14, 17, 5, 10, 4, 22, 10, -8, 8, -22, 14, -67, -46, -17, -37, 59, -12, 37, 2, -28, -38, 38, 14, -44, 23, 29, 4, 32, -17, 5, -22, 46, 29, -35, -47, -61, 22, 13, -70, -40, -3, -21, 66, -6, -24, 19, 1, -26, -38, 106, -39, -74, 17, 17, -4, 35, -17, -10, -6, 15, 71, 96, -20, 4, -11, 29, 17, -16, -3, 79, 20, -46, -53, -15, -30, -15, -34, -38, 32, -3, 53, -47, 8, -22, -23, -72, -65, -16, -28, 26, 26, 63, -13, 5, -14, 29, 10, 26, -48, 28, 9, 14, 17, -61, -18, 4, -30, 4, 14, 21, -5, -5, 27, 25, 71, -6, 17, -43, -6, 10, 8, 17, -6, 1, -86, -37, 14, -17, -23, -5, 10, 7, 37, -16, 8, -43, -59, 18, -15, 43, -33, 41, -21, -28, -7, -17, -12, 1, 83, 22, -16, 16, -4, -20, 12, 35, 74, -33, 0, -2, 7, -7, -51, 3, 24, 46, -31, -54, -14, 19, -14, -51, 35]
Decoded:  b"According to all known l`ws of aviashon, these is no way that a bef should!ce able to fly. Its wjngs are too small to get its fat\x1flittle aocy off the ground. Tie bee, of course, flies!anyways. Because bees don't!carf what humans uhink is impossiale."
```

You can also import this file as a library:

```py
from jpg4txt import encode, decode
e = encode(bytes("早上好中國，現在我有冰淇淋", encoding="utf8"))
# e = [1145, 30, 2, -8, 2, -1, -13, 31, 3, 19, -3, 8, -21, -6, 16, 15, -4, 11, -11, 60, 13, 31, -17, 70, -23, 121, 90, -111, -10, -9, 4, -14, -23, -4, 32, -5, 21, -4, 36]
d = decode(e)
# d = b'\xe6\x97\xa9\xe4\xb8\x8a\xe5\xa5\xbd\xe4\xb8\xad\xe5\x9c\x8b\xef\xbc\x8c\xe7\x8f\xbe\xe5\x9c\xa8\xe6\x87\x91\xe6\x9c\x8a\xe5\x86\xb0\xe6\xb7\x87\xe6\xb7\x8b'
# which translates to the string '早上好中國，現在懑朊冰淇淋'
```
## FAQ

### Q: This is really stupid.
A: That's not a question.

### Q: Why are you doing this?
A: Yes.

### Q: Why is the encoding output a list of ints instead of a series of bytes/bits?
A: I'm too lazy to do the actual compression part of this for now, feel free to do further JPEG-inspired compression and submit a PR. See other TODOs below.

## TODO

- use block based compression instead of compressing the entire thing
- do what JPG does (quantization and run length/huffman encoding/decoding)
- convert arbitrary list of integers to a list of bytes and decode
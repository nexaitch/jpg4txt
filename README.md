# jpg for text compression

Ever wish you could save more space by using lossy text compression? We have the solution for you!

```console
$ python jpg4txt.py
Enter text: According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.
Encoded: b'\x00\x16d\x11\x06\xc5\x07\x84\t\x85A\x00u\x82\x00^\x10\x06\x02\x05\t\x120\x15\x05\xc6\x0e\x0b\xb0H\x0f\x018> !\x0b\x82\x10$\x81\x00\x15\x87\x80\xca\x05\xf0\xd8`\xe0R\x07\xe0\x88p\x11\xc1\x98P\x1c\x83\x10\x88h\x0e \xc0\x08\x8109\x01\x14\x15\x85\x80\x824.\x07\x11\xa0\x84\x14\x01 \n\xa0H\x12\x05\xd8\x18\x03\xa0\x88PP@,\n\x04B\x00\xb48\x02\x1c\x0b\xa0\x8c\t`v\x0c\x81(\x80\xe4\t\xa0L\x0e\x01d\x17\x03\xa1\x00@\x04b\x81h\x17\x01\xd0\x11\xc0\xbe\x07\xb0X\x1a\x01\x1a\x05\x13\x82\xb0\x10\x83A\x88&@\xd4\t\xa05\x00\x9e\x02T\x11\x02! F\x04aQ\xa1\xe0\x11\xc00\x01H\x80\xb8:\x04@\x84\xe0\'\x81@\x17@\xd6\x1f\x07\xa1\xf0"\x814\x08\x07\x03P\x17\xc2\x00\xb4\x17\x80\x91\x01\x06\x08A\xc84\x06\x80~\r\x8a\x0e\x83\xa0\xa04\x03\x088\t\x07\x01\x10\x1e\xc1(\x80z 8\n\x85\x8b\x06\xc0\xc8\x04p\xd0D\x05q\xa1@\x80"\x1a\x80V\x81,8\x08\xc1x\xb0\xa0\xe0%\x02\x10\x80\x15\xc0\xee\t\x03\xe0V\x02\x18\x14\x81X9\x1e\x08\xc3(\x050,\x04 \x80H)\x0c\x01\x18\x04\xa0\x10\xe5\x1c<\x0c\xe6\x06\x00\\\x07\xe0m\x0e\x82`\xe8\x19\xc0\x8d'
Decoded:  b"According to all known l`ws of aviashon, these is no way that a bef should!ce able to fly. Its wjngs are too small to get its fat\x1flittle aocy off the ground. Tie bee, of course, flies!anyways. Because bees don't!carf what humans uhink is impossiale."
Input length: 249, encoded length 322
```

You can also import this file as a library:

```py
from jpg4txt import encode, decode
e = encode(bytes("早上好中國，現在我有冰淇淋", encoding="utf8"))
# e = b'\x00\x11\xe4\x0f\x08\x11#\r\x83\xe3\x02c\x84\x01X\xd0@\x1e\x12\x16\x0b\x81\xe04\x0f\x81\x18\x08\xc0^\x03\xc8\x05\xa0\r\xf0\xa8L@t\x17\x89\x02\x00\xb0T$\t\x10'
d = decode(e)
# d = b'\xe6\x97\xa9\xe4\xb8\x8a\xe5\xa5\xbd\xe4\xb8\xad\xe5\x9c\x8b\xef\xbc\x8c\xe7\x8f\xbe\xe5\x9c\xa8\xe6\x87\x91\xe6\x9c\x8a\xe5\x86\xb0\xe6\xb7\x87\xe6\xb7\x8b'
# which translates to the string '早上好中國，現在懑朊冰淇淋'
```
## FAQ

### Q: This is really stupid.
A: That's not a question.

### Q: Why are you doing this?
A: Yes.

### Q: Why does your compression algorithm make the string longer?
A: I'm too lazy to do the actual compression part of this for now, feel free to do further JPEG-inspired compression and submit a PR. See other TODOs below.

## TODO

- use block based compression instead of compressing the entire thing
- do what JPG does (quantization and run length/huffman encoding/decoding)
- convert arbitrary list of integers to a list of bytes and decode in a better way
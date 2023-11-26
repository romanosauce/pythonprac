import sys

raw_wav = sys.stdin.buffer.read()
if len(raw_wav) < 44:
    print("NO")
    sys.exit()

if (raw_wav[0:4] != b"RIFF"
        or raw_wav[8:16] != b"WAVEfmt "
        or raw_wav[36:40] != b"data"):
    print("NO")
    sys.exit()

print(f"Size={int.from_bytes(raw_wav[4:8], 'little')}, Type={int.from_bytes(raw_wav[20:22], 'little')},",
      f"Channels={int.from_bytes(raw_wav[22:24], 'little')}, Rate={int.from_bytes(raw_wav[24:28], 'little')},",
      f"Bits={int.from_bytes(raw_wav[34:36], 'little')}, Data size={int.from_bytes(raw_wav[40:44], 'little')}")

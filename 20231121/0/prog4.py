import random
import struct
with open('out', 'wb') as f:
    random.seed(1)
    for i in range(10):
        data = random.random(), bytearray((random.randint(1, 10),
                                           random.randint(1, 10),
                                           random.randint(1, 10))), random.randint(1, 10)
        f.write(struct.pack('<f3si', *data))

# with open('out', 'rb') as f:
    # for i in range(10):
        # data = f.read(

"""Generate the app icons (blue dumbbell on dark) as raw PNGs - stdlib only."""
import struct
import zlib
import os

BLUE = (79, 140, 255)
BG = (15, 18, 22)


def chunk(typ, data):
    return struct.pack('>I', len(data)) + typ + data + struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)


def write_png(path, size, pix):
    raw = b''.join(b'\x00' + bytes(v for px in row for v in px) for row in pix)
    data = (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9))
            + chunk(b'IEND', b''))
    with open(path, 'wb') as f:
        f.write(data)


def make(size):
    # design grid is 512x512, scaled to any size
    k = size / 512.0
    pix = [[BG] * size for _ in range(size)]

    def rect(x0, y0, x1, y1, c):
        for y in range(int(y0 * k), int(y1 * k)):
            for x in range(int(x0 * k), int(x1 * k)):
                pix[y][x] = c

    rect(88, 210, 124, 302, BLUE)    # left outer sleeve
    rect(124, 150, 176, 362, BLUE)   # left plate
    rect(176, 232, 336, 280, BLUE)   # handle
    rect(336, 150, 388, 362, BLUE)   # right plate
    rect(388, 210, 424, 302, BLUE)   # right outer sleeve
    write_png(os.path.join('icons', f'icon-{size}.png'), size, pix)


os.makedirs('icons', exist_ok=True)
make(192)
make(512)
print('icons written:', os.listdir('icons'))

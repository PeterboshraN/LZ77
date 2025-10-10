# main.py

from LZ77Compressor import LZ77Compression
from LZ77Decompressor import LZ77Decompression

if __name__ == "__main__":
    text = "ABAABABAABBBBBBBBBBBBA"

    tags = LZ77Compression(text)
    print("Compressed Tags:")
    for t in tags:
        print(t)

    decompressed = LZ77Decompression(tags)
    print("\nDecompressed:", decompressed)

  
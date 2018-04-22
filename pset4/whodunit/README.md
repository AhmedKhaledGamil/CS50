# Questions

## What's `stdint.h`?

It helps using well defined types that makes the code easier for portability allowing only defined minimum and maximum allowable values for each type.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

So each type you want is defined the way want, also treated the way you want from the compiler.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE = 1 byte, DWORD = 4 bytes, LONG = 4 bytes and WORD = 2 bytes.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

Hex: 0x424d and ASCII: BM (bitmap!).

## What's the difference between `bfSize` and `biSize`?

bfSize is the total number of bytes in the file and biSize is the number of bytes in the info header.

## What does it mean if `biHeight` is negative?

 For uncompressed RGB bitmaps, if biHeight is positive, the bitmap is a bottom-up DIB with the origin at the lower left corner.
    If biHeight is negative, the bitmap is a top-down DIB with the origin at the upper left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

If it can't find the file, it will.

## Why is the third argument to `fread` always `1` in our code?

Because it specifies how many elements you want to read, and we're always reading a struct so we only need 1 struct.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

Zero

## What does `fseek` do?

It moves to a specific location in a file.

## What is `SEEK_CUR`?

An integer constant which, when used as the 'whence' argument to the fseek or fseeko function, specifies that the offset provided is relative to
the current file position.

#!/usr/bin/env python2

import hashlib
from PIL import Image

def dHash(image, hash_size = 8):
    image = image.convert('L').resize(
            (hash_size + 1, hash_size),
            Image.ANTIALIAS,
            )

    pixels = list(image.getdata())

    diff = []
    for row in xrange(hash_size):
        for col in xrange(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            diff.append(pixel_left > pixel_right)

    decimal_value = 0
    hex_string = []
    for index, value in enumerate(diff):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)

def user_interface():
    print('Please enter the path of two images')
    img1 = raw_input()
    img2 = raw_input()

    first_image = Image.open(img1)
    second_image = Image.open(img2)

    print 'Are images duplicates: ', dHash(first_image) == dHash(second_image)

if __name__ == '__main__':
    user_interface()

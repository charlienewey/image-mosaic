#! /usr/bin/env python2

import math
import os
import random
import sys

from PIL import Image


def distance(a, b):
    def _difference(a, b):
        if a > b: return a - b
        elif b > a: return b - a
        else: return 0

    assert len(a) == len(b)
    dist = 0
    for i in range(0, len(a)):
        dist += _difference(a[i], b[i])
    return dist


def average_colour(pixels):
    channels = len(pixels[0, 0])
    colours = [0] * channels
    for x in range(0, image.width):
        for y in range(0, image.height):
            for channel in range(0, channels):
                colours[channel] += pixels[x, y][channel]

    colours = list(map(lambda x: int(x / (image.width * image.height)), colours))
    return colours


if __name__ == "__main__":
    PIXEL_SIZE = 64

    images = []
    image_dir = sys.argv[1]
    for name in os.listdir(image_dir):
        path = os.path.join(image_dir, name)

        image = Image.open(path)
        image = image.resize((PIXEL_SIZE, PIXEL_SIZE))
        pixels = image.load()

        images.append({
            "image": image,
            "pixels": pixels,
            "path": path,
            "colour": average_colour(pixels)
        })

    input_image = sys.argv[2]
    image = Image.open(input_image)
    pixels = image.load()
    w, h = image.size

    output_dims = (w * PIXEL_SIZE, h * PIXEL_SIZE)
    output_image = Image.new("RGB", output_dims)

    pos_w = 0
    pos_h = 0
    for x in range(0, w):
        for y in range(0, h):
            for i in images:
                i["distance"] = distance(pixels[x, y], i["colour"])
            best_matches = sorted(images, key=lambda a: a["distance"])
            choice = random.choice(best_matches[0:5])

            output_image.paste(choice["image"], (pos_w, pos_h))

            pos_h += PIXEL_SIZE
            if pos_h == output_dims[1]:
                pos_h = 0
                pos_w += PIXEL_SIZE

    output_image.save(sys.argv[3])

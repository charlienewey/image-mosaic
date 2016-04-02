#! /usr/bin/env python2

import math
import os
import sys

from PIL import Image


def euclidean_distance(a, b):
    assert len(a) == len(b)
    dist = 0.0
    for i in range(0, len(a)):
        diff = math.pow(a[i] - b[i], 2)
        dist += diff
    return math.sqrt(dist)


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
    images = []
    image_dir = sys.argv[1]
    for name in os.listdir(image_dir):
        path = os.path.join(image_dir, name)
        image = Image.open(path)
        pixels = image.load()
        images.append({
            "image": image,
            "path": path,
            "colour": average_colour(pixels)
        })

    input_image = sys.argv[2]
    image = Image.open(input_image)
    pixels = image.load()

    print(pixels)

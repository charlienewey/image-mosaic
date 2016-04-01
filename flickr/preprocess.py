#! /usr/bin/env python2

import os
import sys

from PIL import Image


if __name__ == "__main__":
    image_dir = sys.argv[1]
    out_dir = sys.argv[2]

    for name in os.listdir(image_dir):
        path = os.path.join(image_dir, name)
        image = Image.open(path)

        # crop image to square (anchor at centre)
        w, h = image.size
        if w != h:
            if w > h:
                d = float(w - h) / 2
                box = (d, 0, w - d, h)
            elif h > w:
                d = float(h - w) / 2
                box = (0, d, w, h - d)

            box = map(lambda x: int(x), box)
            image = image.crop(box=box)

        # resize
        image = image.resize(size=(64, 64))

        # write image
        image.save(os.path.join(out_dir, name))

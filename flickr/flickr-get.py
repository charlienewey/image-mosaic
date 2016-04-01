#! /usr/bin/env python2

import json
import os
import sys
import uuid

import flickr_api as fa

if __name__ == "__main__":
    with open(sys.argv[1]) as conf:
        config = json.load(conf)

    KEY = config["api"]["key"]
    SECRET = config["api"]["secret"]

    fa.set_keys(KEY, SECRET)
    path_prefix = "images/"

    w = fa.Walker(fa.Photo.search, tags=sys.argv[2],)
    size = "Small"
    last_owners = []
    for photo in w:
        info = photo.getInfo()
        if str(info["license"]) == "0":
            continue

        if info["owner"]["username"] not in last_owners:
            last_owners.insert(0, info["owner"]["username"])

            if len(last_owners) > 10:
                last_owners.pop()

            title = photo.title.encode("utf-8")
            path = os.path.join(path_prefix, "%s_%d.jpg" % (size.lower(), hash(title)))
            photo.save(path, size_label=size)

            print("Saving '%s' as ''%s'" % (title, path))

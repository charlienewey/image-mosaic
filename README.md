# Image Mosaic

A set of scripts to produce a mosaic from images.

## How to install dependencies

Assuming you have Python (and `pip`) at your disposal, install the dependencies like so:

```bash
pip install flickr_api
pip install Pillow
```


## How to use the Flickr scripts

### flickr-get.py

Get yourself a Flickr API key from [here](https://www.flickr.com/services/api/keys/apply). You
should now have a "key" and a "secret". Put the key and secret in a JSON file, formatted like this:

```json
{
    "api": {
        "key": "your-key-goes-here",
        "secret": "your-secret-goes-here"
    }
}
```

Save that file as `flickr.json`. Now that you have an API key, you can use the `flickr-get.py`
script to download images. Make a directory called `images` in the same place that `flickr-get.py`
is stored. Then you can run the script like this:

```bash
python2 flickr-get.py ./path/to/your/flickr.json "your-keyword-here"
```

Where "your-keyword-here" is a keyword you wish to search for. You **must** specify a keyword.  The
images will download into the `images` directory. You probably need a library of about 500 to 1000
images from Flickr. You must make sure that there is a good range of colours in the images that you
download, or your mosaics won't look good!


### preprocess.py

You must run this script to turn the images that you downloaded from Flickr into evenly-sized tiles.
Make another directory called `tiles`. This will contain the resized images.

```bash
python2 preprocess.py ./path/to/directory/for/images ./path/to/directory/for/tiles
```


## How to use the image mosaic script

This script is easy to use.

Once you have a good library of images to use as mosaic tiles, find an image that you would like to
turn into a mosaic and resize it to a small size using your favourite image editing tool. I suggest
keeping your input image to about 32x32 pixels if you can (because the mosaic will be 64x bigger).
Then run the mosaic script like so:

```bash
python2 colour-mosaic.py ./directory/containing/tiles ./path/to/input.jpg ./path/to/output.jpg
```

You should see a mosaic appear, called `output.jpg`.

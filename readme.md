# Using `eval` method

The code here is a short demo for using the `eval` function of Cloudinary. There are 2 examples:

* Re-upload if the MD5 hash of the files are different, i.e., upload if files are not exact duplicates.
* Re-upload if the width/height of new image is larger than original image

## Dependency

### Libraries

To run the code, please install [Python pillow](https://python-pillow.org/) library. Be sure to read the [installation documentation](https://pillow.readthedocs.io/en/latest/installation.html) as this library requires that you don't use the Python Imaging Library.

### Cloudinary Credentials

This code assumes that the Cloudinary credentials are stored in the environmental variable `CLOUDINARY_URL`. 

### Python3

I assume this code is being executed on `python3`.

## Execution

Just run the python file and you should see the output. e.g.:

    python upload_if_different.py

Output:

```
First file hash: 479ba08ecf4a09f98f4a9a4854d9ab1f
Etag from cloudinary: 479ba08ecf4a09f98f4a9a4854d9ab1f
Second file hash: df7d123be9c16b855e16f127a6b2d261
Etag from cloudinary: df7d123be9c16b855e16f127a6b2d261
Image URL: https://res.cloudinary.com/dbmataac4/image/upload/v1626733581/f1.jpg
```

In both the scripts, the first image to be uploaded is `f1.jpg`. 

![f1.jpt](https://akshayranganath-res.cloudinary.com/image/upload/f_auto,q_auto,w_350,c_scale/blog/aaa2.jpg)

However, the eval condition in second upload will evaluate to a try and we'll end up overwriting the image with `f2.jpg`.

![f2.jpg](https://akshayranganath-res.cloudinary.com/image/upload/f_auto,q_auto,w_350,c_scale/blog/aaa3.jpg)


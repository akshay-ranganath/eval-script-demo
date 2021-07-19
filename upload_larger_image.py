from PIL import Image
import cloudinary.uploader


# get the new image size
with Image.open("f1.jpg") as im:
    i_width = im.width
    i_height = im.height
print(f"First image width={i_width} and height={i_height}")

# upload to Cloudinary and print the dimensions for comparison.
resp = cloudinary.uploader.upload(
    'f1.jpg',
    public_id='f1',
    type='upload',
    resource_type='image',
    overwrite=False,
    unique_filename=False
)
print(f"From Cloudinary: Width={resp['width']}, height={resp['height']}")

# get second image dimensions
with Image.open("f2.jpg") as im:
    n_width = im.width
    n_height = im.height
print(f"New image width={n_width} and height={n_height}")

# now try to upload and capture the dimensions
resp = cloudinary.uploader.upload(
    'f2.jpg',
    public_id='f1',
    type='upload',
    resource_type='image',
    overwrite=False,
    unique_filename=False,
    #eval = 'if(resource_info.width <'+ str(n_width) +' || resource_info.height <'+ str(n_height) + ') { upload_options["overwrite"]=true}'
    eval = 'if(resource_info.width < 1280 || resource_info.height < 800) { upload_options["overwrite"]=true}'
)
# print the final dimensions
print(f"From Cloudinary: Width={resp['width']}, height={resp['height']}")
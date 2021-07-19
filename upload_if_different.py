import hashlib
import cloudinary.uploader

def get_hash(file_name):
    with open(file_name,'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

file1_hash = get_hash('f1.jpg')
print(f"First file hash: {file1_hash}")

resp = cloudinary.uploader.upload(
    'f1.jpg',
    public_id='f1',
    type='upload',
    resource_type='image',
    overwrite=False,
    unique_filename=False
)
if 'etag' in resp:
    print(f'Etag from cloudinary: {resp["etag"]}')

file2_hash = get_hash('f2.jpg')
print(f"Second file hash: {file2_hash}")

resp = cloudinary.uploader.upload(
    'f2.jpg',
    public_id="f1",
    type='upload',
    resource_type='image',
    unique_filename=False,
    overwrite=False,
    eval = 'if(resource_info.etag !=\''+ file2_hash +'\') { upload_options["overwrite"]=true}'
)
print(f'Etag from cloudinary: {resp["etag"]}')
print(f'Image URL: {resp["secure_url"]}')
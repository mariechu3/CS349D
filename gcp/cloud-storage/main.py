import functions_framework

from google.cloud import storage
from time import time
        
def download_blob(blob, download_path):
    blob.download_to_filename(download_path)
    print('Blob {} downloaded to {}.'.format(
        blob.name,
        download_path))

def upload_blob(bucket_name, blob, upload_path):
    blob.upload_from_filename(upload_path)
    print('File {} uploaded to {}.'.format(
        blob.name,
        bucket_name))

def function_handler(request):
    request_json = request.get_json(silent=True)
    if request_json and 'blob_name' in request_json:
      blob_name = request_json['blob_name']
    else: 
      blob_name = '5mb'
    if request_json and 'src_bucket':
      src_bucket = request_json['src_bucket']
    else:
      src_bucket = 'cloud-storage-src'
    if request_json and 'dst_bucket':
      dst_bucket = request_json['dst_bucket']
    else:
      dst_bucket = 'cloud-storage-dst'
    
    storage_client = storage.Client()
    s_bucket = storage_client.get_bucket(src_bucket)
    s_blob = s_bucket.blob(blob_name)
    
    start = time()
    file_path = "/tmp/" + blob_name
    download_blob(s_blob, file_path)
    download_time = time() - start
    
    start = time()
    d_bucket = storage_client.get_bucket(dst_bucket)
    d_blob = d_bucket.blob(blob_name)
    upload_blob(dst_bucket, d_blob, file_path) 
    upload_time = time() - start
    
    result = "Download time : " + str(download_time) + " Upload Time : " + str(upload_time)
    print(result)
    return result

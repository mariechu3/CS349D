import functions_framework
from google.cloud import storage
from time import time
import cv2

def video_processing(blob_name, file_path):
    output_file_path = '/tmp/output-' + blob_name
    video = cv2.VideoCapture(file_path)

    print("opened:" , video.isOpened())
    
    # width = int(video.get(3))
    # height = int(video.get(4))
    width = int(cv2.CAP_PROP_FRAME_WIDTH)
    height = int(cv2.CAP_PROP_FRAME_HEIGHT)
    
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # https://stackoverflow.com/questions/57792837/opencv-ffmpeg-tag-is-not-supported-with-codec-id-12-and-format-mp4-mp4
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(output_file_path, fourcc, 20.0, (width, height))
    
    start = time()
    count = 0
    while(video.isOpened()):
        ret, frame = video.read()
        
        if count % 1000 == 0:
          print('count {} ret {}.'.format(
        ret,
        count))
        count += 1

        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            im = cv2.imwrite('/tmp/frame.jpg', gray_frame)
            gray_frame = cv2.imread('/tmp/frame.jpg')
            out.write(gray_frame)
        else:
            print("video end", count)
            break
            
    latency = time() - start
    
    video.release()
    out.release()
    return latency, output_file_path

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
    if request_json and 'src_bucket' in request_json:
      src_bucket = request_json['src_bucket']
    else:
      src_bucket = 'video-processing-src'
    if request_json and 'blob_name':
      blob_name = request_json['blob_name']
    else:
      blob_name = "sample.mp4"
    if request_json and 'dst_bucket' in request_json:
      dst_bucket = request_json['dst_bucket']
    else:
      dst_bucket = 'video-processing-dst'
    
    storage_client = storage.Client()
    s_bucket = storage_client.get_bucket(src_bucket)
    s_blob = s_bucket.blob(blob_name)
    
    download_path = "/tmp/" + blob_name
    download_blob(s_blob, download_path)
    
    latency, upload_path = video_processing(blob_name, download_path)
    
    d_bucket = storage_client.get_bucket(dst_bucket)
    d_blob = d_bucket.blob(blob_name)
    upload_blob(dst_bucket, d_blob, upload_path)
    
    return "latency : " + str(latency)

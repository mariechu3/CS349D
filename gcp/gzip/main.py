import functions_framework

from time import time
import os
import gzip


def function_handler(request):
    request_json = request.get_json(silent=True)
    file_write_path = '/tmp/file'

    if request_json and 'file_size' in request_json:
      file_size = request_json['file_size']
    else:
      file_size = 5

    start = time()
    with open(file_write_path, 'wb') as f:
        f.write(os.urandom(int(file_size) * 1024 * 1024))
        f.close()
    disk_latency = time() - start

    with open(file_write_path, 'rb') as f:
        start = time()
        with gzip.open('/tmp/result.gz', 'wb') as gz:
            gz.writelines(f)
        compress_latency = time() - start

    print(compress_latency)
    return "disk latency : " + str(disk_latency) \
           + "/ compress latency : " + str(compress_latency)


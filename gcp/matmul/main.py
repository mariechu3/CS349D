import functions_framework

import numpy as np
from time import time

def matmul(N):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    start = time()
    C = np.matmul(A, B)
    latency = time() - start

    return latency

def function_handler(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'N' in request_json:
        N = request_json['N']
    elif request_args and 'N' in request_args:
        N = request_args['N']
    else:
      N = 10
    latency = matmul(int(N))
    print(latency)
    return "latency : " + str(latency)

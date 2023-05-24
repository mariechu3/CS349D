import functions_framework
import math
from time import time

def float_operation(N):
    start = time()
    for i in range(0, N):
        sin_i = math.sin(i)
        cos_i = math.cos(i)
        sqrt_i = math.sqrt(i)
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
    latency = float_operation(int(N))
    print(latency)
    return "latency : " + str(latency)


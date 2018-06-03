from .RDataFrame import RDataFrame
from .Node import Node
from .Proxy import Proxy as proxy, Backend_env, Backend_conf
from .Operation import Operation
from .CallableGenerator import CallableGenerator

def use(backend, conf = {}):

    available_backends = [
    "local",
    "spark"
    ]

    future_backends = [
    "dask"
    ]

    if backend in future_backends:
        raise NotImplementedError(" This backend environment will be considered in the future !")
    elif backend in available_backends:
        Proxy.Backend_env = backend
        Proxy.Backend_conf = conf
    else:
        raise Exception(" Incorrect backend environment \"{}\"".format(backend))
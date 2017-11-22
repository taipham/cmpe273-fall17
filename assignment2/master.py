'''
################################## server.py #############################
# 
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import rocksdb
import uuid
from functools import wraps


from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MyDatastoreServicer(datastore_pb2_grpc.DatastoreServicer):
    data_list = []
    num_connections = 0
    def __init__(self):
        self.db = rocksdb.DB("master.db", rocksdb.Options(create_if_missing=True))

    def replicate(self, request, context):
        i = num_connection
        data_list.append([])
        self.num_connecitons += 1
        
        while len(data_list[i]) != 0:
            data = data_list[i].pop(0)
            yield datastore_pb2.ResponseStream(key=data["key"], value=data["value"])

    def replicator(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            for i in range(num_connections):
                data_list[i].append({"key": args[1].key, "value":args[1].value})
            return f(*args, **kwargs)

        return func_wrapper
        

    @replicator
    def put(self, request, context):
        self.db.put(request.key, request.value)
        return datastore_pb2.GetPutResponse(key=request.key, value=request.value)

    def get(self, request, context):
        value = self.db.get(request.key)
        return datastore_pb2.GetPutResponse(key=request.key, value=value)


def run(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)

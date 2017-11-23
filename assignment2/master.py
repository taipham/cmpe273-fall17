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
    history = []
    num_connections = 0
    def __init__(self):
        self.db = rocksdb.DB("master.db", rocksdb.Options(create_if_missing=True))

    def replicate(self, request, context):
        for item in self.history:
            yield datastore_pb2.Response(data=item)

    def replicator(f):
        @wraps(f)
        def func_wrapper(self, request, context):
            key = f(self, request, context)
            self.history.append(key + ',' + request.data)
            return datastore_pb2.Response(data=key)

        return func_wrapper
        

    @replicator
    def put(self, request, context):
        key = uuid.uuid4().hex
        print('put ' + key + ' ' + request.data)
        self.db.put(key.encode(), request.data.encode())
        return key

    def get(self, request, context):
        value = self.db.get(request.data.encode())
        return datastore_pb2.Response(data=value)


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

'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2
import datastore_pb2_grpc
import sys
import rocksdb

client_num = 0

class DatastoreClient():
    def __init__(self, host='0.0.0.0', port=3000):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2_grpc.DatastoreStub(self.channel)
        self.db = rocksdb.DB("client_" + client_num + ".db", rocksdb.Options(create_if_missing=True))

    def connect(self):
        resp = self.stub.replicate(datastore_pb2.Request())
        for data in resp:
            self.db.put(data.key, data.value)



clienr_num = sys.argv[1]

print("Client is running...")
client = DatastoreClient()

client.connect()
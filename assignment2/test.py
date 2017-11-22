'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2
import datastore_pb2_grpc
import sys
from pathlib import Pat

class DatastoreClient():
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, key, value):
        return self.stub.put(datastore_pb2.Request(key=key, value=value))

    def get(self, key):
        return self.stub.get(datastore_pb2.Request(data=key))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)
    
    key1 = '1'
    value1 = 'foo'
    print("## PUT Request: value = " + value) 
    resp = client.put(key, value)
    key2 = '2'
    value2 = 'bar'
    print("## PUT Request: value = " + value) 
    resp = client.put(key, value)

    print("All slave data:")
    for i in range (10):
        my_file = Path("client_" + i + ".db")
        if my_file.is_file():
            db = rocksdb.DB(my_file,rocksdb.Options(create_if_missing=False))
            print("Result from client #" + i)
            value = db.get(key1)
            print("## GET Request: key1 = " + key1) 
            resp = client.get(key1)
            print("## GET Response: value1 = " + resp.data)
            value = db.get(key2)
            print("## GET Request: key2 = " + key2) 
            resp = client.get(key2)
            print("## GET Response: value2 = " + resp.data)


if __name__ == "__main__":
    main()

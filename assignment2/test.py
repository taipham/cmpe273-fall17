'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2
import datastore_pb2_grpc
import sys
import argparse

PORT = 3000

class DatastoreClient():
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, value):
        return self.stub.put(datastore_pb2.Request(data=value))

    def get(self, key):
        return self.stub.get(datastore_pb2.Request(data=key))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)
    
    # put something in 
    value = 'foo'
    print("## PUT Request: value = " + value) 
    resp = client.put(value)

    value = resp.data
    resp = client.get(value)
    print("## GET Request: key = " + value + " value = "+ resp.data) 

if __name__ == "__main__":
    main()

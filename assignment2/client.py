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
import rocksdb
import time
PORT = 3000


class DatastoreClient():
    def __init__(self, host='0.0.0.0', port=3000, client=0):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2_grpc.DatastoreStub(self.channel)
        self.db = rocksdb.DB("client" + str(client) + ".db", rocksdb.Options(create_if_missing=True))

    def connect(self, value):
        resp = self.stub.replicate(datastore_pb2.RequestInt(data=value))
        return resp
        

#client_num = sys.argv[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    parser.add_argument("client", help="display a square of a given number")
    args = parser.parse_args()
    client_num = int(args.client)
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host, client=client_num)
    while True:
        resp = client.connect(client_num)
        for item in resp:
            op = item.data.split(',')
            client.db.put(op[0].encode(), op[1].encode())
            print("Client #" + str(client_num) + " get key=" + str(op[0].encode()) + " value=" + str(op[1].encode()))
        time.sleep(1)

if __name__ == "__main__":
    main()
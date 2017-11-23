Instruction:

Setup the same way as lab1
https://github.com/taipham/cmpe273-fall17/tree/master/lab1

Run master.py
docker run -p 3000:3000 -it --rm --name lab1-server -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 master.py

Run client.py (client_num is an integer)
docker run -it --rm --name lab1-client -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 client.py 192.168.0.1 <client_num>

Run test.py
docker run -it --rm --name lab2-client -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 test.py 192.168.0.1

Output to the screen
Master:
Server started at...3000
put 191444c494e949fdb1e2744049283b73 foo

Client:
Client is connecting to Server at 192.168.0.1:3000...
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'
Client #2 get key=b'191444c494e949fdb1e2744049283b73' value=b'foo'

Test:
Client is connecting to Server at 192.168.0.1:3000...
## PUT Request: value = foo
## GET Request: key = 191444c494e949fdb1e2744049283b73 value = foo
 

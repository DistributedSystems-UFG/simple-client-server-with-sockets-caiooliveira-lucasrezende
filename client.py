from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

operation1 = ('subtract',(10,20))

s.send(pickle.dumps(operation1))  # send some data
data = s.recv(1024)     # receive the response
print (pickle.loads(data))            # print the result
s.close()               # close the connection

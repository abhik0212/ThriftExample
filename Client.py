#!/usr/bin/env python

host = "localhost"
port = 9090

import sys

sys.path.append('gen-py')

from FileOperation import *
from FileOperation.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

    # Init thrift connection and protocol handlers
    transport = TSocket.TSocket( host , port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Set client
    client = FileOperation.Client(protocol)

       
    #Get argument
    if len(sys.argv)>1:
	n=sys.argv[1]
	try:
		n=int(n)
	except:
		raise Exception("Please enter an integer value")
    #else set the default value to 10
    else:
	n=10

    # Connect to server
    transport.open()

    response = client.deleteFromFile(n)
    print response

    # Close connection
    transport.close()

except Thrift.TException, tx:
    print 'client :Something went wrong : %s' % (tx.message)

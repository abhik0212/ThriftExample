#!/usr/bin/env python

port = 9093

import sys
# your gen-py dir
sys.path.append('gen-py')


from FileOperation import *
from FileOperation.ttypes import *

# Thrift files
import os
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Server implementation
class FileOperationHandler:
    def addToFile(self, s):
	try:
		f = open('b.txt')
		content = f.read()
		f.close()
		f = open('b.txt','w')
		f.write(s)
		f.write(content)
		f.close()
		return "success"
        except:
		print "error opening file"
		return "error"

if __name__ == '__main__':

	# set handler to our implementation
	handler = FileOperationHandler()

	processor = FileOperation.Processor(handler)
	transport = TSocket.TServerSocket(port = port)
	tfactory = TTransport.TBufferedTransportFactory()
	pfactory = TBinaryProtocol.TBinaryProtocolFactory()

	# set server
	server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

	print 'Starting serverB'
	server.serve()

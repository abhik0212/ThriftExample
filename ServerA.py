#!/usr/bin/env python

port = 9090
host = "localhost"

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

def appendtoB(lines):
    try:
        # Init thrift connection and protocol handlers
        transportA = TSocket.TSocket( host , 9093)
        transportA = TTransport.TBufferedTransport(transportA)
        protocolA = TBinaryProtocol.TBinaryProtocol(transportA)

        # Set client to FileOperation
        clientA = FileOperation.Client(protocolA)

        # Connect to server
        transportA.open()

        response = clientA.addToFile(lines)
        
        # Close connection
        transportA.close()
	
	return response

    except Thrift.TException, tx:
        print 'ServerA:Problem in calling serverB : %s' % (tx.message)
        return "Problem in calling server B"
    

# Server implementation
class FileOperationHandler:
    def deleteFromFile(self,n):
	  try:
		  f="a.txt"
		  stdin,stdout = os.popen2("tail -n "+str(n)+" "+f+">temp1.txt")
		  stdin.close()
		  stdout.close()
	  except:
		  print "Could not open a.txt"
		  return "Could not open a.txt"
	  try:
		  if appendtoB("temp1.txt")=="success":
			  stdin,stdout = os.popen2("sed -i -e :a -e '$d;N;2,"+str(n)+"ba' -e 'P;D' "+f)
			  stdin.close()
			  stdout.close()
			  return "deletion and appending successful"
		  else:
			  return "deletion not done because ServerB could not append successfully"
	  except:
		  print "ServerB may not be responding"
		  return "ServerB may not be responding"

if __name__ == '__main__':

	# set handler to our implementation
	handler = FileOperationHandler()

	processor = FileOperation.Processor(handler)
	transport = TSocket.TServerSocket(port = port)
	tfactory = TTransport.TBufferedTransportFactory()
	pfactory = TBinaryProtocol.TBinaryProtocolFactory()

	# set server
	server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

	print 'Starting serverA'
	server.serve()

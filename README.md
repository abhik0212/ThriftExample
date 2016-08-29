# ThriftExample

Have 2 instance of same thrift server running, each having a file at
their possession(passed as parameter). Say a.txt and b.txt. when a client makes a call to
Server A, A should remove last 10 lines from a.txt and then pass it on
to server B. server B should prepend the incoming data to b.txt.

client --------> Server A ------> Server B
       <-----------|<----------------|

also build a client to test it.

How to run:
1>Open 3 terminals
2>Start the server A using python ServerA.py
3>Start the Server B using python ServerB.py
4>Run the client using python Client.py 4 (Here, 4 is the number of lines to be removed from a.txt. Default value is 10)

from socket import *
import time
#establishing host IP and port numbers
HOST = "10.0.0.1"
PORT = 1588
#Setting up the socket configurations
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((HOST, PORT))
#settimeout socket method takes an integer as a parameter in seconds
clientSocket.settimeout(1)
#tracker variable for lost packets
lost_packets = 0
#tracker variable for pings sent
counter = 1
#a list variable to keep track of rtt's
info = []
#since we need to send 10 pings to the server, 
#we set up a while loop for 10 actions
while counter <= 10:
    #code is wrapped into a try-except blocks to correctly handle timeot exceptions
    try:
      data = "Ping "+str(counter)
      #time's method to take in the current time when the sending starts
      time1 = time.time()
      byte_data =data.encode('utf-8')
      clientSocket.sendall(byte_data)
      data = clientSocket.recv(2048)
      data = data.decode('utf-8')
      #take end time after ping has returned
      time2 = time.time()
      #since time returns seconds, convert the difference to miliseconds
      rtt = (time2-time1)*1000
      info.append(rtt)
      print(data + ": rtt = {:.3f} ms".format(rtt))
    #handle timeout exception
    except timeout:
        lost_packets += 1
        print(data + ": Request timed out")
    #increment counter for the next ping
    counter+=1
#resulting metadata
print("Summary values:\nmin_rtt = {:.3f} ms\nmax_rtt = {:.3f} ms\navg_rtt = {:.3f} ms\nPacket loss: {:.2f}%".format(
    min(info), max(info), sum(info)/len(info), lost_packets * 10))

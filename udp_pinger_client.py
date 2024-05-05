from socket import *
import time

HOST = "10.0.0.1"
PORT = 1588

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((HOST, PORT))
clientSocket.settimeout(1)
lost_packets = 0
counter = 1
info = []
while counter <= 10:
    try:
      data = "Ping "+str(counter)
      time1 = time.time()
      byte_data =data.encode('utf-8')
      clientSocket.sendall(byte_data)
      data = clientSocket.recv(2048)
      data = data.decode('utf-8')
      time2 = time.time()
      rtt = (time2-time1)*1000
      info.append(rtt)
      print(data+" rtt = "+str(rtt)+" ms")
    except TimeoutError as e:
      if isinstance(e, socket.timeout):
        lost_packets += 1
        print("Request timed out")
    counter+=1
print("Summary values:\nmin_rtt = "
      +str(min(info))+" ms\nmax_rtt = "
      +str(max(info))+ " ms\navg_rtt = "+str(sum(info)/10)+
      " ms\nPacket loss: "+ lost_packets*10 + ".00%")



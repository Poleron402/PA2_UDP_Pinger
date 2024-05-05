from socket import *
import time

HOST = "10.0.0.1"
PORT = 17171

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
      data, _ = clientSocket.recv(1024)
      time2 = time.time()
      rtt = (time2-time1)*1000
      info.append(rtt)
      print(data+" rtt = "+str(rtt)+" ms")
    except clientSocket.timeout():
      lost_packets += 1
      print("Request timed out")
    counter+=1
print("Summary values:\nmin_rtt = "
      +min(info)+" ms\nmax_rtt = "
      +max(info)+ " ms\navg_rtt = "+sum(info)/10+
      " ms\nPacket loss: "+ lost_packets*10 + ".00%")



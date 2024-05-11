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
      print(data + ": rtt = {:.3f} ms".format(rtt))
    except timeout:
        lost_packets += 1
        print(data + ": Request timed out")
    counter+=1
print("Summary values:\nmin_rtt = {:.3f} ms\nmax_rtt = {:.3f} ms\navg_rtt = {:.3f} ms\nPacket loss: {:.2f}%".format(
    min(info), max(info), sum(info)/len(info), lost_packets * 10))

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(1000,9999):
    result = sock.connect_ex(('5.160.40.36',2414))
    if result == 0:
        print(i)
sock.close()
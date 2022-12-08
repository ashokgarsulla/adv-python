import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 1255
s.bind((HOST,PORT))
s.listen(10)

socketclientobj, address = s.accept()
print("got connection from", address)
conn = True
while conn:
    msg = socketclientobj.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
    if(msg == "quite"):
        conn = False
        s.close()
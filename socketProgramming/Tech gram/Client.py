import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255
s.connect((host,port))
conn = True
while conn:
    msg = input("Enter msg :")
    s.send(msg.encode("utf-8"))
    if msg == "quite":
        conn = False
        s.close()
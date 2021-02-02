import socket
import os
import subprocess as sp

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5063        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while(1):
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if(data.decode()=="byee"):
                    s.close()
                    break
                else:
                    # stream=os.popen(data.decode())
                    # output=stream.read()
                    try:
                        pipe = sp.Popen( data.decode(), shell=True, stdout=sp.PIPE, stderr=sp.PIPE )
                        res = pipe.communicate()
                        res="Response from server: "+str(res)
                        conn.sendall(res.encode())
                    except:
                        conn.sendall("some random error")
                    # if(len(output)>0):
                    #     conn.sendall(output.encode())
                    # else:
                    #     conn.sendall("no output received".encode())
                    # conn.sendall(data)
                    